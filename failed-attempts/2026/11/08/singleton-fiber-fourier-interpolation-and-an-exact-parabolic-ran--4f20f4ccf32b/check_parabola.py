#!/usr/bin/env python3
"""Exact modular rank checks and numerical spectral identities for parabolic Fourier sampling.
Public, self-contained checker; Python 3 standard library only.
"""
import cmath
import math


def primes_up_to(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2, math.isqrt(p)+1))]


def auxiliary_choices(p):
    for l in primes_up_to(30000):
        if l % p == 1:
            for w in range(2,l):
                if pow(w,p,l)==1 and w!=1:
                    yield l,w
                    break


def rank_mod(M,l):
    A=[row[:] for row in M]
    nr=len(A);nc=len(A[0]);r=0
    for col in range(nc):
        pivot=next((j for j in range(r,nr) if A[j][col]%l),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][col],-1,l)
        A[r]=[(z*inv)%l for z in A[r]]
        for j in range(r+1,nr):
            x=A[j][col]
            if x:
                A[j]=[(v-x*w)%l for v,w in zip(A[j],A[r])]
        r+=1
        if r==nr:break
    return r


def rank_case(p,a,b,expected):
    # A nonzero modular minor certifies a nonzero complex cyclotomic minor.
    # A zero modulo one auxiliary prime does NOT certify a complex zero.
    best=0
    for trial,(l,w) in enumerate(auxiliary_choices(p)):
        M=[[pow(w,(a*s*t+b*s*s*t*t)%p,l) for t in range(p)] for s in range(p)]
        best=max(best,rank_mod(M,l))
        if best==expected:return best
        if trial>=30:break
    return best


def spectral_case(p,a,b):
    w=cmath.exp(2j*math.pi/p)
    U=list(range(1,p))
    # Find a primitive generator of F_p^*.
    g=next(x for x in U if len({pow(x,j,p) for j in range(p-1)})==p-1)
    log={pow(g,j,p):j for j in range(p-1)}
    values=[w**((a*u+b*u*u)%p) for u in U]
    Ks=[]
    for j in range(p-1):
        K=sum(z*cmath.exp(2j*math.pi*j*log[u]/(p-1)) for u,z in zip(U,values))
        Ks.append(K)
    S=Ks[0]
    # Verify the action on every multiplicative character, including the zero row.
    for j in range(1,p-1):
        for s in U:
            direct=sum(w**((a*s*t+b*s*s*t*t)%p)*cmath.exp(2j*math.pi*j*log[t]/(p-1)) for t in U)
            predicted=Ks[j]*cmath.exp(-2j*math.pi*j*log[s]/(p-1))
            assert abs(direct-predicted)<2e-10*(p-1)
    # Trace/determinant of the 2x2 exceptional block, computed two ways.
    trace=2*p-1+abs(S)**2
    det2=abs(S-(p-1))**2
    disc=trace*trace-4*det2
    assert disc>=-1e-9
    lo=(trace-math.sqrt(max(0,disc)))/2
    hi=(trace+math.sqrt(max(0,disc)))/2
    assert lo>0 if a else (lo>=-1e-9 if b else lo<1e-8)
    if a:
        assert all(abs(K)>1e-9 for K in Ks[1:])
    elif b:
        for j in range(1,p-1):
            if j%2:assert abs(Ks[j])<1e-9
            else:assert abs(Ks[j])>1e-9
    if b==0 and a:
        assert abs(lo-p)<1e-8 and abs(hi-p)<1e-8
        assert all(abs(abs(K)-math.sqrt(p))<1e-8 for K in Ks[1:])


def main():
    test_cases=0
    for p in (3,5,7,11):
        for a in range(p):
            for b in range(p):
                expected=1 if not a and not b else (p+1)//2 if not a else p
                rank=rank_case(p,a,b,expected)
                assert rank==expected,(p,a,b,rank,expected)
                test_cases+=1
    for p in (13,17,19,23,29):
        samples=[(0,0),(1,0),(0,1),(1,1),(2,1),(1,2),(p-1,p-1)]
        for a,b in samples:
            expected=1 if not a and not b else (p+1)//2 if not a else p
            rank=rank_case(p,a,b,expected)
            assert rank==expected,(p,a,b,rank,expected)
            test_cases+=1
    spectrum_cases=0
    for p in (3,5,7,11,13,17):
        for a,b in ((1,0),(0,1),(1,1),(2,1)):
            spectral_case(p,a,b)
            spectrum_cases+=1
    print('PARABOLA_FOURIER_EXACT_MODULAR_RANK_AND_CHARACTER_SPECTRUM_PASS',
          'rank_cases='+str(test_cases),'spectral_cases='+str(spectrum_cases))

if __name__=='__main__':main()
