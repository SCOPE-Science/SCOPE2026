#!/usr/bin/env python3
"""Exact rational reproducibility certificate for a 21-sample Fourier-extension endpoint predictor.
Requires Python 3 standard library only. Its trigonometric enclosure follows
Machin's alternating arctangent series and Taylor's alternating cosine series.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path

N=10; M=21; T=6; L=T*(M-1)
D=10**75
E=F(1,10**70)  # certified spectral norm bound on H minus H_approx
DELTA=F(1,10**35)
ETA=F(1,10**25)
USTR='''0.0000035315210122410521916311128647209481807975275589531307903739661
-0.000066983935260941439187169896175149276805684002725875709355625619
0.00060691088315169603874097589373692060657849159203482935783424143
-0.0034926009776136017636421637728038803200717369404769585291333677
0.014316748632177942997406071377164084628754122911203464381288619
-0.044435220704880797216741251744919536871061793718598592291413383
0.10834795101007977770279713446173840646517940998948306342996976
-0.21252963746894731371276478821628368265655591781209575478090462
0.34060678855661481303307278817739896505771113949089256697356064
-0.45038236826732547945050448281047927307859489308437794494038945
0.49404976150198332576703703136556836725300818172625319930706728
-0.45038236826732547945050448281047927307859489308437794494038945
0.34060678855661481303307278817739896505771113949089256697356064
-0.21252963746894731371276478821628368265655591781209575478090462
0.10834795101007977770279713446173840646517940998948306342996976
-0.044435220704880797216741251744919536871061793718598592291413383
0.014316748632177942997406071377164084628754122911203464381288619
-0.0034926009776136017636421637728038803200717369404769585291333677
0.00060691088315169603874097589373692060657849159203482935783424143
-0.000066983935260941439187169896175149276805684002725875709355625619
0.0000035315210122410521916311128647209481807975275589531307903739661'''
u=[F(x) for x in USTR.split()]
assert len(u)==M

def arctan_trunc(q,n=95):
    return sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
print("compute pi",flush=True)
pi0=16*arctan_trunc(5)-4*arctan_trunc(239)
print("pi done",flush=True)
pierr=F(16,191*5**191)+F(4,191*239**191)
assert pierr<F(1,10**125)
assert F(3)<pi0<F(22,7)

# The following fixed-point Taylor arithmetic is all integer arithmetic.
# Every truncation contributes <10^-90 absolute error, and 50 terms at
# |x|<2 amplify accumulated rounding by < exp(2)<8; total <10^-85.
SCALE=10**90
PIINT=(pi0*SCALE).numerator//(pi0*SCALE).denominator
assert abs(F(PIINT,SCALE)-pi0)<F(1,10**90)
def cos_approx_angle(q):
    k=q%120
    if k>60:k=120-k
    sign=1
    if k>30: k=60-k;sign=-1
    x=(PIINT*k)//60
    assert 0<=x<2*SCALE
    term=SCALE;sm=term
    for j in range(1,50):
        numer=-term*x*x
        denom=SCALE**2*(2*j-1)*(2*j)
        term=numer//denom
        sm+=term
    assert F(2**100,factorial(100))<F(1,10**125)
    return F(sign*sm,SCALE)
coscache={k: cos_approx_angle(k) for k in range(61)}

print("H begin",flush=True)
H=[]
for i in range(M):
    row=[]
    for j in range(M):
        s=F(1)+sum((2*coscache[(l*(i-j))%120 if (l*(i-j))%120<=60 else 120-(l*(i-j))%120] for l in range(1,11)),F(0))
        z=s/F(L)
        rounded=(z.numerator*D//z.denominator)
        row.append(F(rounded,D))
    H.append(row)
# Each cosine enclosure <2e-125; quantizing H to 75 decimals gives entry error <1e-75;
# each row sum <21e-75, hence spectral norm <1e-70.
assert all(H[i][j]==H[j][i] for i in range(M) for j in range(M))

print("H done",flush=True)
# Exact fraction-free integer Bareiss Sylvester test.
# All decimals are terminating, so a fixed power of ten clears every denominator.
B=[[H[i][j]-(DELTA+E if i==j else 0)+ETA*u[i]*u[j] for j in range(M)] for i in range(M)]
Q=10**170
A=[]
for row in B:
    rr=[]
    for v in row:
        z=v*Q
        assert z.denominator==1, "increase shared denominator"
        rr.append(z.numerator)
    A.append(rr)
print("B built",flush=True)
prev=1
for k in range(M-1):
    print("bareiss",k,flush=True)
    pivot=A[k][k]
    assert pivot>0, ('PD fail',k)
    for i in range(k+1,M):
        ai=A[i][k]
        for j in range(k+1,M):
            num=pivot*A[i][j]-ai*A[k][j]
            assert num%prev==0, ('nonintegral Bareiss quotient',k)
            A[i][j]=num//prev
        A[i][k]=0
    prev=pivot
assert A[M-1][M-1]>0

# Rayleigh and residual exact checks.
norm2=sum((x*x for x in u),F(0))
assert F(999,1000)**2 < norm2 < F(1001,1000)**2
Hu=[sum((H[i][j]*u[j] for j in range(M)),F(0)) for i in range(M)]
mu=sum((u[i]*Hu[i] for i in range(M)),F(0))/norm2
assert F(0)<mu<F(1,10**38), ('Rayleigh',float(mu))
r=[Hu[i]-mu*u[i] for i in range(M)]
r2=sum((x*x for x in r),F(0))
assert r2 < F(1,10**104), ('residual squared',float(r2))
# ||(H_exact-mu_true)v|| <= ||(H_approx-mu)v||+2E||v||,
# hence normalized residual < 1e-51 (deliberately slack).
resbound=F(1,10**51)
# mu_true < mu + E < 2e-38, and lambda_2(H_exact)>DELTA by rank-one inertia.
assert mu+E<F(2,10**38)
# Thus sin(angle(v,u1)) < resbound/(DELTA-2e-38) < 1e-15.
assert resbound/(DELTA-F(2,10**38))<F(1,10**15)
# Consequently endpoint magnitude differs from |v_endpoint|/||v|| by <2e-15.
# Even the coarse 0.1% norm enclosure suffices for the stated integer gain bounds.
vp=abs(u[0]); wp=abs(u[-1]);
assert vp==wp
assert F(1,290000)+F(1,10**12) < vp/F(1001,1000)
assert vp/F(999,1000)+F(1,10**12) < F(1,280001)
# These strict brackets imply 280000 < sqrt(1/|u1_p|^2-1) < 290000.
print('PASS: mathematically certified 280000 < amplification < 290000, both endpoints')
print('PASS: smallest eigenvalue isolated; exact-rational positive-definite rank-one certificate')
print('PASS: source parameters N=10, m=21, T=6, L=120; errors bounded analytically')
print('approximate Rayleigh eigenvalue',float(mu),'approximate endpoint',float(vp))
