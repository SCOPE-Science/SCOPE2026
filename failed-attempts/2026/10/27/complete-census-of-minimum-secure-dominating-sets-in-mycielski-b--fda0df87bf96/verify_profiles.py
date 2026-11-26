#!/usr/bin/env python3
"""Exhaustive proof certificate for secure guard-swap profiles of C5 twin blowups.
The singleton apex class has capacity one; every other capacity is six.
Only sets of at most five guards are considered.
"""
from itertools import product
from math import comb

CAP = (6, 6, 6, 1, 6)
EXPECTED = {
    (1, 1, 1, 1, 1),
    (1, 2, 1, 1, 0),
    (2, 1, 0, 1, 1),
    (2, 2, 0, 0, 1),
    (2, 2, 0, 1, 0),
    (2, 2, 1, 0, 0),
}
COUNTS = ((1, 0, 0), (5, 0, 0), (14, 0, 0),
          (30, 6, 0), (55, 19, 0), (91, 41, 6))


def dominating(s):
    return all(s[i] == CAP[i] or s[(i - 1) % 5] + s[(i + 1) % 5] > 0
               for i in range(5))


def secure(s):
    if not dominating(s):
        return False
    for i in range(5):
        if s[i] == CAP[i]:
            continue
        defended = False
        for j in ((i - 1) % 5, (i + 1) % 5):
            if s[j]:
                new = list(s)
                new[i] += 1
                new[j] -= 1
                if dominating(new):
                    defended = True
                    break
        if not defended:
            return False
    return True


def census():
    rows = []
    profiles = set()
    for t in range(6):
        cand = dom = sec = 0
        for s in product(range(t + 1), repeat=4):
            for apex in range(2):
                p = (s[0], s[1], s[2], apex, s[3])
                if sum(p) != t:
                    continue
                cand += 1
                if dominating(p):
                    dom += 1
                if secure(p):
                    sec += 1
                    profiles.add(p)
        rows.append((cand, dom, sec))
    assert tuple(rows) == COUNTS, (rows, COUNTS)
    assert profiles == EXPECTED, profiles
    for m, n in ((5, 5), (5, 6), (6, 6), (5, 7), (6, 7), (11, 13)):
        capacity = (m, n, m, 1, n)
        exact = sum(__import__('math').prod(comb(z, p) for z, p in zip(capacity, s)) for s in profiles)
        formula = m*m*n*n + m*m*comb(n, 2) + n*n*comb(m, 2) + (m+n+1)*comb(m, 2)*comb(n, 2)
        assert exact == formula, (m,n,exact,formula)
    print('PROFILE_VERIFY_OK table=', rows, 'profiles=', sorted(profiles))


if __name__ == '__main__':
    census()
