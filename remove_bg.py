from rembg import remove
from PIL import Image

input_path = "assets/img/bg/banner-3.jpg"
output_path = "assets/img/bg/banner-3.png"

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
print("Background removed successfully!")
