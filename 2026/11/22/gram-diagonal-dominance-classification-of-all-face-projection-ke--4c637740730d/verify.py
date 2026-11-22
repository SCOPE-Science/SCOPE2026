"""Finite exact checks accompanying the parallelotope orthogonal-kernel formula.

The general theorem is proved analytically; these checks are finite
regression tests on rational Gram matrices, not an infinite proof.
"""
from itertools import combinations, product
from random import Random
from sympy import Matrix, Rational, eye


def bounds(G):
    d=G.rows
    L=[sum((max(G[i,j],0) for j in range(d) if j!=i),Rational(0)) for i in range(d)]
    H=[G[i,i]+sum((min(G[i,j],0) for j in range(d) if j!=i),Rational(0)) for i in range(d)]
    return Matrix(L),Matrix(H)


def check_all_faces(G,b):
    d=G.rows
    for size in range(1,d+1):
        for I in combinations(range(d),size):
            J=tuple(j for j in range(d) if j not in I)
            for e in product((0,1),repeat=len(J)):
                rhs=Matrix([b[i]-sum((G[i,j]*v for j,v in zip(J,e)),Rational(0)) for i in I])
                A=G.extract(I,I)
                x=A.inv()*rhs
                if not all(Rational(0)<v<Rational(1) for v in x):
                    raise AssertionError((G,b,I,J,e,x))
    return True


def tests():
    rng=Random(20261119)
    cases=0; projections=0
    for d in range(2,6):
        for trial in range(15):
            # Large diagonal plus small rational perturbations in Euclidean generators.
            U=Matrix([[10*(i==j)+rng.randint(-1,1) for j in range(d)] for i in range(d)])
            G=U.T*U
            L,H=bounds(G)
            assert all(H[i]>L[i] for i in range(d))
            for trial2 in range(7):
                f=Matrix([Rational(rng.randint(1,9),10) for _ in range(d)])
                b=L+Matrix.diag(*[H[i]-L[i] for i in range(d)])*f
                assert check_all_faces(G,b)
                projections+=sum(__import__('math').comb(d,k)*2**(d-k) for k in range(1,d+1))
            cases+=1
    # Exact Gram-volume ratios, d=3 equiangular rhombohedra.
    for c, expected in [(Rational(1,3),Rational(1,20)),(Rational(-1,4),Rational(4,25))]:
        G=Matrix([[1 if i==j else c for j in range(3)] for i in range(3)])
        L,H=bounds(G)
        ratio=__import__('sympy').prod(H[i]-L[i] for i in range(3))/G.det()
        assert ratio==expected, (ratio,expected)
        assert check_all_faces(G,(L+H)/2)
    G=Matrix([[1,Rational(1,2),Rational(1,2)],[Rational(1,2),1,Rational(1,2)],[Rational(1,2),Rational(1,2),1]])
    L,H=bounds(G)
    assert all(H[i]==L[i] for i in range(3))
    G=Matrix([[1,2],[2,5]])
    assert G.det()>0
    L,H=bounds(G)
    assert H[0]<L[0]
    print('PASS:',cases,'rational Gram matrices;',cases*7,'sample center points;',projections,'proper/full face projections; 2 exact volume ratios; 2 empty-kernel examples')

if __name__=='__main__':tests()
