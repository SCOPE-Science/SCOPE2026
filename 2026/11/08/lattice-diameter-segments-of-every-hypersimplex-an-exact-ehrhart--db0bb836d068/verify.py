"""Exact checks for hypersimplex lattice-diameter segment enumeration.
Only the standard library is needed. Finite checks corroborate the proof.
"""
from itertools import combinations, product
from math import comb, gcd, factorial
from fractions import Fraction


def bounded_compositions(q, s, t):
    if q == 0:
        return int(s == 0)
    if not 0 <= s <= q:
        return 0
    target = s*t
    return sum((-1)**j * comb(q,j) * comb((s-j)*t+q-j-1,q-1)
               for j in range(min(s-1,q)+1)) if s else 1


def formula(n,k,t):
    total = 0
    for p in range(1,min(k,n-k)+1):
        q = n-2*p
        # The number of unoriented balanced ternary directions is integral.
        count = factorial(n)//(factorial(p)**2*factorial(q)*2)
        total += count * bounded_compositions(q,k-p,t)
    return total


def compositions(t,k,n):
    for v in product(range(t+1),repeat=n):
        if sum(v) == k*t:
            yield v


def independent_brute(n,k,t):
    pts = list(compositions(t,k,n))
    return sum(1 for i,u in enumerate(pts) for v in pts[i+1:]
               if gcd(*[abs(a-b) for a,b in zip(u,v)]) == t)


def lagrange_polynomial_values(n,k):
    # Verify exact polynomial degree with finite differences, not infer it.
    d = max(n-3,0) if 1<k<n-1 else 0
    vals = [formula(n,k,t) for t in range(1,d+4)]
    for order in range(d+1):
        vals = [b-a for a,b in zip(vals,vals[1:])]
    return all(v == 0 for v in vals)


def eulerian(N,j):
    if j<0 or j>=N:
        return 0
    return sum((-1)**i*comb(N+1,i)*(j+1-i)**N for i in range(j+2))


def main():
    c=0
    for n in range(2,8):
        for k in range(1,n):
            for t in (1,2,3):
                actual = independent_brute(n,k,t)
                predicted = formula(n,k,t)
                assert actual == predicted, (n,k,t,actual,predicted)
                c+=1
    for n in range(2,15):
        for k in range(1,n):
            assert lagrange_polynomial_values(n,k),(n,k)
            c+=1
            if 2<=k<=n-2:
                d=n-3
                lead = Fraction(comb(n,2)*eulerian(d,k-2),factorial(d))
                # Finite differences of degree d gives d! times lead.
                a=[formula(n,k,t) for t in range(1,d+2)]
                for _ in range(d):
                    a=[y-x for x,y in zip(a,a[1:])]
                assert a[0]==lead*factorial(d),(n,k,lead,a[0])
                c+=1
            else:
                assert formula(n,k,3)==comb(n,2)
                c+=1
    for n in range(4,15):
        for t in range(1,9):
            assert formula(n,2,t)==comb(n,2)*comb(t+n-3,n-3)+3*comb(n,4)
            c+=1
    print('PASS',c,'independent exact assertions')

if __name__=='__main__': main()
