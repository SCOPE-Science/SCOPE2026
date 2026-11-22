"""Independent FKM-generation / weighted-prenecklace checks."""
from fractions import Fraction
from math import gcd

def mu(n):
    p=2;s=1
    while p*p<=n:
        if n%p==0:
            n//=p;s=-s
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    if n>1:s=-s
    return s

def lyndon_count(n,q):
    return sum(mu(d)*q**(n//d) for d in range(1,n+1) if n%d==0)//n

def candidates(n,q):
    # FKM for the reversed alphabet: 0 becomes greatest original symbol.
    a=[0]*n; p=1
    while True:
        yield tuple(q-1-z for z in a),p
        j=n-1
        while j>=0 and a[j]==q-1:j-=1
        if j<0:break
        a[j]+=1;p=j+1
        for i in range(p,n):a[i]=a[i-p]

def inverse_test(w):
    return all(w>w[i:] for i in range(1,len(w)))

for q, nmax in [(2,17),(3,10),(4,7)]:
    for n in range(1,nmax+1):
        ws=list(candidates(n,q))
        assert len(ws)==sum(lyndon_count(d,q) for d in range(1,n+1)),(q,n,len(ws))
        assert all(inverse_test(w) for w,_ in ws)
        assert len(set(w for w,_ in ws))==len(ws)
        # All probability mass is exactly rational for arbitrary rational biases.
        ps=tuple(Fraction(i+1,q*(q+1)//2) for i in range(q))
        mass=sum((__import__('math').prod(ps[a] for a in w) for w,_ in ws),Fraction(0))
        assert 0<mass<=1
        if n in (1,5,nmax):
            print('q',q,'n',n,'prenecklaces',len(ws),'weighted_mass',mass,'n_mass',float(mass*n))
    print('PASS FKM, exact Möbius counts and weights, q=',q,'through',nmax)
