import os
import shutil
import glob
from pathlib import Path


src_folder_png = os.path.join(Path.home(), "Downloads")
dest_folder_png = os.path.join(Path.home(), "Downloads", "images", "Png images")
pattern_png = "\\*png"

files_png = glob.glob(src_folder_png + pattern_png)

# Adds png files to png folder
for png_file in files_png:
    file_name_png = os.path.basename(png_file)
    shutil.move(png_file, dest_folder_png)
    print("Moved: ", png_file)


src_folder_jpg = os.path.join(Path.home(), "Downloads")
dest_folder_jpg = os.path.join(Path.home(), "Downloads", "images", "Jpeg images")
pattern_jpg = "\\*jpg"

jpg_files = glob.glob(src_folder_jpg + pattern_jpg)

# Adds jpg files to Jpeg folder
for jpg_file in jpg_files:
    file_name_jpg = os.path.basename(jpg_file)
    shutil.move(jpg_file, dest_folder_jpg)
    print("Moved: ", jpg_file)
