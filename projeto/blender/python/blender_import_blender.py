
# =========================
# BLENDER SCRIPT - IMPORT POSE.JSON
# =========================

import bpy
import json

# =========================
# CARREGAR DADOS
# =========================

with open("pose.json", "r") as f:
    data = json.load(f)

# =========================
# OBJETO ARMATURE
# =========================

armature = bpy.data.objects["Armature"]

# =========================
# CONFIGURAÇÃO DE ANIMAÇÃO
# =========================

scene = bpy.context.scene
scene.frame_start = 0
scene.frame_end = len(data)

# =========================
# ANIMAÇÃO
# =========================

for frame, joints in data.items():
    frame = int(frame)
    scene.frame_set(frame)

    for joint_id, (x, y, z) in joints.items():

        bone_name = str(joint_id)

        if bone_name not in armature.pose.bones:
            continue

        bone = armature.pose.bones[bone_name]

        # aplica posição
        bone.location.x = x
        bone.location.y = y
        bone.location.z = z

        # grava keyframe
        bone.keyframe_insert(data_path="location")

print("Animação importada com sucesso")