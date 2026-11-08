#!/usr/bin/env python3
"""Self-contained, exhaustive low-dimensional check of the quadratic-slice convolution spectrum.
Uses only the Python standard library. Runs all ambient Fourier characters, not samples.
"""
import cmath, itertools, math
from collections import Counter

class FiniteField:
    def __init__(self, p, degree=1, modulus=None):
        self.p, self.degree, self.q = p, degree, p**degree
        assert degree == 1 or (modulus is not None and len(modulus) == degree+1 and modulus[-1] == 1)
        digits=[]
        for a in range(self.q):
            v=a; row=[]
            for _ in range(degree): row.append(v % p); v//=p
            digits.append(row)
        self.add=[[0]*self.q for _ in range(self.q)]
        self.mul=[[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                u,v=digits[a],digits[b]
                self.add[a][b]=sum(((u[i]+v[i])%p)*p**i for i in range(degree))
                c=[0]*(2*degree-1)
                for i,x in enumerate(u):
                    for j,y in enumerate(v): c[i+j]=(c[i+j]+x*y)%p
                if degree>1:
                    for k in range(2*degree-2,degree-1,-1):
                        t=c[k]
                        for j in range(degree):c[k-degree+j]=(c[k-degree+j]-t*modulus[j])%p
                self.mul[a][b]=sum(c[i]*p**i for i in range(degree))
        traces=[]
        for a in range(self.q):
            acc=0; v=a
            for _ in range(degree):
                acc=self.add[acc][v]
                v=self.power(v,p)
            assert all(x==0 for x in digits[acc][1:])
            traces.append(acc % p)
        self.roots=[cmath.exp(2j*math.pi*tr/p) for tr in traces]
    def power(self,x,k):
        ans=1
        for _ in range(k):ans=self.mul[ans][x]
        return ans

def gaussian_binomial(d,r,q):
    return math.prod(q**(d-j)-1 for j in range(r))//math.prod(q**(j+1)-1 for j in range(r))

def nonsingular_symmetric_forms(r,q):
    k=r//2
    return q**(k*(k+1))*math.prod(q**(2*j+1)-1 for j in range(k+(r%2)))

def nonsingular_alternating_forms(s,q):
    return q**(s*(s-1))*math.prod(q**(2*j+1)-1 for j in range(s))

def multiplicities(q,d):
    if q%2:
        return {round(q**(d-r/2),9):q**(r+1)*gaussian_binomial(d,r,q)*nonsingular_symmetric_forms(r,q) for r in range(d+1)}
    return {q**(d-s):q**(d+2*s+1)*gaussian_binomial(d,2*s,q)*nonsingular_alternating_forms(s,q) for s in range(d//2+1)}

def exhaustive(p,degree,modulus,d):
    f=FiniteField(p,degree,modulus);q=f.q
    monomials=[(i,j) for i in range(d) for j in range(i,d)]
    V=list(itertools.product(range(q),repeat=d))
    features=[]
    for w in V:
        features.append((1, *w, *(f.mul[w[i]][w[j]] for i,j in monomials)))
    ncoef=(d+1)*(d+2)//2
    assert all(len(row)==ncoef for row in features)
    predicted=multiplicities(q,d)
    observed=Counter(); zeros=0; max_error=0.0
    for coeff in itertools.product(range(q),repeat=ncoef):
        total=0j
        for row in features:
            v=0
            for c,x in zip(coeff,row):
                if c:v=f.add[v][f.mul[c][x]]
            total+=f.roots[v]
        a=abs(total)
        if a<1e-7:zeros+=1
        else:
            level=min(predicted,key=lambda x:abs(x-a))
            max_error=max(max_error,abs(level-a))
            if abs(level-a)>1e-6:raise AssertionError((q,d,coeff,a,level))
            observed[level]+=1
    assert dict(observed)==predicted, (q,d,observed,predicted)
    assert zeros+sum(observed.values())==q**ncoef
    assert abs(sum(level*level*mult for level,mult in predicted.items())-q**(ncoef+d))<1e-7*q**(ncoef+d)
    print(f'PASS q={q} d={d} total={q**ncoef} nonzero={sum(observed.values())} zero={zeros} levels={len(predicted)} worst_error={max_error:.2g}')

def asymptotic_checks():
    for q in (2,4,8):
        odd_product=math.prod(1-q**(-(2*j-1)) for j in range(1,100))
        all_product=math.prod(1-q**(-j) for j in range(1,200))
        target_even=(1+odd_product*all_product)/2
        target_odd=(1-odd_product*all_product)/2
        def density(d):
            return sum(multiplicities(q,d).values())/q**((d+1)*(d+2)//2)
        assert abs(density(12)-target_even)<0.002
        assert abs(density(13)-target_odd)<0.002
        print(f'PASS even-field q={q} density_even_limit={target_even:.10f} density_odd_limit={target_odd:.10f}')
    for q in (3,5):
        def density(d):
            return sum(multiplicities(q,d).values())/q**((d+1)*(d+2)//2)
        assert abs(density(12)-q/(q+1))<1e-4
        print(f'PASS odd-field q={q} density_limit={q/(q+1):.10f}')

if __name__=='__main__':
    for case in ((2,1,None,1),(2,1,None,2),(2,1,None,3),(2,1,None,4),
                 (3,1,None,1),(3,1,None,2),(3,1,None,3),
                 (5,1,None,1),(5,1,None,2),
                 (2,2,[1,1,1],1),(2,2,[1,1,1],2),
                 (2,3,[1,1,0,1],1),(3,2,[1,0,1],1)):
        exhaustive(*case)
    asymptotic_checks()
    print('VERONESE_AFFINE_SLICE_SPECTRUM_PASS')
