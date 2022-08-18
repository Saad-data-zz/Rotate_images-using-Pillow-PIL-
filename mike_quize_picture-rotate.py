from PIL import Image

image_obj = Image.open("image_path.png")
rotated_image = image_obj.rotate(90)
rotated_image.save("rotated_image_path.png")