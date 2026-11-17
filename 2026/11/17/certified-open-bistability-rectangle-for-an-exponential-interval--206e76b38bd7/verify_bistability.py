#!/usr/bin/env python3
"""Rigorous rational fixed-grid interval certificate. Python 3, stdlib only."""
from fractions import Fraction
S=10**30

def floor(a,b):return a//b
def ceil(a,b):return -((-a)//b)
def asfrac(a):return Fraction(str(a))
class I:
    def __init__(self,lo,hi=None,raw=False):
        if raw:self.lo,self.hi=lo,hi
        else:
            u=asfrac(lo);v=asfrac(lo if hi is None else hi)
            self.lo=floor(u.numerator*S,u.denominator)
            self.hi=ceil(v.numerator*S,v.denominator)
        assert self.lo<=self.hi
    @classmethod
    def raw(cls,lo,hi):return cls(lo,hi,True)
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I.raw(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self.hi,-self.lo)
    def __sub__(self,o):return self+-(o if isinstance(o,I) else I(o))
    def __rsub__(self,o):return (o if isinstance(o,I) else I(o))+-self
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        vals=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I.raw(floor(min(vals),S),ceil(max(vals),S))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o)
        assert o.lo>0 or o.hi<0
        vals=[(x*S,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return I.raw(min(floor(x,y) for x,y in vals),max(ceil(x,y) for x,y in vals))
    def __repr__(self):
        return '[%.15g, %.15g]'%(self.lo/S,self.hi/S)
    def supabs(self):return max(abs(self.lo),abs(self.hi))

def expneg(t):
    """encloses exp(-t), 0<=t<=10 via nonnegative exp series on t/16."""
    assert 0<=t.lo<=t.hi<=10*S
    z=t/I(16)
    assert z.hi<=S
    term=I(1);sm=I(1)
    for n in range(1,24):
        term=term*z/I(n)
        sm=sm+term
    nextterm=term*z/I(24)
    # For z in [0,1], remaining tail after n=23 bounded by 2*z^24/24!
    ee=I.raw(sm.lo,(sm+I(2)*nextterm).hi)
    r=I(1)/ee
    for _ in range(4):r=r*r
    return r

def sigmapoint(t):
    if t>=0:
        v=expneg(I.raw(t,t))
        return I(1)/(I(1)+v)
    v=expneg(I.raw(-t,-t))
    return v/(I(1)+v)

def sigma(X):
    aa=sigmapoint(X.lo);bb=sigmapoint(X.hi)
    return I.raw(aa.lo,bb.hi)

def h(X,A,B):return X+A*(B-sigma(X))

def hd(X,A):
    s=sigma(X)
    def v(z):return floor(z*(S-z),S),ceil(z*(S-z),S)
    v1=v(s.lo);v2=v(s.hi)
    mn=min(v1[0],v2[0]);mx=max(v1[1],v2[1])
    if s.lo<=S//2<=s.hi:mx=max(mx,ceil(S,4))
    return I(1)-A*I.raw(mn,mx)

def certificate(cstr,rstr,astr,bstr):
    c=I(cstr); r=I(rstr);Ar=I(astr);Br=I(bstr)
    A=I('19.06')+I.raw(-Ar.hi,Ar.hi);B=I('0.3961')+I.raw(-Br.hi,Br.hi)
    J=I.raw(c.lo-r.hi,c.hi+r.hi)
    y=J;D=I(1); ys=[J]
    for i in range(4):
        D=D*hd(y,A)
        y=h(y,A,B)
        ys.append(y)
    e=I(cstr)
    for i in range(4):e=h(e,A,B)
    k=D.supabs(); err=max(abs(e.lo-c.lo),abs(e.hi-c.hi))
    ok=(k<S and err*S <(S-k)*r.lo and (ys[2].hi<J.lo or ys[2].lo>J.hi))
    print('start',cstr,'J',J,'f4(c)',e,'d4',D,'k',k/S,'err',err/S,'margin',(S-k)*r.lo/S**2,'period2_image',ys[2],'OK',ok)
    return ok

if __name__=='__main__':
    import sys
    ar,br,r=sys.argv[1:] if len(sys.argv)>1 else ('0.00005','0.0000001','0.002')
    assert certificate('-7.616520527293',r,ar,br)
    assert certificate('-7.404707992386',r,ar,br)
    # Exclude two differently phased presentations of the same cycle.
    A=I('19.06')+I.raw(-I(ar).hi,I(ar).hi)
    B=I('0.3961')+I.raw(-I(br).hi,I(br).hi)
    c1=I('-7.616520527293');c2=I('-7.404707992386');R=I(r)
    J1=I.raw(c1.lo-R.hi,c1.hi+R.hi)
    J2=I.raw(c2.lo-R.hi,c2.hi+R.hi)
    x=J1
    for n in range(4):
        assert x.hi<J2.lo or J2.hi<x.lo, (n,x,J2)
        x=h(x,A,B)
    # In particular each fixed point has least period 4, and they are inequivalent cycles.
    print('FOUR_PHASE_CROSS_DISJOINTNESS_OK')
    print('CERTIFIED_TWO_DISTINCT_ATTRACTING_PRIMITIVE_FOUR_CYCLES_OK')
