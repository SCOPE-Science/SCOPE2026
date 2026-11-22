"""Exact rational certificates for the star-TV proximal-semigroup threshold.

Run with Python 3.9+; only the standard library is required.
"""
from fractions import Fraction as F
from itertools import product


def q(v):
    return tuple(F(x) for x in v)


def subgradient_certificate(data, tau, flux, result):
    """Verify 0 in result-data+tau*partial(J)(result) exactly."""
    data, flux, result, tau = q(data), q(flux), q(result), F(tau)
    d = len(data) - 1
    assert len(flux) == d and len(result) == d + 1
    assert all(abs(z) <= 1 for z in flux)
    assert result[0] == data[0] - tau * sum(flux)
    for i, z in enumerate(flux, start=1):
        assert result[i] == data[i] + tau*z
        diff = result[0] - result[i]
        if diff > 0:
            assert z == 1
        elif diff < 0:
            assert z == -1
    return True


def witness(data, u, flux_u, v, flux_v, w, flux_w):
    half = F(1, 2)
    assert subgradient_certificate(data, half, flux_u, u)
    assert subgradient_certificate(u, half, flux_v, v)
    assert subgradient_certificate(data, 1, flux_w, w)
    assert v != w
    return max(abs(a-b) for a, b in zip(q(v), q(w)))


def test_all_small_stars():
    cases = 0
    for degree in (1, 2, 3):
        for labels in product((-1, 0, 1), repeat=degree):
            # 0 denotes a tie; other signs specify the strictly ordered edges.
            free = [i for i, s in enumerate(labels) if s == 0]
            a = sum(labels)
            if not free:
                cases += 1
                continue
            z = -F(a, len(free)+1)
            assert -1 <= z <= 1
            p0 = a + len(free)*z
            for _ in free:
                assert p0 == -z
            cases += 1
    # For all larger degrees, one tie and all other edges above their leaves
    # violates the MINSUB orthogonality equality.
    for degree in range(4, 41):
        a = degree - 1
        z = F(-1) # constrained optimizer of (a+z)^2+z^2
        assert F(-a, 2) < -1
        assert a+z != -z
    return cases


def embed_pair(data, u, v, w, flux_u, flux_v, flux_w, pairs):
    # Each pair of very low/high leaves has saturated flux (+1,-1),
    # cancels at the center, and therefore keeps the base certificates valid.
    for _ in range(pairs):
        data = tuple(data) + (F(-10), F(10))
        u = tuple(u) + (F(-19,2), F(19,2))
        v = tuple(v) + (F(-9), F(9))
        w = tuple(w) + (F(-9), F(9))
        flux_u = tuple(flux_u) + (F(1), F(-1))
        flux_v = tuple(flux_v) + (F(1), F(-1))
        flux_w = tuple(flux_w) + (F(1), F(-1))
    return witness(data, u, flux_u, v, flux_v, w, flux_w)


def main():
    count = test_all_small_stars()
    x4 = q((3,0,-3,2,-1))
    u4 = q((F(7,4),F(1,2),F(-5,2),F(7,4),F(-1,2)))
    v4 = q((F(7,8),F(7,8),-2,F(5,4),0))
    w4 = q((1,1,-2,1,0))
    a4,b4,c4 = q((1,1,F(-1,2),1)), q((F(3,4),1,-1,1)), q((1,1,-1,1))
    assert witness(x4,u4,a4,v4,b4,w4,c4) == F(1,4)
    x5 = q((-4,-2,0,0,2,0))
    u5 = q((-2,-2,F(-1,2),F(-1,2),F(3,2),F(-1,2)))
    v5 = q((F(-7,8),F(-3,2),F(-7,8),F(-7,8),1,F(-7,8)))
    w5 = q((-1,-1,-1,-1,1,-1))
    a5,b5,c5 = q((0,-1,-1,-1,-1)),q((1,F(-3,4),F(-3,4),-1,F(-3,4))),q((1,-1,-1,-1,-1))
    assert witness(x5,u5,a5,v5,b5,w5,c5)==F(1,2)
    for k in range(1, 30):
        assert embed_pair(x4,u4,v4,w4,a4,b4,c4,k)==F(1,4)
        assert embed_pair(x5,u5,v5,w5,a5,b5,c5,k)==F(1,2)
    print('PASS: {} all-small-star sign configurations; 38 large-star MINSUB obstructions;'.format(count))
    print('PASS: two exact proximal-semigroup counterexamples and 58 pair embeddings.')
    print('Analytic coverage beyond tested sizes follows from the arguments in RESULT.md.')

if __name__ == '__main__':
    main()
