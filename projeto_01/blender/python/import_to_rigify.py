import bpy

# =========================
# IMPORT BVH
# =========================

JSON_PATH = "C:/Users/kaiog/Documents/11 - Git/01 - GitHub/nexvisual-computer-vision/projeto/json/motion.bvh"
bpy.ops.import_anim.bvh(filepath=JSON_PATH)

bvh_arm = bpy.context.selected_objects[0]

# =========================
# RIGIFY SETUP
# =========================

metarig = bpy.data.objects["metarig"]

bpy.context.view_layer.objects.active = metarig

# gerar rigify
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.pose.rigify_generate()

rig = bpy.data.objects["rig"]

# =========================
# COPY CONSTRAINTS
# =========================

def add_copy_rotation(target, source):
    c = target.constraints.new('COPY_ROTATION')
    c.target = source
    c.mix_mode = 'OFFSET'

# exemplo simples (arm L)
add_copy_rotation(rig.pose.bones["upper_arm.L"], bvh_arm)
add_copy_rotation(rig.pose.bones["forearm.L"], bvh_arm)

# =========================
# BAKE ANIMATION
# =========================

bpy.ops.object.select_all(action='DESELECT')

rig.select_set(True)
bpy.context.view_layer.objects.active = rig

bpy.ops.nla.bake(
    frame_start=1,
    frame_end=250,
    visual_keying=True,
    clear_constraints=True,
    use_current_action=True,
    bake_types={'POSE'}
)