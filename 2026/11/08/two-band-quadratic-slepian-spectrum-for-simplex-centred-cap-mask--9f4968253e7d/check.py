"""Independent quadrature and algebra checks for tetrahedral-cap H2 concentration.
Dependencies: Python 3.10+, numpy, scipy, sympy. No inputs or network needed.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
from sympy import symbols, simplify

CHECKS = 0

def check(ok, msg):
    global CHECKS
    if not ok:
        raise AssertionError(msg)
    CHECKS += 1

def beta_formula(d,a):
    c=gamma(d/2)/(math.sqrt(math.pi)*gamma((d-1)/2))
    return c*(d+4)/((d-1)*(d+1))*a*(1-a*a)**((d-1)/2)*(a*a-3/(d+4))

def beta_integral(d,a):
    c=gamma(d/2)/(math.sqrt(math.pi)*gamma((d-1)/2))
    return c*quad(lambda t: (t**4-6*t*t*(1-t*t)/(d-1)+3*(1-t*t)**2/((d-1)*(d+1)))*(1-t*t)**((d-3)/2),a,1,epsabs=1e-13)[0]

def mass(d,a):
    c=gamma(d/2)/(math.sqrt(math.pi)*gamma((d-1)/2))
    return c*quad(lambda t:(1-t*t)**((d-3)/2),a,1,epsabs=1e-13)[0]

def bands(d,a):
    b=beta_formula(d,a)
    m=mass(d,a)
    lo=(d+1)*(m-b)
    st=lo+((d+2)*(d*d-1)/(2*d))*b
    return lo,st

# Algebraic cap primitive: derivative of F=w*(a(1-a^2)*(a^2-3/(d+4)))
# equals -(d+2)*w*(a^4-6*a^2/(d+4)+3/((d+2)*(d+4))).
d,t=symbols('d t', positive=True)
q=3/(d+4)
expr=(1-t*t)*(3*t*t-q)-(d-1)*t*t*(t*t-q)
q4=t**4-6*t*t/(d+4)+3/((d+2)*(d+4))
check(simplify(expr+(d+2)*q4)==0,'fourth zonal primitive')
for dd in range(3,21):
    cap0=math.sqrt((dd-1)/(2*dd))
    for j in range(1,5):
        aa=cap0+(1-cap0)*j/5
        b1=beta_formula(dd,aa);b2=beta_integral(dd,aa)
        check(abs(b1-b2)<4e-13,f'beta quadrature d={dd}')
        lo,st=bands(dd,aa)
        m=mass(dd,aa)
        dim=(dd-1)*(dd+2)//2
        check(abs((dd*st+(dim-dd)*lo)/dim-(dd+1)*m)<1e-12,'trace')
        check(-2e-12<=lo<=1+2e-12 and -2e-12<=st<=1+2e-12,'bounds')
    root=math.sqrt(3/(dd+4))
    check((root>cap0 if dd==3 else abs(root-cap0)<1e-12 if dd==4 else root<cap0),'crossing dimension')
    # simplex centered quadratic traceless-projector Gram: one 0 and d identical positive eigenvalues.
    nn=dd+1
    GG=np.full((nn,nn),-float(dd-1)/(dd*dd))
    np.fill_diagonal(GG,float(dd-1)/dd)
    ev=np.linalg.eigvalsh(GG)
    check(abs(ev[0])<1e-12 and max(abs(ev[1:]-float(dd*dd-1)/(dd*dd)))<1e-12,'simplex Gram')

# Direct integration over the four 3D spherical caps. Crucially this uses no
# moment tensor or representation-theoretic derivation of the predicted spectrum.
V=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)/math.sqrt(3)
Q=[]
for D in [np.diag([1,-1,0])/math.sqrt(2),np.diag([1,1,-2])/math.sqrt(6)]:Q.append(D)
for i,j in [(0,1),(0,2),(1,2)]:
    A=np.zeros((3,3)); A[i,j]=A[j,i]=1/math.sqrt(2);Q.append(A)
Q=np.array(Q)
nt=32; na=96
from numpy.polynomial.legendre import leggauss
nodes, wg = leggauss(nt)
angles=2*np.pi*np.arange(na)/na
cs=np.cos(angles); sn=np.sin(angles)

def direct_gram(a):
    G=np.zeros((5,5))
    for v in V:
        e=np.array([1.,0.,0.]);
        if abs(float(np.dot(v,e)))>0.8:e=np.array([0.,1.,0.])
        e=e-np.dot(e,v)*v; e=e/np.linalg.norm(e)
        f=np.cross(v,e)
        tt=(1+a)/2+(1-a)/2*nodes
        ww=(1-a)/2*wg
        for t,w in zip(tt,ww):
            xx=t*v+math.sqrt(1-t*t)*(cs[:,None]*e+sn[:,None]*f)
            y=np.einsum('mi,kij,mj->mk',xx,Q,xx)
            G+=(w/(2*na))*(y.T@y)
    return G*(15/2)
for a in [math.sqrt(1/3)+.014,math.sqrt(3/7),.78,.93]:
    ev=np.linalg.eigvalsh(direct_gram(a))
    lo,st=bands(3,a)
    target=np.sort([lo,lo,st,st,st])
    check(max(abs(ev-target))<2e-11,f'independent cap quadrature spectrum a={a}: {ev} vs {target}')
    if abs(a-math.sqrt(3/7))<1e-12:
        check(max(ev)-min(ev)<2e-11,'isotropic five-dimensional eigenspace')
        check(abs(ev[0]-2*(1-math.sqrt(3/7)))<2e-11,'isotropy scalar value')

# Degree-3 harmonic xyz remains nonzero at the isotropic cap radius.
a=math.sqrt(3/7)
cubic=0.
for v in V:
    e=np.array([1.,0.,0.]);
    if abs(float(np.dot(v,e)))>0.8:e=np.array([0.,1.,0.])
    e=e-np.dot(e,v)*v;e/=np.linalg.norm(e);f=np.cross(v,e)
    tt=(1+a)/2+(1-a)/2*nodes;ww=(1-a)/2*wg
    for t,w in zip(tt,ww):
        xx=t*v+math.sqrt(1-t*t)*(cs[:,None]*e+sn[:,None]*f)
        cubic+=(w/(2*na))*np.sum(xx[:,0]*xx[:,1]*xx[:,2])
check(abs(cubic-8/(147*math.sqrt(3)))<1e-12,'nonzero cubic moment')
print(f'SIMPLEX_CAP_H2_CHECKS_PASS {CHECKS}')
