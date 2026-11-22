"""Finite numerical diagnostics for a quadratic Gaussian Fock intensity theorem.
Run: python3 check.py
Only the written proof establishes the quantified statements.
"""
import math
import cmath

def h(a):
    return a**3-2*a*a-7*a+4

def bisect(fun, lo, hi, iterations=95):
    fl = fun(lo)
    assert fl*fun(hi)<0, (lo,hi,fl,fun(hi))
    for _ in range(iterations):
        mid=(lo+hi)/2
        if fl*fun(mid)<=0: hi=mid
        else: lo=mid;fl=fun(mid)
    return (lo+hi)/2

a_lo=bisect(h,0.5,1.0)
a_hi=bisect(h,3.0,4.0)

def f(a,z): return 1+a*z-a*z*z

def intensity(a,z): return math.exp(-abs(z)**2)*abs(f(a,z))**2

def stationary(a,x): return a*(1-2*x)-x*(1+a*x-a*x*x)

def roots(a):
    dz=math.sqrt(1+4/a)
    fm=(1-dz)/2
    fp=(1+dz)/2
    return (bisect(lambda x:stationary(a,x),fm-4-5/math.sqrt(a),fm-1.e-8),
            bisect(lambda x:stationary(a,x),0,fp-1.e-8),
            bisect(lambda x:stationary(a,x),fp+1.e-8,fp+4+5/math.sqrt(a)))

def predicted(a):
    x1,x2,x3=roots(a)
    if a<a_lo: return [complex(x2,0)]
    if a>a_hi: return [complex(x1,0)]
    u=2-1/a
    x=(1-a)/2
    y=math.sqrt(max(0,u-x*x))
    return [complex(x,y),complex(x,-y)] if y>1.e-10 else [complex(x,0)]

count=0
for a in (0.05,0.2,0.5,a_lo,0.516,0.6,1.0,2.0,3.0,3.625,a_hi,3.627,5.0,15.0):
    sites=predicted(a)
    opt=intensity(a,sites[0])
    assert all(abs(intensity(a,z)-opt)<2.e-12*max(1,opt) for z in sites)
    count+=1
    # Global testing grid is a diagnostic, not a proof.
    for ir in range(66):
        r=3.25*ir/65
        for it in range(128):
            z=r*cmath.exp(2j*math.pi*it/128)
            assert intensity(a,z)<=opt+4.e-11*max(1,opt), (a,z,opt)
            count+=1
    # Exact completion of square at unrelated sample sites.
    for z in (0j, 0.3+0.8j, -1.1+0.2j, 1.7-0.9j):
        u=abs(z)**2
        xstar=(1-a*u)/4
        rhs=(1+a/4)*(1+a*u)**2-4*a*(z.real-xstar)**2
        assert abs(abs(f(a,z))**2-rhs)<1.e-9*max(1,abs(f(a,z))**2)
        count+=1
    if a_lo<a<a_hi:
        u=2-1/a
        assert abs(opt-(1+a/4)*4*a*a*math.exp(-u))<1.e-9*max(1,opt)
        count+=1
    if a<a_lo:
        assert 1-a*sites[0].real**2-4*sites[0].real>0
        count+=1
    if a>a_hi:
        assert 1-a*sites[0].real**2-4*sites[0].real<0
        count+=1
assert abs(h(a_lo))<1.e-11 and abs(h(a_hi))<1.e-11
assert .515<a_lo<.516 and 3.626<a_hi<3.627
print(f'PASS: {count} finite diagnostics; thresholds {a_lo:.12f}, {a_hi:.12f}')
