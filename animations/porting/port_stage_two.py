import bpy

animation_lengths = {}

# Get the selected armature
selected_armature = bpy.context.object
if selected_armature and selected_armature.type == 'ARMATURE':
    armature = selected_armature.data

    # Iterate through animation actions
    for action in bpy.data.actions:
        if action.name in animation_lengths:
            # Get the desired length from the dictionary
            desired_length = animation_lengths[action.name]

            # Calculate the scale factor based on desired length and current length
            current_length = action.frame_range[-1]
            scale_factor = desired_length / current_length

            # Apply the scale factor to the action
            for fcurve in action.fcurves:
                for keyframe in fcurve.keyframe_points:
                    keyframe.co.x *= scale_factor

            # Update the action's range to match the desired length
            action.frame_range[-1] = desired_length

    print("Animation scaling completed.")
else:
    print("No armature selected.")