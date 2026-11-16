#!/usr/bin/env python3
"""Independent integer-Laurent arithmetic for phase-only two-block Fourier moments."""
from collections import defaultdict
from itertools import product


def polynomial_power(m, degree):
    # Each monomial has (spatial frequency, u-exponent, v-exponent).
    q = {(0, 0, 0): 1}
    taps = [(0, 0, 0), (1, 0, 0), (m, 1, 0), (m+1, 0, 1)]
    for _ in range(degree):
        new = defaultdict(int)
        for (f, a, b), c in q.items():
            for x, y, z in taps:
                new[(f+x, a+y, b+z)] += c
        q = dict(new)
    return q


def moment_laurent(m, degree):
    q = polynomial_power(m, degree)
    by_frequency = defaultdict(list)
    for (f, a, b), c in q.items():
        by_frequency[f].append((a, b, c))
    out = defaultdict(int)
    for vals in by_frequency.values():
        for a, b, c in vals:
            for a2, b2, c2 in vals:
                out[(a-a2, b-b2)] += c*c2
    return {k: v for k, v in out.items() if v}


def expected_four():
    return {(0,0):28, (1,-1):4, (-1,1):4}


def expected_six(m):
    d={(0,0):256,(1,-1):72,(-1,1):72}
    if m==3:
        for e,c in [((1,0),3),((2,-1),9),((3,-2),3)]:
            d[e] = c
            d[(-e[0],-e[1])] = c
    return d


def eval_int_laurent(d, u, v):
    return sum(c * u**a * v**b for (a,b),c in d.items())


def main():
    checks=0
    for m in range(3, 45):
        assert moment_laurent(m,2)==expected_four()
        assert moment_laurent(m,3)==expected_six(m)
        checks+=2
    for m in (3,4,6,9,25):
        for u,v in product((1,-1,1j,-1j), repeat=2):
            # The Laurent dictionary has exact integer coefficients, so the
            # following comparisons are exact in Gaussian integers.
            fourth=eval_int_laurent(moment_laurent(m,2),u,v)
            sixth=eval_int_laurent(moment_laurent(m,3),u,v)
            assert abs(fourth.imag)<1e-12 and abs(sixth.imag)<1e-12
            c=(u/v).real
            assert abs(fourth.real-(28+8*c))<1e-12
            if m==3:
                psi=u*u/v
                expected=256+144*c+6*(3+2*c)*psi.real
            else:
                expected=256+144*c
            assert abs(sixth.real-expected)<1e-12
            checks+=2
    # Sharp equality examples under the normalization a0=a1=1.
    assert eval_int_laurent(moment_laurent(3,3),1,-1)==106
    assert eval_int_laurent(moment_laurent(3,3),1,1)==430
    for m in (4,5,20):
        assert eval_int_laurent(moment_laurent(m,3),1,-1)==112
        assert eval_int_laurent(moment_laurent(m,3),1,1)==400
    assert eval_int_laurent(moment_laurent(3,2),1,-1)==20
    assert eval_int_laurent(moment_laurent(3,2),1,1)==36
    print(f'VERIFY_OK {checks} exact symbolic / Gaussian-integer comparisons; extremal examples pass')


if __name__=='__main__':
    main()
