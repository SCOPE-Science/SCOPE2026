"""Finite checks of the core-quandle homomorphism census.
Only finite corroboration; universal proof is given in RESULT.md.
"""
import itertools
import math
from collections import Counter


def bits(x, r):
    return [(x >> i) & 1 for i in range(r)]


def lapply(cols, x):
    y = 0
    for i, column in enumerate(cols):
        if (x >> i) & 1:
            y ^= column
    return y


def rank(cols):
    pivots = set()
    vals = set(lapply(cols, x) for x in range(1 << len(cols)))
    return (len(vals)).bit_length() - 1


def gaussian(n, k):
    num = den = 1
    for i in range(k):
        num *= 2**n - 2**i
        den *= 2**k - 2**i
    return num // den


def rank_matrix_count(n,k):
    a=math.prod(2**n-2**i for i in range(k))
    return gaussian(n,k)*a


def stirling(n,k):
    if n==0:return int(k==0)
    if k==0:return 0
    if k>n:return 0
    return k*stirling(n-1,k)+stirling(n-1,k-1)


def falling(a,k):
    return math.prod(a-j for j in range(k))


def mulpoly(p,q):
    z=Counter()
    for i,a in p.items():
        for j,b in q.items():
            z[i+j]+=a*b
    return z


def predicted_endomorphism(n):
    p=Counter()
    for k in range(n+1):
        C=2**(n-k); B=2**k
        one={B*t: B**C*falling(C,t)*stirling(C,t) for t in range(1,C+1)}
        all_p={0:1}
        for _ in range(B):
            all_p=mulpoly(all_p,one)
        for a,v in all_p.items():p[a]+=2**n*rank_matrix_count(n,k)*v
    return p


def predicted_idempotent(n):
    p=Counter()
    for k in range(n+1):
        p[4**k]+=gaussian(n,k)*2**(k*(n-k)+n-k+k*2**n+(n-2*k)*2**k)
    return p


def product(x,y,n):
    """x,y are 0..(4**n-1), encoded by parity p and higher bits u."""
    mask=(1<<n)-1
    p=x&mask; u=x>>n
    q=y&mask
    return p+((u^p^q)<<n)


def transform(cols,c,b,x,n):
    mask=(1<<n)-1
    p=x&mask; u=x>>n
    return (lapply(cols,p)^c)+((lapply(cols,u)^b[p])<<n)


def exhaustive(n):
    R=1<<n; U=1<<(n*R); universe=R*R
    actual_endomorphism=Counter();actual_retractions=Counter();total=0
    for cols in itertools.product(range(R), repeat=n):
        for c in range(R):
            for b in itertools.product(range(R), repeat=R):
                f=[transform(cols,c,b,x,n) for x in range(universe)]
                for x in range(universe):
                    for y in range(universe):
                        assert f[product(x,y,n)]==product(f[x],f[y],n)
                image=len(set(f));actual_endomorphism[image]+=1
                if all(f[f[x]]==f[x] for x in range(universe)):
                    actual_retractions[image]+=1
                total+=1
    pred=predicted_endomorphism(n); pred2=predicted_idempotent(n)
    assert actual_endomorphism==pred, (n,actual_endomorphism,pred)
    assert actual_retractions==pred2,(n,actual_retractions,pred2)
    assert total==2**(n*n+n+n*(2**n))
    print(f'r={n} |End|={total} image={dict(sorted(actual_endomorphism.items()))} idempotents={dict(sorted(actual_retractions.items()))}')
    if n==1:
        found=[]
        for f in itertools.product(range(universe),repeat=universe):
            if all(f[product(x,y,n)]==product(f[x],f[y],n) for x in range(universe) for y in range(universe)):
                found.append(f)
        assert len(found)==total
        print('r=1 brute force all set maps passed, homomorphisms',len(found))


if __name__=='__main__':
    for n in (1,2):exhaustive(n)
    assert sum(predicted_endomorphism(3).values())==2**(3*3+3+3*8)
    print('r=3 symbolic total identity:',sum(predicted_endomorphism(3).values()))
