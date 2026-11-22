"""Standalone checks for bilinear phase control with exponential pulse residues.

Requires only the Python standard library. Algebraic proof is in RESULT.md;
finite numerical checks provide independent diagnostics, not a universal proof.
"""
import math, random
from fractions import Fraction as F
from dataclasses import dataclass

@dataclass(frozen=True)
class Iv:
    lo:F
    hi:F
    def __add__(self,b):
        if not isinstance(b,Iv): b=Iv(F(b),F(b))
        return Iv(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return Iv(-self.hi,-self.lo)
    def __sub__(self,b): return self+-b if isinstance(b,Iv) else self+Iv(-F(b),-F(b))
    def __rsub__(self,b): return (-self)+b
    def __mul__(self,b):
        if not isinstance(b,Iv): b=Iv(F(b),F(b))
        p=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return Iv(min(p),max(p))
    __rmul__=__mul__
    def reciprocal(self):
        assert self.lo>0
        return Iv(1/self.hi,1/self.lo)
    def __truediv__(self,b):
        if not isinstance(b,Iv):b=Iv(F(b),F(b))
        return self*b.reciprocal()

def exp_interval(q,n=42):
    q=F(q)
    if q<0:return exp_interval(-q,n).reciprocal()
    t=F(1); s=t
    for k in range(1,n+1):
        t*=q/k;s+=t
    nxt=t*q/(n+1)
    tail=nxt/(1-q/F(n+2))
    assert tail>0
    return Iv(s,s+tail)

def analytic_overlap(a,b,T,P,Q,phi):
    a,b,T,P,Q,phi=map(float,(a,b,T,P,Q,phi))
    d=-math.expm1(-a*T)*(-math.expm1(-b*T))*(a+b)
    return P*Q/d * ((math.exp(-b*T)-math.exp(-(a+b)*T))*math.exp(b*phi) + (-math.expm1(-b*T))*math.exp(-a*phi))

def phi_star(a,b,T):
    return (math.log(a/b)+ math.log(math.expm1(b*T))-math.log(-math.expm1(-a*T)))/(a+b)

def direct_overlap(a,b,T,P,Q,phi,m=1000):
    A=P/(-math.expm1(-a*T)); B=Q/(-math.expm1(-b*T));h=T/m
    total=0.0
    for j in range(m):
        t=(j+.5)*h
        total+= A*B*math.exp(-a*t-b*((t-phi)%T))
    return h*total

def check():
    N=0
    rnd=random.Random(20231115)
    for _ in range(350):
        a=math.exp(rnd.uniform(-1.5,1.5)); b=math.exp(rnd.uniform(-1.5,1.5));T=math.exp(rnd.uniform(-1,1));P=math.exp(rnd.uniform(-1,1));Q=math.exp(rnd.uniform(-1,1))
        z=phi_star(a,b,T)
        assert 0<z<T
        v0=analytic_overlap(a,b,T,P,Q,0)
        vm=analytic_overlap(a,b,T,P,Q,z)
        assert vm<v0
        assert abs(analytic_overlap(a,b,T,P,Q,T)-v0)<1e-9*max(1,v0)
        for f in (0.13,0.37,0.73):
            p=f*T
            av=analytic_overlap(a,b,T,P,Q,p)
            d=direct_overlap(a,b,T,P,Q,p,1600)
            assert abs(av-d)<3e-6*max(1,av), (a,b,T,p,av,d)
            assert vm<=av+1e-11*max(1,av)
            N+=1
        # middle phi sits at the exact minimizer and determines the phase-changing invasion window
        ell=(v0+vm)/2
        assert ell-v0<0<ell-vm
        N+=6
    for a,b in ((1.,1.),(3.,1.),(1.,3.),(4.,2.)):
        for T in (.0008,.0012):
            v0=analytic_overlap(a,b,T,1,1,0)
            vm=analytic_overlap(a,b,T,1,1,phi_star(a,b,T))
            assert abs((v0-vm)/T-1/8)<2e-4, (a,b,T,v0,vm)
            N+=1
    # Rational interval certificate for one strictly phase-switching pest example.
    # a=3, b=1, T=P=Q=kappa=1, u=v=1/100, r=1/3, so L=8/25.
    e1=exp_interval(F(-1)); e4=exp_interval(F(-4)); e05=exp_interval(F(1,2)); em15=exp_interval(F(-3,2));e3=exp_interval(F(-3))
    C= Iv(F(1),F(1))/ (4*(1-e3)*(1-e1))
    i0=C*(1-e4)
    ihalf=C*((e1-e4)*e05+(1-e1)*em15)
    L=F(8,25)
    assert i0.lo>L and ihalf.hi<L
    N+=2
    # Asymmetric lag, strict barrier, and long-period asymptotic.
    a,b,T=3.,1.,1.
    z=phi_star(a,b,T)
    assert 0.42<z<0.43 and z<T/2
    assert analytic_overlap(a,b,T,1.,1.,0)>8/25
    assert analytic_overlap(a,b,T,1.,1.,z)<8/25
    N+=3
    for a,b in ((3.,1.),(1.,3.),(2.,2.)):
        T=30
        z=phi_star(a,b,T)
        assert abs(z/T-b/(a+b))<.04
        v=analytic_overlap(a,b,T,1,1,z)
        asym=(1/b)*(b/a)**(a/(a+b))*math.exp(-a*b*T/(a+b))
        assert abs(v/asym-1)<.00001
        N+=1
    print('PASS',N,'checks including exact-rational interval witness')
    print('Exact strict intervals: I(0) in [%.12f,%.12f], I(1/2) in [%.12f,%.12f]; L=%.12f'% (float(i0.lo),float(i0.hi),float(ihalf.lo),float(ihalf.hi),float(L)))
    print('Unequal-rate lag phi*(3,1,1)=%.12f'%phi_star(3,1,1))
if __name__=='__main__':check()
