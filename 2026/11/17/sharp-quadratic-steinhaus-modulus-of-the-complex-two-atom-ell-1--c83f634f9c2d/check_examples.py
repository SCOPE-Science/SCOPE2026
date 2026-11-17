#!/usr/bin/env python3
"""Finite cross-checks of a sharp two-complex-atom Steinhaus asymptotic."""
from math import hypot


def l1(a, b):
    return abs(a) + abs(b)


def transverse_value(d, radius):
    delta = d / 2.0
    r, s = (1.0 + delta) / 2.0, (1.0 - delta) / 2.0
    x, y = (complex(r), complex(s)), (complex(s), complex(r))
    assert abs(l1(*x) - 1.0) < 1e-14
    assert abs(l1(*y) - 1.0) < 1e-14
    assert abs(l1(x[0] - y[0], x[1] - y[1]) - d) < 1e-14
    z = (1j * radius, 0j)
    value = abs(l1(x[0] + z[0], x[1] + z[1]) -
                l1(y[0] + z[0], y[1] + z[1]))
    coefficient = d / (1.0 - d * d / 4.0)
    assert value > 0
    ratio = value / (radius * radius * coefficient)
    assert abs(ratio - 1.0) < 0.05
    return ratio


def main():
    total = 0
    for distance in (0.25, 0.6, 1.0, 1.5, 1.9):
        for radius in (0.01, 0.001):
            ratio = transverse_value(distance, radius)
            print(f"distance={distance:.2f} radius={radius:.3f} fraction={ratio:.8f}")
            total += 1
    assert total == 10
    print(f"All {total} finite diagnostic examples passed.")


if __name__ == "__main__":
    main()
