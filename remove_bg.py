from PIL import Image

def remove_white_bg(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")
    
    data = img.getdata()
    new_data = []
    
    # Tolerancia para el color blanco
    threshold = 220
    
    for item in data:
        # Check if the pixel is close to white
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            # Change to transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_white_bg("fausto.jpg", "fausto.png")
