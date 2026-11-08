"""Rational-interval certificates for affine projections on regular polygons.

Run with Python 3 standard library. All sign assertions use rational intervals,
not floating-point arithmetic. Taylor remainders and the arctangent identity
provide certified enclosures for trigonometric constants.
"""
from fractions import Fraction as F
from math import factorial, isqrt, comb

class I:
    def __init__(self, a, b=None):
        if isinstance(a,I): self.a,self.b=a.a,a.b; return
        lo=F(a); hi=F(a if b is None else b)
        scale=10**28
        self.a=F((lo*scale).__floor__(),scale)
        self.b=F(-((-hi*scale).__floor__()),scale)
        assert self.a<=self.b
    @staticmethod
    def cv(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=I.cv(o);return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,o):return self+-I.cv(o)
    def __rsub__(self,o):return I.cv(o)+-self
    def __mul__(self,o):
        o=I.cv(o);p=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I.cv(o);assert o.a>0 or o.b<0
        return self*I(1/o.b,1/o.a)
    def __rtruediv__(self,o):return I.cv(o)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        out=I(1)
        for _ in range(n):out=out*self
        return out
    def __repr__(self):return '[%.14g,%.14g]'%(float(self.a),float(self.b))

def atan_bounds_inv(m,N=20):
    z=F(1,m)
    terms=[(-1)**j*z**(2*j+1)/F(2*j+1) for j in range(N+1)]
    v=sum(terms[:N],F(0)); r=terms[N]
    return I(min(v,v+r),max(v,v+r))
PI=16*atan_bounds_inv(5,21)-4*atan_bounds_inv(239,21)
assert PI.a>F(3) and PI.b<F(22,7)

def trig(theta_num, theta_den, name):
    # theta=2*pi*theta_num/theta_den, reduce to [-pi,pi]
    t=F(2*theta_num,theta_den)
    t-=2*((t+1)//2)
    x=(PI.a+PI.b)/2*t
    dx=(PI.b-PI.a)/2*abs(t)
    assert abs(x)<F(4)
    if name=='cos':
        v=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(18)),F(0))
        err=F(4**36,factorial(36))+dx
    else:
        v=sum(((-1)**j*x**(2*j+1)/factorial(2*j+1) for j in range(18)),F(0))
        err=F(4**37,factorial(37))+dx
    return I(v-err,v+err)

def square_root(a):
    a=I.cv(a);assert a.a>0
    scale=10**36
    lower=isqrt(a.a.numerator*scale**2//a.a.denominator)
    upper=isqrt(a.b.numerator*scale**2//a.b.denominator)+1
    return I(F(lower,scale), F(upper,scale))

def arcsin(a,N=13):
    a=I.cv(a);assert F(0)<a.a<=a.b<F(1)
    res=I(0)
    for j in range(N+1):
        res+=F(comb(2*j,j),4**j*(2*j+1))*(a**(2*j+1))
    return I(res.a,res.b + a.b**(2*N+3)/(1-a.b*a.b))

def cutoff(n):
    cos=trig(1,n,'cos') # actual cos(2*pi/n)
    k=12/(2+cos)
    xcut=-(2+cos)/12
    vertices=[(trig(j,n,'cos'),trig(j,n,'sin')) for j in range(n)]
    polygon=[]
    for j in range(n):
        a=vertices[j];b=vertices[(j+1)%n]
        in_a=a[0].b<xcut.a
        out_a=a[0].a>xcut.b
        in_b=b[0].b<xcut.a
        out_b=b[0].a>xcut.b
        assert in_a or out_a, (n,j,a[0],xcut)
        assert in_b or out_b, (n,j,b[0],xcut)
        if in_a:polygon.append(a)
        if in_a != in_b:
            t=(xcut-a[0])/(b[0]-a[0])
            polygon.append((xcut,a[1]+t*(b[1]-a[1])))
    assert len(polygon)>=3
    twice_area=I(0);six_moment=I(0)
    for a,b in zip(polygon,polygon[1:]+polygon[:1]):
        d=a[0]*b[1]-a[1]*b[0]
        twice_area+=d
        six_moment+=d*(a[0]+b[0])
    area=twice_area/2
    mx=six_moment/6
    base_area=n*trig(1,n,'sin')/2
    defect=-(area+k*mx)/base_area
    return defect

def disk_upper_at_11():
    n=11
    c=trig(1,n,'cos');q=(2+c)/12;k=1/q
    s=square_root(1-q*q)
    cd=-F(1,2)+(q*s+arcsin(q))/PI+(2*k*s**3)/(3*PI)
    # area ratio pi/(n sin(2pi/n)/2)
    ratio=PI/(n*trig(1,n,'sin')/2)
    return ratio*cd

if __name__=='__main__':
    print('PI_ENCLOSURE_OK', PI)
    for n in range(3,12):
        c=cutoff(n)
        if n<=6:assert c.a>F(1,2), (n,c)
        else:assert c.b<F(1,2),(n,c)
        print('CERTIFIED_THRESHOLD',n,c)
    ub=disk_upper_at_11();assert ub.b<F(1,2),ub
    print('CERTIFIED_ALL_N_GE_11_DISK_UPPER',ub)
    print('ALL_REGULAR_POLYGON_INTERVAL_CHECKS_PASSED')
