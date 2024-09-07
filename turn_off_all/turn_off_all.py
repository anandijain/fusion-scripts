import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        rootComp = design.rootComponent
        allOccs = rootComp.allOccurrences
        msg = ""
        for o in allOccs:
            msg += f'{o.component.name}\n'
            o.isLightBulbOn = False
        ui.messageBox(msg)
    
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
