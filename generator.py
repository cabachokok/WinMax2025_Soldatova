from PIL import Image, ImageDraw
import random

palettes = {
    "океан": ["#1B3B6F", "#246EB9", "#64A0D6", "#A9D6E5"],
    "пустыня": ["#C2B280", "#E1C699", "#F5E1A4", "#F8F1C0"],
    "лес": ["#2C5F2D", "#519872", "#88B04B", "#BCE784"],
    "город": ["#4A4A4A", "#7D7D7D", "#B0B0B0", "#D9D9D9"],
    "пляж": ["#FEE9A4", "#FECF89", "#FEBE6A", "#FD7E14"],
    "ледник": ["#CDECF5", "#A1D6E2", "#79C9E2", "#5AA4C7"],
    "горы": ["#555555", "#777777", "#999999", "#BBBBBB"],
    "пещера": ["#2E2E2E", "#4B4B4B", "#6A6A6A", "#8C8C8C"],
    "болото": ["#3B5323", "#556B2F", "#6B8E23", "#90EE90"]
}

size = [8, 16, 32]
details = ["низкий", "средний", "высокий"]

def generate_tile(tile_size, palette, detail_level):
    img = Image.new("RGB", (tile_size, tile_size), color=palette[0])
    draw = ImageDraw.Draw(img)
    
    if detail_level == "низкий":
        num_elements = random.randint(2, 4)
    elif detail_level == "средний":
        num_elements = random.randint(4, 8)
    else:
        num_elements = random.randint(8, 12)
    
    for _ in range(num_elements):
        x0 = random.randint(0, tile_size-1)
        y0 = random.randint(0, tile_size-1)
        x1 = random.randint(x0, tile_size)
        y1 = random.randint(y0, tile_size)
        color = random.choice(palette)
        draw.rectangle([x0, y0, x1, y1], fill=color)
    
    return img

def generate_tileset(rows, cols, tile_size, palette_name, detail_level):
    palette = palettes[palette_name]
    tileset_img = Image.new("RGB", (cols*tile_size, rows*tile_size))
    
    for r in range(rows):
        for c in range(cols):
            tile = generate_tile(tile_size, palette, detail_level)
            tileset_img.paste(tile, (c*tile_size, r*tile_size))
    
    return tileset_img
