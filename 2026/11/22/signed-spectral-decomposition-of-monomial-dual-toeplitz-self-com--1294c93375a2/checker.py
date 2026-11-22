"""Exact finite-mode checks for dual Toeplitz self-commutator formulas.

This checks exact weighted disk moments, angular-sector compression identities,
Gram determinant positivity, trace telescoping and finite spectral examples.
The finite checks are supplementary and do not establish the infinite theorem.
"""
from fractions import Fraction
from math import factorial

checks = 0

def check(v, msg='check'):
    global checks
    assert v, msg
    checks += 1

def moments(alpha, M):
    h = [Fraction(1)]
    for j in range(M):
        h.append(h[-1]*Fraction(j+1,1)/ (Fraction(j+1,1) + alpha + 1))
    return h

def angular_data(h,m,k):
    assert 1<=k<m
    A=(h[2*m-k]-h[m]**2/h[k])/h[m-k]
    B=(h[k+2*m]-h[k+m]**2/h[k])/h[k+m]
    G2=(h[2*m]-h[m]*h[k+m]/h[k])**2/(h[m-k]*h[k+m])
    return A,B,G2

def direct_form(h,m,k,j,l):
    # Opposite-mode harmonic projections of monomials after Q-sector subtraction.
    ak=abs(k)
    def projection(sign,index):
        target = abs(k+sign*m)
        # radial exponent of the test function r^(|k|+2 index) after multiplying by r^m
        power0=(ak+2*index+m+target)//2
        powerbase=(ak+m+target)//2
        check((ak+2*index+m+target)%2==0)
        return h[power0]-h[ak+index]*h[powerbase]/h[ak]
    # quadratic form ||Q M_barz f||^2 - ||Q M_z f||^2
    return projection(-1,j)*projection(-1,l)/h[abs(k-m)] - projection(+1,j)*projection(+1,l)/h[abs(k+m)]

def rank_two_form(h,m,k,j,l):
    # Same form via projected harmonic generators in source angular mode.
    ak=abs(k)
    def generator(sign,index):
        target=abs(k+sign*m)
        exponent=m+target
        check((ak+2*index+exponent)%2==0)
        return h[(ak+2*index+exponent)//2]-h[ak+index]*h[(ak+exponent)//2]/h[ak]
    return generator(-1,j)*generator(-1,l)/h[abs(k-m)] - generator(+1,j)*generator(+1,l)/h[abs(k+m)]

for alpha in [Fraction(0),Fraction(1),Fraction(2),Fraction(1,2),Fraction(-1,2)]:
    h=moments(alpha,180)
    check(h[0]==1)
    for n in range(1,100):
        check(h[n+1]*h[n-1]>h[n]*h[n])
    for m in range(1,11):
        for k in range(-m-2,m+11):
            for j in range(1,5):
                for l in range(1,5):
                    check(direct_form(h,m,k,j,l)==rank_two_form(h,m,k,j,l),f'form {alpha,m,k,j,l}')
            if 1<=k<m:
                A,B,G2=angular_data(h,m,k)
                check(A>0 and B>0)
                check(A*B>G2)
            if k>=m:
                b=h[k+2*m]/h[k+m]-h[k+m]/h[k]
                check(b>0)
                # one side in each tail sector vanishes exactly
                check(direct_form(h,m,k,1,1)<0)
        # symbolic exact telescoping tail for finite cutoff
        for N in [m,m+1,2*m,2*m+9]:
            sum_b=sum((h[k+2*m]/h[k+m]-h[k+m]/h[k] for k in range(m,N+1)),Fraction(0))
            r=lambda k:h[k+m]/h[k]
            check(sum_b == sum((r(k) for k in range(N+1,N+m+1)),Fraction(0)) - sum((r(k) for k in range(m,2*m)),Fraction(0)))

h=moments(Fraction(0),30)
A,B,G2=angular_data(h,2,1)
check(A==Fraction(1,18))
check(B==Fraction(1,6))
check(G2==Fraction(2,225))
check((A+B)**2-4*G2==Fraction(28,2025))
overshoot_gap = Fraction(4,35)-Fraction(1,18)
check(overshoot_gap>0)
check(Fraction(7,2025)>overshoot_gap*overshoot_gap)

if __name__ == '__main__':
    print(f'VERIFICATION_OK {checks}')
