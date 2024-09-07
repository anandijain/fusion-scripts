use clap::Parser;
use std::fs;
use std::io;
use std::path::PathBuf;

/// Command line tool for creating Fusion 360 script folder and files
#[derive(Parser)]
struct Args {
    /// Name of the script (used for naming the folder and files)
    script_name: String,
}

/// Get the project root using the CARGO_MANIFEST_DIR environment variable
fn get_project_root() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR"))
}

fn main() -> io::Result<()> {
    let args = Args::parse();

    // Get the current working directory where the CLI is being run
    let current_dir = std::env::current_dir()?;
    
    // Create the top-level folder with the user-provided name
    let script_folder = current_dir.join(&args.script_name);
    fs::create_dir(&script_folder)?;

    // Get the project root from CARGO_MANIFEST_DIR and append the data folder
    let project_root = get_project_root();
    let data_folder = project_root.join("data");

    // Define the file paths inside the data folder
    let default_manifest = data_folder.join("default.manifest");
    let default_py = data_folder.join("default.py");
    let launch_json = data_folder.join("launch.json");

    // Renaming and copying default.manifest and default.py
    let new_manifest_path = script_folder.join(format!("{}.manifest", &args.script_name));
    let new_py_path = script_folder.join(format!("{}.py", &args.script_name));

    // Copy default.manifest to the new path
    fs::copy(default_manifest, &new_manifest_path)?;
    println!("Created: {:?}", new_manifest_path);

    // Copy default.py to the new path
    fs::copy(default_py, &new_py_path)?;
    println!("Created: {:?}", new_py_path);

    // Create the .vscode folder inside the new script folder
    let vscode_folder = script_folder.join(".vscode");
    fs::create_dir(&vscode_folder)?;

    // Copy launch.json to the .vscode folder
    let new_launch_json_path = vscode_folder.join("launch.json");
    fs::copy(launch_json, &new_launch_json_path)?;
    println!("Created: {:?}", new_launch_json_path);

    Ok(())
}
