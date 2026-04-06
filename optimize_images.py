#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

def get_size_mb(filepath):
    return os.path.getsize(filepath) / (1024 * 1024)

def optimize_png(filepath):
    """Optimize PNG with ImageMagick maintaining quality"""
    original_size = get_size_mb(filepath)
    temp_file = str(filepath) + ".tmp"

    # Use ImageMagick with high quality settings
    cmd = [
        'convert', str(filepath),
        '-strip',  # Remove metadata
        '-quality', '95',
        '-define', 'png:compression-level=9',
        '-define', 'png:compression-strategy=1',
        temp_file
    ]

    result = subprocess.run(cmd, capture_output=True)

    if result.returncode == 0 and os.path.exists(temp_file):
        new_size = get_size_mb(temp_file)
        if new_size < original_size:
            os.replace(temp_file, filepath)
            return original_size, new_size, True
        else:
            os.remove(temp_file)
            return original_size, original_size, False

    return original_size, original_size, False

def main():
    game_dir = Path('/tmp/cc-agent/65400877/project/game')

    total_original = 0
    total_optimized = 0
    count = 0

    print("Starting PNG optimization (maintaining quality)...\n")

    # Find all PNG files
    for png_file in game_dir.rglob('*.png'):
        if '.bak' in str(png_file):
            continue

        original, optimized, changed = optimize_png(png_file)
        total_original += original
        total_optimized += optimized
        count += 1

        if changed:
            savings = original - optimized
            percent = (savings / original) * 100
            print(f"✓ {png_file.name}: {original:.2f}MB → {optimized:.2f}MB (-{percent:.1f}%)")

        if count % 20 == 0:
            print(f"  ... processed {count} images")

    total_saved = total_original - total_optimized
    percent_saved = (total_saved / total_original) * 100 if total_original > 0 else 0

    print(f"\n{'='*60}")
    print(f"PNG Optimization Complete!")
    print(f"Total images: {count}")
    print(f"Original size: {total_original:.2f} MB")
    print(f"Optimized size: {total_optimized:.2f} MB")
    print(f"Space saved: {total_saved:.2f} MB ({percent_saved:.1f}%)")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
