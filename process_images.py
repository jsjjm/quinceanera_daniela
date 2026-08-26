from PIL import Image
import os

def remove_white_bg(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    data = img.getdata()
    
    new_data = []
    for item in data:
        # Change pure white (or close to it) to transparent
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

# Paths
brain_dir = r"C:\Users\OS\.gemini\antigravity\brain\7c690364-d1db-458d-9c74-f1f9fcc65ca6"
dest_dir = r"C:\Users\OS\.gemini\antigravity\scratch\quinceanera_daniela"

bg_img = os.path.join(brain_dir, "enchanted_forest_bg_1787779572263.png")
princess_img = os.path.join(brain_dir, "princess_tiana_1787779650288.png")

# Copy bg image
import shutil
shutil.copy(bg_img, os.path.join(dest_dir, "bg.png"))

# Process princess image
remove_white_bg(princess_img, os.path.join(dest_dir, "princess.png"))
print("Images processed successfully.")
