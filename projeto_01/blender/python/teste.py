import bpy
import json
from mathutils import Vector

#FILE = r"C:/.../motion_clean.json"
FILE = r"C:/Users/kaiog/Documents/11 - Git/01 - GitHub/nexvisual-computer-vision/projeto/Json/motion_clean.json"


with open(FILE, "r") as f:
    data = json.load(f)

frames = data["frames"]
fps = data["fps"]

bpy.context.scene.render.fps = int(fps)

rigify = bpy.data.objects.get("metarig")
if not rigify:
    raise Exception("Rigify não encontrado")

def create_target():
    arm = bpy.data.armatures.new("TARGET")
    obj = bpy.data.objects.new("TARGET", arm)
    bpy.context.collection.objects.link(obj)

    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    eb = arm.edit_bones

    spine = eb.new("spine")
    spine.head = (0,0,0)
    spine.tail = (0,0,1)

    chest = eb.new("chest")
    chest.head = spine.tail
    chest.tail = (0,0,2)
    chest.parent = spine

    ul = eb.new("upper_arm.L")
    ul.head = (0,0,2)
    ul.tail = (-1,0,2)
    ul.parent = chest

    fl = eb.new("forearm.L")
    fl.head = ul.tail
    fl.tail = (-2,0,2)
    fl.parent = ul

    ur = eb.new("upper_arm.R")
    ur.head = (0,0,2)
    ur.tail = (1,0,2)
    ur.parent = chest

    fr = eb.new("forearm.R")
    fr.head = ur.tail
    fr.tail = (2,0,2)
    fr.parent = ur

    bpy.ops.object.mode_set(mode='OBJECT')
    return obj

target = bpy.data.objects.get("TARGET") or create_target()

def add_constraints():
    def add(pb, target_bone):
        c = pb.constraints.new('COPY_ROTATION')
        c.target = target
        c.subtarget = target_bone
        c.mix_mode = 'REPLACE'
        c.target_space = 'POSE'
        c.owner_space = 'POSE'

    pb = target.pose.bones

    add(pb["upper_arm.L"], "upper_arm.L")
    add(pb["forearm.L"], "forearm.L")
    add(pb["upper_arm.R"], "upper_arm.R")
    add(pb["forearm.R"], "forearm.R")
    add(pb["spine"], "spine")

add_constraints()

def apply_frame(frame_data, frame):
    bpy.context.scene.frame_set(frame)

    pb = target.pose.bones

    for bone_name, vec in frame_data.items():
        if bone_name not in pb:
            continue

        v = Vector(vec).normalized()

        # cria rotação simples olhando vetor (stable)
        pb[bone_name].rotation_mode = 'XYZ'
        pb[bone_name].rotation_euler = v.to_track_quat('Y', 'Z').to_euler()

        pb[bone_name].keyframe_insert("rotation_euler", frame=frame)

for i, f in enumerate(frames):
    apply_frame(f, i+1)

print("TARGET ANIMATED")

def bake(frame):
    bpy.context.scene.frame_set(frame)
    bpy.context.view_layer.update()

    for pb in rigify.pose.bones:
        pb.keyframe_insert("rotation_quaternion", frame=frame)

for i in range(len(frames)):
    bake(i+1)

print("BAKE DONE")