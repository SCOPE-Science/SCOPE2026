"""Bounded recovery check: p1(4,d) = sum d_i^2 - (5+k) takes both residues 3 and 7 mod 8
within the v2,v4 != 0 class (p(d) == 0 mod 4). Also notes all-odd multidegrees give 3 mod 8."""

def p1(d):
    return sum(x * x for x in d) - (5 + len(d))

def p_even(d):
    return sum(1 for x in d if x % 2 == 0)

cases = [[3], [5], [2, 2, 2, 2], [2] * 8, [6] * 4, [3, 3], [], [4]]
for d in cases:
    print(d, 'p1 =', p1(d), 'mod 8 =', p1(d) % 8, 'p(d) =', p_even(d))
