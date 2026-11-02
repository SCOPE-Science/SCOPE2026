#!/usr/bin/env python3
from fractions import Fraction
from math import comb
for n in range(1,31):
    for k in range(1,n+1):
        beta=comb(n,k)
        assert Fraction(comb(n-1,k-1),1)==Fraction(k*beta,n)
        num1=0 if n-k==0 else comb(n-1,n-k-1)
        assert Fraction(num1-beta,1)==-Fraction(k*beta,n)
        for m in range(1,8):
            alpha=m+k+1
            lam0=-beta*m
            lam1=-beta*(m+k)
            assert lam1==-beta*(alpha-1)
            assert (-lam1)-(-lam0)==beta*k
            for ell in range(1,12):
                decay=Fraction(beta,1)*(Fraction(m,1)+Fraction(k*ell*(ell+n-1),n))
                assert decay>=beta*(m+k)
print('VERIFY_OK')
