from data import get_major_colors, get_minor_colors
from computation import generate_color_map

def print_color_map():
    major_colors = get_major_colors()
    minor_colors = get_minor_colors()
    color_map = generate_color_map(major_colors, minor_colors)

    for entry in color_map:
        print(f"{entry[0]} | {entry[1]} | {entry[2]}")

    print(f"Total pairs: {len(color_map)}")
    return len(color_map)
