"""Reproduce exact finite spectra for a two-relative-phase quadratic restriction on complex spheres."""
from itertools import combinations_with_replacement
import math
import numpy as np
import sympy as S

P = S.pi
D = S.sqrt(2)
B0=S.Matrix([[S.Rational(1,4)]])
B1=S.Matrix([[S.Rational(1,4),S.Rational(1,8),S.Rational(1,8)],
 [S.Rational(1,8),S.Rational(1,4),1/(4*P)],
 [S.Rational(1,8),1/(4*P),S.Rational(1,4)]])
a=3*D/32
B2=S.Matrix([[S.Rational(1,4),a,0,a,D/(8*P),0],
 [a,S.Rational(1,4),a,1/(4*P),S.Rational(1,8),0],
 [0,a,S.Rational(1,4),0,3*D/(16*P),0],
 [a,1/(4*P),0,S.Rational(1,4),S.Rational(1,8),a],
 [D/(8*P),S.Rational(1,8),3*D/(16*P),S.Rational(1,8),S.Rational(1,4),3*D/(16*P)],
 [0,0,0,a,3*D/(16*P),S.Rational(1,4)]])
Bminus=S.Matrix([[S.Rational(1,4)-1/(4*P),a],[a,S.Rational(1,4)]])
Bplus=S.Matrix([[S.Rational(1,4),S.Rational(3,16),0,D/(8*P)],
 [S.Rational(3,16),S.Rational(1,4)+1/(4*P),a,D/8],
 [0,a,S.Rational(1,4),3/(8*P)],
 [D/(8*P),D/8,3/(8*P),S.Rational(1,4)]])
U=S.zeros(6,6)
U[0,0]=1
U[1,1]=U[3,1]=1/D
U[2,2]=U[5,2]=1/D
U[4,3]=1
U[1,4]=1/D; U[3,4]=-1/D
U[2,5]=1/D; U[5,5]=-1/D
assert S.simplify(U.T*U-S.eye(6))==S.zeros(6)
assert S.simplify(U.T*B2*U-S.diag(Bplus,Bminus))==S.zeros(6)
charplus=S.factor(Bplus.charpoly().as_expr())
charminus=S.factor(Bminus.charpoly().as_expr())
assert S.factor(B2.charpoly().as_expr()-charplus*charminus)==0
print('quadratic-sector characteristic factors:',charminus,charplus)
for d in [3,4,5,8]:
 full = []
 for a0 in range(d):
  for b0 in range(a0,d):
   exp=[0]*d; exp[a0]+=1; exp[b0]+=1; full.append(tuple(exp))
 # Formula on full degree two, from normalized moment, with angular Fourier coefficient.
 def ck(k):return S.Rational(1,2) if k==0 else S.sin(S.pi*k/2)/(S.pi*k)
 def coefficient(x,y):
  if x[3:] != y[3:]: return S.Integer(0)
  v=ck(x[1]-y[1])*ck(x[2]-y[2])
  for t,u in zip(x,y):v*=S.gamma(S.Rational(t+u,2)+1)/S.sqrt(S.factorial(t)*S.factorial(u))
  return S.simplify(v)
 F=S.Matrix([[coefficient(x,y) for y in full] for x in full]);
 expected=sorted(np.r_[np.linalg.eigvalsh(np.array(B2.evalf(),float)),
     np.tile(np.linalg.eigvalsh(np.array(B1.evalf(),float)),d-3),
     np.full((d-3)*(d-2)//2,.25)])
 observed=sorted(np.linalg.eigvalsh(np.array(F.evalf(),float)))
 assert np.max(np.abs(np.array(expected)-np.array(observed)))<1e-12
 print('d',d,'dimension',len(full),'exact factor-block spectral discrepancy:',max(abs(x-y) for x,y in zip(expected,observed)))
# Direct Gaussian simulation (not the analytic phase-angle/gamma factorization)
rng=np.random.default_rng(20261115)
d=3;N=350000
G=rng.standard_normal((N,d))+1j*rng.standard_normal((N,d))
G/=np.linalg.norm(G,axis=1)[:,None]
E=[(2,0,0),(1,0,1),(0,0,2),(1,1,0),(0,1,1),(0,2,0)]
V=np.stack([np.prod(G**np.array(ex),axis=1)*np.sqrt(d*(d+1)/math.prod(math.factorial(j) for j in ex)) for ex in E],axis=1)
mask=(np.real(G[:,0]*np.conj(G[:,1]))>0)&(np.real(G[:,0]*np.conj(G[:,2]))>0)
MC=(V[mask].conj().T@V[mask])/N
M=np.array(B2.evalf(),float)
print('MC halfspace probability',mask.mean(),'matrix max diff',np.max(np.abs(MC-M)),'MC eigen max diff',np.max(np.abs(np.linalg.eigvalsh(MC)-np.linalg.eigvalsh(M))))
assert np.max(np.abs(MC-M))<0.016
print('PASS')
# Certified root separation: exact rational interval evaluation, with pi enclosed via Machin's identity.
from fractions import Fraction

def atan_sum(x,N):
 return sum(((-1)**k)*(x**(2*k+1))/Fraction(2*k+1) for k in range(N))
x=Fraction(1,5);y=Fraction(1,239)
pl=16*atan_sum(x,12)-4*atan_sum(y,13)
pu=16*atan_sum(x,13)-4*atan_sum(y,12)
assert Fraction(3141592653589793,10**15) < pl < pu < Fraction(3141592653589794,10**15)
def interval_add(A,B):return (A[0]+B[0],A[1]+B[1])
def interval_mul(A,B):
 v=[u*w for u in A for w in B];return(min(v),max(v))
def sign_at(expr,dec):
 L=S.symbols('lambda');T=S.symbols('T')
 num=S.together(expr).as_numer_denom()[0].subs(L,S.Rational(dec)).subs(S.pi,T)
 poly=S.Poly(num,T)
 I=(Fraction(0),Fraction(0))
 for v in poly.all_coeffs():
  I=interval_add(interval_mul(I,(pl,pu)),(Fraction(int(v.p),int(v.q)),Fraction(int(v.p),int(v.q))))
 if I[0]>0:return 1
 if I[1]<0:return -1
 raise ValueError('insufficient enclosure at '+dec)
for p,spans in [(charplus,[('0.049','0.050'),('0.119','0.121'),('0.271','0.273'),('0.638','0.640')]),(charminus,[('0.071','0.073'),('0.348','0.350')])]:
 for left,right in spans:
  signs=(sign_at(p,left),sign_at(p,right))
  assert signs[0]*signs[1]==-1
  print('certified root in',left,right,signs)
print('certified complete quadratic block root separation PASS')
