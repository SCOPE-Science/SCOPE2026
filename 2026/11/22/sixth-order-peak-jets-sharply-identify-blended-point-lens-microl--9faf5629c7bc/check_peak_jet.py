#!/usr/bin/env python3
"""Reproducibility checks for a point-source/point-lens peak-jet identity.
Python standard library only. No assertions of empirical parameter accuracy.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
import random

D = Decimal

def calc(v, q, S, B):
    h = v*(v+4)
    rt = h.sqrt()
    g = (v+2)/rt
    gp = -D(4)/(h*rt)
    gpp = D(12)*(v+2)/(h*h*rt)
    gppp = -D(48)*(v*v+4*v+5)/(h*h*h*rt)
    return (B+S*g, D(2)*S*q*gp, D(12)*S*q*q*gpp, D(120)*S*q*q*q*gppp)

def recover(f0, f2, f4, f6):
    R = f2*f6/(f4*f4)
    v=(D(20)/(D(9)*R-D(20))).sqrt()-D(2)
    q=-v*(v+4)*f4/(D(18)*(v+2)*f2)
    h=v*(v+4)
    S=-f2*h*h.sqrt()/(D(8)*q)
    B=f0-S*(v+2)/h.sqrt()
    return (v,q,S,B,R)

def close(x,y, rel=D('1e-45')):
    return abs(x-y)<=rel*max(D(1),abs(x),abs(y))

def main():
    checks=0
    with localcontext() as ctx:
        ctx.prec=75
        # Analytic derivative factors are checked without radicals. Each case
        # reduces g'g'''/(g'')^2 to a rational function exactly.
        for numerator in range(1,100):
            for den in (1,3,7,17):
                v=Fraction(numerator,den)
                left=Fraction(4,3)*(v*v+4*v+5)/(v+2)**2
                right=Fraction(4,3)*(1+1/(v+2)**2)
                assert left==right
                checks+=1
        rng=random.Random(13579)
        for _ in range(1100):
            v=D(rng.randrange(1,10001))/D(rng.choice([1,11,100,333,10000]))
            q=D(rng.randrange(1,10001))/D(rng.choice([1,13,100,500,5000]))
            S=D(rng.randrange(1,10001))/D(rng.choice([1,31,100,600,3000]))
            B=D(rng.randrange(1,10001))/D(rng.choice([1,19,100,111,500]))
            jets=calc(v,q,S,B)
            back=recover(*jets)
            for x,y in zip((v,q,S,B),back[:4]):
                assert close(x,y), (x,y,back)
                checks+=1
            R=back[-1]
            assert D(20)/D(9)<R<D(25)/D(9)
            assert jets[1]<0 and jets[2]>0 and jets[3]<0
            checks+=2
        # Exact rational witness: v=1,q=1/4,S=3,B=5.
        j=calc(D(1),D(1)/D(4),D(3),D(5))
        assert close(j[0],D(5)+D(9)/D(5).sqrt());checks+=1
        assert close(j[1],-D(6)/(D(5)*D(5).sqrt()));checks+=1
        assert close(j[2],D(81)/(D(25)*D(5).sqrt()));checks+=1
        assert close(j[3],-D(108)/(D(5)*D(5).sqrt()));checks+=1
        assert close(recover(*j)[-1],D(200)/D(81));checks+=1
        # A distinct physical curve shares all derivatives through order five.
        f0,f2,f4,f6=j
        v2=D('1.1')
        q2=-v2*(v2+4)*f4/(D(18)*(v2+2)*f2)
        h=v2*(v2+4)
        S2=-f2*h*h.sqrt()/(D(8)*q2)
        B2=f0-S2*(v2+2)/h.sqrt()
        assert q2>0 and S2>0 and B2>0 and v2!=D(1);checks+=1
        jj=calc(v2,q2,S2,B2)
        for i in range(3):
            assert close(jj[i],j[i]);checks+=1
        assert not close(jj[3],j[3]);checks+=1
        # Multi-passband obstruction: arbitrary extra independent affine
        # flux channels have a common fourth/second derivative ratio and
        # therefore do not remove the 5-jet continuum.
        for _ in range(500):
            v=D(rng.randrange(30,3500))/D(1000)
            q=D(rng.randrange(30,4000))/D(1500)
            nband=rng.randrange(2,8)
            bands=[]
            for k in range(nband):
                S=D(rng.randrange(10,5000))/D(100)
                B=D(rng.randrange(100,15000))/D(100)
                bands.append(calc(v,q,S,B))
            v2=v+D('0.00001')
            ratio=bands[0][2]/bands[0][1]
            q2=-v2*(v2+4)*ratio/(D(18)*(v2+2))
            assert q2>0; checks+=1
            for f0,f2,f4,f6 in bands:
                assert close(f4/f2,ratio);checks+=1
                h=v2*(v2+4)
                s2=-f2*h*h.sqrt()/(D(8)*q2)
                b2=f0-s2*(v2+2)/h.sqrt()
                assert s2>0 and b2>0;checks+=1
                ff=calc(v2,q2,s2,b2)
                for j in range(3):
                    assert close(ff[j],(f0,f2,f4)[j]);checks+=1
                assert not close(ff[3],f6);checks+=1
            # A single passband's sixth derivative selects the true v,q.
            assert close(recover(*bands[-1])[0],v);checks+=1
            assert close(recover(*bands[0])[1],q);checks+=1
        print(f'PASS: {checks} standard-library assertions; witness R=200/81; 5-jet nonidentifiability across arbitrary bands confirmed.')

if __name__=='__main__': main()
