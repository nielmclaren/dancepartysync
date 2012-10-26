import Image
import os
import sys

baseUrl = 'http://localhost/2012/dmclaren/dancepartysync'

if len(sys.argv) < 2:
    print "Missing argument.";
    print "Usage: python split.py infile.gif outfile.png\n"
    exit()

def getNumFrames(im):
    im.seek(0)
    while 1:
        try:
            im.seek(im.tell() + 1)
        except EOFError:
            return im.tell()

##
# Adjusted to work with transparency.
# Thanks, DSM.
# @see http://stackoverflow.com/questions/4904940/python-converting-gif-frames-to-png
def iterFrames(im):
    w, h = im.size
    try:
        i = 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0: 
                palette = imframe.getpalette()
                prevframe = imframe = imframe.convert('RGBA')
            else:
                imframe.putpalette(palette)
                imframe = imframe.convert('RGBA')

                prevframe.paste(imframe, (0, 0, w, h), imframe)
                imframe = prevframe

            yield imframe
            i += 1
    except EOFError:
        pass

# Converts a GIF animation to a vertical film strip.
def getFilmstrip(im):
    w, h = im.size
    numFrames = getNumFrames(im)
    result = Image.new('RGBA', (w, h * numFrames))

    for i, frame in enumerate(iterFrames(im)):
        result.paste(frame, (0, h * i))

    return result


im = Image.open(sys.argv[1])
strip = getFilmstrip(im)
outFilename = 'out/' + sys.argv[1][3:-3] + 'png'
strip.save(outFilename, **strip.info)

os.system('open "%s/record.html?width=%d&height=%d&frames=%d&image=%s"' % (baseUrl, im.size[0], im.size[1], getNumFrames(im), outFilename))

