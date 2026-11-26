"""Bounded checks of the two support-function fits, Python 3 standard library."""

import math


def polygon(n, offset, radius):
    return [(radius * math.cos(offset + 2 * math.pi * i / n),
             radius * math.sin(offset + 2 * math.pi * i / n))
            for i in range(n)]


def check(n):
    alpha = math.pi / n
    c, s = math.cos(alpha), math.sin(alpha)
    vertices = polygon(n, 0.0, 1.0)
    polar_vertices = polygon(n, alpha, 1.0 / c)

    count = n * 256  # Include vertex and edge-normal directions.
    p, q = [], []
    for i in range(count):
        angle = 2 * math.pi * i / count
        x, y = math.cos(angle), math.sin(angle)
        shadow = [-y * a + x * b for a, b in vertices]
        p.append(max(shadow) - min(shadow))
        q.append(max(x * a + y * b for a, b in polar_vertices))

    def max_error(scale):
        return max(abs(a - scale * b) for a, b in zip(p, q))

    def integral(values):
        # Periodic Simpson weights; every angular half-sector boundary is an even node.
        return (2 * math.pi / (3 * count)
                * math.fsum((4 if i % 2 else 2) * value
                            for i, value in enumerate(values)))

    scale = integral(a * b for a, b in zip(p, q)) / integral(b*b for b in q)
    error = integral((a - scale*b)**2 for a, b in zip(p, q))
    if n % 4 != 0:
        assert math.isclose(scale, 2*c, abs_tol=1e-12)
        assert error < 1e-26 and max_error(2*c) < 1e-12
        return

    predicted_scale = 2*c*(s + alpha*c)/(alpha + s*c)
    predicted_error = 4*n*s*s*(alpha*alpha - s*s)/(alpha + s*c)
    assert math.isclose(scale, predicted_scale, abs_tol=1e-9, rel_tol=0)
    assert math.isclose(error, predicted_error, rel_tol=1e-7)
    assert math.isclose(max_error(2*c), 2*(1-c), abs_tol=1e-12, rel_tol=0)
    assert max_error(predicted_scale) > max_error(2*c)
    for shift in (-1e-4, 1e-4):
        assert max_error(2*c + shift) > max_error(2*c)


if __name__ == "__main__":
    for sides in (4, 6, 8, 10, 12, 16, 20, 32):
        check(sides)
    print("Finite support-fit checks passed for 8 polygon orders.")
