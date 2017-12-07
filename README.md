# Normalise-Luminance-Across-Images
Normalises the pixel values (luminance) of a group of images such that the variance of the group becomes 0

Python script to normalise a group of images so that each image has the same luminance

Uses the formula sqrt(0.241 * (red ** 2) + 0.691 * (green ** 2) + 0.068 * (blue ** 2))

Simply point it to your folder containing your .png images

It will then:

Scan through the images and find the average luminance across the group

For each image increase/decrease the RGB value of all non-white pixels by 1 until it crosses the average
  
  
The end result is then a collection of images that all have the same luminance value
