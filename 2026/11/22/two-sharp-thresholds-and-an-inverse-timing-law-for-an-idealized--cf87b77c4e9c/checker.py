"""Supplementary checks for the two-timescale fuel/drying surrogate. Pure science verification."""
from math import exp,log,isclose,sqrt
from random import Random

def f(z,r,a): return (1+a*z**r)*(1-z)
def g(z,r): return z**(r-1)*(r-(r+1)*z)
def df(z,r,a): return 1-a*g(z,r)  # equals (d/dt f)/(h*z)
def bisect(fn,lo,hi):
    flo=fn(lo)
    for i in range(90):
        mid=(lo+hi)/2
        if fn(mid)*flo>0: lo,flo=mid,fn(mid)
        else: hi=mid
    return (lo+hi)/2

rng=Random(0x4444)
checks=0
for i in range(2000):
    r=exp(rng.uniform(log(.2),log(.9))) if i%2==0 else exp(rng.uniform(log(1.3),log(8)))
    a=exp(rng.uniform(log(.3),log(15)))
    if abs(r-1)<1e-8: continue
    if r>1:
        zstar=(r-1)/(r+1)
        ac=((r+1)/(r-1))**(r-1)
        ag=r**r/(r-1)**(r-1)
        assert ag>ac and zstar>0
        # analytic max of g, numerical nearby and derivative sign
        for zz in (zstar*.5,zstar*.99,zstar*1.01, min(1,zstar*1.5)):
            assert g(zz,r)<g(zstar,r)+1e-9
            checks+=1
        if a>ac*(1+1e-10):
            zlo=bisect(lambda z: a*g(z,r)-1,1e-22,zstar)
            zhi=bisect(lambda z: a*g(z,r)-1,zstar,r/(r+1))
            assert 0<zlo<zstar<zhi<r/(r+1)
            assert df(zlo*.8,r,a)>-1e-7 and df((zlo+zhi)/2,r,a)<1e-7, (r,a,zlo,zhi,df(zlo*.8,r,a),df((zlo+zhi)/2,r,a))
            assert df((zhi+1)/2,r,a)>-1e-7
            assert (f(zhi,r,a)>1) == (a>ag)
            checks+=4
    else:
        z0=bisect(lambda z: a*g(z,r)-1,1e-30,r/(r+1))
        assert df(z0*.5,r,a)<0 and df((z0+r/(r+1))/2,r,a)>0
        assert f(z0,r,a)>1
        checks+=3
# Exact witness r=2,a=4: zmax=1/2, zmin=1/6
r=2;a=4
assert g(.5,r)*a==1 and abs(g(1/6,r)*a-1)<1e-14
assert f(.5,r,a)==1
assert abs(f(1/6,r,a)-25/27)<1e-15
assert (.5+1/6)==2/3
# Inverse from tmax=ln2,tmin=ln6, unknown recovery rate h: solve sum exp(-ht)=2/3
A,B=log(2),log(6)
h=bisect(lambda x: exp(-x*A)+exp(-x*B)-2/3,1e-7,10)
a_recovered=exp(h*(A+B))/3
assert abs(h-1)<1e-10 and abs(a_recovered-4)<1e-10
# Separate exact overshoot witness: r=2, a=25/3, phases 3/5 and 1/15.
from fractions import Fraction
zz_hi=Fraction(3,5); zz_lo=Fraction(1,15); aa=Fraction(25,3)
assert zz_hi+zz_lo==Fraction(2,3)
assert aa*zz_hi*(2-3*zz_hi)==1 and aa*zz_lo*(2-3*zz_lo)==1
assert (1+aa*zz_hi**2)*(1-zz_hi)==Fraction(8,5)
assert (1+aa*zz_lo**2)*(1-zz_lo)==Fraction(392,405)
checks+=12
print('PASS',checks,'supplementary assertions, exact witness and inverse')
