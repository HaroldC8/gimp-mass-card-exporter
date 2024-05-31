import os, glob, sys, time, math
from gimpfu import *

Width = 2480
Height = 3508
Border = 100
Spacing = 4

# Calculate next card position based on iteration
def layer_pos(sizeX, sizeY, iteration):
	mod = math.floor((Width - 2*Border) / (sizeX + Spacing))
	x = (int)(Border + (Spacing + sizeX) * (iteration % mod))
	y = (int)(Border + (Spacing + sizeY) * math.floor(iteration/mod))
	return x, y

def save_image(outImage, infile, j):
    outfile = os.path.join(os.path.dirname(infile), "processed{}.png".format(j))
    print "Saving to %s" % outfile
    pdb.gimp_image_merge_visible_layers(outImage, 1)
    pdb.gimp_palette_set_background('white')
    pdb.gimp_image_flatten(outImage)
    pdb.file_png_save2(outImage, outImage.active_layer, outfile, outfile, False, 5, False, False, False, False, False, False, False)
    print "Saved to %s" % outfile
    return gimp.Image(Width, Height, RGB)

def process(infile, outImage, values, iteration):
    print "Processing file %s " % infile
    inImage = pdb.gimp_file_load(infile, infile, run_mode=RUN_NONINTERACTIVE)
    i = 0
    # Changing text and durability position
    for layer in inImage.layers:
		if "Value" in layer.name:
			values[i] = values[i].strip()
			print "Changing value of layer %s to %s" % (layer.name, values[i])
			font = pdb.gimp_text_layer_get_font(layer)
			font_size, font_unit = pdb.gimp_text_layer_get_font_size(layer)
			font_color = pdb.gimp_text_layer_get_color(layer)
			pdb.gimp_text_layer_set_text(layer, values[i])
			pdb.gimp_text_layer_set_font(layer, font)
			pdb.gimp_text_layer_set_font_size(layer, font_size, font_unit)
			pdb.gimp_text_layer_set_color(layer, font_color)
			i += 1
		if "ChangePosImage" in layer.name:
			print "Changing image layer %s y pos to %s" % (layer.name, 90*(9-int(values[2])))
			layer.set_offsets(562, 90*(9-int(values[2])))
    single_layer = pdb.gimp_image_merge_visible_layers(inImage, 1)
    copy_layer = gimp.Layer(outImage, "copytest", Width, Height, RGBA_IMAGE, 100, NORMAL_MODE)
    outImage.add_layer(copy_layer, 1)
    pdb.gimp_edit_copy(single_layer)
    copy_layer = pdb.gimp_edit_paste(copy_layer, FALSE)
    offsetX, offsetY = layer_pos(copy_layer.width, copy_layer.height, iteration)
    print "Success1 %s %s" % (offsetX, offsetY)
    copy_layer.set_offsets(offsetX, offsetY)

def run(directory):
    start=time.time()
    print "Running on directory \"%s\"" % directory
    textfile = glob.glob(os.path.join(directory, '*.txt'))
    infiles = glob.glob(os.path.join(directory, '*.xcf'))
    if len(infiles) == 0 or len(textfile) == 0:
	    print "ERORR: no .xcf or .txt input files in provided directory!"
	    return
    text = open(textfile[0], "r")
    lines = text.readlines()
    if len(lines) % 4 != 0:
	    print "ERORR: .txt file is in an incompatible format!"
	    return
    inImage = pdb.gimp_file_load(infiles[0], infiles[0], run_mode=RUN_NONINTERACTIVE)
    outImage = gimp.Image(Width, Height, RGB)
    j = 0
    it = 0
    for i in range(0, len(lines)/4):
	    if layer_pos(inImage.width, inImage.height, it)[1] + inImage.height + Border > Height:
		    outImage = save_image(outImage, infiles[0], j)
		    j += 1
		    it = 0
	    process(infiles[0], outImage, lines[4*i:4*i+4], it)
	    it += 1
    text.close()
    save_image(outImage, infiles[0], j)
    end=time.time()
    print "Finished, total processing time: %.2f seconds" % (end-start)

if __name__ == "__main__":
    print "Running as __main__ with args: %s" % sys.argv