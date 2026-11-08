"""Exact finite-field checks for the Artin--Mumford quotient and zeta factorization.
No external libraries. All calculations take place over explicit finite fields.
"""
from collections import Counter

def is_prime(p):
    return p >= 2 and all(p % j for j in range(2, int(p ** .5)+1))

def checks(p):
    assert is_prime(p) and p % 2 == 1
    nonresidue = next(d for d in range(2, p) if pow(d,(p-1)//2,p) == p-1)
    def add(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x): return ((-x[0])%p,(-x[1])%p)
    def sub(x,y): return add(x,neg(y))
    def mul(x,y):
        a,b=x;c,e=y
        return ((a*c+nonresidue*b*e)%p,(a*e+b*c)%p)
    def power(a,n):
        z=(1,0)
        while n:
            if n&1: z=mul(z,a)
            a=mul(a,a);n//=2
        return z
    zero=(0,0);one=(1,0)
    for degree in [1,2]:
        field=[(a,b) for a in range(p) for b in (range(p) if degree==2 else [0])]
        q=len(field)
        counts=Counter(sub(power(a,p),a) for a in field)
        assert sum(counts.values())==q and all(v==p for v in counts.values())
        C=2*p
        for w in field:
            if w==zero: continue
            wi=power(w,q-2)
            C += counts[w]*counts[wi]
        H={}
        for t in range(1,p):
            n=2
            for w in field:
                if w==zero: continue
                wi=power(w,q-2)
                target=sub(wi,mul((t,0),w))
                n+=counts[target]
            H[t]=n
        assert C-(q+1)==sum(n-(q+1) for n in H.values())
        for t in range(1,p):
            for u in range(1,p):
                t2=t*pow(u,-2,p)%p
                assert H[t]==H[t2],(p,degree,t,u,t2)
        if degree==1:
            assert C==2*p
            assert all(H[t]==(2*p+2 if pow(t,(p-1)//2,p)==1 else 2) for t in H)
        print(f'p={p} field=F_{q} C_points={C} H_square={H[1]} H_nonsquare={H[nonresidue]} L_trace_identity=OK')
for p in [3,5,7,11]: checks(p)
print('ALL_CHECKS_PASSED')
