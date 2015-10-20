import bpy
from bpy import context
from math import sin, cos, radians
import random as rand

bpy.context.scene.render.resolution_x = 500
bpy.context.scene.render.resolution_y = 250


ii = 0
while ii < 100:
    ii += 1
    for material in bpy.data.materials:
        material.user_clear();
        bpy.data.materials.remove(material);
    
    for texture in bpy.data.textures:
        texture.user_clear();
        bpy.data.textures.remove(texture);

    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    links = tree.links
 
    # clear default nodes
    for n in tree.nodes:
        tree.nodes.remove(n)
    
    
    light = bpy.data.objects['Lamp']
    bpy.data.objects['Lamp'].data.use_shadow = False
    bpy.data.objects['Lamp'].data.energy = 5.0
    light.select = False
    camera = bpy.data.objects['Camera']
    camera.select = False

    for item in bpy.data.objects:  
        if item.type == "MESH":  
            bpy.data.objects[item.name].select = True
            bpy.ops.object.delete()
        
    for item in bpy.data.meshes:
      bpy.data.meshes.remove(item)
  
    scene = bpy.context.scene
    magn = 8;
    bpy.ops.mesh.primitive_cube_add(location=((0.5-rand.random())*magn, (0.5-rand.random())*magn, (0.5-rand.random())*magn))
    bpy.ops.transform.rotate(value=rand.random()*3.14, axis=(rand.random(), rand.random(), rand.random()), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.material.new()
    mat1 = bpy.data.materials['Material']
    mat1.diffuse_color = (rand.random(), rand.random(), rand.random())

    bpy.ops.material.new()
    mat2 = bpy.data.materials['Material.001']
    mat2.diffuse_color = (rand.random(), rand.random(), rand.random())

    bpy.data.objects['Cube'].data.materials.append(mat1)
    #bpy.data.objects['Cube'].data.textures.append(bpy.data.textures['Texture'])


    bpy.ops.mesh.primitive_cube_add(location=((0.5-rand.random())*magn, (0.5-rand.random())*magn, (0.5-rand.random())*magn))
    bpy.ops.transform.rotate(value=rand.random()*3.14, axis=(rand.random(), rand.random(), rand.random()), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.data.objects['Cube.001'].data.materials.append(mat2)

    bpy.ops.mesh.primitive_plane_add(radius=1, enter_editmode=False, location=(7, 8, -1), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    bpy.ops.mesh.primitive_plane_add(radius=1, enter_editmode=False, location=(-3, -2, -1), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=3.14, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.mesh.primitive_plane_add(location=(3.5, 0, -5), rotation=(0, 0, 0))
    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    bpy.ops.mesh.primitive_plane_add(location=(3.5, 0, 9), rotation=(0, 0, 0))
    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

    camera = bpy.data.objects['Camera']
    camera.select = True
    camera.rotation_mode = 'XYZ'
    angle1 = 1.3 + (0.5-rand.random())*1
    angle2 = (0.5-rand.random())*1
    angle3 = 0.75 + (0.5-rand.random())*1
    camera.rotation_euler = (angle1, angle2, angle3)
    Cam_x = 10 +(0.5-rand.random())*2
    Cam_y = -3 + (0.5-rand.random())*2
    Cam_z = 3 + (0.5-rand.random())*2
    camera.location = (Cam_x,Cam_y,Cam_z)

    scene.render.use_multiview = True
    scene.render.views_format = 'STEREO_3D'

    camera.data.stereo.convergence_distance = 10000
    camera.data.lens = 15
    camera.data.stereo.interocular_distance = 0.3
    #camera.rotate(value=rand.random()*3.14, axis=(rand.random(), rand.random(), rand.random()), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


    rl = tree.nodes.new(type="CompositorNodeRLayers")    
    composite = tree.nodes.new(type = "CompositorNodeComposite")
    composite.location = 200,0
    links.new(rl.outputs[3],composite.inputs[0])  #

    scene = bpy.context.scene
    scene.render.layers['RenderLayer'].use_pass_mist = True
    scene.world.mist_settings.falloff = 'LINEAR'
    scene.world.mist_settings.intensity = 0.0
    scene.world.mist_settings.depth = 19.2

    links.new(rl.outputs['Mist'],composite.inputs['Image'])

    scene.render.use_multiview = False

    scene.render.filepath = 'Depth_map/DepthMap_'+str(ii)+'.png'
    bpy.ops.render.render( write_still=True ) 

    links.new(rl.outputs['Image'],composite.inputs['Image'])

    scene.render.use_multiview = True

    scene.render.filepath = 'StereoImages/Stereoscopic_'+str(ii)+'.png'
    bpy.ops.render.render( write_still=True ) 
