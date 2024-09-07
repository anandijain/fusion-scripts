import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        # Get all components in the design
        rootComp = design.rootComponent
        allOccs = rootComp.allOccurrences

        # Iterate through all occurrences and hide them
        for occ in allOccs:
            occ.isVisible = False

        ui.messageBox('All components have been hidden.')
    
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
