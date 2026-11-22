"""Reproducible supplementary checks for a 3-periodic Jacobi finite section.
Uses only the Python standard library; exact rational arithmetic and Decimal.
Not a proof for all dimensions.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def dets(q):
    m = 3*q-2
    d = [F(1), F(2)]
    for j in range(2, m+1):
        v = F(2) if (j-1)%3 == 0 else F(1,2)
        d.append(v*d[-1]-d[-2])
    return d


def exact_checks():
    nchecks=0
    for q in [1,3,5,7,9,11]:
        m=3*q-2
        d=dets(q)
        for j in range(m+1):
            r,s=divmod(j,3)
            want=[(-2)**r,2*(-2)**r,0][s]
            assert d[j]==want, (q,j,d[j],want)
            nchecks+=1
        assert d[m]==F(2)**q
        assert d[m-1]/d[m]==F(1,2)
        assert F(1,d[m])==F(1,2**q)
        # Formula for inverse first column via palindrome.
        norm2=sum((F(d[m-j],d[m]))**2 for j in range(1,m+1))
        assert norm2==F(2,3)-F(5,3)*F(1,4**q), (q,norm2)
        nchecks+=4
    return nchecks


def characteristic(n, x):
    # det(xI-H_n) for the full symmetric section -n,...,n
    d0=Decimal(0)
    d1=Decimal(1)
    for j in range(-n,n+1):
        v=Decimal(2) if j%3==0 else Decimal('0.5')
        d0,d1=d1,(x-v)*d1-d0
    return d1


def bisect(n, left, right):
    fleft=characteristic(n,left)
    fright=characteristic(n,right)
    assert fleft*fright < 0
    for _ in range(240):
        middle=(left+right)/2
        fmid=characteristic(n,middle)
        if fmid==0:
            return middle
        if fleft*fmid>0:
            left=middle
            fleft=fmid
        else:
            right=middle
    return (left+right)/2


def numerical_checks():
    with localcontext() as ctx:
        ctx.prec=105
        for k in range(2,9):
            n=3*k+1
            scale=Decimal(4)**(-k)
            eps=Decimal(3)/Decimal(10)*scale
            # Bracket the two closest eigenvalues, not all spectrum.
            left=bisect(n,-Decimal(2)*eps,Decimal(0))
            right=bisect(n,Decimal(0),Decimal(2)*eps)
            assert left<0<right
            assert abs(left/eps+1)<Decimal('0.15'), (k,left,eps)
            assert abs(right/eps-1)<Decimal('0.15'), (k,right,eps)
            print('k=',k,'negative/scale=',left/scale,'positive/scale=',right/scale)
    return 7


if __name__=='__main__':
    print('Exact identities passed:', exact_checks())
    print('Finite spectral pairs checked:', numerical_checks())
