"""Exact permutation-rank checks for stationary sliding-window maximum plateau laws.

Runs on Python 3 standard library only. This verifies finite instances, not the
proof for arbitrary window widths or the weak-limit statements.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def up_survival(w, ell):
    return Fraction(w + 1, w + ell)


def down_survival(w, ell):
    return Fraction((w - ell + 1) * (w + 1), (w + ell - 1) * (w + ell))


def start_survival(w, ell):
    return Fraction(w * (w + 1), (w + ell - 1) * (w + ell))


def forward_survival(w, ell):
    return Fraction(w - ell, w + ell)


def test_w(w):
    # raw positions -1,0,...,2*w-1; window at j is raw[j+1:j+w+1]
    n = 2*w+1
    total = factorial(n)
    cnt_start = cnt_up = cnt_down = 0
    start_ge = [0]*(w+1)
    up_ge = [0]*(w+1)
    down_ge = [0]*(w+1)
    fwd_gt = [0]*(w+1)
    checks = 0
    for p in permutations(range(n)):
        # y index 0 is Y_{-1}, 1 is Y_0, w+1 is Y_w
        y = [max(p[j:j+w]) for j in range(w+2)]
        for ell in range(w+1):
            if all(y[j] == y[1] for j in range(1,ell+2)):
                fwd_gt[ell] += 1
        if y[1] != y[0]:
            cnt_start += 1
            direction = 'up' if y[1] > y[0] else 'down'
            if direction == 'up':
                cnt_up += 1
            else:
                cnt_down += 1
            for ell in range(1,w+1):
                if all(y[j] == y[1] for j in range(1,ell+1)):
                    start_ge[ell] += 1
                    if direction == 'up':
                        up_ge[ell] += 1
                    else:
                        down_ge[ell] += 1
    assert Fraction(cnt_start,total) == Fraction(2,w+1)
    assert Fraction(cnt_up,total) == Fraction(1,w+1)
    assert Fraction(cnt_down,total) == Fraction(1,w+1)
    checks += 3
    for ell in range(1,w+1):
        assert Fraction(up_ge[ell],cnt_up) == up_survival(w,ell), ('up',w,ell)
        assert Fraction(down_ge[ell],cnt_down) == down_survival(w,ell), ('down',w,ell)
        assert Fraction(start_ge[ell],cnt_start) == start_survival(w,ell), ('mix',w,ell)
        checks += 3
    for ell in range(w+1):
        assert Fraction(fwd_gt[ell],total) == forward_survival(w,ell), ('forward',w,ell)
        checks += 1
    print(f'w={w}: {total:,} permutations; {checks} exact identities verified; start counts {cnt_start:,}')
    return total, checks

if __name__ == '__main__':
    values = [test_w(w) for w in range(1,5)]
    print(f'PASS: {sum(a for a,b in values):,} exhaustive rank cases and {sum(b for a,b in values)} exact rational formula identities')
