"""Independent exact arithmetic checks for an all-size K_{3,b} forest correlation theorem.

The finite graph tests enumerate every acyclic edge subset of K_{3,b} for b=2,...,5.
The polynomial-identity tests compare degree-b<=4, degree-x<=10 bivariate
polynomials on a (5)x(11) integer grid, which is an exact certificate by interpolation.
"""
from collections import Counter
from fractions import Fraction


def formulas(b,x):
    a=1+3*x
    f=1+6*x+(9+3*b)*x*x+10*b*x**3+3*b*b*x**4
    u=x*(1+8*x+19*x*x+10*x**3+b*(3*x*x+14*x**3+6*x**4)+3*b*b*x**4)
    br=x*x*a*a*(1+4*x+(2*b+1)*x*x)
    bl=x*x*(1+10*x+(31+3*b)*x*x+(24+18*b)*x**3+(3*b*b+12*b)*x**4)
    bd=x*x*(1+10*x+(32+3*b)*x*x+(30+18*b)*x**3+(3*b*b+12*b+9)*x**4)
    return a,f,u,br,bl,bd


def positive_factors(b,x):
    t=b-1
    pr=(9*t**3*x**6+t*t*(18*x**6+48*x**5+12*x**4)
        +t*(9*x**6+66*x**5+106*x**4+46*x**3+6*x*x)
        +18*x**5+75*x**4+98*x**3+52*x*x+12*x+1)
    pd=(9*b*b*x**6+18*b*b*x**5+7*b*b*x**4+30*b*x**5
        +73*b*x**4+44*b*x**3+7*b*x*x
        +19*x**4+56*x**3+44*x*x+12*x+1)
    return pr,pd


def count_by_size(b):
    edges=[(i,3+j) for j in range(b) for i in range(3)]
    sums=[Counter() for _ in range(5)]
    for mask in range(1<<(3*b)):
        parent=list(range(b+3))
        def find(v):
            while parent[v]!=v:v=parent[v]
            return v
        valid=True
        for k,(v,w) in enumerate(edges):
            if mask&(1<<k):
                v,w=find(v),find(w)
                if v==w:
                    valid=False;break
                parent[v]=w
        if not valid:continue
        k=mask.bit_count()
        sums[0][k]+=1
        if mask&1:
            sums[1][k]+=1
            for col,other_index in enumerate((1,3,4),start=2):
                if mask&(1<<other_index):sums[col][k]+=1
    return sums


def verify():
    checked=0
    for b in range(2,6):
        sums=count_by_size(b)
        for x in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2)):
            a,f,u,br,bl,bd=formulas(b,x)
            expected=[a**(b-2)*f,a**(b-3)*u,a**(b-4)*br,
                      a**(b-4)*bl,a**(b-4)*bd]
            got=[sum(value*x**deg for deg,value in terms.items()) for terms in sums]
            for idx,(lhs,rhs) in enumerate(zip(got,expected)):
                assert lhs==rhs,('forest-enumeration',b,x,idx,lhs,rhs)
                checked+=1
            for both in got[2:]:
                assert got[1]**2>got[0]*both,('negative-covariance',b,x)
                checked+=1
    # F,U,B have degrees in b at most 2 and in x at most 6.
    # The Rayleigh differences have b-degree <=4 and x-degree <=10.
    # Vanishing on a 5x11 distinct-point grid proves polynomial equality globally.
    for b in range(5):
        for x in range(11):
            a,f,u,br,bl,bd=formulas(b,x)
            pr,pd=positive_factors(b,x)
            assert u*u-f*br==x**4*(b-1)*pr
            checked+=1
            assert u*u-f*bd==x**4*pd
            checked+=1
            assert bd-bl==x**4*a*a
            checked+=1
    for b in (2,3,4,10,100):
        for x in (Fraction(1,2),Fraction(1),Fraction(2)):
            a,f,u,br,bl,bd=formulas(b,x)
            pr,pd=positive_factors(b,x)
            assert pr>0 and pd>0 and f>0
            assert u*u-f*br>0 and u*u-f*bl>0 and u*u-f*bd>0
            checked+=1
    print('VERIFY_OK',checked,'independent exact rational and polynomial comparisons')

if __name__=='__main__':verify()
