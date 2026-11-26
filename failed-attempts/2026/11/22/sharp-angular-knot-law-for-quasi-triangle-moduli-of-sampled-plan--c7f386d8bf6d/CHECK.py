"""Supplementary finite checks for a planar conic-spline modulus theorem.

Uses only the Python standard library. These tests complement, not replace,
the stated proof for arbitrary finite complete fans and real exponents.
"""
from fractions import Fraction
from math import atan2, cos, pi, sin, isclose
import random

count=0

def assert_test(ok):
    global count
    assert ok
    count+=1

def lp(x,p):
    return (abs(x[0])**p+abs(x[1])**p)**(1/p)

def l1(x):
    return abs(x[0])+abs(x[1])

def interp(x,rays,values):
    if x==(0,0):
        return 0.0
    a=atan2(x[1],x[0])%(2*pi)
    rr=sorted(zip([atan2(t[1],t[0])%(2*pi) for t in rays],rays,values))
    rr2=rr+[(rr[0][0]+2*pi,rr[0][1],rr[0][2])]
    for i in range(len(rr)):
        lower,lower_r,lower_v=rr2[i]
        upper,upper_r,upper_v=rr2[i+1]
        aa=a if a>=lower else a+2*pi
        if lower-1e-13<=aa<=upper+1e-13:
            d=lower_r[0]*upper_r[1]-lower_r[1]*upper_r[0]
            alpha=(x[0]*upper_r[1]-x[1]*upper_r[0])/d
            beta=(lower_r[0]*x[1]-lower_r[1]*x[0])/d
            if alpha >= -1e-10 and beta >= -1e-10:
                return alpha*lower_v+beta*upper_v
    raise AssertionError(f"Sector not found for {x}, angles {rr}")

random.seed(4519)
for p in (0.28,0.5,0.75,0.93):
    for fan_i in range(13):
        ang0=[0,pi/2,pi,3*pi/2]
        ang1=[random.uniform(0,pi/2) for _ in range(3+fan_i%5)]
        ang=sorted(set(ang0+[a+q*pi/2 for a in ang1 for q in range(4)]))
        def vector(a):
            # Make cardinal rays exact: fractional powers amplify sine(pi/2) roundoff.
            for j in range(4):
                if abs(a-j*pi/2)<1e-12:
                    return ((1,0),(0,1),(-1,0),(0,-1))[j]
            return (cos(a),sin(a))
        rays=[vector(a) for a in ang]
        values=[lp(t,p) for t in rays]
        M=max(v/l1(t) for t,v in zip(rays,values))
        delta=min(abs((a-pi/4+pi/4)%(pi/2)-pi/4) for a in ang)
        a0=pi/4-delta
        MF=(cos(a0)**p+sin(a0)**p)**(1/p)/(cos(a0)+sin(a0))
        assert_test(isclose(M,MF,rel_tol=2e-12,abs_tol=3e-12))
        for j,r in enumerate(rays):
            assert_test(isclose(interp(r,rays,values),values[j],abs_tol=2e-12))
            x=(r[0],0.0)
            y=(0.0,r[1])
            qx=interp(x,rays,values)
            qy=interp(y,rays,values)
            assert_test(isclose(qx,abs(x[0]),rel_tol=1e-11,abs_tol=1e-11))
            assert_test(isclose(qy,abs(y[1]),rel_tol=1e-11,abs_tol=1e-11))
            assert_test(isclose(interp((x[0]+y[0],x[1]+y[1]),rays,values)/(qx+qy),values[j]/l1(r),rel_tol=1e-11,abs_tol=1e-11))
        for k in range(50):
            x=(random.uniform(-2,2),random.uniform(-2,2))
            y=(random.uniform(-2,2),random.uniform(-2,2))
            qx=interp(x,rays,values)
            qy=interp(y,rays,values)
            qsum=interp((x[0]+y[0],x[1]+y[1]),rays,values)
            assert_test(qsum <= M*(qx+qy)+1e-10)
            assert_test(l1(x) <= qx+1e-10)
            assert_test(qx <= M*l1(x)+1e-10)

# Exact-rational conic example, p=1/2 gives q(x)=(sqrt|x1|+sqrt|x2|)^2.
# Exact first-quadrant rays (1,0), (1,1), (0,1).
frac=Fraction
# The exact midpoint diagonal special case uses (1,1) -> q=4 and L1=2.
rays_rat=[(frac(1),frac(0)),(frac(1),frac(1)),(frac(0),frac(1))]
values_rat=[frac(1),frac(4),frac(1)]
for r,v in zip(rays_rat,values_rat):
    assert_test(v>=abs(r[0])+abs(r[1]))
assert_test(max(v/(abs(r[0])+abs(r[1])) for r,v in zip(rays_rat,values_rat)) == frac(2))
for s in range(21):
    u=frac(s,20)
    x=(frac(1),u)
    # x=(1-u)*(1,0)+u*(1,1) on first cone, exact interpolant = 1+3u.
    qi=frac(1)+frac(3)*u
    assert_test(qi>=frac(1)+u)
    assert_test(qi<=frac(2)*(frac(1)+u))

# Explicit endpoint, diagonal and quadratic small-angle law.
for p in (0.25,0.5,0.8):
    top=2**(1/p-1)
    for delta in (0.08,0.04,0.02,0.01):
        theta=pi/4-delta
        F=(cos(theta)**p+sin(theta)**p)**(1/p)/(cos(theta)+sin(theta))
        assert_test(1<F<top)
        approx=top*(1-p)*delta*delta/2
        assert_test(abs((top-F)/approx-1)<0.035)
print('CONIC_SPLINE_MODULUS_CHECK_OK',count)
