import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600), output_format="JPEG"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    img_resized = img.resize(size)
                    base_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                    img_resized.save(output_path, output_format)
                    print(f"✅ {filename} resized and saved as {output_path}")
            except Exception as e:
                print(f"❌ Could not process {filename}: {e}")


if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    target_size = (800, 600)
    output_format = "JPEG"
    
    resize_images(input_folder, output_folder, target_size, output_format)
