"""Independent reproducibility checks for membrane-current optimization.

Python 3 standard library only. Mathematical proof is in RESULT.md.
"""
import math

passes = 0

def ok(condition, label):
    global passes
    if not condition:
        raise AssertionError(label)
    passes += 1

# Exact logarithmic derivative with stable hyperbolic evaluations.
def H(z,u,k):
    coth_u=1/math.tanh(u*z) if u*z<350 else 1.
    coth=1/math.tanh(z) if z<350 else 1.
    csch2=1/math.sinh(z)**2 if z<350 else 0.
    # log[z sinh(uz)/sinh z] = 1/z + u coth(uz)-coth z
    # -log[coth z+k/z] derivative = -(-csch2-k/z²)/(coth+k/z)
    return 1/z+u*coth_u-coth + (csch2+k/z**2)/(coth+k/z)

def root(u,k):
    lo=1e-8
    hi=1.
    while H(hi,u,k)>0:
        hi*=2
        if hi>1e10: raise ArithmeticError('root not bracketed')
    for i in range(115):
        mid=(lo+hi)/2
        if H(mid,u,k)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def flux(D,L,k,u,z):
    # evaluate for z up to ~300 with exponential-safe representation
    if z<300:
        return 2*D*k/L**2 * z*z*math.sinh(u*z)/(z*math.cosh(z)+k*math.sinh(z))
    return 2*D*k/L**2*z*z*math.exp(-(1-u)*z)*(-math.expm1(-2*u*z))/(z*(1+math.exp(-2*z))+k*(-math.expm1(-2*z)))

def neumann_flux(D,L,k,u,z):
    a=2*z/L
    ell=L*(1-u)/2
    x0=ell
    U=a*math.cosh(a*(L-x0))/math.sinh(a*L)
    V=a*math.cosh(a*x0)/math.sinh(a*L)
    kap=k*D/L
    b=2*math.tanh(z)/(D*a)
    return abs(kap*(U-V)/(1+b*kap))

for u in (0.1,0.3,0.5,0.8,0.95,0.99):
  for k in (0.01,0.2,1.0,5.0,50.0):
    r=root(u,k)
    ok(abs(H(r,u,k))<1e-11, 'stationary derivative')
    ok(flux(1,2,k,u,r)>0,'positive flux')
    ok(flux(1,2,k,u,r)>flux(1,2,k,u,r*.9),'left maximality')
    ok(flux(1,2,k,u,r)>flux(1,2,k,u,r*1.1),'right maximality')
    for z in (0.07,0.5,2.,6.):
      ok(math.isclose(flux(1,2,k,u,z),neumann_flux(1,2,k,u,z),rel_tol=2e-11), 'Neumann agreement')
for k in (.1,1,10,100):
  zold=0
  for u in (.05,.2,.4,.6,.8,.9,.99):
    z=root(u,k)
    ok(z>zold,'source monotonicity')
    zold=z
for u in (.1,.4,.8,.95):
  zold=0
  for k in (.001,.1,1,10,100,1000):
    z=root(u,k)
    ok(z>zold,'permeability monotonicity')
    zold=z

def y_limit(eta):
    if math.isinf(eta):return 2.
    return (1-eta+math.sqrt(eta**2+6*eta+1))/2
for eta in (0, .05, .3, 1, 4, 25, math.inf):
  for delta in (.0125,.00625,.003125):
    k=2 if eta==0 else (1/delta**2 if math.isinf(eta) else eta/delta)
    z=root(1-delta,k)
    y=delta*z
    exact=y_limit(eta)
    ok(abs(y-exact)<0.15,'boundary layer convergence')
print(f'{passes} deterministic assertions passed')
