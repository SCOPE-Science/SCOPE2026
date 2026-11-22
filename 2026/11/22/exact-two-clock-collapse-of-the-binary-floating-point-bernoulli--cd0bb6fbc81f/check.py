#!/usr/bin/env python3
"""Independent integer-bit tests of dyadic floating-point Bernoulli dynamics.

No external packages. The state enumeration uses hardware-style exponent/mantissa
cells rather than the odd-numerator characterization used in the proof.
"""
from collections import Counter


def hardware_states(p, E):
    """All nonnegative p-bit floating values in [0,1), scaled by 2**L."""
    L = E + p - 1
    vals = {0}
    for e in range(-E, 0):
        multiplier = 1 << (e + E)
        for sig in range(1 << (p - 1), 1 << p):
            vals.add(sig * multiplier)
    vals.update(range(1, 1 << (p - 1)))  # subnormal cells
    return vals


def expected_census(p, E):
    L = E + p - 1
    H = [1] + [1 << (min(s, p) - 1) for s in range(1, L + 1)]
    K = [1 + sum(H[1:L-t+1]) for t in range(L + 1)]
    return H, K


def check(p, E):
    L = E + p - 1
    denom = 1 << L
    states = hardware_states(p, E)
    H, K = expected_census(p, E)
    assert len(states) == (E+1) * (1 << (p-1))
    f = lambda z: (2*z) % denom
    first = Counter()
    for x in states:
        v = x
        t = 0
        while v:
            v = f(v)
            t += 1
            assert t <= L
        first[t] += 1
    assert [first[t] for t in range(L+1)] == H, (p,E,'hitting')
    image = set(states)
    for t in range(L+1):
        assert len(image) == K[t], (p,E,t,'image')
        image = {f(v) for v in image}
    assert image == {0}
    return len(states),L


def main():
    count = 0
    total = 0
    for p in range(1,8):
        for E in range(1,7):
            n,L = check(p,E)
            count += 1
            total += n
    n,L = check(11,14)  # True IEEE binary16 [0,1), including subnormals.
    count += 1
    total += n
    assert n == 15360 and L == 24
    # Independent bit-level spot tests for large exponent ranges (no iteration
    # over their astronomically many states).
    for p,E in [(24,126), (53,1022)]:
        L = E+p-1
        assert expected_census(p,E)[0][-1] == 1 << (p-1)
        assert expected_census(p,E)[1][-1] == 1
        assert expected_census(p,E)[1][0] == (E+1) * (1 << (p-1))
    print('PASS: exact hardware-style enumeration,',count,'formats,',
          total,'initial float states, full time histograms and image sizes.')
    print('PASS: binary16 15360 states; last nonzero step 24.')
    print('binary32: p=24, E=126, last nonzero step=149, N=1065353216.')
    print('binary64: p=53, E=1022, last nonzero step=1074.')

if __name__ == '__main__':
    main()
