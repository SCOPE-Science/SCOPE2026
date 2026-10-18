"""Exact arithmetic checks for the finite-field cubic-graph fourth moment.

The proof of the infinite-field-family inequality is in RESULT.md. This
program tests every two-sum fiber over four prime fields and independently
checks the nonuniform exact equality witness, without floating-point input.
"""
from collections import defaultdict
from fractions import Fraction
from random import Random


def fibers(p):
    D = defaultdict(list)
    for t in range(p):
        for u in range(p):
            D[((t + u) % p, (t**3 + u**3) % p)].append((t, u))
    return D


def exact_witness_moment(p, D):
    # Coefficient squared magnitudes: 3 at zero, 2 elsewhere.
    w = lambda t: 3 if t == 0 else 2
    total = 0
    for (s, v), pairs in D.items():
        if s == 0 and v == 0:
            assert len(pairs) == p
            # At the zero fiber all pair products have the same phase.
            amp = 3 + 2 * (p-1)
            total += amp * amp
        else:
            # Every nonzero fiber is a singleton ordered diagonal pair
            # or exactly the two permutations of a distinct pair.
            assert len(pairs) in (1, 2)
            t, u = pairs[0]
            total += len(pairs)**2 * w(t) * w(u)
    return total


def run():
    R = Random(72329)
    assertions = 0
    for p in (5, 7, 11, 13):
        D = fibers(p)
        assert len(D) == (p*p + 1)//2
        assertions += 1
        for key, pairs in D.items():
            if key == (0, 0):
                assert set(pairs) == {(t, (-t) % p) for t in range(p)}
            else:
                assert len(pairs) in (1, 2)
                if len(pairs) == 2:
                    assert pairs[0] == tuple(reversed(pairs[1]))
                else:
                    assert pairs[0][0] == pairs[0][1]
            assertions += 1
        E = exact_witness_moment(p, D)
        assert E == 12*p*p - 3, (p, E)
        mass = 2*p + 1
        assert Fraction(E, mass*mass) == Fraction(3*(2*p-1), 2*p+1)
        assertions += 2
        # Independent random integer/complex coefficient checks, using
        # exact Gaussian integers and exact normalized moment comparisons.
        for _ in range(150):
            f = {t: (R.randint(-3, 3), R.randint(-3, 3)) for t in range(p)}
            M = sum(a*a + b*b for a,b in f.values())
            E2 = 0
            for pairs in D.values():
                re = sum(f[t][0]*f[u][0]-f[t][1]*f[u][1] for t,u in pairs)
                im = sum(f[t][0]*f[u][1]+f[t][1]*f[u][0] for t,u in pairs)
                E2 += re*re+im*im
            assert Fraction(E2, 1) <= Fraction(3*(2*p-1), 2*p+1) * M*M
            assertions += 1
        print(f'q={p}  two-sum_fibers={len(D)}  witness_energy={E}  '
              f'sharp_ratio={Fraction(E,mass*mass)}')
    print(f'EXACT_CHECKS_PASS assertions={assertions}')


if __name__ == '__main__':
    run()
