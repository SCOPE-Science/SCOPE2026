#!/usr/bin/env python3
"""Direct finite-ring tests for the commutator Fourier transform on triangular 3x3 algebras."""
from itertools import product
from collections import Counter


def v(a,q,L):
    if a==0:return L
    t=0
    while a%q==0 and t<L:
        a//=q;t+=1
    return t

def spectrum_formula(p,q,r,Q,L):
    a,b,c=v(p,Q,L),v(q,Q,L),v(r,Q,L)
    alpha=min(a,b,c)
    beta=min(L,min(a+b,a+c,b+c,2*c)-alpha)
    return Q**(8*L+2*(alpha+beta)),(alpha,beta)

def B(p,q,r,mod):
    return [[0,0,0,p,0,r],[0,0,0,-p,q,0],[0,0,0,0,-q,-r],[-p,p,0,0,r,0],[0,-q,q,-r,0,0],[-r,0,r,0,0,0]]

def kernel_count(p,q,r,mod):
    # Count solutions to B v=0 by splitting the 6 variables into (a,b,c) and (x,y,z).
    M=B(p,q,r,mod)
    rows=[[a%mod for a in row] for row in M]
    # 4^6=4096 integer tuples, fast enough. Every row equation is checked directly.
    return sum(all(sum(row[j]*vv[j] for j in range(6))%mod==0 for row in rows) for vv in product(range(mod),repeat=6))

def independent_profile_check(Q,L,lim=None):
    mod=Q**L
    triples=list(product(range(mod),repeat=3))
    if lim is not None:
        idxs=sorted({0,len(triples)-1,len(triples)//2,17%len(triples),33%len(triples),71%len(triples),97%len(triples), 127%len(triples)})
        triples=[triples[j] for j in idxs]
    cnt=Counter()
    for p,q,r in triples:
        expected,(alpha,beta)=spectrum_formula(p,q,r,Q,L)
        got=mod**6*kernel_count(p,q,r,mod)
        assert got==expected,(Q,L,p,q,r,got,expected,alpha,beta)
        cnt[alpha+beta]+=1
    return cnt,len(triples)

# Independent matrix multiplication for smallest field (not relying on Pfaffian reduction).
def ring_bracket(X,Y,mod):
    a,b,c,x,y,z=X;d,e,f,s,h,t=Y
    return ((a-b)*s-(d-e)*x,(b-c)*h-(e-f)*y,(a-c)*t-(d-f)*z+x*h-s*y)

def direct_field_fibers(mod):
    F=Counter()
    elems=product(range(mod),repeat=6)
    allX=list(elems)
    for X in allX:
        for Y in allX:
            F[tuple(t%mod for t in ring_bracket(X,Y,mod))]+=1
    # inversion via ordinary integer-valued Ramanujan sums of valuation shells
    def ram(i,z):
        if i==1: return 1
        if z%mod==0: return mod-1
        return -1
    formula={}
    for U in product(range(mod), repeat=3):
        total=0
        for s,t,r in product(range(mod),repeat=3):
            # over prime field, number of primitive frequency vectors grouped by zero/nonzero valuations
            w,_=spectrum_formula(s,t,r,mod,1)
            # primitive additive character orthogonality via residue ring exponent, use exact congruence for q2
            # we use cos via complex Fourier only q2 to stay integral
            if mod==2:
                total+=w*((-1)**((s*U[0]+t*U[1]+r*U[2])%2))
        if mod==2:
            assert total%mod**3==0
            formula[U]=total//mod**3
    if mod==2: assert F==formula,(F,formula)
    return len(F),sum(F.values())

if __name__=='__main__':
    for Q,L,lim in [(2,1,None),(3,1,None),(2,2,None),(2,3,8),(3,2,8)]:
        c,n=independent_profile_check(Q,L,lim)
        print('FOURIER_PFAFFIAN_KERNEL_OK',Q,L,n,sorted(c.items()))
    print('DIRECT_BRACKET_FIBERS_OK',direct_field_fibers(2))
    print('TRIANGULAR_FOURIER_SPECTRUM_OK')

def dual2_mul(a,b):
    x,y=a&1,a>>1
    u,v=b&1,b>>1
    return (x*u) | (((x*v) ^ (y*u))<<1)

def dual2_kernel_count(p,q,r):
    M=[[abs(a) for a in row] for row in B(p,q,r,4)]
    count=0
    for xx in product(range(4),repeat=6):
        okay=True
        for row in M:
            val=0
            for j in range(6):
                val ^= dual2_mul(row[j],xx[j])
            if val:
                okay=False
                break
        if okay:count+=1
    return count

def dual2_verification():
    import itertools
    count=0
    for p,q,r in itertools.product(range(4),repeat=3):
        got=4**6*dual2_kernel_count(p,q,r)
        expected,_=spectrum_formula(p,q,r,2,2)
        assert got==expected,(p,q,r,got,expected)
        count+=1
    return count

if __name__=='__main__':
    print('DUAL_NUMBER_RING_OK',dual2_verification())
