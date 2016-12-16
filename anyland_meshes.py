import os
import bpy
import bpy.utils.previews

custom_icons = None

class AnylandBaseShape(bpy.types.Operator):
    """Anyland Base Shape"""
    bl_idname = 'anyland.base_shape'
    bl_label = 'Anyland Base Shape'
    bl_options = {'REGISTER', 'UNDO'}

    items = (('cube', 'Cube', 'Anyland Cube', 'MESH_CUBE', 1),
             ('pyramid', 'Pyramid', 'Anyland Pyramid', 'MESH_DATA', 2),
             ('sphere', 'Sphere', 'Anyland Sphere', 'MATSPHERE', 3),
             ('cone', 'Cone', 'Anyland Cone', 'MESH_CONE', 4),
             ('cylinder', 'Cylinder', 'Anyland Cylinder', 'MESH_CYLINDER', 5),
             ('triangle', 'Triangle', 'Anyland Triangle', 'MARKER', 6),
             ('trapeze', 'Trapeze', 'Anyland Trapeze', 'MESH_DATA', 7),
             ('hedra', 'Hedra', 'Anyland Hedra', 'PMARKER', 8),
             ('icosphere', 'Icosphere', 'Anyland Icosphere', 'MESH_ICOSPHERE', 9),
             ('low-poly-sphere', 'Low-poly Sphere', 'Anyland LowPolySphere', 'MESH_UVSPHERE', 10),
             ('ramp', 'Ramp', 'Anyland Ramp', 'MESH_DATA', 11),
             ('jitter-cube', 'Jittered Cube', 'Anyland JitterCube', 'MESH_DATA', 12),
             ('chamfer-cube', 'Chamfered Cube', 'Anyland ChamferCube', 'MESH_DATA', 13),
             ('spike', 'Spike', 'Anyland Spike', 'MESH_DATA', 14),
             ('low-poly-cylinder', 'Low-poly Cylinder', 'Anyland LowPolyCylinder', 'MESH_DATA', 15),
             ('half-sphere', 'Half Sphere', 'Anyland HalfSphere', 'MESH_DATA', 16),
             ('jitter-sphere', 'Jittered Sphere', 'Anyland JitterSphere', 'MESH_DATA', 17))

    type = bpy.props.EnumProperty(items = items, name = 'type')
    
    baseIDmap = dict([(i[0], int(i[4])) for i in items])

    def draw(self, context):
        self.layout.prop(self, 'type')
        
    def execute(self, context):
        bpy.ops.wm.collada_import(filepath=os.path.join(os.path.dirname(__file__), 'base-shapes', self.properties.type + '.dae'))
        bpy.context.selected_objects[0].data['baseID'] = AnylandBaseShape.baseIDmap[self.properties.type]
        return {'FINISHED'}

def meshMenu(self, context):
    self.layout.separator()
    self.layout.operator_menu_enum(AnylandBaseShape.bl_idname, 'type', text='Anyland', icon='SPACE2')