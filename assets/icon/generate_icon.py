#!/usr/bin/env python3
"""Generate carnival-themed app icon for Meu Carna BH."""

from PIL import Image, ImageDraw
import math

def create_gradient(width, height):
    """Create a purple-to-pink diagonal gradient."""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    # Colors from the carnival theme
    colors = [
        (106, 27, 154),   # Deep purple #6A1B9A
        (156, 39, 176),   # Purple #9C27B0
        (233, 30, 99),    # Pink #E91E63
    ]

    for y in range(height):
        for x in range(width):
            # Diagonal gradient
            t = (x + y) / (width + height)

            if t < 0.5:
                # Blend between first two colors
                t2 = t * 2
                r = int(colors[0][0] * (1 - t2) + colors[1][0] * t2)
                g = int(colors[0][1] * (1 - t2) + colors[1][1] * t2)
                b = int(colors[0][2] * (1 - t2) + colors[1][2] * t2)
            else:
                # Blend between last two colors
                t2 = (t - 0.5) * 2
                r = int(colors[1][0] * (1 - t2) + colors[2][0] * t2)
                g = int(colors[1][1] * (1 - t2) + colors[2][1] * t2)
                b = int(colors[1][2] * (1 - t2) + colors[2][2] * t2)

            draw.point((x, y), fill=(r, g, b))

    return image

def draw_mask(draw, cx, cy, scale, gold=(255, 215, 0), dark_gold=(184, 134, 11)):
    """Draw a carnival mask shape."""
    # Mask body outline points
    points = []
    for i in range(360):
        angle = math.radians(i)
        # Create mask-like shape (wider, shorter ellipse with pointed ends)
        r = scale * (0.9 + 0.1 * math.cos(2 * angle))
        x = cx + r * math.cos(angle) * 1.4
        y = cy + r * math.sin(angle) * 0.5
        points.append((x, y))

    # Draw mask body
    draw.polygon(points, fill=gold, outline=dark_gold)

    # Eye holes
    eye_width = scale * 0.35
    eye_height = scale * 0.25
    left_eye_cx = cx - scale * 0.5
    right_eye_cx = cx + scale * 0.5
    eye_cy = cy - scale * 0.05

    # Left eye
    draw.ellipse([
        left_eye_cx - eye_width, eye_cy - eye_height,
        left_eye_cx + eye_width, eye_cy + eye_height
    ], fill=(74, 20, 140))  # Dark purple

    # Right eye
    draw.ellipse([
        right_eye_cx - eye_width, eye_cy - eye_height,
        right_eye_cx + eye_width, eye_cy + eye_height
    ], fill=(74, 20, 140))  # Dark purple

def draw_feathers(draw, cx, cy, scale):
    """Draw colorful feathers on top of the mask."""
    feather_colors = [
        (156, 39, 176),   # Purple
        (255, 235, 59),   # Yellow
        (0, 188, 212),    # Cyan
        (255, 152, 0),    # Orange
        (233, 30, 99),    # Pink
    ]

    feather_positions = [
        (-0.8, -0.6, -25),  # x_offset, y_offset, rotation
        (-0.4, -0.75, -12),
        (0, -0.85, 0),
        (0.4, -0.75, 12),
        (0.8, -0.6, 25),
    ]

    for i, (x_off, y_off, rot) in enumerate(feather_positions):
        color = feather_colors[i % len(feather_colors)]
        fx = cx + x_off * scale
        fy = cy + y_off * scale

        # Draw elongated ellipse for feather
        feather_width = scale * 0.15
        feather_height = scale * 0.5

        # Create rotated feather
        for j in range(int(feather_height * 2)):
            t = j / (feather_height * 2)
            # Tapered width
            w = feather_width * (1 - abs(t - 0.3) * 1.5)
            if w < 0:
                w = 0

            y = fy - feather_height + j
            x = fx + math.sin(math.radians(rot)) * (j - feather_height)

            if w > 0:
                draw.ellipse([x - w, y - 2, x + w, y + 2], fill=color)

def draw_gems(draw, cx, cy, scale):
    """Draw decorative gems on the mask."""
    # Center gem (pink)
    gem_cx = cx
    gem_cy = cy - scale * 0.35
    draw.ellipse([gem_cx - 15, gem_cy - 15, gem_cx + 15, gem_cy + 15], fill=(233, 30, 99))
    draw.ellipse([gem_cx - 10, gem_cy - 10, gem_cx + 10, gem_cy + 10], fill=(255, 64, 129))
    draw.ellipse([gem_cx - 5, gem_cy - 8, gem_cx + 2, gem_cy - 3], fill=(255, 255, 255, 150))

    # Side gems (cyan)
    for side in [-1, 1]:
        gem_x = cx + side * scale * 0.9
        gem_y = cy - scale * 0.15
        draw.ellipse([gem_x - 10, gem_y - 10, gem_x + 10, gem_y + 10], fill=(0, 188, 212))
        draw.ellipse([gem_x - 4, gem_y - 6, gem_x + 1, gem_y - 2], fill=(255, 255, 255, 150))

def draw_confetti(draw, width, height):
    """Draw confetti dots around the icon."""
    confetti = [
        (0.15, 0.2, 12, (255, 235, 59)),   # Yellow
        (0.85, 0.18, 10, (0, 188, 212)),    # Cyan
        (0.12, 0.75, 9, (255, 152, 0)),     # Orange
        (0.88, 0.8, 11, (76, 175, 80)),     # Green
        (0.2, 0.45, 8, (255, 235, 59)),     # Yellow
        (0.82, 0.5, 9, (233, 30, 99)),      # Pink
        (0.3, 0.85, 7, (0, 188, 212)),      # Cyan
        (0.7, 0.88, 8, (255, 152, 0)),      # Orange
    ]

    for x_pct, y_pct, radius, color in confetti:
        x = int(width * x_pct)
        y = int(height * y_pct)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=color)

def main():
    size = 1024

    # Create gradient background
    image = create_gradient(size, size)
    draw = ImageDraw.Draw(image)

    # Draw confetti in background
    draw_confetti(draw, size, size)

    # Center and scale for the mask
    cx = size // 2
    cy = size // 2 + 50  # Slightly lower to make room for feathers
    scale = size * 0.25

    # Draw feathers first (behind mask)
    draw_feathers(draw, cx, cy, scale)

    # Draw the mask
    draw_mask(draw, cx, cy, scale)

    # Draw gems on top
    draw_gems(draw, cx, cy, scale)

    # Save the icon
    image.save('icon.png', 'PNG')
    print(f'Icon saved as icon.png ({size}x{size})')

    # Also create an adaptive icon foreground (with transparent background)
    fg_image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    fg_draw = ImageDraw.Draw(fg_image)

    # Draw mask elements on transparent background
    draw_feathers(fg_draw, cx, cy, scale)
    draw_mask(fg_draw, cx, cy, scale)
    draw_gems(fg_draw, cx, cy, scale)

    fg_image.save('icon_foreground.png', 'PNG')
    print(f'Foreground icon saved as icon_foreground.png ({size}x{size})')

if __name__ == '__main__':
    main()
