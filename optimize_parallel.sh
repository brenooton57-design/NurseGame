#!/bin/bash

echo "Optimizing PNG images in parallel..."

# Function to optimize a single PNG
optimize_png() {
    file="$1"
    if [[ "$file" == *".bak"* ]]; then
        return
    fi

    original_size=$(stat -c%s "$file")
    temp_file="${file}.tmp"

    convert "$file" -strip -quality 95 -define png:compression-level=9 "$temp_file" 2>/dev/null

    if [ -f "$temp_file" ]; then
        new_size=$(stat -c%s "$temp_file")
        if [ "$new_size" -lt "$original_size" ]; then
            mv "$temp_file" "$file"
            saved=$(( (original_size - new_size) / 1024 ))
            echo "✓ $(basename "$file"): -${saved}KB"
        else
            rm "$temp_file"
        fi
    fi
}

export -f optimize_png

# Find and optimize all PNGs in parallel (16 jobs at once)
find game -name "*.png" -type f ! -path "*/.bak/*" | \
    xargs -P 16 -I {} bash -c 'optimize_png "$@"' _ {}

echo ""
echo "PNG optimization complete!"
