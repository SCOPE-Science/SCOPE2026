"""Exact algebra and finite sine-block diagnostics for a weighted shift theorem."""
import sympy as s
from math import sin, pi, cos
M,l,r=s.symbols('M l r', positive=True)
Q=s.Matrix([[M/2,l/2],[l/2,(2*M*M-r*r)/(2*M)]])
b=s.Matrix([l,M])
c=s.factor(M/2-(b.T*Q.inv()*b)[0]/4)
expected=(M*M-l*l)*(M*M-r*r)/(2*M*(2*M*M-l*l-r*r))
assert s.simplify(c-expected)==0
assert s.simplify(Q.det()-(2*M*M-l*l-r*r)/4)==0
u=s.simplify((Q.inv()*b/2)[0]);v=s.simplify((Q.inv()*b/2)[1])
assert s.simplify(u-l*(M*M-r*r)/(M*(2*M*M-l*l-r*r)))==0
assert s.simplify(v-(M*M-l*l)/(2*M*M-l*l-r*r))==0
for N in range(1,30):
    x=[sin((k+1)*pi/(N+1)) for k in range(N)]
    lam=2*cos(pi/(N+1))
    for k in range(N):
        left=x[k-1] if k else 0.0
        right=x[k+1] if k+1<N else 0.0
        assert abs(left+right-lam*x[k])<1e-12
print('EXACT_HESSIAN_IDENTITY_OK; FINITE_SINE_DIAGNOSTICS_OK')
