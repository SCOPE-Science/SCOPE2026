"""Exact arithmetic checks of the two-step pedal construction and norm-variance identity.

Run: python check_pedal.py
Requires sympy. This is a finite regression test, not a proof of the theorem.
"""
from itertools import product
from sympy import Matrix, Rational, simplify

EPS = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]


def dot(u,v):
    return (u.T*v)[0]


def verify(A):
    A = Matrix(A)
    assert A.det() != 0
    Q = A.inv().T
    q = [Q[:,i] for i in range(3)]
    D = Matrix.diag(*[1/dot(x,x) for x in q])
    W = Q*D
    C = W.inv().T
    assert simplify(C-A*Matrix.diag(*[dot(x,x) for x in q])) == Matrix.zeros(3,3)
    s = []
    v = []
    for bits in EPS:
        e = Matrix(bits)
        normal = C*e
        # Every cross-polytope facet hyperplane is normal . x = 1.
        for i in range(3):
            assert simplify(dot(normal, bits[i]*W[:,i])) == 1
        si = simplify(dot(normal,normal))
        s.append(si)
        v.append(normal/si)
        assert simplify(dot(normal,v[-1])) == 1
    assert simplify(sum((s[i]*v[i] for i in range(4)), Matrix.zeros(3,1))) == Matrix.zeros(3,1)
    mean = sum(s)/4
    variance = simplify(sum((x-mean)**2 for x in s))
    obstacle = simplify(16*sum(dot(C[:,i],C[:,j])**2 for i in range(3) for j in range(i+1,3)))
    assert simplify(variance-obstacle) == 0
    is_right = all(dot(A[:,i],A[:,j]) == 0 for i in range(3) for j in range(i+1,3))
    assert (variance == 0) == is_right
    return s,variance

cases = [
    Matrix.diag(1,2,3),
    Matrix([[1,1,0],[0,1,0],[0,0,1]]),
    Matrix([[2,Rational(1,2),1],[0,3,Rational(1,3)],[0,0,4]]),
    Matrix([[1,0,1],[0,1,1],[0,0,1]]),
    Matrix([[1,1,1],[1,-1,0],[0,1,-2]]),
]
for j,A in enumerate(cases):
    s,variance=verify(A)
    print(f'case {j}: determinant={A.det()}, s={s}, obstruction={variance}')
print('All exact rational checks passed.')
