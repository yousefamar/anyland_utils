import bpy

# NOTE: This script is not used runtime, just to prepare the models

def get_override(area_type, region_type):
    for area in bpy.context.screen.areas: 
        if area.type == area_type:             
            for region in area.regions:                 
                if region.type == region_type:                    
                    override = {'area': area, 'region': region} 
                    return override
    raise RuntimeError("Wasn't able to find", region_type," in area ", area_type,
                        "\n Make sure it's open while executing script.")

override = get_override('VIEW_3D', 'WINDOW')

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        if 'baseID' not in obj.data:
            continue
        print(obj.name + ' (' + str(obj.data['baseID']) + ')' + ': ' + str(len(obj.data.vertices)))
        
        scale = 0.0
        if obj.name == 'Cube':
            scale = 0.175
        elif obj.name in [
                'JitterCube',
                'JitterSphere',
                'ThickRing',
                'ThinRing',
                'HalfRing',
                'ChamferCube',
                'Spike'
            ]:
            scale = 0.06
        else:
            scale = 0.125
        
        bpy.context.scene.objects.active = obj
        bpy.context.scene.cursor_location = (obj.location[0], obj.location[1], obj.location[2])
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        bpy.ops.mesh.reveal()
        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.transform.resize(override, value=(1/obj.scale[0], 1/obj.scale[1], 1/obj.scale[2]))
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        
        obj.scale[0] = scale
        obj.scale[1] = scale
        obj.scale[2] = scale