"""Finite consistency checks for two-dimensional antiisometric q-numerical ranges.
This is a diagnostic for explicit identities, not a proof of global extrema.
"""
import cmath
import math

N = 0

def check(cond, message):
    global N
    assert cond, message
    N += 1

def dot(x,y):
    return sum(z*w.conjugate() for z,w in zip(x,y))

def Aval(x,a,b):
    z,w = x
    return ((a*z.conjugate()+b*w.conjugate()),(-b*z.conjugate()+a*w.conjugate()))

def annulus(a,b,q):
    R = math.hypot(a,b)
    k = math.sqrt(max(0,1-q*q))
    low = max(0.0, b*k-a*q)
    high = R if q*R <= a else a*q+b*k
    return low, high

for a,b in [(0.,1.),(1.,0.),(3.,4.),(4.,3.),(5.,12.),(12.,5.),(1.,1.)]:
    R=math.hypot(a,b)
    for q in [0.,.08,.2,.4,.6,.7071067811865476,.8,.94,1.]:
        k=math.sqrt(max(0.,1-q*q))
        lo,hi=annulus(a,b,q)
        s_lo=math.inf
        s_hi=0
        for j in range(1801):
            theta=(math.pi/4)*j/1800
            x=(math.cos(theta),1j*math.sin(theta))
            v=(-x[1].conjugate(),x[0].conjugate())
            Ax=Aval(x,a,b)
            check(abs(dot(x,v))<3e-15, ('orthogonal', a,b,q,j))
            check(abs(dot(x,x)-1)<3e-15, ('unit', a,b,q,j))
            check(abs(dot(Ax,Ax)-R*R)<5e-13, ('antiisometry',a,b,q,j))
            s=abs(dot(Ax,x))
            t=abs(dot(Ax,v))
            check(abs(t*t+s*s-R*R)<4e-13, ('Parseval',a,b,q,j))
            down=abs(q*s-k*t)
            up=q*s+k*t
            s_lo=min(s_lo,down)
            s_hi=max(s_hi,up)
            if j%90==0:
                for h in range(8):
                    y=tuple(q*xx+k*cmath.exp(1j*math.pi*h/4)*vv for xx,vv in zip(x,v))
                    check(abs(dot(x,y)-q)<4e-15, ('overlap',a,b,q,j,h))
                    z=dot(Ax,y)
                    check(lo-1e-11<=abs(z)<=hi+1e-11, ('radius bounds',a,b,q,j,h,z,lo,hi))
        check(abs(s_lo-lo)<.01, ('inner formula',a,b,q,s_lo,lo))
        check(abs(s_hi-hi)<.0014, ('outer formula',a,b,q,s_hi,hi))
print('TWO_DIMENSIONAL_ANTILINEAR_Q_RANGE_FINITE_OK',N)
