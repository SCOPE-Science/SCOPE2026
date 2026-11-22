#!/usr/bin/env python3
"""Exact polynomial and spectral diagnostics for real-ball harmonic-coordinate compression."""
from fractions import Fraction
import math
import sympy as s
x,y,z=s.symbols('x y z', real=True); vec=(x,y,z); d=3

def iszero(a): return s.expand(a)==0

def homogeneous_components(P):
    q=s.Poly(s.expand(P),x,y,z)
    comps={}
    for exp,a in q.terms():
        n=sum(exp)
        comps[n]=comps.get(n,0)+a*x**exp[0]*y**exp[1]*z**exp[2]
    return comps

def toeplitz(P,j,beta):
    out=0
    for n,f in homogeneous_components(P).items():
        assert iszero(sum(s.diff(f,v,2) for v in vec)),(n,f)
        if n:
            A=s.Rational(1,2*n+d-2)
            B=s.Rational(1,1)/(2*n+d+2*beta)
            out+=s.expand(vec[j]*f-A*(x*x+y*y+z*z)*s.diff(f,vec[j])+B*s.diff(f,vec[j]))
        else:out+=vec[j]*f
    return s.expand(out)

def run():
    cnt=0
    for beta in [s.Rational(0),s.Rational(1),s.Rational(3,2)]:
        for l in range(1,7):
            polynomials=[s.expand(s.re((x+s.I*y)**l)),s.expand(s.im((x+s.I*y)**l))]
            if l>=2:
                polynomials.append(s.expand(z*s.re((x+s.I*y)**(l-1))))
            for H in polynomials:
                assert iszero(sum(s.diff(H,v,2) for v in vec))
                co=s.factor(-4*(beta+1)/((2*l+d+2*beta)*(2*l+d-2)*(2*l+d+2*beta+2)))
                lhs=toeplitz(toeplitz(H,1,beta),0,beta)-toeplitz(toeplitz(H,0,beta),1,beta)
                rhs=co*(x*s.diff(H,y)-y*s.diff(H,x))
                assert iszero(lhs-rhs),(l,beta,H,lhs,rhs)
                cnt+=1
    # Universal scalar coefficient identity, independent of sampled dimensions.
    L,D,B=s.symbols("L D B")
    coefficient=1/(2*L+D+2*B)-(2*L+D)/((2*L+D-2)*(2*L+D+2*B+2))
    exact=-4*(B+1)/((2*L+D+2*B)*(2*L+D-2)*(2*L+D+2*B+2))
    assert s.factor(coefficient-exact)==0
    cnt+=1
    for D in range(3,9):
        for l in range(1,35):
            dim=(2*l+D-2)*math.factorial(l+D-3)//(math.factorial(l)*math.factorial(D-2))
            dim_weights=math.comb(l+D-3,D-3)+2*sum(math.comb(l-m+D-3,D-3) for m in range(1,l+1))
            assert dim==dim_weights,(D,l,dim,dim_weights)
            cnt+=1
    return cnt
if __name__=='__main__':
    print('PASS:',run(),'symbolic polynomial and representation-dimension diagnostics')
