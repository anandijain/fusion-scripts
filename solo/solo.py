import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Prompt the user to select a component
        sel = ui.selectEntity('Select a component to solo', 'Occurrences')
        
        # Get the selected component
        selectedComp = adsk.fusion.Occurrence.cast(sel.entity)
        if not selectedComp:
            ui.messageBox('Selected entity is not a component')
            return
        
        # Turn off the visibility of all other components
        for occurrence in rootComp.allOccurrences:
            if occurrence != selectedComp:
                occurrence.isLightBulbOn = False
            else:
                occurrence.isLightBulbOn = True
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

