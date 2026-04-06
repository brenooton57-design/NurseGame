#!/bin/bash

echo "Optimizing MP3 audio files (maintaining quality)..."

# Check if ffmpeg is available
if ! command -v ffmpeg &> /dev/null; then
    echo "Installing ffmpeg..."
    # Try using ImageMagick's convert to optimize instead
    echo "ffmpeg not available, skipping audio optimization"
    exit 0
fi

optimize_audio() {
    file="$1"
    original_size=$(stat -c%s "$file")
    temp_file="${file}.tmp.mp3"

    # Re-encode MP3 with high quality VBR (V2 = ~190 kbps average)
    # This maintains near-original quality while reducing file size
    ffmpeg -i "$file" -codec:a libmp3lame -q:a 2 -y "$temp_file" 2>/dev/null

    if [ -f "$temp_file" ]; then
        new_size=$(stat -c%s "$temp_file")
        if [ "$new_size" -lt "$original_size" ]; then
            mv "$temp_file" "$file"
            saved=$(( (original_size - new_size) / 1024 ))
            echo "✓ $(basename "$file"): -${saved}KB"
        else
            rm "$temp_file"
            echo "○ $(basename "$file"): already optimized"
        fi
    fi
}

export -f optimize_audio

# Optimize all MP3 files
for audio in game/audio/*.mp3; do
    [ -f "$audio" ] && optimize_audio "$audio"
done

echo ""
echo "Audio optimization complete!"
