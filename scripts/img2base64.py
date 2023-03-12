from PIL import Image
from io import BytesIO
import base64

file_name = "./assets/000000.jpg"

img = Image.open(file_name) # path to file
img_buffer = BytesIO()
img.save(img_buffer, format=img.format)
byte_data = img_buffer.getvalue()
base64_str = base64.b64encode(byte_data) # bytes
base64_str = base64_str.decode("utf-8") # str

with open("./assets/anime_test.tsv", mode="w") as f:
    f.write(f"1\t1\tabc\tdef\t{base64_str}")