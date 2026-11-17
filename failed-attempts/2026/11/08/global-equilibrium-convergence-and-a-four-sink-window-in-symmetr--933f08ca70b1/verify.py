"""Finite rational-algebra checks for the symmetric mutated May-Leonard vector field.

This finite test suite is supporting evidence, not an infinite-time proof.
Runs under Python 3 with only the standard library.
"""
from fractions import Fraction as F


def equilibrium_and_spectrum(a, t):
    H = t*t + 4*a*t + 2*(a+1)
    mu = (a-1)*t/H
    u = (t+2)/H
    x = [u,u,t*u]
    S = sum(x)
    rhs = [v*(1-a*S+(a-1)*v)+mu*(S-3*v) for v in x]
    assert rhs == [0,0,0], (a,t,rhs)
    J = [[(1-a*S+(a-2)*x[i]-2*mu) if i==j else (mu-a*x[i])
          for j in range(3)] for i in range(3)]
    anti = J[0][0]-J[0][1]
    trace = J[0][0]+J[0][1]+J[2][2]
    det = (J[0][0]+J[0][1])*J[2][2]-2*J[0][2]*J[2][0]
    assert anti == -(a-1)*(t-1)*(t+2)/H
    assert trace == -(a*t*t+(a+3)*t+4*a)/H
    assert det == (a-1)*(t-1)*(t+2)*(t*t-2*(a+1))/(H*H)
    assert trace < 0
    return 5


def dulac(a,mu,u,v):
    return -(a+1)/v-1/u-mu/(u*u)-2*mu/(v*v)


def main():
    n=0
    for a in [F(6,5),F(3,2),F(2),F(3),F(5),F(7)]:
        for t in [F(1,3),F(2,3),F(1),F(3,2),F(2),F(3),F(6),F(11)]:
            n+=equilibrium_and_spectrum(a,t)
            for u,v in [(F(1,5),F(2,3)),(F(3,4),F(1,2))]:
                mu=(a-1)*t/(t*t+4*a*t+2*(a+1))
                assert dulac(a,mu,u,v)<0
                n+=1
    # Homogeneous spectrum and the exact critical threshold.
    for a in [F(3,2),F(2),F(3),F(5)]:
        muc=(a-1)/(3*(2*a+1))
        assert (a-1)/(1+2*a)-3*muc==0
        assert (a-1)/(1+2*a)-3*(muc+F(1,100))<0
        assert (a-1)/(1+2*a)-3*(muc-F(1,100))>0
        n+=3
    print('PASS:',n,'exact arithmetic assertions; finite support only')


if __name__ == '__main__':
    main()
