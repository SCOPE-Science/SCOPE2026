"""Exact moment and Lyapunov identities for correlated-subset residual tracking.
Run with Python 3 and SymPy. Finite tests supplement, not replace, proof.
"""
import sympy as sp

h, q = sp.symbols('h q', real=True)
H = sp.Rational(1, 2)
M0 = sp.Matrix([[1, -2*h, 0], [0, 1, 0], [0, 0, 1]])
M2 = sp.Matrix([[1-4*h, 2*h, 0], [1, 0, 0], [0, 0, 0]])
M1 = sp.Matrix([[1-2*h, 0, 2*h], [H, H, -H], [H, -H, H]])
S = sp.diag(1, 1, -1)
M1p = S*M1*S
probabilities = [q, H-q, H-q, q]
matrices = [M0, M1, M1p, M2]
B = [sp.diag(1, 0, 0), sp.Matrix([[0,H,0],[H,0,0],[0,0,0]]),sp.diag(0,1,0), sp.diag(0,0,1)]
vec = lambda X: sp.Matrix([X[0,0], 2*X[0,1], X[1,1], X[2,2]])
T = sp.Matrix.hstack(*[
    vec(sum((p*M*E*M.T for p,M in zip(probabilities,matrices)), sp.zeros(3))) for E in B
])
expected_T = sp.Matrix([
    [1-4*h+4*h*h+8*h*h*q, -8*h*h*q, 8*h*h*q, 4*h*h*(1-2*q)],
    [1-2*h-4*h*q, (1-2*h+8*h*q)/2, -4*h*q, -2*h*(1-2*q)],
    [(1+2*q)/4, (1-2*q)/4, (1+2*q)/4, (1-2*q)/4],
    [(1-2*q)/4, -(1-2*q)/4, (1-2*q)/4, (1+2*q)/4],
])
checks = 0
for v in (T-expected_T):
    assert sp.factor(v) == 0
    checks += 1
A = (1-q+h*(1-4*q))/(2*h)
Bv = -h*(1+2*q)
C = h*(1+2*q)*(2*h+1)
D = 3*h*(1-2*q)*(2*h+1)
L = sp.Matrix([[A, Bv, C, D]])
F = 3*h*h+3*h*q+q-1
for x,y in zip(L*(T-sp.eye(4)),sp.Matrix([[2*F,0,0,0]])):
    assert sp.factor(x-y)==0
    checks += 1
assert sp.factor((sp.eye(4)-T).det()+h*F)==0
checks+=1
Delta = sp.factor(A*C-Bv**2)
assert sp.factor(Delta-(1+2*q)/2*((1-q)+3*h-6*h*q-12*h*h*q))==0
checks+=1
q_root = (1-3*h*h)/(1+3*h)
assert sp.factor(A.subs(q,q_root)-3*h*(2*h+1)/(3*h+1))==0
assert sp.factor(Delta.subs(q,q_root)-27*h**3*(1-h)*(2*h+1)**2/(3*h+1)**2)==0
checks+=2
# Independently verify one-step moments for many exact initial errors.
starts = [(sp.Rational(a),sp.Rational(b),sp.Rational(c)) for a in [-2,-1,0,1,2] for b in [-1,0,2] for c in [-2,0,1]]
for Q in [sp.Rational(0),sp.Rational(1,8),sp.Rational(1,4),sp.Rational(3,8),sp.Rational(1,2)]:
 for step in [sp.Rational(1,10),sp.Rational(1,3),sp.Rational(2,3)]:
  t=T.subs({q:Q,h:step})
  mats=[M.subs(h,step) for M in matrices]
  ps=[x.subs(q,Q) for x in probabilities]
  for r0 in starts:
   w=sp.Matrix(r0)
   z=sp.Matrix([w[0]**2,w[0]*w[1],w[1]**2,w[2]**2])
   direct=sum((p*sp.Matrix([a[0]**2,a[0]*a[1],a[1]**2,a[2]**2]) for p,M in zip(ps,mats) for a in [M*w]),sp.zeros(4,1))
   assert direct == sp.diag(1,sp.Rational(1,2),1,1)*t*sp.diag(1,2,1,1)*z
   checks+=1
# Rational examples on both sides of the sharp boundary (numerical eigenvalues are checks only).
import math
for Q in [0,0.125,0.25,0.375,0.5]:
 root=(-3*Q+math.sqrt(9*Q*Q+12*(1-Q)))/6
 for factor in [0.9,1.1]:
  from numpy import array, linalg
  arr=array(T.subs({q:Q,h:root*factor}),dtype=float)
  radius=max(abs(linalg.eigvals(arr)))
  assert (radius<1 if factor<1 else radius>1)
  checks+=1
print('VERIFY_OK',checks)
