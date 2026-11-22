#!/usr/bin/env python3
"""Exact-rational checks for finite-horizon Lyapunov covariance quadrature.

Proof is in RESULT.md. These finite tests exercise the stated formulae;
they do not replace the proof for arbitrary dimensions or step counts.
"""
from fractions import Fraction as F
from math import factorial
from sympy import Matrix


def moment(k, T):
    return T**(k+1) / F(k+1)


def nodes_weights(kind, N, T):
    h=T/N
    if kind=='trap':
        return [(j*h, h*(F(1,2) if j in (0,N) else 1)) for j in range(N+1)]
    if kind=='simpson':
        return [(j*h/F(2), h*(F(1,6) if j in (0,2*N) else (F(2,3) if j%2 else F(1,3)))) for j in range(2*N+1)]
    raise ValueError(kind)


def rule_moment(nodes, k):
    return sum((w*t**k for t,w in nodes), F(0))


def gram(n, N, T, kind):
    nodes=nodes_weights(kind,N,T)
    approx=Matrix(n,n,lambda i,j: rule_moment(nodes,i+j)/F(factorial(i)*factorial(j)))
    exact=Matrix(n,n,lambda i,j: moment(i+j,T)/F(factorial(i)*factorial(j)))
    return approx,exact,approx-exact


def test():
    count=0
    for kind,m in [('trap',1),('simpson',2)]:
        for N in range(1,5):
            T=F(7,5)
            h=T/N
            nodes=nodes_weights(kind,N,T)
            assert len(nodes)==(N+1 if kind=='trap' else 2*N+1)
            assert sum((w for t,w in nodes),F(0))==T
            for k in range(2*m):
                assert rule_moment(nodes,k)==moment(k,T)
            expected=(T*h*h/F(6) if kind=='trap' else T*h**4/F(120))
            assert rule_moment(nodes,2*m)-moment(2*m,T)==expected
            for n in range(1,8):
                approx,exact,E=gram(n,N,T,kind)
                assert approx.rank()==min(n,len(nodes))
                assert exact.rank()==n
                if n<=m:
                    assert E==Matrix.zeros(n,n)
                elif n==m+1:
                    expected_E=Matrix.zeros(n,n)
                    expected_E[m,m]=expected/F(factorial(m)**2)
                    assert E==expected_E
                else:
                    i=m-1;j=m+1
                    assert E[i,i]==0
                    assert E[i,j]==expected/F(factorial(i)*factorial(j))
                    assert E[i,i]*E[j,j]-E[i,j]**2<0
                count+=1
    # headline certificates at a rational physical horizon
    T=F(7,5)
    _,_,E2=gram(3,2,T,'trap')
    _,_,E3=gram(4,2,T,'simpson')
    assert E2[0,2]==T*(T/F(2))**2/F(12)
    assert E3[1,3]==T*(T/F(2))**4/F(720)
    print('PASS',count,'exact-rational dimension/panel checks; rank and Loewner threshold certificates')


if __name__=='__main__': test()
