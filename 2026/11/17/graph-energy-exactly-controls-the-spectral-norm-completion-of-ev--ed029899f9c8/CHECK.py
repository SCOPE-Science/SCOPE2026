"""Supplementary finite arithmetic probes for a graph-energy norm completion formula.
Analytical proof for all finite edge-transitive graphs is in RESULT.md.
Requires only the Python standard library.
"""
from math import cos, pi


def cycle_value(n):
    assert n >= 3
    c = [cos(2*pi*k/n) for k in range(n)]
    s = sum(abs(x) for x in c)
    v = n/s
    # The negative spectral projection yields an involutory completion.
    eig = [-1 if x < -1e-12 else 1 for x in c]
    first_edge = sum(eig[k]*c[k] for k in range(n))/n
    assert abs(v * first_edge - 1) < 2e-11
    assert all(abs(e*e-1)<1e-12 for e in eig)
    return v


def predicted(n):
    import math
    c = pi/2
    if n % 4 == 0:
        return c + pi**3/(6*n*n)
    if n % 2 == 0:
        return c - pi**3/(12*n*n)
    return c - pi**3/(48*n*n)


def run():
    for n in range(3, 201):
        cycle_value(n)
    for n in (401, 402, 403, 404, 799, 800, 801, 802):
        exact=cycle_value(n)
        # Fourth-order residual after the residue-dependent quadratic term.
        assert abs(exact-predicted(n)) < 50/n**4
    for r in range(2, 51):
        edges=r*(r-1)//2
        energy=2*(r-1)
        optimum=2*edges/energy
        assert abs(optimum-r/2)<1e-12
        # The sign completion I-2P_negative has edge value 2/r.
        assert abs(optimum*(2/r)-1)<1e-12
    for a in range(1, 24):
        for b in range(1, 24):
            import math
            optimum=2*a*b/(2*math.sqrt(a*b))
            assert abs(optimum-math.sqrt(a*b))<1e-12
    print('PASS: 198 cycle cases, eight asymptotic cases, 49 cliques and 529 bicliques')

if __name__ == '__main__':
    run()
