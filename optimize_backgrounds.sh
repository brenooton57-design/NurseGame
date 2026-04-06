#!/bin/bash

echo "Optimizing large background images (quality 92)..."

# List of large background files
backgrounds=(
    "game/images/break_room.png"
    "game/images/locker_room.png"
    "game/images/Recepcao_hospital.png"
    "game/images/fundo_quarto.png"
    "game/images/Corredor_hospital.png"
    "game/images/nurse_station.png"
    "game/images/hospital_morning.png"
    "game/images/Fundo_hospital.png"
    "game/images/Fundo_casa.png"
    "game/images/main_menu.png"
    "game/images/bar1.png"
    "game/images/fundo_bar.png"
)

total_saved=0

for bg in "${backgrounds[@]}"; do
    if [ -f "$bg" ]; then
        original_size=$(stat -c%s "$bg")
        temp_file="${bg}.tmp"

        # More aggressive compression for backgrounds (quality 92 instead of 95)
        convert "$bg" -strip -quality 92 -define png:compression-level=9 "$temp_file" 2>/dev/null

        if [ -f "$temp_file" ]; then
            new_size=$(stat -c%s "$temp_file")
            if [ "$new_size" -lt "$original_size" ]; then
                mv "$temp_file" "$bg"
                saved=$(( (original_size - new_size) / 1024 ))
                total_saved=$(( total_saved + saved ))
                echo "✓ $(basename "$bg"): -${saved}KB"
            else
                rm "$temp_file"
            fi
        fi
    fi
done

echo ""
echo "Background optimization complete!"
echo "Total saved: ${total_saved}KB (~$((total_saved / 1024))MB)"
