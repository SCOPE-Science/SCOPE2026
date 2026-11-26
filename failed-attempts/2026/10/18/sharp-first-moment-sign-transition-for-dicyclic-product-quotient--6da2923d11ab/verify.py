"""Exact integer-arithmetic checks for the dicyclic first-moment sign theorem.

The infinite portion is proved algebraically in RESULT.md. This program only
checks the finite range and independently audits the cycle decompositions.
"""
from math import gcd
from functools import lru_cache

@lru_cache(None)
def lucas(m):
    assert m >= 1
    a, b = 2, 1
    for _ in range(m):
        a, b = b, a + b
    return a


def first_moment(n):
    assert n >= 2
    mod = 2*n
    total = -4*n*7**(n-1)
    for j in range(mod):
        d = gcd(mod,j)
        e = gcd(mod,n-j)
        quotient_avoid = lucas(mod//d)**(2*d)
        product_avoid = 3**(n-int(j % 2 == 0)) * lucas(mod//e)**e
        total += quotient_avoid-product_avoid
    return total


def lower_bound_tripled(n):
    # Exactly three times the sufficient lower bound on M_1(n).
    return (2*9**n - 3**(n+1)
            - 3*(2*n-2)*8**n - 12*n*7**(n-1))


def mul(x, y, n):
    i, t = x
    j, u = y
    return ((i + (-1)**t*j + n*t*u) % (2*n), (t+u)%2)


def inverse(x, n):
    i, t = x
    return ((-i if not t else i+n)%(2*n),t)


def cycles(p):
    used=set(); sizes=[]
    for a in range(len(p)):
        if a not in used:
            i=a; sz=0
            while i not in used:
                used.add(i); sz+=1; i=p[i]
            sizes.append(sz)
    return sizes


def independent_product(p):
    result=1
    for m in cycles(p):
        result*=lucas(m)
    return result


def first_moment_permutations(n):
    G=[(i,t) for t in (0,1) for i in range(2*n)]
    ids={a:i for i,a in enumerate(G)}
    ans=0
    for g in G:
        P=[ids[mul(inverse(x,n),g,n)] for x in G]
        Q=[ids[mul(g,x,n)] for x in G]
        ans+=independent_product(Q)-independent_product(P)
    return ans


def first_moment_bruteforce(n):
    G=[(i,t) for t in (0,1) for i in range(2*n)]
    l=len(G); ids={a:i for i,a in enumerate(G)}
    products=[[1<<ids[mul(x,y,n)] for y in G] for x in G]
    quotients=[[1<<ids[mul(x,inverse(y,n),n)] for y in G] for x in G]
    ans=0
    for mask in range(1<<l):
        chosen=[i for i in range(l) if mask>>i&1]
        p=q=0
        for i in chosen:
            for j in chosen:
                p|=products[i][j]
                q|=quotients[i][j]
        ans+=p.bit_count()-q.bit_count()
    return ans


def main():
    values={n:first_moment(n) for n in range(2,41)}
    assert all(values[n]<0 for n in range(2,30))
    assert all(values[n]>0 for n in range(30,41))
    assert values[29]==-203011530049362987071455440
    assert values[30]==397569666293094423242677920
    assert lower_bound_tripled(41)==105308709116820901835784452756627203197>0
    for n in range(2,16):
        assert first_moment_permutations(n)==values[n],n
    for n in range(2,5):
        assert first_moment_bruteforce(n)==values[n],n
    print('VERIFICATION_OK: n=2..40 exact sign; n=2..15 permutation; n=2..4 direct subsets')
    print('M1(29) =',values[29])
    print('M1(30) =',values[30])
    print('3 * lower_bound(41) =',lower_bound_tripled(41))


if __name__ == '__main__':
    main()
