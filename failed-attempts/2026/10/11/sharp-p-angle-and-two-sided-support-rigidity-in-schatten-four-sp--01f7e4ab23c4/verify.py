"""Reproducibility checks for the exact Schatten-four P-angle identity.

Requires Python 3, SymPy and NumPy. The theorem's infinite-dimensional
proof is the trace expansion in RESULT.md; these are finite exact checks.
"""
import random
import math
import sympy as sp
import numpy as np

q=sp.sqrt(2)
k=2-q
a,b=sp.symbols("a b",positive=True)
assert sp.simplify(k*k-4*k+2)==0
factor=(a**4+b**4)-(a*a+b*b-k*a*b)**2-2*k*a*b*(a-b)**2
assert sp.simplify(factor)==0

# Exact fourth power: tr[(X.T X)^2] over integer matrices.
def mm(A,B):
    n=len(A); m=len(B); l=len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(l)] for i in range(n)]
def tr(A):return sum(A[i][i] for i in range(len(A)))
def transpose(A):return [list(z) for z in zip(*A)]
def plus(A,B):return [[x+y for x,y in zip(r,s)] for r,s in zip(A,B)]
def minus(A,B):return [[x-y for x,y in zip(r,s)] for r,s in zip(A,B)]
def fourth(A):
    Q=mm(transpose(A),A)
    return tr(mm(Q,Q))
def hs2(A):return tr(mm(transpose(A),A))

rng=random.Random(4321)
exact=0
for n in (2,3,4):
    for trial in range(200):
        U=[[rng.randint(-4,4) for j in range(n)] for i in range(n)]
        V=[[rng.randint(-4,4) for j in range(n)] for i in range(n)]
        W=mm(U,transpose(V))
        K=plus(mm(transpose(U),V),mm(transpose(V),U))
        left=fourth(plus(U,V))+fourth(minus(U,V))-2*(fourth(U)+fourth(V))
        right=4*hs2(W)+2*hs2(K)
        assert left==right,(n,trial,left,right)
        exact+=1

# A diagonal pair is an exact maximizer.
P=sp.diag(1,0)
Q=sp.diag(0,1)
X=2**(-sp.Rational(1,4))*(P+Q)
Y=2**(-sp.Rational(1,4))*(P-Q)
assert sp.simplify(sp.trace((X.T*X)**2)-1)==0
assert sp.simplify(sp.trace((Y.T*Y)**2)-1)==0
U=X+Y;V=X-Y
U4=sp.simplify(sp.trace((U.T*U)**2))
V4=sp.simplify(sp.trace((V.T*V)**2))
assert U4==V4==8
AA=sp.sqrt(sp.sqrt(U4));BB=sp.sqrt(sp.sqrt(V4))
cos=sp.simplify((AA**2+BB**2-4)/(2*AA*BB))
assert sp.simplify(cos-(1-1/sp.sqrt(2)))==0
assert U*V.T==sp.zeros(2) and U.T*V==sp.zeros(2)

# Supplementary floating-point checks for noncommuting operators.
def norm4(M):return np.sum(np.linalg.svd(M,compute_uv=False)**4)**0.25
rg=np.random.default_rng(31843)
numeric=0
for n in (2,3,5):
    for trial in range(240):
        A=rg.standard_normal((n,n));B=rg.standard_normal((n,n))
        A=A/norm4(A);B=B/norm4(B)
        U=A+B;V=A-B
        a=norm4(U);b=norm4(V)
        s=math.sqrt(a**4+b**4)
        K=U.T@V+V.T@U
        defect=4-a*a-b*b+(2-math.sqrt(2))*a*b
        rhs=(2*np.linalg.norm(U@V.T,'fro')**2+np.linalg.norm(K,'fro')**2)/(4+s)
        rhs+=2*(2-math.sqrt(2))*a*b*(a-b)**2/(s+a*a+b*b-(2-math.sqrt(2))*a*b)
        assert abs(defect-rhs)<1e-9,(n,trial,defect,rhs)
        assert defect>=-1e-10
        numeric+=1
print(f"VERIFY_OK symbolic_factor=1 exact_trace_cases={exact} noncommuting_cases={numeric} extremum=1-1/sqrt2")
