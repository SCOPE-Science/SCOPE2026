"""Independent exact-rational lattice-count check for two-row rook-polytope moments.

Run: python verification/check_rook_moments.py
No third-party dependencies. Weighted lattice-point sums and forward differences
check the full-dimensional volume and selected monomial integrals.
"""
from fractions import Fraction
from math import comb, factorial
from functools import lru_cache

@lru_cache(None)
def compositions_leq(n, t):
    if n == 0:
        return ((),)
    return tuple((k,) + tail for k in range(t + 1)
                 for tail in compositions_leq(n - 1, t - k))


def integral_two_row(n, alpha, beta):
    """Claimed unnormalized integral, using the explicit polynomial cap formula."""
    A, B = sum(alpha), sum(beta)
    Q = Fraction(1, factorial(n + A) * factorial(n + B))
    for z in alpha:
        Q *= factorial(z)
    for z in beta:
        Q *= factorial(z)
    cap_sum = Fraction(0)
    for j in range(n):
        a = n - 1 + A - alpha[j]
        b = n - 1 + B - beta[j]
        coef = Fraction(1, factorial(a) * factorial(b))
        for i in range(n):
            if i != j:
                coef *= factorial(alpha[i]) * factorial(beta[i])
        integ = Fraction(0)
        for p in range(alpha[j] + 1):
            for q in range(beta[j] + 1):
                integ += (Fraction((-1)**(p+q)*comb(alpha[j],p)*comb(beta[j],q)
                                   *factorial(a+p)*factorial(b+q),
                                   factorial(a+b+p+q+2)))
        cap_sum += coef * integ
    return Q - cap_sum


def weighted_lattice_sums(n, names, max_t):
    result = {name: [] for name in names}
    for t in range(max_t+1):
        sums = {name: 0 for name in names}
        rows = compositions_leq(n,t)
        for x in rows:
            for y in rows:
                if all(x[k]+y[k] <= t for k in range(n)):
                    xx=x[0]
                    y0=y[0]
                    y1=y[1] if n>=2 else 0
                    x1=x[1] if n>=2 else 0
                    if 'one' in sums: sums['one'] += 1
                    if 'x' in sums: sums['x'] += xx
                    if 'xx' in sums: sums['xx'] += xx*xx
                    if 'row' in sums: sums['row'] += xx*x1
                    if 'col' in sums: sums['col'] += xx*y0
                    if 'cross' in sums: sums['cross'] += xx*y1
                    if 'cubic' in sums: sums['cubic'] += xx*xx*y1
        for name in names:
            result[name].append(sums[name])
    return result


def leading(values, degree):
    assert len(values) >= degree+1
    return Fraction(sum((-1)**(degree-t)*comb(degree,t)*values[t]
                        for t in range(degree+1)), factorial(degree))


def main():
    comparisons=0
    for n in (1,2,3,4):
        names=['one'] if n==4 else (['one','x','xx','col'] if n==1 else
                                    ['one','x','xx','row','col','cross','cubic'])
        exponents = {}
        for label in names:
            a=[0]*n; b=[0]*n
            if label in ('x','xx','row','col','cross','cubic'): a[0]=2 if label in ('xx','cubic') else 1
            if label == 'row': a[1]=1
            if label == 'col': b[0]=1
            if label in ('cross','cubic'): b[1]=1
            exponents[label]=(tuple(a),tuple(b))
        degrees = {label:2*n+sum(a)+sum(b) for label,(a,b) in exponents.items()}
        sums=weighted_lattice_sums(n,names,max(degrees.values()))
        for label in names:
            actual=leading(sums[label],degrees[label])
            predicted=integral_two_row(n,*exponents[label])
            assert actual==predicted, (n,label,actual,predicted)
            comparisons+=1
        V=integral_two_row(n,(0,)*n,(0,)*n)
        assert factorial(2*n)*V == comb(2*n,n)-n
        comparisons+=1
        if n>=2:
            z=V
            mm={name:integral_two_row(n,*exponents[name])/z for name in ('x','xx','row','col','cross') if name in exponents}
            if n<=3:
                assert mm['xx']-mm['x']**2>0
                assert mm['row']-mm['x']**2<0
                assert mm['col']-mm['x']**2<0
                assert mm['cross']-mm['x']**2>0
                comparisons+=4
        print('n',n,'normalized_volume',factorial(2*n)*V,'lattice_ehrhart_checks',len(names))
    print('TWO_ROW_ROOK_EXACT_CHECKS_PASSED',comparisons)

if __name__=='__main__':
    main()
