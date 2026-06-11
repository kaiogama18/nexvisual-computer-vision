import bpy
import json
import os

filepath = bpy.path.abspath("//json/metarig.json")

obj = bpy.context.active_object

if obj and obj.type == 'ARMATURE':
    rig_data = obj.data
    bone_hierarchy = {}

    for bone in rig_data.bones:
        bone_hierarchy[bone.name] = {
            "parent": bone.parent.name if bone.parent else "",
            "matrix_local": [list(row) for row in bone.matrix_local],
        }

    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(filepath, 'w') as f:
        json.dump(bone_hierarchy, f, indent=4)

    print(f"Exported rig to {filepath}")
else:
    print("Please select an armature object and make it active.")