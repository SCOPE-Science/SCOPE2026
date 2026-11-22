"""Independent rational checks of the stopped rotational-diffusion identities.
The mathematical arguments are given in RESULT.md; this checker is supplementary.
"""
from fractions import Fraction as F
from itertools import product


def lap_radial_polynomial(coefficients):
    # polynomial sum coefficients[k]*r**k, radial Laplacian in 2D.
    return {k - 2: v * k * k for k, v in coefficients.items() if k >= 2}


def qmean(R, s, D):
    return (R**4-s**4)/(16*D)


def qsecond(R, s, D):
    return (3*R**8-4*R**4*s**4+s**8)/(512*D**2)


def qvariance(R, s, D):
    return (R**8-s**8)/(512*D**2)


def area_only_variance(R, s, D, omega):
    u=qmean(R,s,D)
    return 2*D/u+omega**2*qvariance(R,s,D)/u**2


def full_information(R, s, D):
    return qmean(R,s,D)/(2*D)


assert lap_radial_polynomial({4: F(-1,16)}) == {2: -F(1)}
assert lap_radial_polynomial({4: F(-4,512),8: F(1,512)}) == {2: -F(1,8),6: F(1,8)}
checks=2
for R, s, D, omega in product([F(1),F(2),F(5)], [F(0),F(1,3),F(3,4)], [F(1,2),F(2),F(3)], [F(0),F(2,3),F(-5,2)]):
    if s>=R: continue
    u=qmean(R,s,D)
    v=qsecond(R,s,D)
    w=qvariance(R,s,D)
    assert v-u*u==w
    checks+=1
    assert area_only_variance(R,s,D,omega)==32*D**2/(R**4-s**4)+omega**2*(R**4+s**4)/(2*(R**4-s**4))
    checks+=1
    assert area_only_variance(R,s,D,omega)*full_information(R,s,D)==1+omega**2*(R**4+s**4)/(64*D**2)
    checks+=1
    assert u>0 and w>0
    checks+=1
assert F(1,2)==(F(1,512)/F(1,16)**2)
checks+=1
print('PASS',checks,'exact rational checks')
