"""Standalone numerical diagnostics for a two-survey carcass-detection theorem.
Only Python's standard library is required. Finite tests do not replace the proof.
"""
import math
import random

def surv(t, weights, rates):
    return sum(w * math.exp(-r*t) for w,r in zip(weights, rates))

def antiderivative(t, weights, rates):
    return sum(w * (-math.expm1(-r*t))/r for w,r in zip(weights, rates))

def expect(t, v, weights, rates, p, intensity=1.0):
    # Corrects for duplicate detection of the SAME surviving carcass.
    cross = antiderivative(v,weights,rates) - antiderivative(v-t,weights,rates)
    return intensity*p*(antiderivative(t,weights,rates)+antiderivative(v,weights,rates)-p*cross)

def bisect(func, lo, hi, n=95):
    a,b=func(lo),func(hi)
    if a==0: return lo
    if b==0: return hi
    assert a*b < 0,(a,b,lo,hi)
    for _ in range(n):
        mid=(lo+hi)/2
        if mid==lo or mid==hi: break
        if func(mid)*a > 0:
            lo,a=mid,func(mid)
        else: hi=mid
    return (lo+hi)/2

def opt(weights,rates,p,H):
    S=lambda t:surv(t,weights,rates)
    if S(H)>=p: return H
    return bisect(lambda t:S(t)-p*S(H-t),0,H)

def mean(weights,rates): return sum(w/r for w,r in zip(weights,rates))

def crossing(weights,rates):
    M=mean(weights,rates)
    F=lambda t: sum(w * math.exp((1/M-r)*t) for w,r in zip(weights,rates))-1
    high=1
    while F(high)<=0: high*=2
    # avoid zero endpoint, near 0 F negative
    return bisect(F,1e-8,high)

def simpson(f, a, b, n=1600):
    if a==b:return 0.0
    d=(b-a)/n
    return d/3*(f(a)+f(b)+4*sum(f(a+i*d) for i in range(1,n,2))+2*sum(f(a+i*d) for i in range(2,n,2)))

rng=random.Random(114477)
tests=0
for _ in range(180):
    k=rng.randrange(2,6)
    rates=sorted(0.2+4*rng.random() for _ in range(k))
    raw=[0.1+rng.random() for _ in range(k)]
    weights=[w/sum(raw) for w in raw]
    p=0.03+0.94*rng.random()
    H=0.4+7*rng.random()
    t=opt(weights,rates,p,H)
    S=lambda x:surv(x,weights,rates)
    # Exact arrival-time integration independently reproduces two-survey expectation.
    u=rng.random()*H
    v=u+(H-u)*rng.random()
    integrand_before=lambda s:p*S(u-s)+p*S(v-s)-p*p*S(v-s)
    integrand_after=lambda s:p*S(v-s)
    direct=simpson(integrand_before,0,u)+simpson(integrand_after,u,v)
    assert abs(direct-expect(u,v,weights,rates,p))<2e-9
    tests+=1
    # The second time must be terminal; derivative's sign is strict.
    assert expect(u,H,weights,rates,p) >= expect(u,v,weights,rates,p)-1e-11
    tests+=1
    # Compare analytic global optimizer against a complete finite grid (not an infinite proof).
    best=expect(t,H,weights,rates,p)
    for i in range(25):
        ti=H*i/24
        for j in range(i,25):
            vi=H*j/24
            assert best >= expect(ti,vi,weights,rates,p)-1e-10
            tests+=1
    # Strictly decreasing hazard for any non-degenerate exponential mixture.
    for age in (0.0,H/2,H,2*H):
        tmp=[w*math.exp(-r*age) for w,r in zip(weights,rates)]
        scale=sum(tmp)
        tilted=[x/scale for x in tmp]
        hazard=sum(q*r for q,r in zip(tilted,rates))
        variance=sum(q*(r-hazard)**2 for q,r in zip(tilted,rates))
        assert variance>0
        tests+=1
    M=mean(weights,rates)
    H_E=-M*math.log(p)
    t_exp=H if H<=H_E else (H+H_E)/2
    t0=crossing(weights,rates)
    p0=math.exp(-t0/M)
    if p<=p0:
        assert t >= t_exp - 1e-9
        tests+=1
    else:
        hc=bisect(lambda z:S(z)-p,0,max(H,20)) if S(H)>p else bisect(lambda z:S(z)-p,0,H)
        assert hc<H_E+1e-8
        tests+=1

weights=(0.5,0.5); rates=(1.,3.); p=.5; M=2/3
z=1.8392867552141612
p0=z**(-3)
assert abs(p0-0.16071324478583884)<1e-12
tests+=1
he=M*math.log(2)
hc=bisect(lambda t:surv(t,weights,rates)-p,0,2)
hstar=he-math.log(2**(4/3)-2)
assert abs(hc-0.3822450858400359)<1e-11
assert abs(hstar-1.1163282881427354)<1e-11
for H in (0.6,hstar,2.0):
    tm=opt(weights,rates,p,H)
    te=(H+he)/2
    assert abs(tm-[0.5024051456880655,0.7892132042580222,1.2780123946477202][(0.6,hstar,2.0).index(H)])<1e-10
    if H<hstar-1e-5: assert tm<te
    elif H>hstar+1e-5: assert tm>te
    else: assert abs(tm-te)<1e-10
    tests+=1
# Verify strict growth of skew past threshold.
last=hc
for H in [hc+0.05*j for j in range(1,301)]:
    skew=2*opt(weights,rates,p,H)-H
    assert skew > last-1e-8
    last=skew
    tests+=1
assert abs(last-math.log(2))<1e-6
print('PASS',tests,'supplementary numerical assertions; finite diagnostics are not a proof')
