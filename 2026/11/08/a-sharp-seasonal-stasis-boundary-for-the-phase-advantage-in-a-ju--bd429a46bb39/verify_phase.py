"""Exact certificate checks for a two-season juvenile-adult phase comparison.

Requires only the Python standard library. Tests corroborate, but do not
replace, the all-parameter proof stated in RESULT.md.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import random


def model(a, d, f, s):
    return ((a, f), (s, d))


def mul(X, Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def tr(X):
    return X[0][0] + X[1][1]


def det(X):
    return X[0][0]*X[1][1]-X[0][1]*X[1][0]


def phase_matrices(a1,d1,a2,d2,F,f,S,s):
    aligned = mul(model(a2,d2,f,s), model(a1,d1,F,S))
    opposite = mul(model(a2,d2,f,S), model(a1,d1,F,s))
    return aligned, opposite


def chi(X, z):
    return z*z - tr(X)*z+det(X)


def perron(X):
    with localcontext() as ctx:
        ctx.prec=70
        def dec(x):return Decimal(x.numerator)/Decimal(x.denominator)
        T=dec(tr(X));D=dec(det(X))
        return (T+(T*T-4*D).sqrt())/2


def run():
    rng=random.Random(20261103)
    checked=0
    for _ in range(4000):
        a1,d1,a2,d2=[Q(rng.randint(1,9),10) for z in range(4)]
        F=Q(rng.randint(2,40),10)
        f=F*Q(rng.randint(2,9),10)
        S=Q(rng.randint(2,9),10)
        s=S*Q(rng.randint(2,9),10)
        A,O=phase_matrices(a1,d1,a2,d2,F,f,S,s)
        Df=F-f;Ds=S-s
        R1=a1*d1; R2=a2*d2
        assert tr(O)-tr(A)==Df*Ds
        assert det(O)-det(A)==Ds*(R2*F-R1*f)
        z=Q(rng.randint(1,50),10)
        assert chi(O,z)-chi(A,z)==Ds*(R2*F-R1*f-Df*z)
        K=(R2*F-R1*f)/Df
        ra=perron(A); ro=perron(O)
        with localcontext() as ctx:
            ctx.prec=70
            k=Decimal(K.numerator)/Decimal(K.denominator)
            eps=Decimal('1e-50')
            if abs(ra-k)>eps:
                assert (ro>ra)==(ra>k)
            if R2<=R1:
                assert ro>ra
        checked+=1
    a1=Q(1,5);d1=Q(3,20);a2=Q(2,5);d2=Q(3,4)
    F=Q(63,40);f=Q(3,2);S=Q(2,5);s=Q(3,20)
    assert a1+S<1 and a2+S<1
    A,O=phase_matrices(a1,d1,a2,d2,F,f,S,s)
    assert A==((Q(17,25),Q(171,200)),(Q(33,100),Q(279,800)))
    assert O==((Q(61,200),Q(171,200)),(Q(77,400),Q(297,400)))
    assert chi(A, Q(1)) == -Q(59,800)
    assert chi(O, Q(1)) == Q(23,1600)
    # Smaller roots lie below both diagonal entries, which are below one.
    assert max(A[0][0], A[1][1], O[0][0], O[1][1]) < 1
    assert perron(A)>Decimal(1)>perron(O)
    # At a larger fertility contrast, the opposite-phase pattern wins.
    A2,O2=phase_matrices(a1,d1,a2,d2,Q(4),f,S,s)
    assert perron(O2)>perron(A2)
    print(f'PASS: {checked} rational polynomial identities and phase comparisons')
    print('PASS: exact persistence-boundary witness and opposite-phase restoration')

if __name__=='__main__':
    run()
