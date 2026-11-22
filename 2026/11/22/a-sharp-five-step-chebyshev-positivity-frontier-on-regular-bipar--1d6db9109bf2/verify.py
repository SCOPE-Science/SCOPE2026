"""Exact finite checks for graph-Chebyshev inverse-positivity theorem.

Only Python's standard library is needed. These computations verify identities
and finite examples; the universal assertions rely on the supplied proof.
"""
from fractions import Fraction as F


def add(a, b):
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0))
            for i in range(max(len(a), len(b)))]


def chebyshev(n):
    a, b = [1], [0, 1]
    if n == 0:
        return a
    for _ in range(2, n + 1):
        a, b = b, add([0, *[2*x for x in b]], [-x for x in a])
    return b


def evaluate(c, x):
    return sum(F(a) * x**j for j, a in enumerate(c))


def divided_difference(n, z):
    # (T_n(z)-T_n(t))/(z-t) expressed in ascending powers of t.
    a = chebyshev(n)
    return [sum(F(a[j]) * z**(j-1-k) for j in range(k+1, len(a)))
            for k in range(n)]


def transition_power_entries(d, steps):
    # Probability of the random walk on Q_d, from the origin to each mask.
    mass = {0: F(1)}
    for _ in range(steps):
        new = {}
        for mask, val in mass.items():
            for bit in range(d):
                dst = mask ^ (1 << bit)
                new[dst] = new.get(dst, F(0)) + val / d
        mass = new
    return mass


def hypercube_polynomial_column(d, z, n):
    coeff = divided_difference(n, z)
    denom = d * evaluate(chebyshev(n), z)
    out = {}
    for k, ck in enumerate(coeff):
        for mask, prob in transition_power_entries(d, k).items():
            out[mask] = out.get(mask, F(0)) + ck * prob / denom
    return out


def test():
    expected = {
        1: [1],
        2: ['2*z', 2],
        3: ['4*z*z-3', '4*z', 4],
        4: ['8*z*z*z-8*z', '8*z*z-8', '8*z', 8],
        5: ['16*z**4-20*z*z+5', '16*z**3-20*z', '16*z*z-20', '16*z', 16],
    }
    total = 0
    for z in [F(101, 100), F(21,20), F(9,8), F(3,2), F(5,1), F(101, 2)]:
        for n in range(1,6):
            c = divided_difference(n, z)
            assert c == [F(eval(str(a), {'z':z})) for a in expected[n]]
            total += 1
            for t in [F(-1), F(0), F(1,3), F(1)]:
                assert (z-t)*evaluate(c,t) == evaluate(chebyshev(n),z)-evaluate(chebyshev(n),t)
                total += 1
    for d in range(1,8):
        for z in [F(21,20), F(9,8), F(3,2), F(3,1)]:
            for n in range(1,6):
                v = hypercube_polynomial_column(d,z,n)
                # Degree <=4 means no mask at graph distance >4 can be reached.
                assert all(mask.bit_count() <= n-1 for mask in v)
                total += 1
                if n <= 4 or z >= F(9,8):
                    assert all(x >= 0 for x in v.values())
                    total += 1
                # The action on constants equals the scalar output at eigenvalue mu.
                assert sum(v.values()) == (1-F(1)/evaluate(chebyshev(n),z))/(d*(z-1))
                total += 1
    # Hypercube adjacent vertex: P^1 = 1/d, P^3 = (3d-2)/d^3.
    for d in range(1,8):
        z=F(21,20)
        actual=hypercube_polynomial_column(d,z,5).get(1,F(0))
        rhs=F(16)*z/(d*d*evaluate(chebyshev(5),z)) * (z*z-F(5,4)+F(3*d-2,d*d))
        assert actual==rhs
        total += 1
    d=32; z=F(21,20)
    neg=F(16)*z/(d*d*evaluate(chebyshev(5),z)) * (z*z-F(5,4)+F(3*d-2,d*d))
    assert neg == F(-17825,49113088) < 0
    total += 1
    # Rational perturbation of the unit point mass gives strictly positive b.
    # The polynomial row sums are positive, so epsilon*ones changes the bad entry
    # by epsilon times this positive constant.
    rowsum = (1-F(1)/evaluate(chebyshev(5),z))/(d*(z-1))
    eps = -neg/(2*rowsum)
    assert eps>0 and neg+eps*rowsum<0
    total+=1
    print(f'PASS: {total} exact rational polynomial, walk, and counterexample checks')
    print(f'Q_32 at z=21/20: neighboring entry {neg}, approx {float(neg):.12f}')
    print(f'Positive perturbation epsilon={eps}, rowsum={rowsum}')


if __name__ == '__main__':
    test()
