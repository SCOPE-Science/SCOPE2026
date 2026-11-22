"""Independent numerical checks of the biased-membrane current-reversal theorem.
Run: python verify_biased_membrane.py. Requires NumPy and SciPy.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.sparse import diags, lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.integrate import quad

checks = 0

def near(a, b, tol=1e-8):
    global checks
    assert np.isfinite(a) and np.isfinite(b) and abs(a-b) <= tol*(1+abs(a)+abs(b)), (a,b,tol)
    checks+=1

def source_boundaries(D,L,r,source):
    eta=np.sqrt(r/D)
    a=sum(w*np.cosh(eta*(L-x)) for x,w in source)
    b=sum(w*np.cosh(eta*x) for x,w in source)
    return eta*a/np.sinh(eta*L),eta*b/np.sinh(eta*L)

def analytic_current(D,L,r,kappa,beta,source):
    A,B=source_boundaries(D,L,r,source)
    eta=np.sqrt(r/D)
    g=np.tanh(eta*L/2)/(D*eta)
    current=kappa*(B-beta*A)/(1+kappa*g*(1+beta))
    return current, A+g*current,B-g*current

def finite_volume_current(D,L,r,kappa,beta,weights, n=300):
    dx=L/n
    kap=kappa/(1+kappa*(1+beta)*dx/(2*D))
    A=diags([-D/dx**2*np.ones(n-1), (r+2*D/dx**2)*np.ones(n),-D/dx**2*np.ones(n-1)], [-1,0,1],format='lil')
    A[0,0]=r+D/dx**2+kap*beta/dx
    A[0,n-1]=-kap/dx
    A[n-1,n-1]=r+D/dx**2+kap/dx
    A[n-1,0]=-kap*beta/dx
    A=A.tocsc()
    p=spsolve(A,r*np.asarray(weights))
    near(dx*np.sum(p),1,2e-8)
    assert np.min(p)>0
    return kap*(p[-1]-beta*p[0])

# 1. Exact analytic boundary residual and rate classification for one-sided discrete measures.
for D,L in [(1.,1.),(2.,1.5),(.7,2.)]:
  for support in [[(.18*L,1.)],[(.1*L,.35),(.2*L,.65)],[(.1*L,.15),(.3*L,.35),(.49*L,.5)]]:
    for beta in [.2,.5,.9]:
      eta=brentq(lambda z: source_boundaries(D,L,D*z*z,support)[1]/source_boundaries(D,L,D*z*z,support)[0]-beta,1.e-5,100/L)
      rc=D*eta**2
      for kappa in [.1,1.,9.]:
        for rate in [.5*rc,rc,2*rc]:
          j,p0,pL=analytic_current(D,L,rate,kappa,beta,support)
          assert p0>0 and pL>0
          near(j,kappa*(pL-beta*p0))
          if rate<rc: assert j>0
          elif rate>rc: assert j<0
          else: near(j,0,1e-9)
          checks+=2
# 2. Right semicircle obeys reflected classification, even if source weights asymmetric.
for beta in [1.1,1.4,3.]:
    support=[(.6,.7),(.8,.3)]
    eta=brentq(lambda z: source_boundaries(1.,1.,z*z,support)[1]/source_boundaries(1.,1.,z*z,support)[0]-beta,1.e-5,100)
    for kappa in [.2,1.,10.]:
        for fac in [.5,2.]:
            j,_,_=analytic_current(1,1,fac*eta**2,kappa,beta,support)
            assert (j<0 if fac<1 else j>0)
            checks+=1
# 3. Exact uniform half-interval formula vs direct one-dimensional quadrature.
for D,L in [(1,1),(.6,1.8)]:
    for beta in [.25,.5,.75]:
        expected=4*D/L**2*np.arccosh((1+1/beta)/2)**2
        for r in [expected*.5, expected, expected*2]:
            eta=np.sqrt(r/D)
            B=(2/L)*quad(lambda y:np.cosh(eta*y),0,L/2)[0]
            A=(2/L)*quad(lambda y:np.cosh(eta*(L-y)),0,L/2)[0]
            ratio=B/A
            near(ratio, 1/(2*np.cosh(eta*L/2)-1))
            if r==expected: near(ratio,beta)
# 4. Independent finite-volume elliptic solves; source is uniform on left semicircle.
for D,L,r,kappa,beta in [(1,1,1.,1.7,.5),(1,1,3.705037129235,3.,.5),(1,1,8.,.4,.5),(.7,1.3,2.,2.,.65),(2.,2.,5.,.25,.4)]:
    eta=np.sqrt(r/D)
    A=(2/L)*np.sinh(eta*L/2)/eta
    B=(2/L)*np.sinh(eta*L/2)/eta
    # A comes from integral cosh[eta(L-y)] over left half.
    A=(2/L)*(np.sinh(eta*L)-np.sinh(eta*L/2))/eta
    fac=eta/np.sinh(eta*L)
    A*=fac; B*=fac
    g=np.tanh(eta*L/2)/(D*eta)
    expected=kappa*(B-beta*A)/(1+kappa*g*(1+beta))
    vals=[]
    for n in [120,240,480]:
        dx=L/n
        weights=[2/L if (i+.5)*dx<L/2 else 0. for i in range(n)]
        vals.append(finite_volume_current(D,L,r,kappa,beta,weights,n))
    assert abs(vals[-1]-expected)<8e-5*(1+abs(expected)), (expected,vals)
    assert abs(vals[-1]-expected) < 0.4*abs(vals[0]-expected)+1.e-10,(expected,vals)
    checks+=2
print(f'PASS {checks} checks: classification, endpoint laws, exact uniform threshold, independent finite-volume solver')
