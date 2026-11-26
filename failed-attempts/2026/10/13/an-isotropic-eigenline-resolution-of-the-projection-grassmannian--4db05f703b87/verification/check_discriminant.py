"""Exact finite checks for an isotropic-eigenline incidence construction.

Requires Python 3 and SymPy. Run: python verification/check_discriminant.py
These finite calculations illustrate, rather than prove, the all-n theorem.
"""
import sympy as s

I = s.I
B = s.Matrix([[I, 1], [1, -I]])
v2 = s.Matrix([1, -I])
assert B * v2 == s.zeros(2, 1)
assert (v2.T * v2)[0] == 0
assert B ** 2 == s.zeros(2)
assert B.rank() == 1

a, b, c = s.symbols('a b c')
q2 = s.Matrix([[a,b],[b,c]])
z = s.symbols('z')
f2 = q2.charpoly(z).as_expr()
d2 = s.factor(s.discriminant(f2,z))
assert s.expand(d2 - (a-c)**2 - 4*b*b) == 0
assert s.expand(d2 - ((a-c)+2*I*b)*((a-c)-2*I*b)) == 0

for n in range(3,9):
    N = n*(n+1)//2
    x = s.symbols('x0:'+str(N))
    Q = s.zeros(n)
    t=0
    for j in range(n):
        for k in range(j,n):
            Q[j,k]=Q[k,j]=x[t]
            t+=1
    v = s.Matrix([1,I]+[0]*(n-2))
    w = Q*v
    # Basis of the quotient V/Cv: (w2-i*w1,w3,...,wn).
    quotient = s.Matrix([w[1]-I*w[0]]+list(w[2:]))
    J=quotient.jacobian(s.Matrix(x))
    assert J.rank() == n-1, (n,J.rank())
    assert N-(n-1) == (n*n-n+2)//2

    # An exact defective matrix with just one double eigenvalue.
    Q0 = s.diag(B,*list(range(3,n+1)))
    f=s.factor(Q0.charpoly(z).as_expr())
    expected=z*z
    for t in range(3,n+1): expected *= (z-t)
    assert s.expand(f-expected)==0
    assert Q0.rank() == n-1
    # Exact first-order coefficient of characteristic discriminant on
    # perturbing only the (1,1)-entry of B by epsilon.
    # The quadratic block has discriminant eps^2 + 4*i*eps,
    # while all other pairwise root differences are nonzero at eps=0.
    others=list(range(3,n+1))
    derivative = 4*I
    for xj in others: derivative *= xj**4
    for j in range(len(others)):
        for k in range(j+1,len(others)):
            derivative *= (others[j]-others[k])**2
    assert derivative != 0
    eps = s.symbols('eps')
    perturbed_charpoly = z*z-eps*z-I*eps
    for j in others:
        perturbed_charpoly *= (z-j)
    actual_derivative = s.diff(s.discriminant(perturbed_charpoly,z),eps).subs(eps,0)
    assert s.expand(actual_derivative-derivative) == 0

print('VERIFY_OK: n=2 factorization, isotropic Jordan block, surjectivity and reduced discriminant witness for n=3..8')
