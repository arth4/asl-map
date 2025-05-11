import os
import json
import re

def generate_gif_mapping(root_dir='.'):
    mapping = {}

    # Regex to match coord folders: coord_<cx>_<cy>
    pattern = re.compile(r'^coord_(\d+)_(\d+)$')

    for entry in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, entry)
        if os.path.isdir(folder_path) and pattern.match(entry):
            gif_files = sorted([
                f for f in os.listdir(folder_path)
                if f.endswith('.gif')
            ])
            if gif_files:
                mapping[entry] = [os.path.join("gifs", entry, f).replace('\\', '/') for f in gif_files]

    return mapping

if __name__ == '__main__':
    gif_mapping = generate_gif_mapping()
    with open('gif_mapping.json', 'w') as f:
        json.dump(gif_mapping, f, indent=4)
    print("✅ gif_mapping.json created with", len(gif_mapping), "entries.")
