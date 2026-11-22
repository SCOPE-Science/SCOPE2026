"""Reproduce exact balanced two-stage community stability calculations."""
import sympy as sp
import numpy as np


def construction(G, Delta):
    n=G.rows
    one=sp.ones(2,1)
    H=-sp.ones(2)
    K=sp.Matrix([[0,1],[-1,0]])
    R=sp.Matrix([[2-Delta,Delta],[Delta,2-Delta]])
    B=sp.zeros(2*n)
    RR=sp.zeros(2*n)
    for i in range(n):
        RR[2*i:2*i+2,2*i:2*i+2]=R
        for j in range(n):
            B[2*i:2*i+2,2*j:2*j+2]=H if i==j else G[i,j]*K
    e=sp.ones(2*n,1)
    assert RR*e+B*e==sp.zeros(2*n,1)
    J=RR+B+sp.diag(*list(B*e))
    # orthogonal transformation, interleaved state to grouped means/differences
    q=sp.sqrt(2)/2
    T=sp.zeros(2*n)
    for i in range(n):
        T[2*i,i]=q; T[2*i+1,i]=q
        T[2*i,n+i]=q;T[2*i+1,n+i]=-q
    Jp=sp.simplify(T.T*J*T)
    expected=sp.diag(*([-2]*n+[-2*Delta]*n))
    expected[:n,n:]=-G
    expected[n:,:n]=G
    assert sp.simplify(Jp-expected)==sp.zeros(2*n)
    return J,Jp

g,d=sp.symbols('g d',positive=True)
Gr=sp.Matrix([[0,g,0,-g],[g,0,-g,0],[0,-g,0,g],[-g,0,g,0]])
Gc=sp.Matrix([[0,g,0,-g],[-g,0,g,0],[0,-g,0,g],[g,0,-g,0]])
assert Gr==Gr.T and Gc==-Gc.T
assert Gr*sp.ones(4,1)==Gc*sp.ones(4,1)==sp.zeros(4,1)
assert Gr.applyfunc(abs)==Gc.applyfunc(abs)
for G in (Gr,Gc):
    J,Jp=construction(G,d)
    assert Jp[:4,:4]==-2*sp.eye(4)
    assert Jp[4:,4:]==-2*d*sp.eye(4)

z=sp.symbols('z')
_,Jr=construction(Gr,d)
_,Jc=construction(Gc,d)
charR=sp.factor(Jr.charpoly(z).as_expr())
charC=sp.factor(Jc.charpoly(z).as_expr())
print('reciprocal characteristic polynomial:',charR)
print('circulating characteristic polynomial:',charC)
assert sp.simplify(charR - ((z+2)*(z+2*d))**2 *((z+2)*(z+2*d)+4*g*g)**2)==0
assert sp.simplify(charC - ((z+2)*(z+2*d))**2 *((z+2)*(z+2*d)-4*g*g)**2)==0
# Exact sign test for fully physical parameters d=9 (mortality=7) and g=2 or g=4
for G,label in ((Gr,'reciprocal'),(Gc,'circulating')):
 for gv in (2,3,4,30):
  JJ=np.array(construction(G.subs(g,gv),sp.Integer(9))[0],dtype=float)
  eigen=np.linalg.eigvals(JJ)
  if label=='reciprocal': assert np.max(eigen.real)<-1e-8
  if label=='circulating':
   if gv<3:assert np.max(eigen.real)<-1e-8
   if gv==3:assert abs(np.max(eigen.real))<1e-8
   if gv>3:assert np.max(eigen.real)>1e-8
  print(label,'d=9, g=',gv,'max real',max(eigen.real))
# Distinct nonring skew symmetric networks; diagonalization theorem numeric crosscheck
from numpy.random import default_rng
rng=default_rng(32)
for n in [3,4,5,8]:
 for _ in range(10):
  raw=rng.normal(size=(n,n))
  # Orthogonal compression into orthogonal complement of ones ensures G 1=0
  P=np.eye(n)-np.ones((n,n))/n
  A=P@(raw-raw.T)@P
  A=A-np.diag(np.diag(A)) # diagonal zero for skew
  # row balanced up to roundoff
  assert np.linalg.norm(A@np.ones(n))<1e-12
  delta=float(rng.uniform(2.1,15))
  mat=np.block([[-2*np.eye(n),-A],[A,-2*delta*np.eye(n)]])
  lam=max(np.linalg.eigvals(mat).real)
  cond=np.linalg.svd(A,compute_uv=False)[0]**2-4*delta
  assert (lam>0)==(cond>1e-8)
print('ALL CHECKS PASS')
# Exact all-eigenvalue criterion, including nonnormal balanced real networks.
for a,b in [(1,0),(0,1),(1,1),(2,1),(0.1,3),(3,2),(-2,4)]:
 for gv in [0.2,2.,3.,5.,20.]:
  delta=9.0
  G=np.array((a*Gr+b*Gc).subs(g,gv),dtype=float)
  M=np.block([[-2*np.eye(4),-G],[G,-2*delta*np.eye(4)]])
  eigG=np.linalg.eigvals(G)
  denom=(delta+1)**2+eigG.real**2
  margins=(delta+1)**2*(4*delta+eigG.real**2)/denom -eigG.imag**2
  actual=np.max(np.linalg.eigvals(M).real)
  if abs(min(margins))>1e-6 and abs(actual)>1e-6:
   assert (actual<0) == (min(margins)>0), (a,b,gv,min(margins),actual)
  print('balanced network',a,b,gv,'eigG',np.round(eigG,2),'margin',round(min(margins),4),'growth',round(actual,4))
print('ALL EXTENDED CHECKS PASS')
for n in (4,5,7):
 for i in range(80):
  A=rng.normal(0,1,(n,n))
  np.fill_diagonal(A,0.)
  A=A-A.sum(axis=1)[:,None]/(n-1)*(1-np.eye(n))
  assert np.linalg.norm(A@np.ones(n))<1e-10
  assert np.max(abs(np.diag(A)))<1e-12
  Amp=0.5+40*rng.uniform()
  G=A*Amp
  delta=2.1+15*rng.uniform()
  M=np.block([[-2*np.eye(n),-G],[G,-2*delta*np.eye(n)]])
  eigG=np.linalg.eigvals(G)
  margins=(delta+1)**2*(4*delta+eigG.real**2)/((delta+1)**2+eigG.real**2)-eigG.imag**2
  grow=np.max(np.linalg.eigvals(M).real)
  if abs(min(margins))>1e-5 and abs(grow)>1e-6:
   assert (grow<0)==(min(margins)>0), (n,i,min(margins),grow)
print('ALL GENERAL NONNORMAL NETWORK TESTS PASS')
# Mixed-mode circulant: first possible nonzero-frequency instability (four species).
Gmix=sp.Matrix([[0,g,-g,0],[0,0,g,-g],[-g,0,0,g],[g,-g,0,0]])
assert Gmix*sp.ones(4,1)==sp.zeros(4,1)
assert sp.factor(Gmix.charpoly(z).as_expr())==z*(z+2*g)*(z*z-2*g*z+2*g*g)
Jmix=construction(Gmix,sp.Integer(9))[1]
assert sp.simplify(Jmix.subs(g,sp.sqrt(60)).charpoly(z).as_expr().subs(z,6*sp.I))==0
assert sp.simplify(Jmix.subs(g,sp.sqrt(60)).charpoly(z).as_expr().subs(z,-6*sp.I))==0
for gv,expected in [(sp.Integer(7),-1),(sp.sqrt(60),0),(sp.Integer(8),1)]:
    e=np.linalg.eigvals(np.array(Jmix.subs(g,gv),dtype=float))
    top=max(e.real)
    assert (top<-1e-6 if expected<0 else abs(top)<1e-6 if expected==0 else top>1e-6)
print('MIXED-MODE CRITICAL FREQUENCY CHECKS PASS')
