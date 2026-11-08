"""Reproducible numerical diagnostics for Gaussian-reset harmonic diffusion.

The proof of the infinite-distance asymptotics is analytic; these finite tests
exercise independently evaluated covariance, derivatives, and quadratures.
Requires NumPy >=1.23 and SciPy >=1.10. Run: python verify_tail.py
"""
from math import sqrt, pi, gamma
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

Q = np.eye(2)
S = np.diag([4.0, 0.25])
B = S-Q
alpha = 1.4
checks = 0

def expect(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def geometry(direction, q=Q, s=S, a=alpha):
    e = np.array(direction, dtype=float)
    e = e/np.linalg.norm(e)
    b = s-q
    def C(y): return q+y*b
    def f(y): return float(e@np.linalg.solve(C(y), e))
    def deriv(y):
        u = np.linalg.solve(C(y),e)
        return float(-u@b@u)
    def second(y):
        u = np.linalg.solve(C(y),e)
        v = b@u
        return float(2*v@np.linalg.solve(C(y),v))
    def h(y): return (2*pi)**(-len(e)/2)/sqrt(np.linalg.det(C(y)))
    d0,d1 = deriv(0),deriv(1)
    if np.linalg.norm(b@np.linalg.solve(q,e)) < 1e-12:
        name,point = 'flat',None
    elif abs(d0) < 1e-10:
        name,point = 'old-tangent',0.0
    elif abs(d1) < 1e-10:
        name,point = 'young-tangent',1.0
    elif d0>0:
        name,point = 'old',0.0
    elif d1<0:
        name,point = 'young',1.0
    else:
        name,point = 'interior',brentq(deriv,0,1)
    if name=='flat':
        power=0
        coefficient=quad(lambda y:a*y**(a-1)*h(y),0,1,epsabs=1e-13)[0]
        rate=f(0)
    else:
        rate=f(point)
        if name=='old':
            power=2*a
            coefficient=h(0)*gamma(a+1)*(2/d0)**a
        elif name=='old-tangent':
            power=a
            coefficient=h(0)*gamma(1+a/2)*(4/second(0))**(a/2)
        elif name=='interior':
            power=1
            coefficient=a*point**(a-1)*h(point)*2*sqrt(pi/second(point))
        elif name=='young-tangent':
            power=1
            coefficient=a*h(1)*sqrt(pi/second(1))
        else:
            power=2
            coefficient=2*a*h(1)/(-d1)
    def relative_asymptotic(t):
        # Numerically integrate only the nonexponential prefactor,
        # avoiding underflow at the far Gaussian tail.
        z=quad(lambda y:a*y**(a-1)*h(y)*np.exp(-0.5*t*t*(f(y)-rate)),
               0,1,points=[point] if point is not None and 0<point<1 else None,
               epsabs=1e-13,epsrel=1e-12,limit=600)[0]
        return z*t**power/coefficient
    return name,point,rate,power,coefficient,relative_asymptotic,deriv,second,f

examples = [
    ('old',(0,1)),
    ('old-tangent',(1,2)),
    ('interior',(1,1)),
    ('young-tangent',(8,1)),
    ('young',(1,0)),
]
for name,vec in examples:
    typ,y,rate,power,k,ratio,fp,fpp,f=geometry(vec)
    expect(typ==name, f'wrong phase {name}: {typ}')
    expect(k>0 and rate>0, 'nonpositive rate/coefficient')
    for pt in np.linspace(0,1,11):
        expect(fpp(pt)>0, 'strict convexity')
        # Centered differences are independent of analytic matrix derivative.
        if 0.00001<pt<0.99999:
            h=1e-5
            derivative_fd=(f(pt+h)-f(pt-h))/(2*h)
            expect(abs(derivative_fd-fp(pt))<1e-7, 'first derivative mismatch')
    for t,tolerance in [(30,0.05),(50,0.03)]:
        r=ratio(t)
        expect(abs(r-1)<tolerance, f'{name}, t={t}: asymptotic ratio {r}')
    print(name,'y*=',y,'rate=',rate,'power=',power,'ratio(t=50)=',round(ratio(50),6))

# Exact geometric witness: joint density along a ray is dominated by an
# intermediate reset age even though its one-dimensional projection is not.
name,y,rate,power,k,ratio,fp,fpp,f = geometry((1,1))
expect(abs(y-2/9)<1e-12, 'wrong interior age')
expect(abs(rate-9/10)<1e-12, 'wrong exponent')
expect(abs(f(0)-1)<1e-12, 'wrong equilibrium exponent')
expect(abs(f(1)-17/8)<1e-12, 'wrong reset exponent')
e=np.array([1.,1.])/sqrt(2)
expect(float(e@S@e)>float(e@Q@e), 'projection endpoint comparison incorrect')

# Flat-rate case: covariance changes transverse to the observation ray.
q=np.eye(2);s=np.diag([1.,4.])
name,y,rate,power,k,ratio,fp,fpp,f=geometry((1,0),q,s)
expect(name=='flat' and abs(rate-1)<1e-12, 'flat case failed')
for t in [1,4,10]:
    expect(abs(ratio(t)-1)<1e-11, 'flat exact ratio failed')

# The exponent of the scalar projected marginal is controlled by an
# endpoint variance; it differs from the pointwise joint exponent above.
e_flat=np.array([1.,0.])
project_var_Q = float(e_flat@q@e_flat)
project_var_S = float(e_flat@s@e_flat)
expect(project_var_Q==project_var_S, 'the flat projected direction should match')
print('PASS: ',checks,'deterministic assertions. Finite tests are not a proof.')
