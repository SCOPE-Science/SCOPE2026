"""Exact checks for a two-row residual-tracking sampling stability theorem.
Scientific computations only; requires SymPy and NumPy. Execute: python verify.py.
"""
import sympy as s
p, alpha = s.symbols('p alpha', positive=True)
q = 1 - p
T1 = s.Matrix([[1-alpha/p, alpha*q/p, -alpha], [1,0,0], [0,0,1]])
T2 = s.Matrix([[1-alpha/q, -alpha, alpha*p/q], [0,1,0], [1,0,0]])
# Unnormalized covariance coordinates: (Y,Ys1,Ys2,s1^2,s1s2,s2^2).
B = [s.Matrix([[1,0,0],[0,0,0],[0,0,0]]),
     s.Matrix([[0,1,0],[1,0,0],[0,0,0]]),
     s.Matrix([[0,0,1],[0,0,0],[1,0,0]]),
     s.Matrix([[0,0,0],[0,1,0],[0,0,0]]),
     s.Matrix([[0,0,0],[0,0,1],[0,1,0]]),
     s.Matrix([[0,0,0],[0,0,0],[0,0,1]])]
# Each B corresponds to monomial coordinates as a symmetric covariance matrix.
def coords(A):
    return s.Matrix([A[0,0], A[0,1], A[0,2], A[1,1], A[1,2], A[2,2]])
M = s.Matrix.hstack(*(coords(p*T1*E*T1.T+q*T2*E*T2.T) for E in B))
u=p*q
Q = (1-5*u+4*u*u)*alpha**3+(1-3*u-u*u)*alpha**2-u*u
assert s.factor((s.eye(6)-M).det(method='domain-ge') + 4*alpha*Q)==0
la=s.symbols('la')
assert s.simplify(M.subs(alpha,0).charpoly(la).as_expr()-la*(la-1)*(la-p)**2*(la-q)**2)==0
# Perron eigenvalue derivative at zero: right eigenvector all ones, left e1.
assert s.simplify((M.diff(alpha).subs(alpha,0)*s.ones(6,1))[0]+4)==0
# Verify one-step stochastic update and second-moment transport on rational examples.
checks=0
for pp in [s.Rational(1,10),s.Rational(1,4),s.Rational(2,5),s.Rational(1,2),s.Rational(3,4)]:
 for aa in [s.Rational(1,12),s.Rational(1,4),s.Rational(2,3)]:
  mm=M.subs({p:pp,alpha:aa})
  for v in [s.Matrix([1,2,-3]),s.Matrix([-2,0,5]),s.Matrix([3,-1,2])]:
   v2=s.Matrix([v[0]**2,v[0]*v[1],v[0]*v[2],v[1]**2,v[1]*v[2],v[2]**2])
   x=T1.subs({p:pp,alpha:aa})*v
   y=T2.subs({p:pp,alpha:aa})*v
   expected=pp*coords(x*x.T)+(1-pp)*coords(y*y.T)
   assert mm*v2 == expected
   checks+=1
# Sampling-balanced unique optimum follows strictly from Q_u<0.
assert s.simplify(Q.subs(p,s.Rational(1,2))-(3*alpha*alpha-1)/16)==0
for pp in [s.Rational(1,10),s.Rational(1,4),s.Rational(2,5),s.Rational(1,2)]:
 roots=[complex(z) for z in s.nroots(s.together(Q.subs(p,pp)).as_numer_denom()[0])]
 pos=[z.real for z in roots if abs(z.imag)<1e-9 and z.real>0]
 assert len(pos)==1
 acrit=pos[0]
 import numpy as np
 m=np.array(M.subs({p:pp,alpha:acrit*.995}),dtype=float)
 n=np.array(M.subs({p:pp,alpha:acrit*1.005}),dtype=float)
 assert max(abs(np.linalg.eigvals(m))) < 1 and max(abs(np.linalg.eigvals(n))) > 1
print('VERIFY_OK symbolic covariance determinant, six eigenvalues at zero, derivative,',checks,'rational one-step tests, and sample crossing checks')
