import os
import plistlib
import sys
import xml.etree.ElementTree as ET


def write_contents_plist(ufo_path):
    glyph_dir = os.path.join(ufo_path, 'glyphs')
    glif_files = [
        file for file in os.listdir(glyph_dir) if
        os.path.splitext(file)[-1] == '.glif']

    d_dict = {}

    for glif_file in glif_files:
        glif_path = os.path.join(glyph_dir, glif_file)
        tree = ET.parse(glif_path)
        root = tree.getroot()
        # we need to enter the XML file to find out the
        # glyph name assigned in the UFO
        gname = list(root.findall(".")[0].items())[0][1]
        d_dict[gname] = glif_file

    pl_path = os.path.join(ufo_path, 'glyphs', 'contents.plist')
    with open(pl_path, 'wb') as pl_file:
        plistlib.dump(d_dict, pl_file)

    print('done')


ufo_paths = sys.argv[1:]
for ufo_path in ufo_paths:
    if os.path.exists(ufo_path) and os.path.isdir(ufo_path):
        write_contents_plist(ufo_path)
    else:
        print('Please supply a UFO file.')
