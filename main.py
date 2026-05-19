import math
from pathlib import Path

def aurora_path(n=24, radius=12.0, twist=0.45):
    points = []
    for i in range(n):
        t = i / (n - 1)
        angle = t * 2 * math.pi * 1.35
        r = radius * (0.55 + 0.45 * math.sin(t * math.pi))
        x = r * math.cos(angle + twist * t)
        y = r * math.sin(angle)
        points.append((round(x, 3), round(y, 3)))
    return points

def normalize_points(points):
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    def scale(v, lo, hi):
        if hi == lo:
            return 0.0
        return (v - lo) / (hi - lo)

    return [(scale(x, min_x, max_x), scale(y, min_y, max_y)) for x, y in points]

def render_ascii(points, width=42, height=18, mark="*"):
    grid = [[" " for _ in range(width)] for _ in range(height)]
    for x, y in normalize_points(points):
        cx = min(width - 1, max(0, int(x * (width - 1))))
        cy = min(height - 1, max(0, int((1 - y) * (height - 1))))
        grid[cy][cx] = mark
    return "\n".join("".join(row) for row in grid)

def save_points(points, filename="aurora_points.txt"):
    text = "\n".join(f"{x:.3f}, {y:.3f}" for x, y in points)
    Path(filename).write_text(text, encoding="utf-8")

def main():
    points = aurora_path()
    save_points(points)

    print("Aurora Path Coordinates:")
    for p in points:
        print(p)

    print("\nASCII Preview:")
    print(render_ascii(points))

    print("\nSaved: aurora_points.txt")

if __name__ == "__main__":
    main()
