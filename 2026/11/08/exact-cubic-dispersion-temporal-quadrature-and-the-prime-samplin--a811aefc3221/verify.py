#!/usr/bin/env python3
"""Exact integer checks for uniform time quadrature of positive cubic Fourier bands."""
from math import gcd

def aliased(K, N):
    return [(h,r,m) for h in range(1,K) for r in range(1,K-h)
            for m in range(K-h-r) if 3*h*r*(2*m+h+r) % N == 0]

def residue_test(K,N):
    M=N//gcd(N,3)
    for h in range(1,K):
        for r in range(1,K-h):
            t=M//gcd(M,h*r)
            g=gcd(2,t)
            if (h+r)%g: continue
            mod=t//g
            inv=pow(2//g,-1,mod) if mod>1 else 0
            m0=(-(h+r)//g*inv)%mod if mod>1 else 0
            if m0<=K-1-h-r:return True
    return False

def prime(p):
    return p>1 and all(p%d for d in range(2,int(p**0.5)+1))

def nextprime(n):
    while not prime(n):n+=1
    return n

def direct_and_defect(K,N):
    # positive rational coefficients make positivity and coefficient ordering exact
    a=[2+j+(j%3) for j in range(K)]
    s=sum(x*x for x in a)
    continuous=2*s*s-sum(x**4 for x in a)
    # Directly enumerate pairs of ordered pairs in each spatial frequency.
    sampled=0
    for i in range(K):
        for j in range(K):
            for k in range(K):
                l=i+j-k
                if not 0<=l<K:continue
                if ((i**3+j**3-k**3-l**3)%N)==0:
                    sampled+=a[i]*a[j]*a[k]*a[l]
    defect=4*sum(a[m+h]*a[m]*a[m+h+r]*a[m+r] for h,r,m in aliased(K,N))
    assert sampled == continuous+defect, (K,N,sampled,continuous,defect)
    return continuous, sampled

def main():
    checked=0
    for K in range(1,17):
        for N in range(1,85):
            x=bool(aliased(K,N)); assert x==residue_test(K,N),(K,N,x)
            assert x==any(3*h*r*(2*m+h+r)%N==0 for h in range(1,K) for r in range(1,K-h) for m in range(K-h-r))
            if K<=9:direct_and_defect(K,N)
            checked+=1
    for K in range(4,36):
        p=nextprime(2*K-3)
        assert not aliased(K,p)
        for prime_candidate in range(2,p):
            if prime(prime_candidate):assert aliased(K,prime_candidate),(K,prime_candidate)
    assert aliased(3,2) and aliased(3,3) and not aliased(3,4)
    # Signed defect and all four coefficient phases, directly against ordered quadruples.
    for K in range(3,7):
        for N in range(1,23):
            a=[complex(j+1,(-1)**j*(j%3+1)) for j in range(K)]
            S=sum(abs(z)**2 for z in a)
            cont=2*S*S-sum(abs(z)**4 for z in a)
            direct=sum(a[i]*a[j]*a[k].conjugate()*a[l].conjugate()
                       for i in range(K) for j in range(K) for k in range(K)
                       for l in [i+j-k] if 0<=l<K
                       if (i**3+j**3-k**3-l**3)%N==0)
            defect=4*sum((a[m+h]*a[m].conjugate()*a[m+h+r].conjugate()*a[m+r]).real
                         for h,r,m in aliased(K,N))
            assert abs(direct.imag)<1e-9 and abs(direct.real-cont-defect)<1e-9, (K,N,direct,cont,defect)
    assert 4*sum((a[m+h]*a[m].conjugate()*a[m+h+r].conjugate()*a[m+r]).real
                 for h,r,m in aliased(3,2) for a in [(1,1,-1)]) == -4
    assert not aliased(1,1) and not aliased(2,1)
    # A direct strict difference from quadratic sampling: seven modes, seven time samples.
    assert (1,2,2) in aliased(7,7)
    print('CUBIC_TEMPORAL_QUADRATURE_CHECK_PASS')
    print('exact integer residue cases:', checked)
    print('direct fourth-moment pairs:',9*84)
    print('prime-band thresholds:', 32)
    print('Gaussian complex coefficients: 88 direct comparisons')
    print('signed negative defect K=3,N=2: -4')
    print('special boundary K=3,N=4: exact')
if __name__=='__main__':main()
