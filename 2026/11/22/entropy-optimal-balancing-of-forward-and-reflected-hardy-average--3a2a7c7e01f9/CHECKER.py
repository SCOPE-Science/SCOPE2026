#!/usr/bin/env python3
"""Independent numerical checks for a sharp BV approximation result for reflected Hardy averaging."""
import math
import random

def jump_error(s, a):
    return -a*s*math.log(s)-(1-a)*(1-s)*math.log1p(-s)

def root(a):
    lo, hi=1e-12, 1-1e-12
    for _ in range(140):
        mid=(lo+hi)/2
        d=a*(-math.log(mid)-1)+(1-a)*(math.log1p(-mid)+1)
        if d>0: lo=mid
        else: hi=mid
    return (lo+hi)/2

def simpson(fun,lo,hi,N=1000):
    if lo>=hi: return 0.
    dx=(hi-lo)/N
    ans=fun(lo)+fun(hi)
    for j in range(1,N):
        ans+=(4 if j%2 else 2)*fun(lo+j*dx)
    return ans*dx/3

def exact_numerical_error(jumps,a):
    jumps=sorted(jumps)
    pts=[0.0]+[s for s,w in jumps]+[1.0]
    total=0.
    for left,right in zip(pts[:-1],pts[1:]):
        mass_left=sum(w*s for s,w in jumps if s<=left+1e-13)
        mass_right=sum(w*(1-s) for s,w in jumps if s>=right-1e-13)
        f=lambda x:abs(a*mass_left/x if x>0 else 0.0) if mass_right==0 else abs((a*mass_left/x if x>0 else 0.0)-(1-a)*mass_right/(1-x) if x<1 else 0.0)
        # Piecewise integrable; the only endpoint singularities have zero coefficients.
        total+=simpson(f,left,right,300)
    return total

for a in [0.,.01,.2,.5,.8,.99,1.]:
    s=root(a); c=jump_error(s,a)
    assert math.log(2)/2-1e-12<=c<=math.e**-1+1e-12
    assert jump_error(s-1e-4,a)<c and jump_error(s+1e-4,a)<c
    assert abs(s-root(1-a)-(2*s-1))<1e-10 if a==.5 else abs(s+root(1-a)-1)<1e-10
print('SEVEN_WEIGHT_OPTIMUM_AND_REFLECTION_CHECKS_PASS')

for a in [.1,.5,.9]:
    for s in [.03,.17,.4,.5,.77,.96]:
        err=exact_numerical_error([(s,1)],a)
        assert abs(err-jump_error(s,a))<1.5e-6,(a,s,err,jump_error(s,a))
print('EIGHTEEN_INDEPENDENT_JUMP_QUADRATURE_CHECKS_PASS')

rnd=random.Random(19217)
for trial in range(420):
    a=rnd.uniform(.03,.97)
    jumps=sorted((rnd.uniform(.05,.95),rnd.uniform(-2,2)) for _ in range(rnd.randrange(2,9)))
    norm=sum(abs(w) for s,w in jumps)
    err=exact_numerical_error(jumps,a)
    assert err < jump_error(root(a),a)*norm + 1e-7,(trial,err,norm,a)
    if abs(a-.5)<1e-2:
        rhs=sum((s-.5)**2*abs(w) for s,w in jumps)
        assert math.log(2)/2*norm-err+1e-7>=rhs
print('FOUR_HUNDRED_TWENTY_SIGNED_MULTIJUMP_TESTS_PASS')

for s in [.001,.03,.1,.2,.3,.45,.499,.5,.501,.7,.9,.99,.999]:
    delta=math.log(2)/2-jump_error(s,.5)
    assert delta+1e-14>=(s-.5)**2
for d in [1e-2,1e-3,1e-4]:
    quotient=(math.log(2)/2-jump_error(.5+d,.5))/(d*d)
    assert abs(quotient-1)<2e-3,(d,quotient)
print('SHARP_QUADRATIC_BV_STABILITY_CHECKS_PASS')

for a in [i/100 for i in range(101)]:
    c=jump_error(root(a),a)
    assert c>=math.log(2)/2-1e-13
    if a!=.5: assert c>math.log(2)/2+1e-8
print('ONE_HUNDRED_ONE_MINIMAX_MIXTURE_CHECKS_PASS')
print('ALL_REFLECTED_HARDY_BV_CHECKS_PASS')
