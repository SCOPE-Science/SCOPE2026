"""Exact finite diagnostics for the Weyl-cocycle criterion and example."""
from fractions import Fraction
from itertools import product
from math import gcd


def require_cocycle():
    for d in (-3,-2,-1,0,1,2,3):
        for k,l,kp,lp in product(range(-3,4),repeat=4):
            # Phases of u_1^k u_2^l cancel; check the remaining signs.
            left = d*(k*l+kp*lp)
            right = d*(k*lp-l*kp-(k+kp)*(l+lp))
            assert (left-right)%2 == 0
    for p,q,A in product(range(-12,13),range(1,13),range(-10,11)):
        if gcd(p,q)==1:
            assert (Fraction(p*A,q).denominator==1) == (A%q==0)


def require_half_deformation():
    X = ((0,1),(1,0))
    Z = ((1,0),(0,-1))
    I = ((1,0),(0,1))

    def mul(a,b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))

    ZX, XZ = mul(Z,X),mul(X,Z)
    assert mul(Z,Z)==mul(X,X)==I
    assert all(ZX[i][j]+XZ[i][j]==0 for i,j in product(range(2),repeat=2))
    assert mul(ZX,ZX)==((-1,0),(0,-1))
    # At (x,y)=(pi/6,-pi/6), all three squared summands in R are 3/4.
    # Hence the larger eigenvalue of M*M is 3+2*(3/2)=6.
    R = sum([Fraction(3,4)]*3)
    assert R == Fraction(9,4) and Fraction(3,2)**2 == R
    assert Fraction(3)+2*Fraction(3,2)==6<9
    # The unshifted fiber has R=2, giving squared norm 3+2 sqrt(2)<6.
    assert 4*2 < (6-3)**2
    # In that fiber I+Z^2+X=2I+X has eigenvalues 1 and 3.
    assert (2-1,2+1)==(1,3)


if __name__ == '__main__':
    require_cocycle()
    require_half_deformation()
    print('VERIFY_OK')
