"""Reproducible rational and symbolic checks for the stated RNA-binding burst theorem.

Requires Python 3.10+ and SymPy for the symbolic portion. No network access.
"""
from fractions import Fraction as Q
import random
import sympy as s


def matrix(j, pars):
    u0, v0, u1, v1, a, b = pars
    U0, U1 = u0+v0, u1+v1
    D = U0*(U1+b)+a*j*U1
    return (((U1+b)*u0/D, a*j*u1/D),
            (b*u0/D, (U0+a*j)*u1/D))


def tail(n, k, pars):
    v = (Q(1), Q(1))
    for j in reversed(range(n, n+k)):
        T = matrix(j, pars)
        v = (T[0][0]*v[0] + T[0][1]*v[1],
             T[1][0]*v[0] + T[1][1]*v[1])
    return v[0]


def rat_tests():
    rng = random.Random(4352)
    count = 0
    for _ in range(150):
        pars = tuple(Q(rng.randrange(1,9),rng.randrange(1,7)) for _ in range(6))
        u0,v0,u1,v1,a,b = pars
        delta = u1*v0-u0*v1
        for n in (0,1,2,4,7):
            for k in range(1,9):
                difference = tail(n+1,k,pars)-tail(n,k,pars)
                assert (difference>0)-(difference<0) == (delta>0)-(delta<0)
                count+=1
    assert count==6000
    for u1 in (Q(0),Q(1),Q(5)):
        pars=(Q(2),Q(3),u1,Q(7),Q(4),Q(1))
        u0,v0,u1,v1,a,b=pars
        U0,U1=u0+v0,u1+v1
        delta=u1*v0-u0*v1
        p1=u1/U1
        for n in (0,1,3,15):
            D=U0*(U1+b)+a*n*U1
            assert tail(n,1,pars)-p1 == -delta*(U1+b)/(U1*D)
    return count


def sym_tests():
    u0,v0,u1,v1,a,b,j,f,g=s.symbols('u0 v0 u1 v1 a b j f g',nonnegative=True)
    U0=u0+v0; U1=u1+v1; D=U0*(U1+b)+a*j*U1
    T=s.Matrix([[(U1+b)*u0,a*j*u1],[b*u0,(U0+a*j)*u1]])/D
    v=s.Matrix([f,g]); R=U0*u1*g-U1*u0*f
    assert s.factor((T*v)[1]-(T*v)[0]-R/D)==0
    assert all(s.factor(s.diff((T*v)[i],j)-a*R*c/D**2)==0 for i,c in enumerate((U1+b,b)))
    p1=u1/U1
    tinf=s.Matrix([[0,p1],[0,p1]])
    dif=T-tinf
    assert s.factor(dif[0,0]-(U1+b)*u0/D)==0
    assert s.factor(dif[0,1]+(U1+b)*p1*U0/D)==0
    assert s.factor(dif[1,0]-b*u0/D)==0
    assert s.factor(dif[1,1]+b*p1*U0/D)==0
    assert s.factor((T*s.ones(2,1))[0]-p1+(u1*v0-u0*v1)*(U1+b)/(U1*D))==0


if __name__=='__main__':
    print('Passed finite exact rational tail comparisons:',rat_tests())
    sym_tests()
    print('Passed symbolic cone, derivative, matrix limit, and first-tail identities.')
