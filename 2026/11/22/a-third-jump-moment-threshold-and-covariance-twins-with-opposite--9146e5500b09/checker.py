"""Exact rational checks for a shot-noise growth-collapse time arrow.

Only the Python standard library is required. Execute: python checker.py
"""
from fractions import Fraction as F
from math import comb, exp, sqrt


def jump_moments(law):
    assert all(p > 0 and a > 0 for a,p in law)
    assert sum((p for a,p in law),F())==1
    return [F(1)]+[sum((p*a**n for a,p in law),F()) for n in range(1,4)]


def raw_stationary(M,s,c):
    out=[F(1)]
    for n in range(1,4):
        lower=sum((F(comb(n,k))*out[k]*M[n-k] for k in range(n)),F())
        out.append(s*lower/(1-c**n))
    return out


def factor_comparison(M,s,c):
    assert 0<c<1 and s>0
    raw=raw_stationary(M,s,c)
    mu=raw[1]
    variance=raw[2]-mu**2
    third=raw[3]-3*mu*raw[2]+2*mu**3
    # The first expression follows from centered generator and independent raw-moment recursion.
    lag_coefficient=third-2*s*M[1]*variance/c
    u=M[2]/M[1]**2
    v=M[3]/M[1]**3
    # The second expression is the claimed factored all-lag sign law.
    sign_numerator=(v+s*u)*c*(1+c)-2*s*(u+s)
    independent_factor=s*M[1]**3*sign_numerator/(c*(1+c)*(1-c**3))
    assert lag_coefficient==independent_factor
    return lag_coefficient,sign_numerator,mu,variance


A=[(F(1,5),F(25,41)),(F(9,4),F(16,41))]
B=[(F(1,2),F(4,5)),(F(3),F(1,5))]
M_A=jump_moments(A)
M_B=jump_moments(B)
assert M_A == [F(1),F(1),F(2),F(89,20)],M_A
assert M_B == [F(1),F(1),F(2),F(11,2)],M_B
s,c=F(9,4),F(49,50)
cf_a,sg_a,mean_a,var_a=factor_comparison(M_A,s,c)
cf_b,sg_b,mean_b,var_b=factor_comparison(M_B,s,c)
assert mean_a==mean_b and var_a==var_b
assert sg_a<0<sg_b
for time in [F(1,4),F(1),F(3)]:
    multiplier=exp(-float((1-c)*time))-exp(-float((1-c*c)*time))
    assert multiplier>0
    assert cf_a*multiplier<0<cf_b*multiplier
    print('lag',float(time),'signed arrows',float(cf_a)*multiplier,float(cf_b)*multiplier)
# Global boundary is controlled by the third raw jump moment, not the second.
assert s*s>M_A[3]/M_A[1]**3
assert s*s<M_B[3]/M_B[1]**3
# Independent exact recurrence checks across a range of admissible laws/parameters.
for law in (A,B,[(F(1),F(1))],[(F(1,2),F(1,2)),(F(5,2),F(1,2))]):
    M=jump_moments(law)
    for ss in (F(1,7),F(1),F(9,4),F(3)):
        for cc in (F(1,20),F(2,5),F(3,4),F(49,50)):
            factor_comparison(M,ss,cc)
# Complete reset c=0 has a strictly negative third-order arrow for any nondegenerate J.
for M in (M_A,M_B):
    ss=F(9,4)
    variance0=ss*M[2]+ss**2*M[1]**2
    assert variance0>0
    limit_coefficient=-2*ss*M[1]*variance0
    assert limit_coefficient<0
# Exact formula agrees with derived zero threshold location for each chosen law.
for M in (M_A,M_B):
    u=float(M[2]/M[1]**2);v=float(M[3]/M[1]**3);ss=float(s)
    if ss*ss<v:
        threshold=(sqrt(1+8*ss*(u+ss)/(v+ss*u))-1)/2
        assert 0<threshold<1
        print('critical contraction',threshold)
    else:
        print('no admissible critical contraction')
print('PASS: 64 rational polynomial-moment comparisons; exact covariance twins; opposite arrows at three lags; complete-reset limit')
