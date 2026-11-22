#!/usr/bin/env python3
"""Exact arithmetic checks for the asymmetric-star Crank--Nicolson positivity theorem.
Requires sympy; run: python verify.py
"""
from fractions import Fraction as F
from random import Random
import sympy as sp

def run():
    checks = 0
    m, a, b, s = sp.symbols('m a b s', positive=True)
    T=1+s*(b+m*a)
    R_h=(1+s*b)/T
    R_l=1/(1+s*b)+s*s*a*b/((1+s*b)*T)
    assert sp.simplify(2*R_h-1-(1+s*(b-m*a))/T)==0; checks+=1
    assert sp.simplify(2*R_l-1-(1+m*a*s-b*(b+(m-2)*a)*s*s)/((1+s*b)*T))==0; checks+=1
    s_h=1/(m*a-b)
    assert sp.simplify((2*R_l-1).subs(s,s_h) - (a*m*m-(2*m-1)*b)/(a*m*m)) == 0;checks+=1
    r=sp.Rational
    rng=Random(1989)
    for mm in range(2,12):
        for iteration in range(20):
            aa=r(rng.randrange(1,11),rng.randrange(1,12))
            bb=r(rng.randrange(1,13),rng.randrange(1,12))
            ss=r(rng.randrange(1,10),rng.randrange(1,10))
            Q=sp.zeros(mm+1)
            for i in range(1,mm+1):
                Q[0,i]=aa;Q[0,0]-=aa
                Q[i,0]=bb;Q[i,i]-=bb
            B=sp.eye(mm+1)-ss*Q
            Res=B.inv()
            C=2*Res-sp.eye(mm+1)
            assert Res[0,0] == R_h.subs({m:mm,a:aa,b:bb,s:ss});checks+=1
            assert Res[1,1] == R_l.subs({m:mm,a:aa,b:bb,s:ss});checks+=1
            assert all(C[i,j]>0 for i in range(mm+1) for j in range(mm+1) if i!=j);checks+=1
            assert all(sum(C[i,j] for j in range(mm+1))==1 for i in range(mm+1));checks+=1
            hh = (1+ss*(bb-mm*aa))>=0
            ll = 1+mm*aa*ss-bb*(bb+(mm-2)*aa)*ss*ss>=0
            assert (C[0,0]>=0)==hh;checks+=1
            assert (C[1,1]>=0)==ll;checks+=1
            assert (min(C[i,i] for i in range(mm+1))>=0)==(hh and ll);checks+=1
        # Exact switch: at a=1, b=m*m/(2m-1), hub+leaves hit zero simultaneously.
        bb=r(mm*mm,2*mm-1); ss=r(2*mm-1,mm*(mm-1))
        assert sp.factor((2*R_h-1).subs({m:mm,a:1,b:bb,s:ss})) == 0;checks+=1
        assert sp.factor((2*R_l-1).subs({m:mm,a:1,b:bb,s:ss})) == 0;checks+=1
        # Three rates on both sides of the switch, endpoints and outside.
        for rate in [bb/2,bb,bb*2]:
            Q=sp.zeros(mm+1)
            for i in range(1,mm+1):
                Q[0,i]=1;Q[0,0]-=1
                Q[i,0]=rate;Q[i,i]-=rate
            # compare diagonal inequalities at a point either side of exact positive root
            cl=rate*(rate+mm-2)
            sl=(sp.Integer(mm)+sp.sqrt(mm*mm+4*cl))/(2*cl)
            sh=(sp.Rational(1,1)/(mm-rate)) if rate < mm else sp.oo
            root=sp.Min(sh,sl)
            for factor in [sp.Rational(1,2),sp.Integer(1),sp.Integer(2)]:
                ss0=sp.N(root*factor,40)
                C=2*(sp.eye(mm+1)-ss0*Q).inv()-sp.eye(mm+1)
                diag=[float(C[i,i]) for i in range(mm+1)]
                if factor==sp.Rational(1,2): assert min(diag)>-1e-25
                if factor==2: assert min(diag)<-1e-25
                checks+=1
    print('PASS exact symbolic identities and',checks,'finite checks')
if __name__=='__main__': run()
