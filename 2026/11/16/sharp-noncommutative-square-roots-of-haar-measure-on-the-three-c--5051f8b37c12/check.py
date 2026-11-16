"""Exact symbolic check of the cyclic three-point matrix Fourier identities.
Requires SymPy. The analytic classification is established separately in RESULT.md.
"""
import sympy as s
r=s.symbols('r', real=True, nonnegative=True)
w=(-1+s.I*s.sqrt(3))/2
I=s.eye(2)
A=[s.Matrix([[1,r*w**(-j)],[r*w**j,1]])/3 for j in range(3)]
Z=s.zeros(2)
def eqzero(M):
    return all(s.simplify(s.expand_complex(s.expand(z)))==0 for z in M)
assert eqzero(sum(A,Z)-I)
for j in range(3):
    assert s.simplify(A[j].det()-(1-r*r)/9)==0
    assert s.simplify(s.trace(A[j])-s.Rational(2,3))==0
    assert eqzero(sum((A[k]*A[(j-k)%3] for k in range(3)),Z)-I/3)
for j in range(3):
    for k in range(j+1,3):
        C=A[j]*A[k]-A[k]*A[j]
        assert eqzero(C*C+s.Rational(1,27)*r**4*I)
print('CHECK_OK symbolic_convolution=3 positivity_determinants=3 commutator_squares=3')
