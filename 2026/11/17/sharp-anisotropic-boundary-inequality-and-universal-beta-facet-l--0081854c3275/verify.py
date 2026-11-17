#!/usr/bin/env python3
"""Independent exact Gram checks for a two-colour stretched cycle-edge polytope."""
import math
import sympy as S
from fractions import Fraction

def check(m,a,b):
    n=2*m;d=n-2
    U=S.zeros(n,n)
    for i in range(n):
        U[i,i]=a if i%2==0 else b
        j=(i+1)%n
        U[j,i]=a if j%2==0 else b
    area_sq=[]
    for i in range(m):
        for j in range(m):
            inds=[k for k in range(n) if k!=2*i and k!=2*j+1]
            B=S.Matrix.hstack(*(U[:,k]-U[:,inds[0]] for k in inds[1:]))
            gram=B.T*B
            wedge_squared=gram.det()
            t=(j-i)%m
            E=m*t*(m-t)
            O=m*(t+1)*(m-t-1)
            pred=(a*b)**(2*m-2)*(S.Rational(E,a*a)+S.Rational(O,b*b))
            assert S.simplify(wedge_squared-pred)==0, (m,a,b,i,j,wedge_squared,pred)
            area_sq.append((t,wedge_squared))
    # Check the affine complementary basis wedge gives the exact volume formula.
    odd=list(range(0,n,2));even=list(range(1,n,2))
    Q=S.Matrix.hstack(*([U[:,odd[k]]-U[:,odd[-1]] for k in range(m-1)]+[U[:,even[k]]-U[:,even[-1]] for k in range(m-1)]))
    det=(Q.T*Q).det()
    assert det==m**4*(a*b)**(2*m-2), (m,a,b,det)
    return len(area_sq)

if __name__=='__main__':
    count=0
    for m in range(2,7):
        for a,b in [(S.Integer(1),S.Integer(1)),(S.Integer(2),S.Integer(3)),(S.Integer(1),S.Rational(1,4))]:
            count+=check(m,a,b)
    print(f'CYCLE_ANISOTROPIC_PASS cases={count} m=2..6 distinct_scales=3')
