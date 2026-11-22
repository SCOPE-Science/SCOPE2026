#!/usr/bin/env python3
"""Independent rational and asymptotic checks for size-ranked broken-stick triangles."""
from fractions import Fraction
from math import factorial, lgamma, log, exp, sqrt


def failure_factorial(n, i):
    m = n - i - 1
    return Fraction(factorial(n) * factorial(2*m+1), factorial(m+1)*factorial(n+m))


def failure_beta(n, i):
    # A second computation: exp(-E_(i)) has Beta(n-i+1,i) law.
    m = n-i-1
    p = Fraction(1,1)
    for j in range(m):
        p *= Fraction(m+2+j, n+1+j)
    return p


def failure_product(n, i):
    m = n - i - 1
    v=Fraction(1,1)
    for r in range(m+2,n+1):
        v *= Fraction(r,r+m)
    return v


def main():
    count=0
    for n in range(3,101):
        arr=[]
        for i in range(1,n-1):
            f=failure_factorial(n,i)
            assert f==failure_beta(n,i)==failure_product(n,i)
            assert 0<f<1
            arr.append(f);count+=2
            if i<n-2:
                m=n-i-1
                expected=Fraction((m+1)*(n+m),2*m*(2*m+1))
                assert failure_factorial(n,i+1)/f==expected
                assert (expected<1)==(n<=3*m-2)
                count+=2
        optimum=n-1-(n+1)//3
        assert arr[optimum-1]==min(arr)
        assert arr.count(min(arr))==1
        assert all(arr[j]>arr[j+1] for j in range(optimum-1))
        assert all(arr[j]<arr[j+1] for j in range(optimum-1,len(arr)-1))
        count+=4
    # An independent direct calculation for the classical n=3 case.
    assert failure_factorial(3,1)==Fraction(3,4)
    assert 1-failure_factorial(4,2)==Fraction(2,5)
    count+=2
    for n in (300,600,1200,2400):
        m=(n+1)//3
        lp=lgamma(n+1)+lgamma(2*m+2)-lgamma(m+2)-lgamma(n+m+1)
        ratio=exp(lp-n*log(Fraction(3,4)))
        assert abs(ratio-sqrt(6))<0.08
        count+=1
    print(f'PASS: {count} independent exact/scale checks')

if __name__=='__main__':
    main()
