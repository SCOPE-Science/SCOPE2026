#!/usr/bin/env python3
"""Exact arithmetic checks for piecewise-affine projection on midpoint-refined stars.

All matrices and edge absolute-integrals are constructed from the graph, not
from the proposed rational closed forms. Finite tests support, but do not
replace, the all-degree algebraic proof.
"""
from fractions import Fraction as Q

def inverse(A):
    n=len(A)
    aug=[[Q(x) for x in A[i]]+[Q(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if aug[i][k]),None)
        assert p is not None
        aug[k],aug[p]=aug[p],aug[k]
        v=aug[k][k];aug[k]=[z/v for z in aug[k]]
        for i in range(n):
            if i!=k:
                v=aug[i][k]
                if v: aug[i]=[a-v*b for a,b in zip(aug[i],aug[k])]
    return [r[n:] for r in aug]

def integral_abs_linear(a,b):
    a,b=Q(a),Q(b)
    if a*b>=0:return (abs(a)+abs(b))/2
    A,B=abs(a),abs(b)
    return (A*A+B*B)/(2*(A+B))

def projector_vertex_norms(d,refined=True):
    if refined:
        # center=0, intermediate i=1+i, leaf i=1+d+i
        vertices=1+2*d
        edges=[(0,1+i) for i in range(d)]+[(1+i,1+d+i) for i in range(d)]
    else:
        vertices=1+d
        edges=[(0,1+i) for i in range(d)]
    # For unrefined edges of length 2, common edge length cancels in
    # the inverse-Gram/kernel product, so the same combinatorial mass
    # matrix can be used.
    A=[[Q(0) for _ in range(vertices)] for _ in range(vertices)]
    for i,j in edges:
        A[i][i]+=Q(2)
        A[j][j]+=Q(2)
        A[i][j]+=Q(1)
        A[j][i]+=Q(1)
    M_inv=inverse(A)
    # Gram = A/6. The value of the evaluation kernel at vertex i on
    # edge (j,k), at coordinate theta, is 6[(1-theta)M_inv[i,j]
    # + theta M_inv[i,k]].
    return [sum((6*integral_abs_linear(row[i],row[j]) for i,j in edges),Q(0)) for row in M_inv],M_inv

def test():
    counts=0
    for d in range(2,18):
        got, inv=projector_vertex_norms(d,True)
        center=Q(17,9)
        middle=Q(76*d+29,9*(4*d+3))
        leaf=Q(1552*d*d+928*d+19,9*(4*d+3)*(20*d+1))
        assert got[0]==center
        assert all(x==middle for x in got[1:d+1])
        assert all(x==leaf for x in got[d+1:])
        assert leaf>center and leaf>middle
        assert inv[0][0]*6==Q(7,2*d)
        assert inv[1][0]*6==-Q(1,d)
        assert inv[d+1][0]*6==Q(1,2*d)
        unref,_=projector_vertex_norms(d,False)
        L0=Q(7*d+3,3*(d+1))
        assert max(unref)==L0
        assert (leaf>L0)==(d<=3)
        assert leaf!=L0
        counts+=1
    print('EXACT_DENSE_GRAM_INVERSION_AND_SIGNED_KERNELS_OK',counts)
    import sympy as s
    d=s.symbols('d',integer=True,positive=True)
    C=s.Rational(17,9)
    M=(76*d+29)/(9*(4*d+3))
    L=(1552*d*d+928*d+19)/(9*(4*d+3)*(20*d+1))
    U=(7*d+3)/(3*(d+1))
    assert s.simplify((s.factor(L-C))-(32*(d-1)*(6*d+1)/(9*(4*d+3)*(20*d+1))))==0
    assert s.simplify((s.factor(L-M))-(2*(16*d*d+136*d-5)/(9*(4*d+3)*(20*d+1))))==0
    assert s.simplify((s.factor(L-U))-(-4*(32*d**3-104*d*d-77*d+2)/(9*(d+1)*(4*d+3)*(20*d+1))))==0
    assert s.simplify((s.factor(s.diff(L,d)))-(1568*(16*d*d+4*d+1)/(9*(4*d+3)**2*(20*d+1)**2)))==0
    assert s.limit(L,d,s.oo)==s.Rational(97,45)
    assert s.limit(U,d,s.oo)==s.Rational(7,3)
    x=s.symbols('x',nonnegative=True)
    assert s.expand((32*d**3-104*d*d-77*d+2).subs(d,x+4))==32*x**3+280*x*x+627*x+78
    assert (32*d**3-104*d*d-77*d+2).subs(d,2)<0
    assert (32*d**3-104*d*d-77*d+2).subs(d,3)<0
    print('EXACT_UNIVERSAL_COMPARISON_POLYNOMIALS_OK')
    print('EXACT_REFINEMENT_REVERSAL_AND_LIMITS_OK')
    print('ALL_MIDPOINT_STAR_PROJECTION_CHECKS_OK')
if __name__=='__main__': test()
