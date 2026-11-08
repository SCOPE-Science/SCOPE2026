#!/usr/bin/env python3
"""Exact symbolic finite-instance checks for two-equator cubic restriction.
Requires sympy. Universal theorem is proved separately by polynomial divisibility.
"""
import sympy as S
from itertools import combinations_with_replacement

def three(n, c, s):
    u=S.Matrix([1]+[0]*(n-1))
    v=S.Matrix([c,s]+[0]*(n-2))
    A=c*S.eye(n)+v*u.T+u*v.T
    return u,v,A

def verify():
    checks=0
    x=S.symbols('x0:8')
    for d in range(3,9):
        for c,s in [(S.Integer(0),S.Integer(1)),(S.Rational(1,2),S.sqrt(3)/2),(-S.Rational(1,2),S.sqrt(3)/2),(S.Rational(3,5),S.Rational(4,5)),(S.Rational(5,13),S.Rational(12,13))]:
            u,v,A=three(d,c,s)
            assert S.simplify(A.det()-c**(d-2)*(4*c*c-1))==0
            checks+=1
            assert (A*(u+v)-(1+2*c)*(u+v))==S.zeros(d,1)
            checks+=1
            assert (A*(u-v)-(2*c-1)*(u-v))==S.zeros(d,1)
            checks+=1
            assert A.rank()==(d-(d-2 if c==0 else 1 if 4*c*c==1 else 0))
            checks+=1
            for w in [u+v,u-v]+[S.eye(d).col(j) for j in range(2,d)]:
                U=sum(u[i]*x[i] for i in range(d))
                V=sum(v[i]*x[i] for i in range(d))
                W=sum(w[i]*x[i] for i in range(d))
                f=S.expand(U*V*W)
                lap=sum(S.diff(f,x[i],2) for i in range(d))
                target=2*sum((A*w)[i]*x[i] for i in range(d))
                assert S.expand(lap-target)==0
                checks+=1
        # Independent one-equator nullity: harmonic cubic coefficient constraints
        ms=list(combinations_with_replacement(range(d),3))
        def monomial(m):
            out=S.Integer(1)
            for k in m:out*=x[k]
            return out
        polys=[monomial(m) for m in ms]
        lap=[sum(S.diff(p,x[i],2) for i in range(d)) for p in polys]
        rows=[]
        for k in range(d):
            rows.append([S.expand(p).coeff(x[k]) for p in lap])
        for m in combinations_with_replacement(range(1,d),3):
            rows.append([int(ms[j] == m) for j in range(len(ms))])
        # Nullity is cubic harmonic polynomials with first coord divisor.
        M=S.Matrix(rows)
        dim=len(polys)-M.rank()
        assert dim==d*(d-1)//2,(d,dim)
        checks+=1
    print('TWO_EQUATOR_CUBIC_CHECKS_PASS',checks)
if __name__=='__main__':verify()
