"""Supplemental numerical checks for the two-step SU(2) class convolution theorem.
The general theorem is established by the proof, not by this finite test suite.
"""
import math

PI=math.pi

def P(L):
    return 4*L**7*(2-L)-4*PI**2*L**2+PI**4

def root():
    lo,hi=PI/2,2.0
    assert P(lo)>0 and P(hi)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if P(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def haar_cdf(a):
    if a<=-1: return 0.
    if a>=1: return 1.
    return .5+(a*math.sqrt(1-a*a)+math.asin(a))/PI

def tv_formula(a):
    if not (-1<=a<1):
        return 1.
    L=1-a
    if L<=PI/2:
        return haar_cdf(a)
    b=math.sqrt(1-PI*PI/(4*L*L))
    return haar_cdf(a)+(2/PI)*math.asin(b)-b/L

def radial_density(t):
    return (2/PI)*math.sqrt(max(0,1-t*t)) if -1<=t<=1 else 0.

def simpson(f,a,b,n=30000):
    if a==b:return 0.
    assert n%2==0
    h=(b-a)/n
    sm=f(a)+f(b)
    for k in range(1,n):
        sm+=(4 if k%2 else 2)*f(a+k*h)
    return sm*h/3

def tv_direct(a):
    if a>=1:return 1.
    L=1-a
    intervals=[-1,a,1]
    if L>PI/2:
        b=math.sqrt(1-PI*PI/(4*L*L))
        intervals=[-1,a,-b,b,1]
    ans=0.
    for left,right in zip(intervals,intervals[1:]):
        inside=((left+right)/2>=a)
        f=(lambda t:abs(radial_density(t)-(1/L if inside else 0.)))
        ans+=simpson(f,left,right,6000)
    return ans/2

def main():
    L=root();a=1-L
    b=math.sqrt(1-PI*PI/(4*L*L))
    assert PI/2<L<2 and -1<a<-b<0
    assert abs(P(L))<2e-12
    assert abs((2/PI)*math.sqrt(1-a*a)-2*b/L**2)<1e-13
    assert 243/32 < PI**2 and 27/16 < PI**2/4
    exact=tv_formula(a)
    assert .10252<exact<.10254
    assert abs(exact-tv_direct(a))<2e-7
    cases=[-1.,-.99,-.95,-.9,-.875,-.8,-.7,-.6,-.4,-.2,0.,.2,.5,.8]
    for t in cases:
        assert abs(tv_formula(t)-tv_direct(t))<3e-6, t
        assert tv_formula(t)>=exact-1e-12, t
    for dd in [1e-3,1e-2,5e-2]:
        assert tv_formula(a-dd)>exact and tv_formula(a+dd)>exact
    # Distinct from the separately known L2 spectral tuning cos(theta)=1/4.
    assert abs(a+7/8)>1e-3
    print('CHECKS_PASS')
    print('L*',format(L,'.15g'))
    print('a*',format(a,'.15g'))
    print('theta_degrees',format(math.degrees(math.acos(a)/2),'.15g'))
    print('min_TV',format(exact,'.15g'))
    print('equatorial_TV',format(tv_formula(-1),'.15g'))
    print('L2_optimal_angle_TV',format(tv_formula(-7/8),'.15g'))

if __name__=='__main__': main()
