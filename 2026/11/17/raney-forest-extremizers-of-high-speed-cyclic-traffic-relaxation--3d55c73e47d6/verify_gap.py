"""Independent finite enumeration in the gap-coordinate dynamical system."""
from math import comb

def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail

def advance(gaps, speed):
    actual = [min(gap, speed) for gap in gaps]
    return tuple(gaps[i] - actual[i] + actual[(i + 1) % len(gaps)]
                 for i in range(len(gaps)))

def entry(gaps, speed):
    for t in range(len(gaps)):
        if min(gaps) >= speed:
            return t
        gaps = advance(gaps, speed)
    raise AssertionError('Exceeds rigorous bound')

def run():
    cases = 0
    for speed in (1, 2, 3, 4, 5):
        for cars in range(2, 7):
            for surplus in (0, 1, 2):
                holes = speed * cars + surplus
                if comb(holes + cars - 1, cars - 1) > 140000:
                    continue
                last = 0
                latest = 0
                for g in compositions(holes, cars):
                    t = entry(g, speed)
                    latest = max(t, latest)
                    last += t == cars - 1
                expected = comb((speed + 1) * cars - 2, cars - 1)
                assert latest == cars - 1, (speed, cars, surplus, latest)
                assert last == expected, (speed, cars, surplus, last, expected)
                cases += 1
    print('gap-system exhaustive cases:', cases)
    print('all sharp m-1 bounds and Raney counts: PASS')

if __name__ == '__main__':
    run()
