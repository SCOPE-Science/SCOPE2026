"""Exact symbolic checks for a three-step Chebyshev inverse on tree Laplacians.

Run: python verify.py
Requires: sympy. The assertions certify the displayed algebraic identities;
the proof of the universal statements is in RESULT.md.
"""
import sympy as s

u, h, z = s.symbols('u h z', positive=True)
T3 = lambda t: 4*t**3 - 3*t
c = u+h/2
d = h/2
r3 = s.factor(T3((c-z)/d)/T3(c/d))
q2 = s.factor((1-r3)/z)
D0 = h*h + 16*h*u + 16*u*u
b2=32/((h+2*u)*D0)
b1=-48/D0
b0=6*(h+4*u)*(3*h+4*u)/((h+2*u)*D0)
assert s.simplify(q2-(b2*z**2+b1*z+b0)) == 0
print('Chebyshev polynomial identity: PASS')

k,l,x=s.symbols('k l x', integer=True, nonnegative=True)
p=x**3-(k+l+4)*x**2+(k*l+2*(k+l)+5)*x-(k+l+2)
R=s.symbols('R',integer=True,nonnegative=True)
for parity,formula in [
    (0, 2*(R+1)*(2*R**2-8*R-1)/27),
    (1, (2*R+3)*(2*R**2-6*R-9)/27),
]:
    n=2*R+parity; xx=s.Rational(2,3)*(n+2)
    assert s.factor(p.subs({k:R,l:R+parity,x:xx})-formula)==0
    for rr in range(5):
        assert formula.subs(R,rr)<0
print('Balanced-double-star comparison at all sizes through eleven: PASS')

m=s.symbols('m',integer=True,positive=True)
lam=(m+3+s.sqrt(m*m+6*m+1))/2
assert s.simplify(p.subs({k:m,l:m,x:lam}))==0
muc=s.factor(2*m+2-s.Rational(3,2)*lam)
assert s.simplify(muc-(5*m-1-3*s.sqrt(m*m+6*m+1))/4)==0
for mm in range(1,25):
    assert (muc.subs(m,mm)>0) == (mm>=5)
print('Symmetric double-star spectrum and shift threshold: PASS')

# An exact 12-vertex Laplacian and its Chebyshev polynomial inverse.
N=12
L=s.zeros(N)
edges=[(0,1)]+[(0,i) for i in range(2,7)]+[(1,i) for i in range(7,12)]
for i,j in edges:
    L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
H=4+s.sqrt(14)
U=s.Rational(1,4)
A=L+U*s.eye(N)
D0v=s.factor(D0.subs({h:H,u:U}))
B=b2.subs({h:H,u:U})*(A*A)+b1.subs({h:H,u:U})*A+b0.subs({h:H,u:U})*s.eye(N)
q_bridge=s.simplify(B[0,1]); predicted=s.simplify(b2.subs({h:H,u:U})*(U+s.Rational(3,2)*H-12))
assert s.simplify(q_bridge-predicted)==0
assert q_bridge<0
for i in range(N):
 for j in range(N):
    if i!=j and {i,j}!={0,1}:
        assert B[i,j]>=0
print('Exact bridge-only negative sign on the twelve-vertex double-star: PASS')
print('Hub-bridge entry:',q_bridge)

# Supplemental finite cross-check (not used for the universal proof).
try:
    import networkx as nx
    import numpy as np
    count=0
    for n in range(2,12):
        for graph in nx.nonisomorphic_trees(n):
            mat=np.zeros((n,n))
            for i,j in graph.edges():
                mat[i,i]+=1;mat[j,j]+=1;mat[i,j]-=1;mat[j,i]-=1
            LL=np.linalg.eigvalsh(mat)[-1]
            for i,j in graph.edges():
                assert graph.degree(i)+graph.degree(j)<1.5*LL+1e-9
            count+=1
    print('Supplemental independent isomorphism-class computations:',count,'PASS')
except ImportError:
    print('Optional graph enumeration skipped (networkx/numpy not installed)')
