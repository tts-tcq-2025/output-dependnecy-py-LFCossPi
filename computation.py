def generate_color_map(major_colors, minor_colors):
    color_map = []
    pair_number = 0
    for major in major_colors:
        for minor in minor_colors:
            color_map.append((pair_number, major, minor))
            pair_number += 1
    return color_map
