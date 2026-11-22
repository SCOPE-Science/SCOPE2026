"""Independent small-case checks for partial induced-automorphism ranks of bicliques.
Standard-library only; execute: python3 verify_partial_biclique.py
"""
from itertools import combinations, permutations
from math import comb, factorial
from fractions import Fraction


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def rank_formula(a, b, k):
    if k == 0:
        return 1
    if k == 1:
        return (a + b) ** 2
    independent = choose(a, k) + choose(b, k)
    result = factorial(k) * independent ** 2
    for i in range(1, k // 2 + 1):
        j = k - i
        multiplicity = choose(a, i) * choose(b, j)
        if i < j:
            multiplicity += choose(a, j) * choose(b, i)
            result += factorial(i) * factorial(j) * multiplicity ** 2
        else:
            result += 2 * factorial(i) ** 2 * multiplicity ** 2
    return result


def brute(a, b, maxrank):
    n = a + b
    V = tuple(range(n))
    result = [1]
    for k in range(1, min(maxrank, n) + 1):
        masks = []
        for domain in combinations(V, k):
            edges = tuple((i < a) != (j < a) for i, j in combinations(domain, 2))
            masks.append((domain, edges))
        count = 0
        for domain, orig_edges in masks:
            for image, _ in masks:
                for perm in permutations(image):
                    if all(edge == ((perm[i] < a) != (perm[j] < a)) for (i, j), edge in zip(combinations(range(k), 2), orig_edges)):
                        count += 1
        result.append(count)
    return result


def exact_polynomial_certificate():
    """Exact identity certificate by bounded bivariate polynomial interpolation.

    Both sides of the c4 identity have degree <=8 in n and <=4 in m;
    agreement on a 9-by-5 rectangular grid implies polynomial identity.
    Computations use exact rational arithmetic, not floating point.
    """
    # Degree <=6 in n and <=2 in m; a 7-by-3 grid certifies c3.
    for n in range(7):
        K = Fraction(n * (n - 1), 2)
        for m in range(3):
            c2 = 2 * ((K-m)**2 + m*m)
            T = Fraction(m*(n-2),2)
            E = Fraction(n*(n-1)*(n-2),6) - T
            c3 = 6*E*E + 2*T*T
            assert c3 == Fraction((n-2)**2,2) * (c2 - Fraction(2,3)*K*K)
    for n in range(9):
        K = Fraction(n * (n - 1), 2)
        def c4(n, m):
            u = Fraction(n**4-6*n**3+11*n*n-6*n-4*m*n*n+18*m*n-22*m+2*m*m, 24)
            v = Fraction(m*(n*n-3*n+4-2*m), 6)
            w = Fraction(m*(m-n+1),4)
            return 24*u*u+6*v*v+8*w*w
        for m in range(5):
            t=Fraction(m)-K/2
            lhs=c4(n,m)-c4(n,K-m)
            rhs=Fraction(2,3)*(n-2)*t*(8*t*t-n*(n-1))
            assert lhs==rhs, (n,m,lhs,rhs)


def validate():
    exact_polynomial_certificate()
    tests = [(2,2,4), (2,3,4), (3,3,4), (2,6,4), (4,4,4)]
    for a, b, k in tests:
        actual = brute(a,b,k)
        predicted = [rank_formula(a,b,r) for r in range(k+1)]
        assert actual == predicted, (a,b,actual,predicted)
    for h in range(2,20):
        pair1 = (h*h,h*h)
        pair2 = (h*h-h,h*h+h)
        for k in range(4):
            assert rank_formula(*pair1,k) == rank_formula(*pair2,k)
        assert rank_formula(*pair1,4) != rank_formula(*pair2,4)
    for n in range(4,100):
        signatures = {}
        for a in range(2,n//2+1):
            b=n-a
            sig=tuple(rank_formula(a,b,k) for k in (1,2,4))
            assert sig not in signatures, (n,a,b,signatures.get(sig))
            signatures[sig]=(a,b)
    print('BICLIQUE_PARTIAL_AUTOMORPHISM_CHECKS_PASSED')
    print('K_4,4 ranks 0..4', [rank_formula(4,4,k) for k in range(5)])
    print('K_2,6 ranks 0..4', [rank_formula(2,6,k) for k in range(5)])


if __name__=='__main__':
    validate()
