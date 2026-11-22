"""Reproducibility checks for prescribed square fibers in truncated cyclic path algebras.
Python 3 standard library; F_4 encoded as binary polynomials modulo X^2+X+1.
"""
from itertools import product
from collections import Counter
from math import prod


def mul(a,b,q):
    if q!=4: return a*b%q
    v=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1: v ^=1<<(i+j)
    if v & 8: raise AssertionError
    if v & 4: v^=7  # X^2=X+1 in F4
    return v

def inv(a,q):
    assert a
    return next(b for b in range(1,q) if mul(a,b,q)==1)

def weighted_path(k,w):
    if k<=0:return 1
    f0,f1=1,1+w
    for _ in range(2,k+1):f0,f1=f1,f1+w*f0
    return f1

def weighted_cycle(n,w):
    return weighted_path(n-1,w)+w*weighted_path(n-3,w)

def formula(c,q):
    n=len(c);w=q-1; e=[x!=0 for x in c]
    if all(e):
        even=odd=1
        for i,v in enumerate(c):
            if i%2==0:even=mul(even,v,q)
            else:odd=mul(odd,v,q)
        if n%2==0:return w if even==odd else 0
        r=mul(even,inv(odd,q),q)
        return sum(mul(x,x,q)==r for x in range(q))
    if not any(e):return weighted_cycle(n,w)
    gaps=[]
    for i in range(n):
        if e[i] and not e[(i+1)%n]:
            j=(i+1)%n;L=0
            while not e[j]:
                L+=1;j=(j+1)%n
            gaps.append(L)
    if any(L==1 for L in gaps):return 0
    return w**len(gaps)*prod(weighted_path(L-3,w) for L in gaps)

def transfer_trace(n,w):
    states=list(product((0,1),repeat=2)); T=[[0]*4 for _ in states]
    for i,(a,b) in enumerate(states):
        for j,(d,c) in enumerate(states):
            if d==b and not(a==1 and b==0 and c==1):T[i][j]=w if c else 1
    P=[[int(i==j) for j in range(4)] for i in range(4)]
    def mm(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    for _ in range(n):P=mm(P,T)
    return sum(P[i][i] for i in range(4))

def image_formula(n,q):
    w=q-1
    full=(w**(n-1) if n%2==0 else w**n//__import__('math').gcd(2,w))
    return transfer_trace(n,w)-w**n+full

def verify(q,n):
    samples=Counter()
    for a in product(range(q),repeat=n):
        c=tuple(mul(a[i],a[(i+1)%n],q) for i in range(n))
        samples[c]+=1
    for c in product(range(q),repeat=n):
        assert samples[c]==formula(c,q),(q,n,c,samples[c],formula(c,q))
    assert len(samples)==image_formula(n,q),(q,n,len(samples),image_formula(n,q))
    print(f'q={q}, n={n}: tested {q**n} root inputs and {q**n} prescribed targets; image={len(samples)}, zero_fiber={samples[(0,)*n]}, full_support_attainable={sum(1 for c in samples if all(c))}; PASS')

if __name__=='__main__':
    for q,n in [(2,3),(2,4),(2,5),(2,6),(2,8),(3,3),(3,4),(3,5),(3,6),(4,3),(4,4),(4,5),(5,3),(5,4)]:verify(q,n)
