#!/usr/bin/env python3
"""Exact standard-library certificate for two CPUE-biomass reversals.

This verifies an explicit example and Descartes' root-count bound;
the general two-species statement is established in the accompanying proof.
"""
from fractions import Fraction as F
from math import comb

# The three stocks have r=(20,3,4), q=(3,2,1), K=(3,4,6), E=1.
# z=exp(-t); F_i(t)=N_i(t)/K_i as rational functions of z.
P = {20:36,18:-1080,17:1476,4:1632,3:-2688,1:672,0:-48}

def p(z):
    return sum(F(v)*z**j for j,v in P.items())

def f(z):
    return [F(17,1)/(20-3*z**17), F(1,1)/(3-2*z), F(3,1)/(4-z**3)]

def verify():
    checks=0
    assert p(F(1)) == 0; checks += 1
    # P is numerator after clearing the three positive denominators.
    for z in [F(0),F(1,100),F(1,3),F(9,10),F(1),F(1,2),F(2,5)]:
        f1,f2,f3=f(z)
        num=(48*f1+12*f2-60*f3)*(20-3*z**17)*(3-2*z)*(4-z**3)
        assert num==p(z), (z,num,p(z))
        checks += 1
    assert p(F(9,10))<0<p(F(1,3)) and p(F(1,100))<0
    checks += 1
    # Synthetic division P(z)=12(z-1)R(z), with r_j coefficients low-to-high.
    v=[P.get(j,0) for j in range(21)]
    r=[0]*20
    r[19]=v[20]//12
    for j in range(19,0,-1):
        r[j-1]=v[j]//12+r[j]
        assert v[j]==12*(r[j-1]-r[j]); checks+=1
    assert v[0]==-12*r[0]; checks+=1
    # S(y)=(1+y)^19 R(y/(1+y)); maps z in (0,1) bijectively to y>0.
    s=[sum(r[j]*comb(19-j,k-j) for j in range(k+1)) for k in range(20)]
    expected=[459,5049,26333,87924,202912,318784,288864,-33592,-611728,-1166880,-1382576,-1179256,-752352,-360128,-126752,-31212,-4792,-304,24,4]
    assert list(reversed(s))==expected; checks+=1
    signs=[1 if c>0 else -1 for c in reversed(s) if c]
    variations=sum(signs[i]!=signs[i-1] for i in range(1,len(signs)))
    assert variations==2; checks+=1
    # Independent exact sample ODE checks at a rational z: dN/dt.
    for z in [F(1,10),F(1,4),F(9,10)]:
        n=[3*f(z)[0],4*f(z)[1],6*f(z)[2]]
        for i,(rr,qq,kk) in enumerate(zip((20,3,4),(3,2,1),(3,4,6))):
            # z'=-z, so derivative of rational N(z) is -z*N'(z).
            if i==0: dn=3*17*(3*17*z**16)/(20-3*z**17)**2*(-z)
            elif i==1: dn=4*(2)/(3-2*z)**2*(-z)
            else: dn=6*3*(3*z**2)/(4-z**3)**2*(-z)
            rhs=(rr*(1-n[i]/kk)-qq)*n[i]
            assert dn==rhs,(z,i,dn,rhs); checks+=1
    # Root existence at two disjoint intervals and Descartes at most two => exactly two.
    print('EXACT CERTIFICATE PASS',checks,'assertions')
    print('P signs at z=1/100,1/3,9/10:',[('-' if p(z)<0 else '+') for z in (F(1,100),F(1,3),F(9,10))])
    print('Descartes variations:',variations)

if __name__=='__main__':
    verify()
