import os
import folder_paths
import shutil
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
# 传入参考图片到服务器
current_path = os.path.dirname(os.path.abspath(__file__))
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
pngs = os.listdir(os.path.join(current_path,"images"))
pngs_path = [os.path.join(current_path,"images",x) for x in pngs]
input_folder_path = folder_paths.get_input_directory()
for png_path in pngs_path:
    png_name = os.path.split(png_path)[1]
    input_png_path = os.path.join(input_folder_path,png_name)
    if os.path.exists(input_png_path):
        continue
    else:
        shutil.copy2(png_path,input_png_path)