#!/usr/bin/env python3
"""Numerical checks for sharp finite Hermite spectral tomography of radial masks.
Requires mpmath; finite precision tests corroborate, rather than prove, the all-order theorem.
"""
import mpmath as mp
import random

mp.mp.dps = 70

def moments_integral(xs, count):
    return [sum(mp.quad(lambda t: mp.exp(-t)*t**j/mp.factorial(j), [xs[2*k], xs[2*k+1]])
                for k in range(len(xs)//2)) for j in range(count)]

def moments_closed(xs, count):
    # Independent incomplete-gamma evaluation.
    return [sum((mp.gammainc(j+1, xs[2*k], xs[2*k+1]))/mp.factorial(j)
                for k in range(len(xs)//2)) for j in range(count)]

def jacobian(xs):
    n=len(xs)
    return mp.matrix([[(-1 if i%2==0 else 1)*mp.exp(-xs[i])*xs[i]**j/mp.factorial(j)
                       for i in range(n)] for j in range(n)])

def determinant_formula(xs):
    n=len(xs)
    z=(-1)**(n//2)*mp.exp(-sum(xs))
    for j in range(n): z/=mp.factorial(j)
    for i in range(n):
        for j in range(i+1,n): z*=xs[j]-xs[i]
    return z

rng=random.Random(41723)
largest_integral_error = mp.mpf('0')
largest_relative_det_error = mp.mpf('0')
cases=0
for m in (1,2,3,4):
    for attempt in range(4):
        vals=[]; x=mp.mpf('0.3')
        for i in range(2*m):
            x+=mp.mpf(str(rng.uniform(.15,2.5)))
            vals.append(x)
        a=moments_integral(vals,2*m)
        b=moments_closed(vals,2*m)
        err=max(abs(u-v) for u,v in zip(a,b))
        largest_integral_error=max(largest_integral_error,err)
        assert err < mp.mpf('1e-55')
        d=mp.det(jacobian(vals)); f=determinant_formula(vals)
        er=abs(d/f-1)
        largest_relative_det_error=max(largest_relative_det_error,er)
        assert er < mp.mpf('1e-48')
        assert abs(f)>0
        cases+=1

# Exact low-dimensional rational Vandermonde determinant, with sympy if present.
try:
    import sympy as sp
    x=sp.symbols('x0:6')
    for m in (1,2):
        n=2*m
        M=sp.Matrix([[(-1)**(i+1)*x[i]**j/sp.factorial(j) for i in range(n)] for j in range(n)])
        V=(-1)**m*sp.prod(x[j]-x[i] for i in range(n) for j in range(i+1,n))/sp.prod(sp.factorial(j) for j in range(n))
        assert sp.factor(M.det()-V)==0
except ImportError:
    print('SYMPY_OPTIONAL_UNAVAILABLE')

# Explicit 1-parameter family, for two separated annuli, with first 3 moments fixed.
base=[mp.mpf('0.4'), mp.mpf('1.1'), mp.mpf('2.4'), mp.mpf('3.0')]
pre=moments_closed(base,3)
sol=[]
for shift in [mp.mpf('-0.03'),mp.mpf('0.03')]:
    top=base[3]+shift
    funcs=lambda a,b,c:(*(moments_closed([a,b,c,top],3)[j]-pre[j] for j in range(3)),)
    xyz=mp.findroot(funcs,(base[0],base[1],base[2]),tol=mp.mpf('1e-55'))
    pts=[xyz[0],xyz[1],xyz[2],top]
    assert 0<pts[0]<pts[1]<pts[2]<pts[3]
    assert max(abs(a-b) for a,b in zip(moments_closed(pts,3),pre))<mp.mpf('1e-54')
    assert abs(moments_closed(pts,4)[3]-moments_closed(base,4)[3])>mp.mpf('1e-9')
    sol.append(pts)
assert abs(moments_closed(sol[0],4)[3]-moments_closed(sol[1],4)[3])>mp.mpf('1e-9')

# The boundary-moment identity uses left-endpoint MINUS and right-endpoint PLUS.
xs=[mp.mpf('.3'),mp.mpf('1.2'),mp.mpf('2.5'),mp.mpf('4.3')]
lam=moments_closed(xs,len(xs))
for j in range(len(xs)):
    boundary=sum((-1 if i%2==0 else 1)*mp.exp(-x)*x**j for i,x in enumerate(xs))
    target=mp.factorial(j)*((lam[j-1] if j else 0)-lam[j])
    assert abs(boundary-target)<mp.mpf('1e-50')
J=jacobian(xs)
h=mp.mpf('1e-15')
for i in range(len(xs)):
    up=xs.copy(); dn=xs.copy()
    up[i]+=h; dn[i]-=h
    lm=moments_closed(up,len(xs)); ln=moments_closed(dn,len(xs))
    for j in range(len(xs)):
        assert abs((lm[j]-ln[j])/(2*h)-J[j,i])<mp.mpf('1e-25')
print('INVERSE_ANNULAR_STFT_PASS', 'moment_cases='+str(cases),
      'symbolic_dimensions=2,4', 'nonidentifiability_fiber=m2_two_sides', 'boundary_moments=checked', 'finite_difference_jacobian=checked',
      'max_integral_error='+mp.nstr(largest_integral_error,6),
      'max_det_relative_error='+mp.nstr(largest_relative_det_error,6))
