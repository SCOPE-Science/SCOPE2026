"""Exact-rational finite checks for the stated max-plus capture-time theorem.

The proof of the all-real statement is in RESULT.md; this checker only tests
specified exact-rational cases and the explicit first-hit-time partition.
"""
from fractions import Fraction as Q
from itertools import product


def step(p, b):
    x, y = p
    z = max(x, Q(0))
    return (y + 2*z, -b - 2*z)


def predicted(x, y, b):
    if x == -b and y == -b:
        return 0
    if x <= 0:
        if y == -b:
            return 1
        if y <= 0:
            return 2
        if y <= b/2:
            return 4
        if y <= 3*b/2:
            return 5
        return 6
    if y <= -2*x:
        return 3
    if y <= b/2 - x:
        return 4
    if y <= 3*b/2:
        return 5
    return 6


def hit_time(p, b):
    target = (-b, -b)
    for j in range(8):
        if p == target:
            return j
        p = step(p, b)
    raise AssertionError('not captured by step 7')


def run():
    counts = {j: 0 for j in range(7)}
    xs = [Q(k, 8) for k in range(-28,29)]
    ys = [Q(k, 8) for k in range(-28,29)]
    cases = 0
    for b in [Q(1, 10),Q(1,2),Q(1),Q(7,3),Q(11)]:
        scaled_xs = [x*b for x in xs]
        scaled_ys = [y*b for y in ys]
        for x,y in product(scaled_xs,scaled_ys):
            want = predicted(x,y,b)
            got = hit_time((x,y),b)
            assert got == want, (b,x,y,got,want)
            counts[got] += 1
            cases += 1
            p=(x,y)
            for _ in range(6):p=step(p,b)
            assert p==(-b,-b)
    for t in range(7):
        assert counts[t] > 0, (t, counts[t])
    # Exact, deliberately selected knife-edge and arbitrarily large states.
    for b in [Q(1),Q(1,100),Q(100)]:
        for x in [Q(-10000)*b,Q(0),Q(1,17)*b,Q(10000)*b]:
            for y in [Q(-10000)*b, -2*x, (b/2)-x, -b, Q(0), b/2, 3*b/2, 3*b/2+b/1000, Q(10000)*b]:
                assert hit_time((x,y),b)==predicted(x,y,b)
                cases+=1
    print('CHECK_OK exact-rational cases=',cases,'first-hit counts=',counts)


if __name__ == '__main__':
    run()
