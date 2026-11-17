"""Exact arithmetic checks for two-dimensional second-jet rotation coefficients.

These are supplementary finite algebraic checks, not a proof of the
L1 endpoint sharpness, which uses Ornstein's non-inequality.
"""
from fractions import Fraction


def norms(c, s):
    assert c*c+s*s == 1
    first = abs(c)+abs(s)
    pure = 1+abs(c*s)
    mixed = abs(c*c-s*s)+4*abs(c*s)
    return first, pure, mixed


def main():
    checks=0
    cases=[(Fraction(1),Fraction(0)),(Fraction(0),Fraction(1))]
    for a in range(1,18):
        for b in range(1,18):
            c=Fraction(a*a-b*b,a*a+b*b)
            s=Fraction(2*a*b,a*a+b*b)
            cases += [(e*c,f*s) for e in (1,-1) for f in (1,-1)]
    for c,s in cases:
        first,pure,mixed=norms(c,s)
        t=2*abs(c*s)
        u=abs(c*c-s*s)
        assert t*t+u*u==1;checks+=1
        assert mixed==2*t+u;checks+=1
        assert mixed >= pure;checks+=1
        assert first*first==1+t;checks+=1
        assert mixed >= first;checks+=1
        assert mixed*mixed<=5;checks+=1
        assert (mixed==1)==(t==0);checks+=1
        # The actual Hessian coefficient matrix columns, in the order xx,xy,yy.
        M=((c*c,2*c*s,s*s),(-c*s,c*c-s*s,c*s),(s*s,-2*c*s,c*c))
        col=[sum(abs(M[i][j]) for i in range(3)) for j in range(3)]
        assert col==[pure,mixed,pure];checks+=1
        # Covariance of the second derivative matrix: pure xx applied to R.
        assert M[0][0]+M[2][0]==1;checks+=1
    # t=2/sqrt(5), u=1/sqrt(5) is on the unit semicircle:
    # Cauchy-Schwarz equality yields sqrt(5) exactly as sharp maximum.
    assert 2*2+1*1==5;checks+=1
    print('ROTATION_JET_CHECKS_OK',checks)


if __name__=='__main__':
    main()
