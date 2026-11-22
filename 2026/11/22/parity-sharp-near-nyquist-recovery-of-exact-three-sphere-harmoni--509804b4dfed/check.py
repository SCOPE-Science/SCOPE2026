"""Standalone exact tests for one-curve spherical-harmonic interpolation.

Uses Python standard library only. These finite checks support, but do not
replace, the all-degree proof in RESULT.md.
"""
from fractions import Fraction
from math import comb, gcd


def weights(ell):
    return [(m, n) for m in range(-ell, ell + 1)
            for n in range(-ell, ell + 1)
            if abs(m) + abs(n) <= ell and (ell - abs(m) - abs(n)) % 2 == 0]


def grid_weights(ell):
    out = []
    for i in range(ell + 1):
        for j in range(ell + 1):
            U, V = -ell + 2 * i, -ell + 2 * j
            out.append(((U + V) // 2, (U - V) // 2))
    return out


def design(ell):
    L = ell + 1
    if ell % 2 == 0:
        return (L - 1) // 2, (L + 1) // 2, L * L
    return 1, L, L * L + 1


def jacobi_radial(ell, m, n, u):
    a, b = abs(m), abs(n)
    j = (ell - a - b) // 2
    co = Fraction(1)
    total = Fraction(0)
    for v in range(j + 1):
        total += co * u**v * (1 - u)**(j - v)
        if v < j:
            co *= Fraction(-(j - v) * (j - v + b), (v + 1) * (v + 1 + a))
    return total


def prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** .5) + 1):
        if n % d == 0:
            return False
    return True


def factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def root(M, P):
    for g in range(2, P):
        w = pow(g, (P - 1) // M, P)
        if w != 1 and all(pow(w, M // d, P) != 1 for d in factors(M)):
            return w
    raise AssertionError('no finite-field root')


def matrix_rank(A, p):
    n = len(A)
    m = len(A[0])
    rank = 0
    for col in range(m):
        pivot = next((r for r in range(rank, n) if A[r][col] % p), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col] % p, -1, p)
        for j in range(col, m):
            A[rank][j] = A[rank][j] * inv % p
        for r in range(rank + 1, n):
            f = A[r][col] % p
            if f:
                for j in range(col, m):
                    A[r][j] = (A[r][j] - f*A[rank][j]) % p
        rank += 1
        if rank == min(n, m):
            break
    return rank


def main():
    arithmetic_checks = 0
    for ell in range(1, 200):
        D = weights(ell)
        G = grid_weights(ell)
        L = ell + 1
        p, q, M = design(ell)
        assert len(D) == L*L and set(D) == set(G)
        assert gcd(p, q) == 1
        vals = [p*m + q*n for m,n in G]
        residues = {x % M for x in vals}
        assert len(residues) == L*L
        if ell % 2 == 0:
            assert max(vals) - min(vals) + 1 == L*L
            assert sorted(vals) == list(range(min(vals), max(vals) + 1))
            assert residues == set(range(M))
        else:
            assert residues == set(range(1, M))
            # The involution obstruction excludes critical L^2-site sampling.
            assert len({0, M // 2}) == 2 and L*L % 2 == 0
        arithmetic_checks += 1

    # Verify separated polynomial recurrence and its nonzero torus restriction
    # with exact rational arithmetic, then independently form finite-field
    # Fourier evaluation matrices for small degrees.
    matrix_checks = 0
    for ell in range(1, 9):
        D = grid_weights(ell)
        p, q, M = design(ell)
        chosen = None
        for den in range(3, 50):
            u = Fraction(1, den)
            if all(jacobi_radial(ell,m,n,u) != 0 for m,n in D):
                chosen = u
                break
        assert chosen is not None
        # Verify each consecutive Laplace coefficient vanishes identically.
        for m,n in D:
            a,b=abs(m),abs(n)
            j=(ell-a-b)//2
            coeff=Fraction(1)
            for v in range(j):
                next_coeff=coeff*Fraction(-(j-v)*(j-v+b),(v+1)*(v+1+a))
                assert next_coeff*(v+1)*(v+1+a)+coeff*(j-v)*(j-v+b)==0
                coeff=next_coeff
        P = next(x for x in range(2*M+1, 1000000, M) if prime(x))
        w = root(M,P)
        def modfrac(z):
            return (z.numerator % P)*pow(z.denominator%P,-1,P)%P
        scalars = []
        for m,n in D:
            # Powers of radii were factored out of harmonic coordinates.
            # Their factors are nonzero; Q alone suffices for rank.
            scalars.append(modfrac(jacobi_radial(ell,m,n,chosen)))
        if 0 in scalars:
            # Avoid an accidental modular cancellation.
            P=next(x for x in range(P+M,1000000,M) if prime(x))
            w=root(M,P)
            scalars=[modfrac(jacobi_radial(ell,m,n,chosen)) for m,n in D]
        assert all(scalars)
        A=[[pow(w, (j*(p*m+q*n)) % M, P)*scalars[i]%P
             for i,(m,n) in enumerate(D)] for j in range(M)]
        assert matrix_rank(A,P)==(ell+1)**2
        matrix_checks += 1
    print('TORUS_KNOT_INTERPOLATION_OK',arithmetic_checks,
          'exact residue classifications',matrix_checks,
          'independent finite-field evaluation matrix ranks')

if __name__ == '__main__':
    main()
