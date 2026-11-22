#!/usr/bin/env python3
"""Finite arithmetic checks for generalized derangements with parameter 2.
No external libraries required. Run: python3 verify.py
"""
from math import factorial


def poly_add(a,b):
    n=max(len(a),len(b))
    return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def poly_scale(a,z):return [z*x for x in a]

def falling(r,cut):
    f=[1];total=[0]
    for j in range(cut):
        total=poly_add(total,poly_scale(f,(-1)**j))
        f=poly_mul(f,[r-j,2])
    return total

def get_mod_coeff(p,m):
    return [v%m for v in p]

def verify_polynomial_normal_forms():
    for r,limit,target in [(0,5,[0,1]),(1,6,[1,1])]:
        x=[r,2]
        p=poly_add(poly_add(poly_mul(x,x),poly_scale(x,5)),[5])
        f=falling(r,limit)
        if r==0:
            num=poly_add(poly_mul(p,f),poly_scale(poly_add(x,[5]),-1))
        else:
            num=poly_add(poly_add(x,[3]),poly_scale(poly_mul(p,f),-1))
        assert all(c%4==0 for c in num)
        q=[c//4 for c in num]
        assert get_mod_coeff(q,2)[:len(target)]==target
        assert all(v%2==0 for v in q[len(target):])
    return 2


def generalized(nmax,mod=None):
    a,b=(1,2) if mod is None else (1%mod,2%mod)
    out=[a,b]
    for n in range(2,nmax):
        a,b=b,(n+1)*b+(n-1)*a
        if mod is not None: b%=mod
        out.append(b)
    return out[:nmax]


def ord2(z):
    if not z:return float('inf')
    return (abs(z)&-abs(z)).bit_length()-1


def direct_formula_tests():
    seq=generalized(50)
    d=[1,0]
    for n in range(2,52): d.append(n*d[-1]+(-1)**n)
    for n in range(50):
        lhs=seq[n]
        rhs=(d[n]+2*d[n+1]+d[n+2])//2
        assert lhs==rhs,(n,lhs,rhs)
        assert (d[n]+2*d[n+1]+d[n+2])%2==0
    # Coefficient formula in the original motivating paper.
    for n in range(15):
        z=sum((-1)**j*factorial(n)//factorial(j)*__import__('math').comb(2+n-j,n-j) for j in range(n+1))
        assert seq[n]==z,(n,seq[n],z)
    return 65


def residue_tests():
    checks=0
    for k in range(1,14):
        m=1<<k
        out=generalized(2*m,mod=m)
        assert len(set(out[:m]))==m
        assert out[m:2*m]==out[:m]
        for i,a in enumerate(out[:m]):
            assert a%2!=i%2
            checks+=1
        for s in range(0,m, max(1,m//71)):
            for t in range(s+1,m,max(1,m//73)):
                assert ord2(out[s]-out[t])==ord2(s-t),(k,s,t)
                checks+=1
    return checks


def forbidden(x):
    if x==0:return False
    v=ord2(x)
    return v%2==0 and ((x>>v)%8==7)


def three_squares_tests():
    # All residue classes of each forbidden stratum have a unique index class.
    out=generalized(1<<14,mod=1<<20)
    c=0
    expected=[2,23,115,227,675]
    for j,a in enumerate(expected):
        m=1<<(2*j+3)
        target=(7<<(2*j))%m
        found=[i for i in range(m) if out[i]%m==target]
        assert found==[a],(j,found)
        c+=m
    # Testing 10000 terms directly with giant integers
    # is unnecessary: check the same local residue implications mod 2^20.
    for n in range(10000):
        v=out[n]
        if v%8==7:assert n%8==2
        if v%32==28:assert n%32==23
        c+=1
    return c

if __name__=='__main__':
    counts={
        'polynomial_normal_forms':verify_polynomial_normal_forms(),
        'recurrence_and_closed_formula':direct_formula_tests(),
        'complete_residue_and_distance_tests':residue_tests(),
        'obstruction_progressions':three_squares_tests(),
    }
    print('PASS',counts,'total_assertion_families',sum(counts.values()))
