import adsk.core, adsk.fusion, adsk.cam, traceback

def turn_off_joint_visibility(component):
    # Iterate through all joints in the current component and turn off visibility
    for joint in component.joints:
        joint.isVisible = False
    
    # Recursively handle all occurrences (nested components)
    for occurrence in component.occurrences:
        # occurrence.component gives the nested component, and we apply the function to it
        turn_off_joint_visibility(occurrence.component)

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct

        # Start with the root component
        root_comp = design.rootComponent
        turn_off_joint_visibility(root_comp)

        ui.messageBox('All joints are turned off.')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

