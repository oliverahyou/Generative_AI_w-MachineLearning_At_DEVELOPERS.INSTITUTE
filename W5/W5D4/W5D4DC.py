# Daily Challenge: Hands-On Image Transformation and Visualization
from PIL import Image
image_path = '19_010.png'
original_image = Image.open(image_path)
img = Image.open("19_010.png")
img.show()
rotated_img = img.rotate(30)
rotated_img.show()
from PIL import ImageOps
horizontal_flip = ImageOps.mirror(img)
vertical_flip = ImageOps.flip(img)
horizontal_flip.show()
vertical_flip.show()
width, height = img.size
new_width = int(width * 1.2)
new_height = int(height * 1.2)
zoomed_img = img.resize((new_width, new_height))
zoomed_img.show()



