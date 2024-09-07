import adsk.core, adsk.fusion, adsk.cam, traceback

def turn_off_sketch_visibility(component: adsk.fusion.Component):
    # Iterate through all sketches in the component and turn off visibility
    for sketch in component.sketches:
        sketch.isVisible = False

    # Recursively handle all occurrences (nested components)
    for occurrence in component.occurrences:
        turn_off_sketch_visibility(occurrence.component)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct

        # Start with the root component
        root_comp = design.rootComponent
        # root_comp.isSketchFolderLightBulbOn = False
        turn_off_sketch_visibility(root_comp)

        ui.messageBox('All sketches are turned off.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))