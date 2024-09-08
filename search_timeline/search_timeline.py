import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct

        if not isinstance(design, adsk.fusion.Design):
            ui.messageBox('No active Fusion 360 design')
            return

        # Prompt the user to input a search string
        search_string = ui.inputBox("Enter the string to search for in the timeline:", "Search Timeline")[0]

        # If the user cancels the input box, it returns None, so we handle that
        if search_string is None:
            return

        # Get the timeline
        timeline = design.timeline

        # Initialize an empty list to store matching events
        matching_events = []

        # Loop through each timeline event and search for matching events
        for index in range(timeline.count):
            timelineObj = timeline.item(index)
            
            # Check if the event's name contains the search string (case insensitive)
            if search_string.lower() in timelineObj.name.lower():
                # Add event info to the list if it matches
                matching_events.append((index, timelineObj))
        
        # If no matches are found, inform the user
        if not matching_events:
            ui.messageBox(f"No events found with the string '{search_string}'.")
            return

        # Build the message to display the list of matching events
        timeline_info = "Matching events:\n"
        for event in matching_events:
            timeline_info += f"Event {event[0]}: {event[1].name}, type: {event[1].objectType}\n"
        
        # Display the accumulated string in a message box
        timeline_info += "\nEnter the event number you want to select:"
        event_number_str = ui.inputBox(timeline_info)[0]

        # If the user cancels the input box, it returns None, so we handle that
        if event_number_str is None:
            return

        # Try to convert the input into an integer and select the event
        try:
            event_number = int(event_number_str)
            # Find the event in the matching events list
            selected_event = next(event for event in matching_events if event[0] == event_number)

            # Select the corresponding timeline event
            timeline.item(event_number).isSelected = True

        except ValueError:
            ui.messageBox("Invalid input. Please enter a valid event number.")
        except StopIteration:
            ui.messageBox(f"No event found with the number {event_number}.")

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

