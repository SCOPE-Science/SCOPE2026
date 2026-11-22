#!/usr/bin/env python3
"""Supplementary finite diagnostics for a three-mask two-sparse Fourier theorem.
No finite loop substitutes for the analytic all-dimension proof.
"""
import cmath, math, random
from fractions import Fraction


def masks(n):
    rho = 2.0 ** (1.0 / n)
    theta = math.pi / n
    return ([1+0j]*n,
            [rho**j+0j for j in range(n)],
            [rho**(2*j)*cmath.exp(1j*theta*j) for j in range(n)])


def acorr(mask, sig):
    n=len(sig)
    z=[a*b for a,b in zip(mask,sig)]
    return [sum(z[(s+h)%n]*z[s].conjugate() for s in range(n)) for h in range(n)]


def isclose(a,b,tol=1e-7):
    return abs(a-b)<=tol*max(1.0,abs(a),abs(b))


def decode(n, data):
    q=2.0**(2.0/n)
    masklist=masks(n)
    m0=data[0][0].real
    if isclose(m0,0):return [0j]*n
    m1=data[1][0].real
    m2=data[2][0].real
    if isclose(m2*m0,m1*m1,1e-9):
        a=min(range(n),key=lambda j:abs(q**j-m1/m0))
        assert isclose(q**a,m1/m0)
        y=[0j]*n;y[a]=math.sqrt(m0)
        return y
    candidates=[]
    for a in range(n):
        for b in range(a+1,n):
            A=q**a;B=q**b
            u=(B*m0-m1)/(B-A)
            v=(m1-A*m0)/(B-A)
            if u<=0 or v<=0:continue
            if not isclose(m2,(A+B)*m1-A*B*m0,2e-9):continue
            h=b-a
            if 2*h==n:
                # C0(n)=2 Re(P), C2(n)=-2q^(a+b) Im(P).
                P=complex(data[0][h].real/2,-data[2][h].real/(2*q**(a+b)))
            else:
                P=data[0][h]
            if not isclose(abs(P)**2,u*v,2e-8):continue
            y=[0j]*n
            y[a]=math.sqrt(u)
            y[b]=P/math.sqrt(u)
            if all(all(isclose(acorr(masklist[l],y)[h], data[l][h], 2e-8)
                       for h in range(n)) for l in range(3)):
                candidates.append(y)
    assert len(candidates)==1,('ambiguous',n, len(candidates))
    return candidates[0]


def equiv(a,b):
    ids=[j for j,x in enumerate(a) if abs(x)>1e-8]
    ids2=[j for j,x in enumerate(b) if abs(x)>1e-8]
    if ids!=ids2:return False
    if not ids:return True
    phase=a[ids[0]]/b[ids[0]]
    return isclose(abs(phase),1,1e-7) and all(isclose(x,phase*y,1e-7) for x,y in zip(a,b))


def exact_identity_tests():
    ct=0
    for R in (Fraction(2),Fraction(3),Fraction(5)):
        for x in (Fraction(1),Fraction(2),Fraction(5)):
            for y in (x+Fraction(1,10),x*(R+1)/2):
                if not x<y<R*x:continue
                t=R*(x+y)/(R+1)
                left=x*x*(t-x)*(R*x-t)-y*y*(t-y)*(R*y-t)
                right=-R*(x-y)*(x+y)*(R*x-y)*(x-R*y)/(R+1)**2
                assert left==right and left!=0
                ct+=1
    return ct


def main():
    rng=random.Random(20261119)
    cases=0
    for n in range(4,21,2):
        w=masks(n)
        z=[0j]*n
        assert equiv(z,decode(n,[acorr(g,z) for g in w]))
        for a in range(n):
            y=[0j]*n;y[a]=complex(0.2+a/7,-0.6)
            assert equiv(y,decode(n,[acorr(g,y) for g in w]))
            cases+=1
        for a in range(n):
            for b in range(a+1,n):
                for j in range(5):
                    u=0.5+0.7*rng.random()
                    v=0.3+0.9*rng.random()
                    phi=([math.pi/2,-math.pi/2,0, math.pi/4,0.77])[j]
                    y=[0j]*n
                    y[a]=u
                    y[b]=v*cmath.exp(1j*phi)
                    result=decode(n,[acorr(g,y) for g in w])
                    assert equiv(y,result), (n,a,b,j)
                    cases+=1
    print('CHECK_OK', 'two_sparse_cases='+str(cases),
          'rational_factor_identities='+str(exact_identity_tests()),
          'dimensions=4,6,...,20')

if __name__=='__main__':main()
