"""Exact identities and direct Lindblad checks for reset Bell-pair correlations.

Run with: python checker.py   (requires SymPy and NumPy).
"""
import math
import numpy as np
import sympy as sp

checks = 0

def eq(expr):
    global checks
    assert sp.cancel(expr) == 0, sp.factor(expr)
    checks += 1

r, s, z = sp.symbols('r s z', positive=True)
a, b = sp.symbols('a b', nonnegative=True)
S=a+b
Q=a*b
h=r*r+S*r+Q
c=r/(2*(r+S/2))
P11=r/(2*(r+S))
P10=r/2*(1/(r+a)-1/(r+S))
P01=r/2*(1/(r+b)-1/(r+S))
P00=1-P11-P10-P01
t=2*c
v=sp.factor(1-2*(P01+P10))
eq(v-(r**3+S*r*r+Q*(S+3*r))/((S+r)*h))
eq(v-(1-r*(2*r+S)/h+2*r/(r+S)))
eq(t-2*r/(2*r+S))
eq(sp.factor(P01*P10)-r*r*Q/(4*(r+S)**2*h))
eq(sp.factor((v-t)*(S+r)*(S+2*r)*h)-((S*S+3*S*r+4*r*r)*Q-S*r*r*(S+r)))
q0=s*r*r*(s+r)/(s*s+3*s*r+4*r*r)
eq(q0.subs(r,s)-s*s/4)
assert sp.factor(sp.diff(q0,r)).subs({r:sp.Rational(1,2),s:3})>0
checks+=1
assert all(vv>0 for vv in sp.Poly(sp.together(sp.diff(q0,r)).as_numer_denom()[0],r,s).coeffs());checks+=1
v_bal=sp.factor(v.subs({a:S/2,b:S/2})) if False else (s*s+s*r+2*r*r)/((s+r)*(s+2*r))
eq((1-t.subs({a:0,b:s})**2-v_bal**2)*(s+r)**2*(s+2*r)**2 -4*r*(s**3+s*s*r-r**3))
# For arbitrary a,b, all denominator formulas follow from population identity and physical reset.

sm=np.array([[0,1],[0,0]],dtype=complex)
I=np.eye(2,dtype=complex)
L1=np.kron(sm,I)
L2=np.kron(I,sm)
rho_init=np.zeros((4,4),dtype=complex)
rho_init[0,0]=rho_init[3,3]=rho_init[0,3]=rho_init[3,0]=.5
xops=np.array([[0,1],[1,0]],dtype=complex)
yops=np.array([[0,-1j],[1j,0]],dtype=complex)
zops=np.diag([1.,-1.]).astype(complex)
paulis=(xops,yops,zops)

def l0(rho, aa, bb):
    out=np.zeros((4,4),dtype=complex)
    for rate,L in ((aa,L1),(bb,L2)):
        P=L.conj().T @ L
        out+=rate*(L@rho@L.conj().T - (P@rho+rho@P)/2)
    return out

def direct(rr,aa,bb):
    basis=[]
    for i in range(4):
        for j in range(4):
            E=np.zeros((4,4),dtype=complex);E[i,j]=1
            basis.append(E)
    M=np.stack([(rr*E-l0(E,aa,bb)).ravel() for E in basis],axis=1)
    coef=np.linalg.solve(M,rr*rho_init.ravel())
    rho=sum(x*E for x,E in zip(coef,basis))
    return rho

def formula(rr,aa,bb):
    total=aa+bb
    p11=rr/(2*(rr+total))
    p10=rr/2*(1/(rr+aa)-1/(rr+total))
    p01=rr/2*(1/(rr+bb)-1/(rr+total))
    cc=rr/(2*(rr+total/2))
    ans=np.zeros((4,4),complex)
    ans[0,0]=1-p11-p10-p01
    ans[1,1]=p01;ans[2,2]=p10;ans[3,3]=p11
    ans[0,3]=ans[3,0]=cc
    return ans

rng=np.random.default_rng(1924)
for aa,bb in ((0.,2.),(2.,0.),(1.,1.),(0.5,2.),(0.12,10.3),(1.,3.),(2.,2.)) + tuple((float(x),float(y)) for x,y in rng.uniform(.03,9.,size=(180,2))):
  for rr in (0.05,0.25,0.87,1.17*(aa+bb), 2.8*(aa+bb)):
    rho=direct(rr,aa,bb)
    expected=formula(rr,aa,bb)
    assert np.max(np.abs(rho-expected))<2e-12,(aa,bb,rr)
    checks+=1
    T=np.array([[np.trace(rho@np.kron(P,Q)).real for Q in paulis] for P in paulis])
    tv=2*rr/(2*rr+aa+bb)
    uv=1-2*(expected[1,1].real+expected[2,2].real)
    assert np.max(np.abs(T-np.diag([tv,-tv,uv])))<3e-12
    checks+=1
    sv=np.linalg.svd(T,compute_uv=False)
    actual=2*math.sqrt(sv[0]**2+sv[1]**2)
    predicted=2*math.sqrt(tv**2+max(tv**2,uv**2))
    assert abs(actual-predicted)<2e-12
    checks+=1
    yy=np.kron(yops,yops)
    M=rho@yy@rho.conj()@yy
    ev=np.linalg.eigvals(M)
    ev=np.sort(np.sqrt(np.maximum(ev.real,0)))[::-1]
    concurrence=max(0.,ev[0]-sum(ev[1:]))
    predC=tv-rr*math.sqrt(aa*bb)/((rr+aa+bb)*math.sqrt((rr+aa)*(rr+bb)))
    assert abs(concurrence-predC)<2e-7,(aa,bb,rr,concurrence,predC)
    checks+=1
    boundary=(1+math.sqrt(2))*(aa+bb)/2
    assert (actual>2+1e-10)==(rr>boundary+1e-10) or abs(rr-boundary)<1e-9,(aa,bb,rr,actual)
    checks+=1
    if rr>=aa+bb:
      assert abs(actual-2*math.sqrt(2)*tv)<2e-12
      checks+=1

# Prove exact threshold test against dense grids of symmetry-breaking splits.
for SS in (0.4,2.,11.,29.):
  threshold=(1+math.sqrt(2))*SS/2
  for frac in np.linspace(0,1,51):
    aa=SS*frac;bb=SS-aa
    for rat in (.01,.09,.22,.6,.99,1,1.01,1.8,5.):
      rr=rat*threshold
      mat=formula(rr,aa,bb)
      tt=2*rr/(2*rr+SS)
      uu=1-2*(mat[1,1].real+mat[2,2].real)
      B=2*math.sqrt(tt*tt+max(tt*tt,uu*uu))
      assert abs(B-2)<3e-12 if rat==1 else ((B>2)==(rat>1)),(SS,frac,rat,B)
      checks+=1
print('checks_passed',checks)
