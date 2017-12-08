from PIL import Image, ImageStat
import glob
import numpy as np
import math

path = 'C:\\folder'
files = glob.glob(path+'/*.png')
imagewidth = 256  # Number pixels in width
imageheight = 256  # Number pixels in height

def getlum(im):
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean
    lum = math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
    return lum


def distance(avg, image):
        return abs(avg - getlum(image))


def main():
    # Calculate average
    lums = np.empty(len(files))
    for i, filename in enumerate(files):
        im = Image.open(filename)
        lums[i] = getlum(im)
    averageLum = np.mean(lums)

    print('Starting average luminance of ', averageLum, '(stdev', np.std(lums), ')')

    # Adjust images
    newlums = np.empty(len(files))
    for i, filename in enumerate(files):
        im = Image.open(filename)
        pixels = im.load()
        if getlum(im) > averageLum:
            modifier = -1
        else:
            modifier = 1

        # Iterate through all pixels and adjust them slightly while they are still not equal to average
        while distance(averageLum, im) > 1:
            for k in range(imagewidth):
                for l in range(imageheight):
                    if not all(i > 245 for i in pixels[k, l]):  # Skip whitespace
                        pixels[k, l] = tuple(x + modifier for x in pixels[k, l])

        im.save(filename)
        newlums[i] = getlum(im)
        print(i,'done')
    print('Finishing average luminance of ', np.mean(newlums), '(stdev', np.std(newlums), ')')


if __name__ == '__main__':
    main()


