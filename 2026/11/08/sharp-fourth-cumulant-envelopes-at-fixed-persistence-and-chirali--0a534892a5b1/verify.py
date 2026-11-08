"""Independent moment and feasible-Fourier-region checks for planar tumbling.
Run: python verify.py ; requires sympy, numpy, scipy.
"""
import math
import sympy as s
import numpy as np
from scipy.linalg import expm

checks = 0

def check(condition, desc):
    global checks
    if not condition:
        raise AssertionError(desc)
    checks += 1

I=s.I
x,y=s.symbols('x y',real=True,nonzero=True)
z=x+I*y; A=1/(1-z); R=1-x*x-y*y; d=(1-x)**2+y*y
conj=lambda q:s.conjugate(q)
real=lambda q:s.simplify(s.re(s.expand_complex(q)))
center=conj(1-z*z)/(4*y*y)
rad=R/(4*y*y)
base=2*real(A)*real(A*A)
low=s.factor(real(A*A*center)-real(A*conj(A))*rad-base)
high=s.factor(real(A*A*center)+real(A*conj(A))*rad-base)
check(s.simplify(low +2*(1-x)**2*R/d**3)==0,'lower symbolic envelope')
check(s.simplify(high-R*((1-x)**2-y*y)**2/(2*y*y*d**3))==0,'upper symbolic envelope')

# Model-independent complex angular step harmonics; no assumption of a density.
def c4(z,w,alpha=1,v=1):
    a1=alpha*(1-complex(z)); a2=alpha*(1-complex(w))
    return 3*v**4*((1/(a1*a1*a2)).real-2*(1/a1).real*(1/(a1*a1)).real)

def bounds(z,alpha=1,v=1):
    z=complex(z); xx=z.real; yy=z.imag; r=1-abs(z)**2; dd=abs(1-z)**2
    if abs(yy)>1e-12:
        lo=-2*(1-xx)**2*r/dd**3
        hi=r*((1-xx)**2-yy**2)**2/(2*yy**2*dd**3)
    else:
        lo=(-3-4*xx)/(2*(1-xx)**3*(1+xx)); hi=math.inf
    return 3*v**4/alpha**3*lo, 3*v**4/alpha**3*hi

# Three exact 2-atom witnesses with the same first Fourier mode i/2.
witnesses=[
    ((s.Rational(13,28),(12+5*I)/13),(s.Rational(15,28),(-4+3*I)/5)),
    ((s.Rational(5,8),(3+4*I)/5),(s.Rational(3,8),-1)),
]
for witness in witnesses:
    zz=s.simplify(sum(p*u for p,u in witness)); ww=s.simplify(sum(p*u*u for p,u in witness))
    check(zz==I/2,'fixed first harmonic')
    check(s.simplify( (ww-zz*zz)*conj(ww-zz*zz)-(1-zz*conj(zz))**2)==0,'extremal 2-atom moment disk')
    val=c4(zz,ww); lo,hi=bounds(zz)
    check(min(abs(val-lo),abs(val-hi))<1e-10,'attained bound')
check(abs(c4(I/2,s.Rational(31,65)-I*s.Rational(12,65))-s.Rational(162,125))<1e-10,'positive witness')
check(abs(c4(I/2,s.Rational(1,5)+I*s.Rational(3,5))+s.Rational(288,125))<1e-10,'negative witness')

# Exceptional chiral angle: exactly half stationary 0-degree and pi/2-degree jumps.
zz=(1+I)/2; ww=0
check(abs(c4(zz,ww))<1e-12,'zero fourth cumulant at sharp chiral line')
lo,hi=bounds(zz)
check(abs(hi)<1e-12 and lo<0,'no positive value for same first harmonic')

# Achiral sharp transition.
for r0,sign in [(-s.Rational(9,10),1),(-s.Rational(3,4),0),(-s.Rational(1,2),-1)]:
    rr=complex(r0); w0=2*r0*r0-1; value=c4(r0,w0)
    lo,_=bounds(r0)
    check(abs(value-lo)<1e-10,'achiral minimum')
    check(value*sign>0 if sign else abs(value)<1e-12,'achiral sign')

# Finite-time moments independently from a truncated Fourier-mode Feynman-Kac hierarchy.
# Starts with theta_0 uniform, so E[e^{in theta}]=delta_{n0}.
def finite_c4(harmonics, t, alpha=1,v=1,D=0):
    nmax=4; pairs=[(order,n) for order in range(5) for n in range(-nmax,nmax+1)]
    ix={p:i for i,p in enumerate(pairs)}; mat=np.zeros((len(pairs),len(pairs)),complex)
    for order,n in pairs:
        i=ix[(order,n)]
        harm=harmonics(n)
        mat[i,i]=-alpha*(1-harm)
        if order:
            for m in (n-1,n+1):
                if abs(m)<=nmax: mat[i,ix[(order-1,m)]]+=order*v/2
        if order>=2: mat[i,ix[(order-2,n)]]+=D*order*(order-1)
    init=np.zeros(len(pairs),complex); init[ix[(0,0)]]=1
    out=expm(mat*t)@init
    second=out[ix[(2,0)]].real;fourth=out[ix[(4,0)]].real
    return fourth-3*second*second

def h_atoms(wit):
    return lambda n: complex(sum(p*u**n for p,u in wit))

for wit in witnesses:
    zz=sum(p*u for p,u in wit);ww=sum(p*u**2 for p,u in wit)
    analytic=c4(zz,ww)
    for t in (100,200,400):
        numeric=finite_c4(h_atoms(wit),t)/t
        check(abs(numeric-analytic)<max(.2,.2*abs(analytic)),'Feynman-Kac large-time finite moment vs exact limit')

# Separate exact 4-state Markov tilted determinant: theta progresses by pi/2 at effective rate 1/2.
k,lam=s.symbols('k lam',real=True)
Q=s.zeros(4)
for j in range(4):Q[j,(j+1)%4]=s.Rational(1,2);Q[j,j]=-s.Rational(1,2)
H=Q+s.diag(k,0,-k,0)
poly=s.factor((lam*s.eye(4)-H).det())
check(poly.subs({lam:0,k:0})==0,'initial zero eigenvalue')
# Put lam=c2*k^2+c4*k^4 and cancel coefficients to fourth order.
c2,c4coef=s.symbols('c2 c4')
expr=s.expand(poly.subs(lam,c2*k*k+c4coef*k**4))
sol2=s.solve(expr.coeff(k,2),c2)
check(len(sol2)==1,'unique quadratic coefficient')
sol4=s.solve(expr.coeff(k,4).subs(c2,sol2[0]),c4coef)
check(sol4==[s.Rational(1,4)],'four-state orientation-conditioned quartic coefficient')
# A four-state walk samples one fixed orientation coset; Haar initial orientation
# averages cosets, cancelling the quartic tilted-eigenvalue coefficient.
Hrot=Q+s.diag(k/s.sqrt(2),-k/s.sqrt(2),-k/s.sqrt(2),k/s.sqrt(2))
prot=s.factor((lam*s.eye(4)-Hrot).det())
exprrot=s.expand(prot.subs(lam,c2*k*k+c4coef*k**4))
q2=s.solve(exprrot.coeff(k,2),c2)
q4=s.solve(exprrot.coeff(k,4).subs(c2,q2[0]),c4coef)
check(q2==sol2 and q4==[-s.Rational(1,4)],'orthogonally rotated coset reverses quartic coefficient')
check(s.simplify(sol4[0]+q4[0])==0,'Haar-average quartic coefficient vanishes')

# Rational chords and convex combinations test all second harmonics within feasible disk.
rational_pts=[(3+4*I)/5,(5+12*I)/13,(12+5*I)/13,(-4+3*I)/5,1,-1,I,-I]
for i in range(len(rational_pts)):
  for j in range(i+1,len(rational_pts)):
    for p in [s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
        zc=p*rational_pts[i]+(1-p)*rational_pts[j]
        wc=p*rational_pts[i]**2+(1-p)*rational_pts[j]**2
        if abs(complex(wc)-1)<1e-12:continue
        lowc,highc=bounds(zc)
        val=c4(zc,wc)
        check(lowc-1e-8<=val<=highc+1e-8,'moment feasibility and fourth cumulant sharp envelope')

print('PASS',checks,'checks')
print('positive:',c4(I/2,s.Rational(31,65)-I*s.Rational(12,65)))
print('negative:',c4(I/2,s.Rational(1,5)+I*s.Rational(3,5)))
print('zero:',c4((1+I)/2,0))
print('quartic characteristic polynomial:',poly)
