import adsk.core, adsk.fusion, adsk.cam, traceback
import json
import os

def run(context):
    ui = None
    try:
        # Get the application and user interface
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get the active design
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active Fusion 360 design', 'Import Parameters')
            return

        # Prompt user to select a JSON file to import
        file_dlg = ui.createFileDialog()
        file_dlg.title = 'Select Parameters JSON File to Import'
        file_dlg.filter = 'JSON files (*.json)'
        file_dlg.isMultiSelectEnabled = False

        if file_dlg.showOpen() != adsk.core.DialogResults.DialogOK:
            return

        file_path = file_dlg.filename

        # Read the JSON data from the file
        with open(file_path, 'r') as json_file:
            params_list = json.load(json_file)

        # Import parameters
        for param_info in params_list:
            name = param_info['name']
            expression = param_info['expression']
            unit = param_info['unit']
            comment = param_info.get('comment', '')
            is_favorite = param_info.get('isFavorite', False)

            # Check if the parameter already exists
            existing_param = design.allParameters.itemByName(name)
            if existing_param:
                # Update existing parameter
                existing_param.expression = expression
                existing_param.comment = comment
                existing_param.isFavorite = is_favorite
            else:
                # Create new user parameter
                design.userParameters.add(name, adsk.core.ValueInput.createByString(expression), unit, comment)
                new_param = design.allParameters.itemByName(name)
                if new_param:
                    new_param.isFavorite = is_favorite

        # Notify the user of success
        ui.messageBox(f'Parameters imported successfully from:\n{file_path}', 'Import Successful')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
