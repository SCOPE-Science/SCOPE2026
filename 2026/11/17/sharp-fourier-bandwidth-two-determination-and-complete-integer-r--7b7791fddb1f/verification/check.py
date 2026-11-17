"""Supplementary numerical tests of the box Fourier reconstruction formulas.

Run: python3 verification/check.py
Uses Python's standard library only. Numerical checks are not a proof of
statements concerning all dimensions, boxes, or integer frequencies.
"""
import cmath
import itertools
import math
import random


def sinc_pi(x):
    return 1.0 if x == 0 else math.sin(math.pi * x) / (math.pi * x)


def coordinate(k, width, center):
    return sinc_pi(k * width) * cmath.exp(-2j * math.pi * k * center)


def spectrum(widths, centers, frequencies):
    out = math.prod(widths)
    for k, width, center in zip(frequencies, widths, centers):
        out *= coordinate(k, width, center)
    return out


def reconstruct(widths, centers):
    d = len(widths)
    volume = spectrum(widths, centers, (0,) * d)
    recovered = []
    for j in range(d):
        n = [0] * d
        n[j] = 1
        b1 = spectrum(widths, centers, n) / volume
        n[j] = 2
        b2 = spectrum(widths, centers, n) / volume
        if abs(b1) < 1e-11:
            recovered.append(None)
            continue
        r = abs(b2 / b1)
        recovered_width = math.sqrt(max(0.0, 1.0-r*r))/(math.pi*abs(b1))
        recovered_phase = b1/sinc_pi(recovered_width)
        recovered.append((recovered_width, recovered_phase))

    def spectral_value(n):
        result = volume
        for k, entry in zip(n, recovered):
            if entry is None:
                if k:
                    return 0j
            elif k:
                width, phase = entry
                result *= sinc_pi(k * width) * phase**k
        return result

    return recovered, spectral_value


def bisection_on_unit_interval(target):
    a, b = 0.5, 0.99
    for _ in range(90):
        m = (a+b)/2
        if sinc_pi(m) > target:
            a = m
        else:
            b = m
    return (a+b)/2


def main():
    random.seed(2501)
    count = 0
    for d in (1, 2, 3, 4):
        for rep in range(55):
            widths = [random.uniform(.13, 4.3) for _ in range(d)]
            centers = [random.uniform(-2, 2) for _ in range(d)]
            if rep % 5 == 0:
                widths[rep % d] = float(random.randint(1, 5))
            recovered, spectral_value = reconstruct(widths, centers)
            for width, entry in zip(widths, recovered):
                if width.is_integer():
                    assert entry is None
                else:
                    assert entry is not None
                    assert abs(width - entry[0]) < 2e-7
                count += 1
            for n in itertools.product(range(-2, 3), repeat=d):
                expected = spectrum(widths, centers, n)
                obtained = spectral_value(n)
                assert abs(expected - obtained) < 1e-7 * max(1, math.prod(widths))
                count += 1

    # Sharpness witness: two boxes with the same entire first Fourier cube
    # and unequal second-axial Fourier samples.
    small = bisection_on_unit_interval(abs(sinc_pi(1.5)))
    widths1, centers1 = (small, 1.5), (0.0, 0.5)
    widths2, centers2 = (1.5, small), (0.5, 0.0)
    assert .5 < small < 1 and small != 1.5
    for n in itertools.product(range(-1, 2), repeat=2):
        assert abs(spectrum(widths1, centers1, n) -
                   spectrum(widths2, centers2, n)) < 1e-12
        count += 1
    gap = abs(spectrum(widths1, centers1, (2, 0)) -
              spectrum(widths2, centers2, (2, 0)))
    assert gap > .2
    count += 1

    print('PASS: {} supplementary checks; first-cube witness width={:.15g};'
          ' second-frequency gap={:.12g}'.format(count, small, gap))


if __name__ == '__main__':
    main()
