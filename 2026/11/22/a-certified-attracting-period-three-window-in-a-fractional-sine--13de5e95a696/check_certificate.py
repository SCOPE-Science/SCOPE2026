#!/usr/bin/env python3
"""Exact rational certificate for attracting 3-cycles of sin(pi*x)/(1+r*x).
No external dependencies; pi bounded by Machin's arctangent identity and
alternating series. A finite recurrence check is not used as an infinite proof.
"""
from fractions import Fraction as Q
from math import factorial

def frac(s): return Q(str(s))

def atan_bracket(t, n=20):
    terms=[(-1)**j*t**(2*j+1)/Q(2*j+1) for j in range(n+1)]
    p=sum(terms[:n],Q(0)); q=p+terms[n]
    return min(p,q),max(p,q)

A=atan_bracket(Q(1,5)); B=atan_bracket(Q(1,239))
PI=(16*A[0]-4*B[1], 16*A[1]-4*B[0])
assert PI[1]-PI[0]<Q(1,10**20)
PI_MID=sum(PI)/2
PI_ERR=(PI[1]-PI[0])/2

# sin(z) and cos(z) Taylor bounds centered at rational z=pi_mid*t.
# By |derivative|<=1, Lagrange remainder is bounded by z^(d+1)/(d+1)!.
def trig_point(t, cosine=False):
    z=PI_MID*t
    m=18
    if cosine:
        val=sum(((-1)**j*z**(2*j)/factorial(2*j) for j in range(m+1)),Q(0))
        err=z**(2*m+1)/factorial(2*m+1)+PI_ERR*abs(t)
    else:
        val=sum(((-1)**j*z**(2*j+1)/factorial(2*j+1) for j in range(m+1)),Q(0))
        err=z**(2*m+2)/factorial(2*m+2)+PI_ERR*abs(t)
    return (val-err,val+err)

def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    w=[a[i]*b[j] for i in range(2) for j in range(2)]
    return min(w),max(w)
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def scale(a,x):return mul(a,(x,x))
def D(x):return (x,x)
def sin_interval(lo,hi):
    assert 0<=lo<=hi<=1
    if hi<=Q(1,2):return trig_point(lo)[0],trig_point(hi)[1]
    if lo>=Q(1,2):return trig_point(hi)[0],trig_point(lo)[1]
    raise ValueError('straddling maximum')
def cos_interval(lo,hi):
    assert 0<=lo<=hi<=1
    return trig_point(hi,True)[0],trig_point(lo,True)[1]

def f_point(x,k):
    return div(trig_point(x),(1+k*x,1+k*x))

def derivative_interval(lo,hi,krange):
    x=(lo,hi); den=add(D(1),mul(x,krange))
    num=sub(mul(PI,mul(cos_interval(lo,hi),den)),mul(sin_interval(lo,hi),krange))
    return div(num,mul(den,den))

I0=(frac('.1632'),frac('.1633'))
I1=(frac('.48073'),frac('.48100'))
I2=(frac('.94158'),frac('.94161'))
intervals=[I0,I1,I2]
K=(Q(124999,1000000),Q(125001,1000000))
Ds=[]
for j,(lo,hi) in enumerate(intervals):
    dd=derivative_interval(lo,hi,K)
    Ds.append(dd)
    print('derivative',j,*[float(q) for q in dd])
    if j<2:
        assert dd[0]>0
        image=(f_point(lo,K[1])[0],f_point(hi,K[0])[1])
    else:
        assert dd[1]<0
        image=(f_point(hi,K[1])[0],f_point(lo,K[0])[1])
    next_interval=intervals[(j+1)%3]
    print('image',j,*[float(q) for q in image])
    assert next_interval[0]<image[0] and image[1]<next_interval[1],('containment fails',j)
assert Q(262344,100000)<Ds[0][0] and Ds[0][1]<Q(262406,100000)
assert Q(6575,100000)<Ds[1][0] and Ds[1][1]<Q(6828,100000)
assert -Q(278190,100000)<Ds[2][0] and Ds[2][1]<-Q(278179,100000)
product=mul(mul(Ds[0],Ds[1]),Ds[2])
print('product',*[float(q) for q in product])
assert -1 < product[0] and product[1] < 1
assert -Q(499,1000)<product[0] and product[1]<-Q(479,1000)
assert product[1]<0
assert all(intervals[i][1]<intervals[i+1][0] for i in range(2))
print('CERTIFIED: a primitive attracting 3-cycle exists for every r in [124999/1000000,125001/1000000].')
