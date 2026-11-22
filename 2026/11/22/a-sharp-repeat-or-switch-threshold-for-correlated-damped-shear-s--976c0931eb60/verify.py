"""Exact checks for the two-step correlated damped-shear selection theorem.

No external packages are required. The common exponential scalar is factored
out; matrix identities are verified over exact rational parameters.
"""
from fractions import Fraction as F
from itertools import product


def mm(A, B):
    return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(2)) for j in range(2)) for i in range(2))


def trans(A):
    return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))


def add(A, B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))


def scale(A, q):
    return tuple(tuple(q*A[i][j] for j in range(2)) for i in range(2))


def apply(A, v):
    return tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))


def norm2(v):
    return sum(t*t for t in v)


def moment(k, q):
    U=((F(1), k), (F(0), F(1)))
    L=((F(1), F(0)), (-k, F(1)))
    choices=[(U,U,q/2), (L,L,q/2), (U,L,(1-q)/2), (L,U,(1-q)/2)]
    Q=((F(0),F(0)),(F(0),F(0)))
    for first,second,w in choices:
        P=mm(second,first)
        Q=add(Q,scale(mm(trans(P),P),w))
    m=F(1)+2*q*k*k+(1-q)*k**4/2
    assert Q==((m,F(0)),(F(0),m)), (k,q,Q,m)
    return choices,m


def finite_blocks(choices,m,initial,depth):
    # Exact enumeration of all correlated outcomes across independent blocks.
    aggregate=F(0)
    for seq in product(range(4),repeat=depth):
        w=F(1)
        v=initial
        for t in seq:
            first,second,prob=choices[t]
            w*=prob
            v=apply(second,apply(first,v))
        aggregate+=w*norm2(v)
    assert aggregate==m**depth*norm2(initial), (depth,aggregate,m)


def main():
    tests=0
    for k in [F(1,5),F(1,2),F(1),F(3,2),F(2),F(5,2),F(3),F(4)]:
        for q in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            choices,m=moment(k,q)
            tests+=1
            for v in [(F(1),F(0)),(F(1),F(2)),(F(-2),F(3))]:
                for depth in [1,2,3]:
                    finite_blocks(choices,m,v,depth)
                    tests+=1
            if k<F(2):
                assert F(1)+k**4/2 < F(1)+2*k*k
            elif k>F(2):
                assert F(1)+2*k*k < F(1)+k**4/2
            else:
                assert F(1)+2*k*k == F(1)+k**4/2
            tests+=1
    # Exact stability witnesses follow since 2<e<3 and 27/10<e<3.
    assert F(3,2)<F(2) and F(3)>F(27,10)
    assert F(1)+2*F(1)**2==3
    assert F(1)+F(1)**4/2==F(3,2)
    assert F(1)+2*F(3)**2==19
    assert F(1)+F(3)**4/2==F(83,2)
    assert F(27,10)**3>19 and F(3)**3<F(83,2)
    print('VERIFICATION_OK',tests,'rational identities and block tests')

if __name__=='__main__':
    main()
