"""Standard-library verification of the exact polar-width joint density."""
import math
import random

PI=math.pi
ROOT3=math.sqrt(3.0)
M0=1.0/ROOT3
M1=1.0/math.sqrt(2.0)


def support(m):
    q=math.sqrt(max(0.0, 2.0*(1.0-m*m)))
    low=(2*m+math.sqrt(max(0,1.0-2*m*m))) if m<=M1 else (m+math.sqrt(max(0,1.0-m*m)))
    return low, m+q, q


def angle_low(m):
    low, _, q=support(m)
    if q==0: return PI/4
    return math.asin(max(-1.,min(1.,(low-m)/q)))


def simpson(f,a,b,n=24000):
    assert n%2==0
    h=(b-a)/n
    total=f(a)+f(b)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*f(a+h*i)
    return h*total/3


def integrated_moment(power_m=0,power_s=0):
    def integrand(m):
        a=angle_low(m)
        q=support(m)[2]
        extent=PI/2-a
        if power_s==0:
            value=extent
        elif power_s==1:
            value=m*extent+q*math.cos(a)
        else:
            raise ValueError
        return (12/PI)*m**power_m*value
    return simpson(integrand,M0,M1)+simpson(integrand,M1,1.0)


# Independent analytic marginals and same-direction cross moment.
assert abs(integrated_moment()-1)<2e-6
assert abs(integrated_moment(1,0)-(3*math.sqrt(2)/(2*PI))*math.acos(1/3))<2e-6
assert abs(integrated_moment(0,1)-1.5)<2e-6
assert abs(integrated_moment(1,1)-(1/3+2*math.sqrt(2)/PI))<2e-6

# In the large-maximum regime, the conditional angular interval is [pi/4,pi/2].
for j in range(1,600):
    m=M1+(1-M1)*j/600
    assert abs(angle_low(m)-PI/4)<1e-11
    low,high,q=support(m)
    assert low<=high+1e-12 and q>0


def joint_cdf(mcut,scut):
    if mcut<=M0: return 0.
    def marginal_integrand(m):
        low,high,q=support(m)
        if scut<=low: return 0.
        a=angle_low(m)
        top=(PI/2 if scut>=high else math.asin(min(1.,max(-1.,(scut-m)/q))))
        return (12/PI)*max(0.,top-a)
    end=min(1.,mcut)
    if end<=M1: return simpson(marginal_integrand,M0,end,16000)
    return simpson(marginal_integrand,M0,M1,16000)+simpson(marginal_integrand,M1,end,16000)

# Direct uniformly oriented sphere simulation, not sampled from the asserted density.
rng=random.Random(541911)
cutoffs=[(0.62,1.64),(0.78,1.60),(0.89,1.49),(0.95,1.70)]
counts=[0]*len(cutoffs)
N=240000
for i in range(N):
    xyz=[rng.gauss(0.,1.) for _ in range(3)]
    n=math.sqrt(sum(x*x for x in xyz))
    arr=[abs(x)/n for x in xyz]
    m=max(arr)
    s=sum(arr)
    lo,hi,_=support(m)
    assert lo-2e-12<=s<=hi+2e-12
    for k,(r,t) in enumerate(cutoffs):
        if m<=r and s<=t: counts[k]+=1
for i,(r,t) in enumerate(cutoffs):
    prob=joint_cdf(r,t)
    observed=counts[i]/N
    assert abs(prob-observed)<0.012,(i,prob,observed)
print('VERIFY_OK: normalization, marginal means, cross moment, 599 conditional-angle checks, 240000 Haar samples, 4 joint-CDF comparisons')
