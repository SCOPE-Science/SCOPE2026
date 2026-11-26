"""Finite numerical consistency checks for the conditional chord direction law."""
from math import asin, atan, cos, isclose, pi, sin, sqrt


def half_width(h, b):
    return asin(h * (1 - b*b) / (1 - h*b*b)) / (2*h)


def simpson(f, n=10000):
    return sum((1 if j in (0, n) else 4 if j % 2 else 2) * f(j/n)
               for j in range(n+1)) / (3*n)


for h in (.002, .02, .2, .5, .91):
    cutoff = 2 * sqrt(2 / (1+h))
    for j in range(4):
        for i in range(-10, 11):
            z = sqrt(h) * i / 11
            b = z / sqrt(h)
            for k in range(-10, 11):
                q = pi * k / 43
                phi = pi/4 + j*pi/2 + q
                x, y = sqrt(1-z*z)*cos(phi), sqrt(1-z*z)*sin(phi)
                chord = 2/sqrt(max(x*x+z*z, y*y+z*z))
                if not isclose(chord, cutoff, rel_tol=1e-13):
                    assert (chord > cutoff) == (abs(q/h) < half_width(h, b))
    t, s = sqrt((1-h)/2), sqrt(h)
    pair_overlap = (4/pi) * (atan(s) - t*atan(s/t))
    area = 4 * simpson(lambda b: half_width(h, b))
    assert isclose(pair_overlap, area*h**1.5/pi, rel_tol=2e-9)

for h in (.04, .02, .01, .005, .0025):
    def excess(b):
        return half_width(h, b) - (1-b*b)/2
    shell = 4 * simpson(excess)
    assert shell > 0
    distance = shell / (4/3 + shell)
    shell_height_second_moment = 4 * simpson(lambda b: b*b*excess(b)) / shell
    assert abs(distance/h - 1/5) < h
    assert abs(shell_height_second_moment - 3/7) < h

print('Conditional support, overlap area, sharp TV scale, and shell-height moment checks passed.')
