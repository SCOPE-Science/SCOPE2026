"""Finite exact checks for the covariance of uniform rectangular partial permutations.

Execute with Python 3: python verify.py
This checker samples no random inputs; it is not a proof of the infinite family.
"""
from fractions import Fraction as Q
from math import comb, factorial


def count(p, q):
    return sum(comb(p, k) * comb(q, k) * factorial(k)
               for k in range(min(p, q) + 1))


def eig(p, q):
    F = count(p, q)
    a = Q(count(p - 1, q - 1), F)
    b = Q(count(p - 2, q - 2), F)
    return (a + (p - 1) * (q - 1) * b - p * q * a * a,
            a - (q - 1) * b,
            a - (p - 1) * b,
            a + b)


def all_matching_vertices(p, q):
    def extend(i, used, indices):
        if i == p:
            yield tuple(indices)
            return
        yield from extend(i + 1, used, indices)
        for j in range(q):
            if not ((used >> j) & 1):
                indices.append(i * q + j)
                yield from extend(i + 1, used | (1 << j), indices)
                indices.pop()
    return list(extend(0, 0, []))


def check_direct(p, q):
    vertices = all_matching_vertices(p, q)
    N = len(vertices)
    assert N == count(p, q)
    d = p * q
    incidences = [0] * d
    pair = [[0] * d for _ in range(d)]
    for v in vertices:
        for a in v:
            incidences[a] += 1
            for b in v:
                pair[a][b] += 1
    av = Q(count(p - 1, q - 1), N)
    bv = Q(count(p - 2, q - 2), N)
    C = [[Q(pair[i][j], N) - Q(incidences[i] * incidences[j], N*N)
          for j in range(d)] for i in range(d)]
    for i in range(d):
        assert Q(incidences[i], N) == av
        for j in range(d):
            x, y = divmod(i, q)
            s, t = divmod(j, q)
            predicted = (av if i == j else
                         bv if x != s and y != t else 0) - av*av
            assert C[i][j] == predicted
    modes = [([1] * d, 0),
             ([1 if i//q == 0 else -1 if i//q == 1 else 0 for i in range(d)], 1),
             ([1 if i%q == 0 else -1 if i%q == 1 else 0 for i in range(d)], 2),
             ([1 if i//q in (0, 1) and i%q in (0, 1) and
               ((i//q == 0) == (i%q == 0)) else
               -1 if i//q in (0, 1) and i%q in (0, 1) else 0
               for i in range(d)], 3)]
    lam = eig(p, q)
    for vector, label in modes:
        for i in range(d):
            assert sum(C[i][j] * vector[j] for j in range(d)) == lam[label] * vector[i]
    assert 0 < lam[0] < lam[1] < lam[2] < lam[3]
    return N


def check_algebra(p, q):
    assert 2 <= p < q
    lam = eig(p, q)
    assert 0 < lam[0] < lam[1] < lam[2] < lam[3]
    F = count(p, q)
    kmean = sum(k * comb(p, k)*comb(q, k)*factorial(k)
                for k in range(p+1))
    ksecond = sum(k*k*comb(p, k)*comb(q, k)*factorial(k)
                  for k in range(p+1))
    var = Q(ksecond, F)-Q(kmean, F)**2
    assert lam[0] == var/(p*q)
    # Laguerre coefficient identity for Z(t) = p! t**p L_p^(q-p)(-1/t).
    assert all(comb(p, k)*comb(q, k)*factorial(k) ==
               factorial(p)*comb(q, k)//factorial(p-k)
               for k in range(p+1))
    a = Q(count(p - 1, q - 1), F)
    b = Q(count(p - 2, q - 2), F)
    assert lam[2]-lam[1] == (q-p)*b
    assert lam[3]-lam[2] == p*b
    assert lam[1]-lam[0] == p*(q*a*a-(q-1)*b)


def main():
    profiles = 0
    vertices = 0
    for p in range(2, 5):
        for q in range(p+1, 7):
            vertices += check_direct(p, q)
            profiles += 1
    algebra = 0
    for p in range(2, 26):
        for q in range(p+1, 81):
            check_algebra(p, q)
            algebra += 1
    for p in (2, 3, 5):
        # Quantitative consistency, not a proof of the asymptotic.
        q = 10000
        small, _, _, large = eig(p, q)
        assert abs(float(small*q*q)-1) < 0.003
        assert abs(float(large*q)-1) < 0.003
    print('RECTANGULAR_MATCHING_INERTIA_CHECKS_PASSED',
          'exhaustive_profiles=', profiles, 'vertices=', vertices,
          'exact_algebra_profiles=', algebra)


if __name__ == '__main__':
    main()
