"""Exact checks for Gaussian quadratic control-variate regression identities.

The sharp moment theorem is analytic. These checks verify finite algebraic
identities, examples and the one-variable spherical-moment calculation.
"""
import random
from sympy import Matrix, Rational, symbols, factor, simplify, diff

rng=random.Random(20261101)
checks=0
for n in range(3,9):
    for d in range(1,min(4,n-1)+1):
        for trial in range(12):
            X=Matrix(n,d,lambda i,j:Rational(rng.randrange(-9,10),3))
            ones=Matrix.ones(n,1)
            xm=Matrix([[sum(X[i,j] for i in range(n))/n for j in range(d)]])
            U=X-ones*xm
            S=U.T*U
            if S.det()==0: continue
            R=Matrix(d,d,lambda i,j:Rational(rng.randrange(-4,5),4))
            A=(R+R.T)/2
            b=Matrix(d,1,lambda i,j:Rational(rng.randrange(-5,6),7))
            c=Rational(rng.randrange(-5,6),6)
            f=Matrix(n,1,lambda i,j:(X.row(i)*A*X.row(i).T)[0]+(X.row(i)*b)[0]+c)
            D=ones.row_join(X)
            ols=(D.T*D).inv()*D.T*f
            z=Matrix(n,1,lambda i,j:(U.row(i)*A*U.row(i).T)[0])
            beta=S.inv()*U.T*z
            claimed=c+(S*A).trace()/n-(xm*A*xm.T)[0]-(xm*beta)[0]
            assert simplify(ols[0]-claimed)==0
            # The exact coefficient identity is independent of the linear term.
            f0=Matrix(n,1,lambda i,j:(X.row(i)*A*X.row(i).T)[0]+c)
            ols0=(D.T*D).inv()*D.T*f0
            assert simplify(ols[0]-ols0[0])==0
            checks+=2

n=symbols('n',integer=True,positive=True)
a=(n-1)/n
b=-1/n
pairs=factor(15*n*a**3+n*(n-1)*(9*a*a*b+6*b**3))
expected_pairs=6*(n-2)*(n-1)/n
assert simplify(pairs-expected_pairs)==0
r2=factor(pairs/((n+1)*(n+3)))
expected_r2=6*(n-2)*(n-1)/(n*(n+1)*(n+3))
assert simplify(r2-expected_r2)==0
risk=factor(2/n+4/n**2+r2/n)
assert simplify(risk-(2/n+4/n**2+6*(n-2)*(n-1)/(n*n*(n+1)*(n+3))))==0
checks+=3

# Explicit near-rank-loss pole: n=3, d=2, A=diag(1,0).
eps=symbols('eps',positive=True)
y=Matrix([1,0,-1]);q=Matrix([1,-2,1]);
U=Matrix.hstack(y+eps*q,y)
A=Matrix([[1,0],[0,0]])
z=Matrix(3,1,lambda i,j:(U.row(i)*A*U.row(i).T)[0])
beta=(U.T*U).inv()*U.T*z
assert simplify(beta[0]+eps-1/(3*eps))==0
assert simplify((eps*beta[0]).limit(eps,0)-Rational(1,3))==0
checks+=2
print('PASS: %d exact rational/symbolic assertions'%checks)
print('One-dimensional coefficient second moment:',expected_r2)
print('One-dimensional integration MSE:',risk)
print('Two-dimensional singular coefficient:',simplify(beta[0]))
print('Infinite-moment threshold uses the analytic residual-Gaussian radial integral, not finite tests.')
