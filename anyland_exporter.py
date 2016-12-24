import bpy
import bpy_extras
from bpy_extras.io_utils import ExportHelper 
import json

class ExportAnylandJSON(bpy.types.Operator, ExportHelper):
    """Export as Anyland JSON"""
    bl_idname = "export.anyland_json"
    bl_label = "Export Anyland JSON"
    
    filename_ext = ".json"
    
    def execute(self, context):
        filepath = self.filepath
        filepath = bpy.path.ensure_ext(filepath, self.filename_ext)
        thing = {}

        # Name
        thing['n'] = 'test'
        # Parts
        thing['p'] = []

        for obj in context.scene.objects:
            if obj.type == 'MESH':
                if 'baseID' not in obj.data:
                    continue
                print(obj.name + ' (' + str(obj.data['baseID']) + ')' + ': ' + str(len(obj.data.vertices)))
                # Part
                thing['p'].append({
                    # Base shape ID
                    'b': obj.data['baseID'],
                    # State
                    's': [{
                        # Position
                        'p': (obj.location[0], obj.location[1], obj.location[2]),
                        # Rotation
                        'r': (obj.rotation_euler[0] % 360, obj.rotation_euler[1] % 360, obj.rotation_euler[2] % 360),
                        # Scale
                        's': (obj.scale[0], obj.scale[1], obj.scale[2]),
                        # Color
                        'c': (obj.active_material.diffuse_color[0], obj.active_material.diffuse_color[1], obj.active_material.diffuse_color[2])
                    }]
                })
        
        with open(filepath, 'w') as f:
            json.dump(thing, f)

        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager

        if True:
            # File selector
            wm.fileselect_add(self) # will run self.execute()
            return {'RUNNING_MODAL'}
        elif True:
            # search the enum
            wm.invoke_search_popup(self)
            return {'RUNNING_MODAL'}
        elif False:
            # Redo popup
            return wm.invoke_props_popup(self, event) #
        elif False:
            return self.execute(context)

def exportMenu(self, context):
    self.layout.operator(ExportAnylandJSON.bl_idname, text="Anyland (.json)")
