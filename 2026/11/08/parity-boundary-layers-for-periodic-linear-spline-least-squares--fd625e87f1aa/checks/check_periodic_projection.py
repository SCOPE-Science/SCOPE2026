#!/usr/bin/env python3
"""Independent finite rational and high-precision checks for periodic linear splines.

The infinite-size statement relies on the proof, not on this finite checker.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def inverse_rational(matrix):
    n=len(matrix)
    a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for col in range(n):
        p=next(j for j in range(col,n) if a[j][col])
        a[col],a[p]=a[p],a[col]
        d=a[col][col]
        a[col]=[x/d for x in a[col]]
        for j in range(n):
            if j != col:
                t=a[j][col]
                if t:
                    a[j]=[u-t*v for u,v in zip(a[j],a[col])]
    return [row[n:] for row in a]


def edge_l1(a,b):
    if a*b>=0:
        return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))


def rational_cycle(n):
    # Knot spacing 1: Gram integrals of unit-spaced triangular hats.
    M=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        M[i][i]+=F(2,3)
        M[i][(i+1)%n]+=F(1,6)
        M[i][(i-1)%n]+=F(1,6)
    A=inverse_rational(M)
    c=A[0]
    norm=sum((edge_l1(c[j],c[(j+1)%n]) for j in range(n)), F(0))
    # The kernel is piecewise linear, so its absolute integral is exact.
    assert norm>1 and norm<2
    assert sum(c)==1
    for i in range(n):
        for j in range(n):
            assert sum(M[i][k]*A[k][j] for k in range(n)) == (i==j)
    return norm,c


def formula_cycle(n,precision=65):
    with localcontext() as ctx:
        ctx.prec=precision
        rt3=Decimal(3).sqrt()
        q=Decimal(2)-rt3
        z=Decimal(1)-(-q)**n
        c=[rt3*((-q)**j+(-q)**(n-j))/z for j in range(n)]
        val=Decimal(0)
        for j in range(n):
            a,b=c[j],c[(j+1)%n]
            val+=(abs(a)+abs(b))/2 if a*b>=0 else (a*a+b*b)/(2*(abs(a)+abs(b)))
        return val,q


def asymptotic_constants(terms=45):
    with localcontext() as ctx:
        ctx.prec=70
        rt3=Decimal(3).sqrt()
        q=Decimal(2)-rt3
        ce=2*rt3*(1-q)**2/(1+q)*sum((q**j/(1+q**(2*j+1)) for j in range(terms)), Decimal(0))
        co=4*rt3/(1+q)*(q*q/2+q*q/(1-q)-(1-q)**2/2*sum((q**(3*j)/(1-q**(2*j)) for j in range(1,terms)),Decimal(0)))
        assert Decimal('1.6830')<ce<Decimal('1.6831')
        assert Decimal('0.7011')<co<Decimal('0.7012')
        return ce,co



def overlap_constant_by_direct_intervals(parity,cutoff=16):
    # Independent integration of |T(s)|+|T(parity-s)|-|T(s)+T(parity-s)|.
    with localcontext() as ctx:
        ctx.prec=70
        q=Decimal(2)-Decimal(3).sqrt()
        def T(k):
            return (-q)**k
        total=Decimal(0)
        for j in range(-cutoff,cutoff+1):
            u0,u1=T(j),T(j+1)
            v0,v1=T(parity-j),T(parity-j-1)
            total+=edge_l1(u0,u1)+edge_l1(v0,v1)-edge_l1(u0+v0,u1+v1)
        return Decimal(3).sqrt()*total


def main():
    count=0
    with localcontext() as ctx:
        ctx.prec=65
        for n in range(3,22):
            exact,c=rational_cycle(n)
            approx,q=formula_cycle(n)
            assert abs(Decimal(exact.numerator)/Decimal(exact.denominator)-approx)<Decimal('1e-45'), n
            for j in range(n):
                a=Decimal(c[j].numerator)/Decimal(c[j].denominator)
                cj=Decimal(3).sqrt()*((-q)**j+(-q)**(n-j))/(1-(-q)**n)
                assert abs(a-cj)<Decimal('1e-20'),(n,j)
            count+=1
    print('EXACT_RATIONAL_GRAM_INVERSE_AND_INTEGRAL_OK',count)
    ce,co=asymptotic_constants()
    for m in (6,8,10,12):
        for parity,C in ((0,ce),(1,co)):
            n=2*m+parity
            val,q=formula_cycle(n)
            ratio=(Decimal(2)-val)/q**m
            # The asymptotic convergence is predicted by the analytic argument.
            assert abs(ratio-C)<Decimal('0.001') if m>=8 else abs(ratio-C)<Decimal('0.01')
    assert abs(overlap_constant_by_direct_intervals(0)-ce)<Decimal('1e-8')
    assert abs(overlap_constant_by_direct_intervals(1)-co)<Decimal('1e-8')
    print('PERIODIC_PARITY_ASYMPTOTIC_CONSISTENCY_OK')
    print('INDEPENDENT_OVERLAP_INTEGRATION_OK')
    print('LEADING_COEFFICIENTS',format(ce,'.16f'),format(co,'.16f'))
    print('ALL_PERIODIC_LINEAR_SPLINE_CHECKS_OK')

if __name__=='__main__':
    main()
