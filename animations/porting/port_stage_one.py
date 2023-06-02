import bpy

def get_animation_lengths(armature):
    animation_lengths = {}
    actions = bpy.data.actions
    for action in actions:
        animation_lengths[action.name] = action.frame_range[-1] - action.frame_range[0]
    return animation_lengths

# Select the armature
selected_obj = bpy.context.active_object
if selected_obj.type != 'ARMATURE':
    raise ValueError("Please select an armature object.")

animation_lengths = get_animation_lengths(selected_obj)
print("Animation Lengths:")
print(animation_lengths)