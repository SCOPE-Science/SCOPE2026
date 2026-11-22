"""Supplementary exact-rational sanity checks for separated-support signed moments.
The infinite-dimensional theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial


def legendre_at(x, k):
    out=[F(1)]
    if k:
        out.append(x)
    for j in range(1,k):
        out.append(((2*j+1)*x*out[-1]-j*out[-2])/(j+1))
    return out


def moment(n):
    # Uniform distribution on [1/2,1]: 2 integral_{1/2}^1 t^n dt.
    return 2*(F(1)-F(1,2)**(n+1))/F(n+1)


def det(mat):
    A=[list(row) for row in mat]
    n=len(A); result=F(1)
    for i in range(n):
        p=next((j for j in range(i,n) if A[j][i]),None)
        if p is None:return F(0)
        if p!=i:
            A[i],A[p]=A[p],A[i];result=-result
        d=A[i][i];result*=d
        for j in range(i+1,n):
            t=A[j][i]/d
            for l in range(i+1,n):A[j][l]-=t*A[i][l]
            A[j][i]=F(0)
    return result


def hankel(n,k,epsilon):
    return [[moment(n+i+j)-epsilon*F(1,4)**(n+i+j) for j in range(k+1)] for i in range(k+1)]


def check():
    vals=legendre_at(F(-2),8)
    assert vals[:4]==[F(1),F(-2),F(11,2),F(-17)]
    K=[sum((2*j+1)*vals[j]**2 for j in range(k+1)) for k in range(9)]
    assert K[:4]==[F(1),F(13),F(657,4),F(8749,4)]
    assert F(4,8749)<F(1,1000)<F(4,657)
    # Exactly 2-hyponormal, not 3-hyponormal for epsilon=1/1000.
    e=F(1,1000)
    for k in range(3):
        for n in range(15):
            H=hankel(n,k,e)
            assert all(det([row[:r] for row in H[:r]])>0 for r in range(1,k+2)),(n,k)
    assert det(hankel(0,3,e))<0
    # Equality at epsilon=4/657: zero determinant at n=0, strict positive for n>=1.
    e=F(4,657)
    assert det(hankel(0,2,e))==0
    for n in range(1,12):
        H=hankel(n,2,e)
        assert all(det([row[:r] for row in H[:r]])>0 for r in range(1,4))
    # General separated two-positive / two-negative atomic test, with all signed masses positive.
    nu=[(F(1,2),F(1,4)),(F(3,4),F(1,4)),(F(1),F(1,2))]
    sig=[(F(0),F(1,300)),(F(1,4),F(1,300))]
    def Q(n,coeff):
        poly=lambda x:sum(v*x**i for i,v in enumerate(coeff))
        return sum(w*x**n*poly(x)**2 for x,w in nu)-sum(w*x**n*poly(x)**2 for x,w in sig)
    from itertools import product
    for coeff in product([F(-1),F(0),F(1)],repeat=3):
        if coeff==(F(0),)*3:continue
        for n in range(12):
            assert Q(n,coeff)>=F(1,2)**n*Q(0,coeff)
    print('PASS: 9 Legendre values; 4 exact kernels; 45 positive Hankel blocks; 1 negative block; 12 boundary blocks; 312 signed-support inequalities')

if __name__=='__main__':check()
