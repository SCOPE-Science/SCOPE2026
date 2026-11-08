#!/usr/bin/env python3
"""Exact symbolic checks for the two-by-two frozen-Sylvester construction.

Requires sympy. All-parameter verification supports the accompanying algebraic
proof; finite parameter samples never replace quantified analytic arguments.
"""
from sympy import (Matrix, symbols, sqrt, eye, zeros, simplify, factor,
                   Rational, diag, kronecker_product, S)

k,t=symbols('k t', positive=True)  # k=sqrt(K)
K=k**2
Z=diag(K,1)
root=Matrix([[K,t*k],[t*k,1]])
A=root*root

def sylv_inv(B):
    assert B.shape==(2,2)
    return Matrix([[B[0,0]/(2*K),B[0,1]/(K+1)],
                   [B[1,0]/(K+1),B[1,1]/2]])

def reduce_matrix(M):
    return M.applyfunc(lambda a: factor(simplify(a)))

def update(X):
    return reduce_matrix(X+sylv_inv(A-X*X))

X1=update(Z)
X2=update(X1)
expected_1=Matrix([[K+t*t/2,t*k],[t*k,1+K*t*t/2]])
expected_2=Matrix([[K-t**4/(8*K),t*k*(1-t*t/2)],
                   [t*k*(1-t*t/2),1-K**2*t**4/8]])
assert reduce_matrix(X1-expected_1)==zeros(2)
assert reduce_matrix(X2-expected_2)==zeros(2)
assert simplify(root.det()-K*(1-t*t))==0
assert reduce_matrix(root*root-A)==zeros(2)

E=root-Z
basis=[Matrix([[1,0],[0,0]]), Matrix([[0,1/sqrt(2)],[1/sqrt(2),0]]),
       Matrix([[0,0],[0,1]]),Matrix([[0,1/sqrt(2)],[-1/sqrt(2),0]])]
def deriv(H):
    return reduce_matrix(-sylv_inv(E*H+H*E))
J=Matrix([[factor(simplify(sum((Bi.T*deriv(Bj)).diagonal())))
           for Bj in basis] for Bi in basis])
expected_J=-t*Matrix([[0,1/(sqrt(2)*k),0,0],
                      [sqrt(2)*k/(K+1),0,sqrt(2)*k/(K+1),0],
                      [0,k/sqrt(2),0,0],[0,0,0,0]])
assert reduce_matrix(J-expected_J)==zeros(4)
lam=symbols('lam')
assert simplify(J.charpoly(lam).as_expr()-lam**2*(lam-t)*(lam+t))==0
expected_singular_squares=[t*t*(K+1/K)/2,4*t*t*K/(K+1)**2]
JJ=reduce_matrix(J.T*J)
for value in expected_singular_squares:
    assert factor(JJ.charpoly(lam).as_expr().subs(lam,value))==0
assert simplify((K*K+1)*(K+1)**2-8*K*K-(K-1)**2*(K*K+4*K+1))==0

values={k:S(4),t:Rational(1,2)}
assert root.subs(values)==Matrix([[16,2],[2,1]])
assert A.subs(values)==Matrix([[260,34],[34,5]])
assert X1.subs(values)==Matrix([[Rational(129,8),2],[2,3]])
assert X2.subs(values)==Matrix([[Rational(32767,2048),Rational(7,4)],
                                  [Rational(7,4),-1]])
assert X2.subs(values)[1,1]<0
for kk in [S(1),S(2),S(3),S(4),S(8),S(16),S(100)]:
    for tt in [Rational(1,10),Rational(1,2),Rational(9,10)]:
        sub={k:kk,t:tt}
        for M in [X1,X2]:
            assert reduce_matrix(M.subs(sub))==M.subs(sub)
        assert all(v.is_real for v in J.subs(sub).eigenvals().keys())
        assert all(x>0 for x in [root.subs(sub)[0,0],root.subs(sub).det()])
print('VERIFY_OK: exact iterates, Jacobian, nonzero singular squares, witness; 21 parameter cases')
