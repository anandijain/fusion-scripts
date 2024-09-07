#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        docs = app.documents
        ui  = app.userInterface
        design = app.activeProduct

        # Start with the root component
        root_comp = design.rootComponent
        msg = ""
        for doc in docs:
            msg += doc.name + "\n" 
        ui.messageBox(msg)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
