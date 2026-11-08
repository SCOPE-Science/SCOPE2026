"""Exact symbolic checks for unconditional [2/2] Padé positivity on weighted paths.

Requires Python 3 and SymPy. These checks supplement the all-order proof.
"""
import sympy as s

x, t = s.symbols('x t', positive=True)

def laplacian(weights):
    n = len(weights) + 1
    L = s.zeros(n)
    for k, a in enumerate(weights):
        L[k, k] += a
        L[k + 1, k + 1] += a
        L[k, k + 1] -= a
        L[k + 1, k] -= a
    return L

def endpoint(weights):
    M = x * laplacian(weights)
    I = s.eye(M.rows)
    return (M*M + 6*M + 12*I).inv() * (M*M - 6*M + 12*I)

def check_entry(mat, i, j, numerator, denominator):
    assert s.cancel(mat[i,j] - numerator/denominator) == 0, (i,j)

# Two-vertex exact spectral projector formula.
E2 = endpoint([s.Integer(1)])
F2 = (4*x*x - 12*x + 12)/(4*x*x + 12*x + 12)
for i in range(2):
    check_entry(E2, i, i, 1+F2, 2)
    check_entry(E2, i, 1-i, 1-F2, 2)

# Three vertices: every independent off-diagonal entry.
E3 = endpoint([s.Integer(1),t])
D3 = (3*x**4*t*t + 12*x**3*t*t + 12*x**3*t +
      16*x*x*t*t + 44*x*x*t + 16*x*x + 48*x*t+48*x+48)
N3 = {
    (0,1): 4*x*((2*t*t-t)*x*x+6*t*x+12),
    (1,2): 4*x*t*((2-t)*x*x+6*x+12),
    (0,2): 8*x*x*t*((t+1)*x+3),
}
for (i,j), N in N3.items():
    check_entry(E3,i,j,N,D3)
    check_entry(E3,j,i,N,D3)
assert s.simplify(E3*s.ones(3,1)-s.ones(3,1)) == s.zeros(3,1)

# Four vertices at the unique allowable ray of conductances.
E4 = endpoint([s.Integer(1),s.Integer(2),s.Integer(1)])
D4 = (x*x+3*x+3)*(x**4+9*x**3+30*x*x+27*x+9)
N4 = {
    (0,1): 9*x*(x**3+5*x*x+6*x+3),
    (0,2): 3*x*x*(x**3+6*x*x+15*x+9),
    (0,3): 3*x**3*(2*x*x+6*x+3),
    (1,2): 9*x*(x*x+6*x+6),
}
for (i,j),N in N4.items():
    check_entry(E4,i,j,N,D4)
    check_entry(E4,j,i,N,D4)
for i in range(4):
    for j in range(i+1,4):
        a,b = (i,j)
        mirror = (3-j,3-i)
        assert s.cancel(E4[a,b]-E4[mirror[0],mirror[1]])==0
assert s.simplify(E4*s.ones(4,1)-s.ones(4,1)) == s.zeros(4,1)

# Independent matrix-resistance/adjacent group-inverse identity.
for n in range(2,10):
    resistances = [s.Rational((j % 4)+1,(j % 3)+1) for j in range(1,n)]
    W = [1/r for r in resistances]
    L = laplacian(W)
    J = s.ones(n,n)/n
    K = (L+J).inv()-J
    for k in range(1,n):
        formula = (sum(j*j*resistances[j-1] for j in range(1,k))+
                   sum((n-j)**2*resistances[j-1] for j in range(k+1,n))-
                   k*(n-k)*resistances[k-1])/n**2
        assert s.cancel(K[k-1,k]-formula)==0,(n,k)

# Symbolic threshold matrix for n=4; strict increment at n>=5 by proof.
B4 = s.Matrix([[0,s.Rational(1,1),s.Rational(1,3)],
               [s.Rational(1,3),0,s.Rational(1,3)],
               [s.Rational(1,3),s.Integer(1),0]])
assert B4*s.Matrix([3,2,3]) == s.Matrix([3,2,3])
print('VERIFY_OK')
