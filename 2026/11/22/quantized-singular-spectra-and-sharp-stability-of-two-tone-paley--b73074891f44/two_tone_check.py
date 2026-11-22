"""Finite-fiber reproducibility checks for two-tone bandlimited multiplication.

Only finite algebra and floating-point evaluations are checked. The direct-integral
identification and infinite-dimensional conclusions require the written proof.
"""
from fractions import Fraction
import math

checks=0
for n in range(1,33):
    for r in (Fraction(1,3), Fraction(1,1), Fraction(7,4)):
        B=[[Fraction(0) for _ in range(n)] for _ in range(n+1)]
        for j in range(n):
            B[j][j]=r
            B[j+1][j]=Fraction(1)
        for i in range(n):
            for j in range(n):
                lhs=sum(B[k][i]*B[k][j] for k in range(n+1))
                rhs=Fraction(1)+r*r if i==j else (r if abs(i-j)==1 else Fraction(0))
                assert lhs==rhs,(n,r,i,j,lhs,rhs)
                checks+=1
        # Check the exact sine eigenvector identity in real arithmetic.
        Q=[[float(sum(B[k][i]*B[k][j] for k in range(n+1)))
            for j in range(n)] for i in range(n)]
        for j in range(1,n+1):
            v=[math.sin((a+1)*j*math.pi/(n+1)) for a in range(n)]
            eigenvalue=float(1+r*r+2*r*math.cos(math.pi*j/(n+1)))
            residual=math.sqrt(sum((sum(Q[a][b]*v[b] for b in range(n))-eigenvalue*v[a])**2 for a in range(n)))
            vnorm=math.sqrt(sum(x*x for x in v))
            assert residual<1e-9*(1+vnorm),(n,r,j)
            checks+=1

# The fiber-count arithmetic is verified independently using direct enumeration.
for sigma in (0.37,1.,1.4,2.5,3.2,5.0):
    for eta in (.17,.32,.6,1.,1.31,2.5,4.6,10.):
        h=2*eta
        L=2*sigma
        ratio=L/h
        m=math.ceil(ratio-1e-13)
        for j in range(1,100):
            t=h*j/100
            count=sum(1 for k in range(-1,100) if 0<=t+k*h<L)
            assert count in (m,m-1), (sigma,eta,t,count,m)
            checks+=1
        assert m>=1
        checks+=1

print(f'TWO_TONE_PALEY_WIENER_CHECK_OK {checks}')
