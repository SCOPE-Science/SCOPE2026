"""Reproducibility checks for the two-cluster Bargmann-Fock collision spectrum.
Scientific checks only; high-precision finite tests supplement the all-order proof.
Run with Python 3 and mpmath: python verify.py
"""
import math
import mpmath as mp
from fractions import Fraction

mp.mp.dps=90

def delta(m, r):
    if r == 0: return mp.mpf(1)
    t=mp.mpf(1)
    for i in range(r):
        t*=mp.sqrt(mp.factorial(m+i)/mp.factorial(m-r+i))*mp.factorial(i)/mp.factorial(r+i)
    return t

def overlap(m, a):
    t=a*a
    c=mp.matrix(m)
    for k in range(m):
        for j in range(m):
            if k>=j:
                c[k,j]=mp.exp(-t/2)*mp.sqrt(mp.factorial(j)/mp.factorial(k))*a**(k-j)*mp.laguerre(j,k-j,t)
            else:
                c[k,j]=mp.exp(-t/2)*mp.sqrt(mp.factorial(k)/mp.factorial(j))*(-a)**(j-k)*mp.laguerre(k,j-k,t)
    return c

def leakage(m,a,K=55):
    t=a*a
    M=mp.matrix(K-m,m)
    for k in range(m,K):
        for j in range(m):
            M[k-m,j]=mp.exp(-t/2)*mp.sqrt(mp.factorial(j)/mp.factorial(k))*a**(k-j)*mp.laguerre(j,k-j,t)
    return M

def det_fraction(mat):
    n=len(mat); a=[[Fraction(x) for x in row] for row in mat]
    out=Fraction(1)
    for j in range(n):
        for k in range(j,n):
            if a[k][j]:break
        else: return Fraction(0)
        if k!=j: a[j],a[k]=a[k],a[j];out=-out
        pivot=a[j][j];out*=pivot
        for k in range(j+1,n):
            factor=a[k][j]/pivot
            for h in range(j+1,n):a[k][h]-=factor*a[j][h]
            a[k][j]=Fraction(0)
    return out

checks=0
for r in range(1,8):
    mat=[[Fraction(1, math.factorial(r+i-j)) for j in range(r)] for i in range(r)]
    lhs=det_fraction(mat)
    rhs=Fraction(math.prod(math.factorial(i) for i in range(r)),math.prod(math.factorial(r+i) for i in range(r)))
    assert lhs==rhs,(r,lhs,rhs)
    checks+=1

for m in range(1,7):
    c=(delta(m,m)/delta(m,m-1))**2
    f=mp.mpf(1)/(mp.factorial(2*m-1)*mp.binomial(2*m-2,m-1)**2)
    assert abs(c/f-1)<mp.mpf('1e-77'),(m,c,f)
    checks+=1
    for ar in ['0.04','0.07','0.10']:
        a=mp.mpf(ar)
        C=overlap(m,a)
        E=mp.eigsy(C.T*C,eigvals_only=True)
        T=leakage(m,a,K=48)
        D=mp.eigsy(T.T*T,eigvals_only=True)
        for i in range(m):
            # The C singular squares ascend, while the leakage squares ascend.
            # In an exact full-space calculation they add to one in reversed order.
            assert abs(E[i]+D[m-1-i]-1)<mp.mpf('2e-70'), (m,ar,i)
            checks+=1
        for r in range(1,m+1):
            # descending singular values of leakage, and lower Gram eigenvalues
            s2=D[m-r]
            a2=(delta(m,r)/delta(m,r-1))**2
            predicted=a2*a**(4*r-2)
            ratio=s2/predicted
            # finite-distance asymptotics need not equal one exactly
            assert abs(ratio-1)<mp.mpf('.12'), (m,ar,r,str(ratio))
            if ar=='0.04':
                assert abs(ratio-1)<mp.mpf('.025'), (m,ar,r,str(ratio))
            checks+=1
print('PASS: %d checks; reciprocal-factorial determinant identities and all %d spectral orders tested.' % (checks, sum(range(1,7))))
print('The high-precision overlap and independent 48-term Fock-tail calculations agree.')
print('All asymptotic ratios are within 12% at separations 0.04, 0.07 and 0.10.')
for m in (1,2,3,4,5,6):
    a=mp.mpf('.04');T=leakage(m,a,K=48);D=mp.eigsy(T.T*T,eigvals_only=True)
    r=m
    pred=(delta(m,r)/delta(m,r-1))**2*a**(4*r-2)
    print('m=%d worst-channel ratio at a=0.04: %s' % (m,mp.nstr(D[0]/pred,16)))
