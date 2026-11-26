"""Finite exact-rational illustrations of the Bernoulli-thinning criterion."""

from fractions import Fraction as Q


def canonical_by_division(nu, theta, r, end):
    """Coefficients of G'/G, obtained from the series of G/G(0)."""
    nb = [Q(1)]
    for k in range(1, end + 1):
        nb.append(nb[-1] * theta * (nu + k - 1) / k)
    f = [nb[0]] + [nb[k] + r * nb[k - 1] for k in range(1, end + 1)]
    b = [Q(0)]
    for k in range(1, end + 1):
        b.append(k * f[k] - sum(b[j] * f[k - j] for j in range(1, k)))
        assert b[k] == nu * theta**k + (-1)**(k - 1) * r**k
    return b


def main():
    theta, r = Q(1, 2), Q(1, 3)
    b = canonical_by_division(Q(1), theta, r, 24)
    assert all(v > 0 for v in b[1:]) and b[2] < b[3]
    assert Q(1) - (r / (1 + r))**2 == Q(15, 16)
    b = canonical_by_division(Q(2), theta, r, 24)
    assert all(b[k] > b[k + 1] for k in range(1, 24))
    critical_shape = (1 + r) * r*r / ((1 - theta) * theta*theta)
    assert critical_shape == Q(32, 27)
    b = canonical_by_division(critical_shape, theta, r, 24)
    assert b[2] == b[3] and all(b[k] > b[k + 1] for k in range(1, 24) if k != 2)
    b = canonical_by_division(Q(3), theta, theta, 24)
    assert all((b[k] > b[k + 1]) if k % 2 else (b[k] == b[k + 1]) for k in range(1, 24))
    b = canonical_by_division(Q(20), theta, Q(2, 3), 24)
    assert b[2] > b[3] and b[12] < b[13]
    print('PASS: finite exact-rational thinning checks')


if __name__ == '__main__':
    main()
