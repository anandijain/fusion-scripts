import adsk.core, adsk.fusion, adsk.cam, traceback
import json
import re

def sanitize_filename(name):
    # Remove invalid filename characters
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def run(context):
    ui = None
    try:
        # Get the application and user interface
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get the active design
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active Fusion 360 design', 'Export Parameters')
            return

        # Get all parameters (both user and model parameters)
        all_params = design.allParameters

        # Collect parameter data
        params_list = []
        for param in all_params:
            param_info = {
                'name': param.name,
                'expression': param.expression,
                'unit': param.unit,
                'comment': param.comment,
                'isFavorite': param.isFavorite
            }
            params_list.append(param_info)

        # Convert the list to JSON format
        json_data = json.dumps(params_list, indent=4)

        # Prompt user to select a folder to save the JSON file
        folder_dlg = ui.createFolderDialog()
        folder_dlg.title = 'Select Folder to Save Parameters JSON File'
        if folder_dlg.showDialog() != adsk.core.DialogResults.DialogOK:
            return
        folder_path = folder_dlg.folder

        # Get the design name and sanitize it for filename use
        design_name = design.rootComponent.name
        sanitized_name = sanitize_filename(design_name)

        # Define the file path with the design's name
        file_name = f"{sanitized_name}_parameters.json"
        file_path = f"{folder_path}/{file_name}"

        # Write the JSON data to the file
        with open(file_path, 'w') as json_file:
            json_file.write(json_data)

        # Notify the user of success
        ui.messageBox(f'Parameters exported successfully to:\n{file_path}', 'Export Successful')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
