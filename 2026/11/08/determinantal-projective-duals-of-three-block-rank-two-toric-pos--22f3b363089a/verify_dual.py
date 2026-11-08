#!/usr/bin/env python3
"""Exact supplementary checks for complete-tripartite toric projective duals.
The unlimited-parameter classification is proved in RESULT.md, not by this finite check.
"""
from math import comb
import sympy as S


def witness(a,b):
    assert 2 <= a <= b
    M=S.eye(a).row_join(S.ones(a,b-a)*(2*a))
    alpha=S.Matrix([1]*(a-1)+[-(a-1)])
    lam=S.ones(a,1)
    beta=M.T*lam
    u=-lam
    v=S.Matrix([int(-alpha[i]-2*a*(b-a)) for i in range(a)]+[1]*(b-a))
    w=1
    T=M.row_join(alpha).col_join(beta.T.row_join(S.zeros(1,1)))
    assert M.rank()==a and T.rank()==a
    assert all(z!=0 for z in list(u)+list(v)+[w])
    assert M*v+w*alpha==S.zeros(a,1)
    assert M.T*u+w*beta==S.zeros(b,1)
    assert (alpha.T*u+beta.T*v)==S.zeros(1,1)
    assert (u.T*M*v+w*alpha.T*u+w*beta.T*v)==S.zeros(1,1)
    assert len(M.nullspace())==b-a
    print('TORUS_TANGENCY_CERTIFICATE',a,b,'dual_codimension',b-a+1,
          'dual_degree',comb(b+1,a),'contact_dimension',b-a)


def square_identity(a):
    M=S.Matrix(a,a,lambda i,j:S.Symbol('m%d%d'%(i,j)))
    alpha=S.Matrix(a,1,lambda i,_:S.Symbol('a%d'%i))
    beta=S.Matrix(a,1,lambda i,_:S.Symbol('b%d'%i))
    T=M.row_join(alpha).col_join(beta.T.row_join(S.zeros(1,1)))
    assert S.expand(T.det()+ (alpha.T*M.adjugate().T*beta)[0])==0
    print('SQUARE_ADJUGATE_IDENTITY',a,'degree',a+1)


def determinant_factor(a):
    M=S.Matrix(a,a,lambda i,j:S.Symbol('m%d%d'%(i,j)))
    alpha=S.Matrix(a,1,lambda i,_:S.Symbol('a%d'%i))
    beta=S.Matrix(a,1,lambda i,_:S.Symbol('b%d'%i))
    H=S.zeros(2*a+1)
    H[:a,a:2*a]=M
    H[a:2*a,:a]=M.T
    H[:a,2*a]=alpha
    H[2*a,:a]=alpha.T
    H[a:2*a,2*a]=beta
    H[2*a,a:2*a]=beta.T
    delta=(alpha.T*M.adjugate().T*beta)[0]
    assert S.expand(H.det()-((-1)**(a+1)*2*M.det()*delta))==0
    print('HESSIAN_EXTRANEOUS_FACTOR',a)


if __name__=='__main__':
    for a,b in [(2,2),(2,3),(2,6),(3,3),(3,4),(4,6)]:witness(a,b)
    for a in (2,3):square_identity(a)
    for a in (2,):determinant_factor(a)
    print('ALL_EXACT_DUAL_CHECKS_PASS')
