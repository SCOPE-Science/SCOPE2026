#!/usr/bin/env python3
"""Check the exact squared-distance spectrum of cycle graphic zonotopes.
Only mathematical definitions and reproducible checks are included.
"""
from itertools import product
from collections import Counter
from math import comb

def polynomial_formula(n):
    # For a row-indexed transfer matrix A, the contribution of a closed walk
    # is product A[i][j] over cyclic adjacent states.
    def poly_mat_mul(A,B):
        m=len(A); out=[[Counter() for _ in range(m)] for _ in range(m)]
        for i in range(m):
            for k in range(m):
                for j in range(m):
                    for x,c in A[i][k].items():
                        for y,d in B[k][j].items():
                            out[i][j][x+y]+=c*d
        return out
    def trpow(states,weights):
        m=len(states)
        A=[[Counter({(states[i]-states[j])**2:weights[j]}) for j in range(m)] for i in range(m)]
        B=[[Counter({0:int(i==j)}) if i==j else Counter() for j in range(m)] for i in range(m)]
        for _ in range(n):B=poly_mat_mul(B,A)
        return sum((B[i][i] for i in range(m)), Counter())
    # Addition in Python's Counter drops negative intermediates; subtract last.
    a=trpow([-1,0,1],[1,2,1]);b=trpow([0,1],[1,1]);
    return {k:a[k]-4*b[k]+(4 if k==0 else 0) for k in a.keys()|b.keys()|{0} if a[k]-4*b[k]+(4 if k==0 else 0)}

def brute(n):
    labels=[s for s in product((-1,1),repeat=n) if len(set(s))>1]
    X=[tuple((s[i]-s[(i-1)%n])//2 for i in range(n)) for s in labels]
    out=Counter()
    for x in X:
        for y in X:
            out[sum((a-b)**2 for a,b in zip(x,y))]+=1
    return dict(out)

def check(n):
    model=polynomial_formula(n)
    assert all(v>=0 and k%2==0 for k,v in model.items()),model
    assert sum(model.values())==(2**n-2)**2
    assert model.get(0)==2**n-2
    assert max(model)==4*(n if n%2==0 else n-1)
    assert model[max(model)]==(2 if n%2==0 else 2*n)
    if n<=8:
        ref=brute(n)
        assert model==ref,(n,model,ref)
    print(n,'PASS','vertices',2**n-2,'distance_types',len(model),'diameter2',max(model),'diametral_ordered',model[max(model)])
if __name__=='__main__':
    for n in range(3,10):check(n)
    print('CYCLE_ZONOTOPE_VERTEX_DISTANCE_EXACT_PASS')

def closed_recurrence(n):
    """Independent integer-polynomial recurrence for the three transfer eigenvalues."""
    def add(*ps):
        out=Counter()
        for p in ps:
            for k,v in p.items():out[k]+=v
        return dict((k,v) for k,v in out.items() if v)
    def mul(p,q):
        out=Counter()
        for i,a in p.items():
            for j,b in q.items():out[i+j]+=a*b
        return dict((k,v) for k,v in out.items() if v)
    s0={0:2};s1={0:3,4:1}
    a={0:3,4:1}; b={0:-2,2:4,4:-2}
    for j in range(2,n+1):
        new=add(mul(a,s1),mul(b,s0))
        s0,s1=s1,new
    sn=s1
    ant={4*j:comb(n,j)*(-1)**j for j in range(n+1)}
    # (1+z)^n+(1-z)^n has only even degrees.
    beta={j:-8*comb(n,j) for j in range(0,n+1,2)}
    return add(ant,sn,beta,{0:4})

def independent_checks():
    from fractions import Fraction
    for n in range(3,41):
        p=closed_recurrence(n)
        if n<=10:assert p==polynomial_formula(n),(n,'recurrence/transfer')
        assert all(k%2==0 and v>0 for k,v in p.items())
        q=(2**n-2)**2
        assert sum(p.values())==q
        assert p.get(0)==2**n-2
        mu=Fraction(sum(k*v for k,v in p.items()),q)
        m2=Fraction(sum(k*k*v for k,v in p.items()),q)
        assert mu==Fraction(n*(4**n-2**(n+1)),q)
        assert m2==Fraction(4**n*(n*n+2*n)-2**n*n*(n+1),q)
        assert max(p)==4*(n if n%2==0 else n-1)
        assert p[max(p)]==(2 if n%2==0 else 2*n)
    print('CYCLE_ZONOTOPE_RECURRENCE_MOMENTS_PASS 38')

if __name__=='__main__':independent_checks()
