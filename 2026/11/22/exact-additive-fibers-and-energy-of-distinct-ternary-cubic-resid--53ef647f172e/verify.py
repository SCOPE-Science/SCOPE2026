"""Independent finite consistency checks for cubic-value additive fibers.

Requires only the Python standard library. No external data files.
"""
from collections import Counter
from fractions import Fraction


def predicted(k, target, cardinalities, previous):
    modulus = 3**k
    h = 3**(k-2)
    t = target % 9
    if t in (2, 7):
        return h
    if t in (1, 8):
        return 2*cardinalities[k-3]
    if t == 0:
        return 2*h + (previous[(target//27) % (3**(k-3))] if target % 27 == 0 else 0)
    return 0


def main():
    sizes = [1, 3, 3]
    energies = [1, 27, 19]
    all_fibers = []
    count = 0
    for k in range(0, 9):
        q = 3**k
        cubes = {pow(x, 3, q) for x in range(q)}
        size = len(cubes)
        if k >= 3:
            h = 3**(k-2)
            assert size == 2*h + sizes[k-3]
            sizes.append(size)
        else:
            assert size == sizes[k]
        histogram = [0]*q
        for a in cubes:
            for b in cubes:
                histogram[(a+b) % q] += 1
        assert sum(histogram) == size**2
        energy = sum(x*x for x in histogram)
        if k >= 3:
            assert energy == energies[k-3] + 6*h**3 + 12*h*sizes[k-3]**2
            energies.append(energy)
            for y, count_y in enumerate(histogram):
                assert count_y == predicted(k, y, sizes, all_fibers[k-3]), (k,y,count_y,predicted(k,y,sizes,previous_fibers))
                count += 1
        else:
            assert energy == energies[k]
        periodic = (10, 30, 12)[k % 3]
        assert size == (3**(k+1) + periodic)//13
        assert energy >= size**4 // q
        all_fibers.append(histogram)
    c = Fraction(38, 4563)/(1-Fraction(1, 27**3))
    assert c == Fraction(13851, 1663129)
    assert c / Fraction(3**4, 13**4) == Fraction(2223, 757)
    for k in range(9, 16):
        h = 3**(k-2)
        s = 2*h + sizes[k-3]
        e = energies[k-3] + 6*h**3 + 12*h*sizes[k-3]**2
        assert s == (3**(k+1)+(10,30,12)[k % 3])//13
        sizes.append(s)
        energies.append(e)
    print(f'CUBIC_VALUE_FIBERS_PASS depths=0..8 checked_targets={count} recurrence_depth=15')


if __name__ == '__main__':
    main()
