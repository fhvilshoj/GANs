import imageio
import os 

images = []
for f in range(0, 31):
	images.append(imageio.imread(str(f) + ".png"))

print(images)

imageio.mimsave("gif.gif", images, duration=.25)
