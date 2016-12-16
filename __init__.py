import os
import bpy
from .anyland_exporter import *
from .anyland_meshes import *

bl_info = {
    "name": "Anyland Utils",
    "author": "Yousef Amar <yousef@amar.io> (http://yousefamar.com/)",
    "version": (0, 1, 0),
    "blender": (2, 78, 0),
    "description": "Add Anyland meshes to a scene, and export geometry to Anyland JSON format for upload",
    "category": "Import-Export"
}

def register():
    bpy.utils.register_class(ExportAnylandJSON)
    bpy.utils.register_class(AnylandBaseShape)
    bpy.types.INFO_MT_file_export.append(exportMenu)
    bpy.types.INFO_MT_add.append(meshMenu)

def unregister():
    bpy.types.INFO_MT_add.remove(meshMenu)
    bpy.types.INFO_MT_file_export.remove(exportMenu)
    bpy.utils.unregister_class(AnylandBaseShape)
    bpy.utils.unregister_class(ExportAnylandJSON)

if __name__ == "__main__":
    register()