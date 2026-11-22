"""Exact-arithmetic spot checks for rank-one-spike Nyström trace identities.

Run with: python verify.py
Finite checks illustrate the analytical proof; they do not certify all parameters.
Requires only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def inverse(A):
    n = len(A)
    B = [[Q(A[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if B[j][i] != 0)
        B[i], B[pivot] = B[pivot], B[i]
        fac = B[i][i]
        B[i] = [v / fac for v in B[i]]
        for j in range(n):
            if j != i:
                fac = B[j][i]
                B[j] = [u - fac * v for u, v in zip(B[j], B[i])]
    return [row[n:] for row in B]


def matrix_error(a, b, r, I):
    # v=r/sqrt(sum_i r_i^2), so K is rational even if v is irrational.
    n = len(r)
    R = sum(z*z for z in r)
    assert R > 0
    K = [[(a if i == j else Q(0)) + b*Q(r[i]*r[j], R) for j in range(n)] for i in range(n)]
    Inv = inverse([[K[i][j] for j in I] for i in I])
    J = [j for j in range(n) if j not in I]
    tr = Q(0)
    for j in J:
        cross = [K[j][i] for i in I]
        tr += K[j][j] - sum(cross[p]*Inv[p][q]*cross[q] for p in range(len(I)) for q in range(len(I)))
    return tr


def predicted_error(a, b, r, I):
    n = len(r)
    R = sum(z*z for z in r)
    s = Q(sum(r[i]*r[i] for i in I), R)
    return a*(n-len(I)) + a*b*(1-s)/(a+b*s)


def symmetric_e(a, b, n, k):
    return Q(comb(n, k))*a**(k-1)*(a+b*Q(k,n))


def main():
    cases = 0
    tests = 0
    for n in range(4, 9):
        for k in range(2, n-1):
            for a,b in [(Q(1),Q(1)), (Q(3,2),Q(7,3))]:
                # Nonflat and flat spike orientations.
                for r in [list(range(1, n+1)), [1]*n, [0]*(n-1)+[1]]:
                    R = sum(z*z for z in r)
                    masses = sorted([Q(z*z,R) for z in r],reverse=True)
                    smax = sum(masses[:k],Q(0))
                    best_formula = a*(n-k) + a*b*(1-smax)/(a+b*smax)
                    all_values = []
                    for I in combinations(range(n),k):
                        direct=matrix_error(a,b,r,I)
                        formula=predicted_error(a,b,r,I)
                        assert direct == formula, (n,k,a,b,r,I,direct,formula)
                        all_values.append(direct)
                        tests += 1
                    assert min(all_values) == best_formula
                    equality = (best_formula == a*(n-k)*(a+b*Q(k+1,n))/(a+b*Q(k,n)))
                    assert equality == (len(set(masses)) == 1)
                    cases += 1
                dpp=(k+1)*symmetric_e(a,b,n,k+1)/symmetric_e(a,b,n,k)
                desired=a*(n-k)*(a+b*Q(k+1,n))/(a+b*Q(k,n))
                assert dpp==desired
                tests += 1
    print(f"PASS: {cases} orientations and {tests} rational equalities; all claimed interior subset sizes through n=8.")

if __name__=='__main__':
    main()
