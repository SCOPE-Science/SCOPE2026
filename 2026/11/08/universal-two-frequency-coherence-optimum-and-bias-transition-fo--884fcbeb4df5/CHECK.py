#!/usr/bin/env python3
"""Numerical corroboration of finite odd-base two-frequency Fourier coherence.
Run: python CHECK.py. The theorem's proof is algebraic; these are finite tests.
"""
from math import pi, sin, sqrt, cos
from cmath import exp
from itertools import product

def compare(base, weights):
    depth = len(weights)
    modulus = base**depth
    data = [(0, 1.0)]
    for j, w in enumerate(weights, 1):
        delta = 2 * base**(depth-j)
        data = [(s, p*(1-w)) for s,p in data] + [(s+delta, p*w) for s,p in data]
    assert len({s for s, _ in data}) == 2**depth
    pred = 1.0
    for j,w in enumerate(weights,1):
        pred *= sqrt((1-2*w)**2 + 4*w*(1-w)*sin(pi/(2*base**j))**2)
    values = []
    for k in range(1, modulus):
        actual = abs(sum(p*exp(-2j*pi*k*s/modulus) for s,p in data))
        fact = 1.0
        for j,w in enumerate(weights,1):
            fact *= abs((1-w)+w*exp(-4j*pi*k/(base**j)))
        assert abs(actual-fact) < 1.2e-9, (base,weights,k,actual,fact)
        values.append((k,actual))
    observed = min(v for _,v in values)
    expected = {k for k in range(1,modulus) if (4*k)%modulus in (1,modulus-1)}
    attainers = {k for k,v in values if abs(v-observed)<1.e-9}
    assert attainers == expected, (base,weights,attainers,expected)
    assert len(expected) == 2
    assert abs(observed-pred) < 1.2e-9
    assert 0 < pred < 1
    # Off-diagonal Gram modulus equals the direct finite Fourier coefficient.
    assert abs((1-pred)+(1+pred)-2)<1.e-12
    assert (1+pred)/(1-pred) > 1
    return modulus-1

def main():
    tests = 0; residues = 0
    for base,maximum in ((3,5),(5,4),(7,3),(9,3),(11,3)):
        for depth in range(1,maximum+1):
            for weights in ([0.5]*depth, [0.25]*depth, [0.8]*depth,
                            [0.2+0.6*(j%2) for j in range(depth)]):
                residues += compare(base,weights)
                tests += 1
    print('CHECK_OK configurations=%d frequency_classes=%d' % (tests,residues))

if __name__ == '__main__': main()
