"""Exact fourth-moment enumerator and reproducible endpoint/deficit checks.
All model identities use only Python's standard library.
"""
from collections import Counter
from itertools import product
from fractions import Fraction as Q
from math import cos, sin, pi, isclose
import cmath


def exact_fourier_tensor(b):
    freqs = [1, b, b*b]
    indexed = [(f,2*j) for j,f in enumerate(freqs)]+[(-f,2*j+1) for j,f in enumerate(freqs)]
    out = Counter()
    for ind in product(range(6), repeat=4):
        if sum(indexed[i][0] for i in ind)==0:
            monomial=[0]*6
            for i in ind:
                monomial[indexed[i][1]]+=1
            out[tuple(monomial)]+=1
    return out


def expected_fourier_tensor(b):
    out=Counter()
    def add(inds, c):
        m=[0]*6
        for j in inds:m[j]+=1
        out[tuple(m)]+=c
    for j in range(3):add((2*j,2*j,2*j+1,2*j+1),6)
    for i in range(3):
        for j in range(i+1,3):add((2*i,2*i+1,2*j,2*j+1),24)
    if b==2:
        add((0,0,2,5),12);add((1,1,3,4),12)
    if b==3:
        add((0,0,0,3),4);add((1,1,1,2),4)
        add((2,2,2,5),4);add((3,3,3,4),4)
    return out


def moment4(b,u):
    P,Qv,R=(abs(z)**2 for z in u)
    base=Q(3,2)*(P*P+Qv*Qv+R*R)+6*(P*Qv+P*R+Qv*R)
    if b==2:base+=6*(u[0]**2*u[1]*u[2].conjugate()).real
    if b==3:base+=2*(u[0]**3*u[1].conjugate()+u[1]**3*u[2].conjugate()).real
    return base/4


def numerical_moment(b,u,n=4096):
    sums=[0.,0.]
    for j in range(n):
        t=2*pi*j/n
        v=(u[0]*cmath.exp(1j*t)+u[1]*cmath.exp(1j*b*t)+u[2]*cmath.exp(1j*b*b*t)).real
        sums[0]+=v*v;sums[1]+=v**4
    return sums[0]/n,sums[1]/n

for b in (2,3,4,5,6,7,10,19):
    assert exact_fourier_tensor(b)==expected_fourier_tensor(b),(b,'quartic coefficients')
print('EXACT_ALL_FOURTH_MOMENT_COEFFICIENTS_OK gaps=2,3,4,5,6,7,10,19')

P,Qv,R=Q(3,7),Q(2,7),Q(2,7)
S=P+Qv+R;T=P*Qv
fourth=Q(3,2)*(P*P+Qv*Qv+R*R)+6*(P*Qv+P*R+Qv*R)+6*T
assert S==1 and fourth==Q(45,14)
assert Q(45,14)>Q(5,2)>Q(3,2)
print('EXACT_DYADIC_SHARP_ENDPOINT_45_OVER_14_OK')

# Exact restriction of the two deficit identities on rational-amplitude profiles
for a,b,c in product(range(-4,5),repeat=3):
    if (a,b,c)==(0,0,0): continue
    P,Qv,R=a*a,b*b,c*c; S=P+Qv+R; T=a*a*b*c
    F=Q(3,2)*(P*P+Qv*Qv+R*R)+6*(P*Qv+P*R+Qv*R)+6*T
    low=3*P*(abs(b)-abs(c))**2+3*Qv*R+6*(P*abs(b*c)+T)
    high=Q(21,4)*(P-Q(3,7)*S)**2+Q(3,4)*(Qv-R)**2+3*P*(abs(b)-abs(c))**2+6*(P*abs(b*c)-T)
    assert F-Q(3,2)*S*S==low
    assert Q(45,14)*S*S-F==high
    assert low>=0 and high>=0
print('EXACT_DYADIC_TWO_POSITIVE_DEFICITS_OK 728_NONZERO_INTEGER_PROFILES')

# Cubic-gap witnesses, with distinct arithmetic signatures.
a=Q(-1,4)
m4=Q(3,8)*(1+a**4)+Q(3,2)*a*a+a/2
m2=Q(1,2)*(1+a*a)
assert m4/m2**2==Q(707,578)<Q(3,2)
assert Q(53,18)>Q(5,2)
print('EXACT_TERNARY_GAP_SUB_BASELINE_AND_SUP_GENERIC_WITNESSES_OK')

# Check Haar fourth moment directly by quadrature for independent complex coefficients.
for b in (2,3,4,7):
    for u in ((1.0+0j,1.0+0j,1.0+0j), (1.1+.8j,-.7+.2j,.5-1.2j)):
        empirical2,empirical4=numerical_moment(b,u)
        assert isclose(empirical2,sum(abs(x)**2 for x in u)/2,rel_tol=1e-10,abs_tol=1e-10)
        assert isclose(empirical4,moment4(b,u),rel_tol=1e-10,abs_tol=1e-10)
print('INDEPENDENT_HAAR_QUADRATURE_CONSISTENCY_OK 8_CASES')
print('ALL_LACUNARY_FOURTH_MOMENT_CHECKS_OK')
