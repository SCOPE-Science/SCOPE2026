"""Supplementary reproducibility diagnostics for a Steele--Beer two-level light theorem.
Uses only the standard library. Finite tests do not establish infinite-domain claims.
"""
import math
import random

checks=0

def check(condition, message):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(message)

def j(p,d):
    # two-point moment-generating Jensen gap, with q=1-p
    q=1-p
    return p*math.expm1(q*d)+q*math.expm1(-p*d)

def jprime(p,d):
    q=1-p
    return p*q*(math.exp(q*d)-math.exp(-p*d))

def gain_from_formula(m,d,p,h):
    a=math.exp(-h)
    return math.e/h * (math.exp(-a*m)*j(p,a*d)-math.exp(-m)*j(p,d))

def production(m,h):
    a=math.exp(-h)
    return math.e/h*(math.exp(-a*m)-math.exp(-m))

def direct_simpson(m,d,p,h,n=256):
    q=1-p
    low=m-q*d
    high=m+p*d
    def f(z,irr):
        x=irr*math.exp(-h*z)
        return math.e*x*math.exp(-x)
    def integrate(irr):
        vals=f(0,irr)+f(1,irr)
        for k in range(1,n):
            vals+=(4 if k%2 else 2)*f(k/n,irr)
        return vals/(3*n)
    return p*integrate(low)+q*integrate(high)-integrate(m)

def critical_m(p,d,h):
    a=math.exp(-h)
    return (math.log(j(p,d))-math.log(j(p,a*d)))/(1-a)

def onset_m(p,d):
    return d*jprime(p,d)/j(p,d)

def find_hc(m,p,d):
    check(m>onset_m(p,d), 'existence of root requires supercritical mean')
    lo,hi=1e-8,1.0
    while gain_from_formula(m,d,p,hi)>0:
        hi*=2
        if hi>80:
            raise AssertionError('unbracketed')
    for _ in range(90):
        mid=(lo+hi)/2
        if gain_from_formula(m,d,p,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

r=random.Random(20261118)
for i in range(2000):
    p=r.uniform(.04,.96)
    d=r.uniform(.08,3.5)
    m=(1-p)*d+r.uniform(.01,7)
    h=r.uniform(.07,5)
    val=gain_from_formula(m,d,p,h)
    threshold=critical_m(p,d,h)
    check((val>0)==(m>threshold),'strict threshold comparison')
    check(abs(val-direct_simpson(m,d,p,h))<1e-9,'quadrature versus exact formula')
    check(j(p,d)>0 and onset_m(p,d)>(1-p)*d,'physical onset above low-light cutoff')
    # check the directly integrated water-column mean itself
    a=math.exp(-h)
    check(abs(production(m,h)-math.e/h*(math.exp(-a*m)-math.exp(-m)))<1e-14,'direct representation')

for i in range(400):
    p=r.uniform(.08,.92)
    d=r.uniform(.1,3.0)
    m=onset_m(p,d)+r.uniform(.1,4)
    hc=find_hc(m,p,d)
    for mult,sign in ((.4,1),(.85,1),(1.1,-1),(2,-1)):
        val=gain_from_formula(m,d,p,hc*mult)
        check(sign*val>1e-13,'one sharp crossing as depth increases')
    # root itself is under the numerical function tolerance
    check(abs(gain_from_formula(m,d,p,hc))<1e-12,'critical equality')

for p in (.1,.3,.5,.9):
 for d in (.2,1,2):
    c=onset_m(p,d)
    for h in (.1,1,4):
        check(gain_from_formula(c,d,p,h)<0,'at surface-critical mean deeper layers lose')
        check(critical_m(p,d,h)>c,'positive optical depth raises cutoff')

# symmetric special case m=s, d=2*delta and p=.5
for delta in (.15,.7,1.6,2.2):
    for h in (.1,.5,2,6):
        crit=critical_m(.5,2*delta,h)
        a=math.exp(-h)
        explicit=(2/(1-a))*math.log(math.sinh(delta/2)/math.sinh(a*delta/2))
        check(abs(crit-explicit)<1e-10, 'explicit symmetric critical mean')
    c=onset_m(.5,2*delta)
    check(abs(c-delta/math.tanh(delta/2))<1e-10,'coth onset')

# high mean asymptotic: h_crit = m/2 - .5 log(2J/(p(1-p)d^2)) + o(1).
for p,d in ((.2,1),(.5,2),(.8,.5)):
    for m in (15,25,35):
        hc=find_hc(m,p,d)
        approx=m/2-.5*math.log(2*j(p,d)/(p*(1-p)*d*d))
        check(abs(hc-approx)<.02,'high-light asymptotic')

print('PASS',checks,'diagnostic assertions')
print('Example p=1/2, delta=1, m=3:', 'm_onset=',onset_m(.5,2),'h_crit=',find_hc(3,.5,2))
print('Example p=.3, difference=2, mean=3:', 'm_onset=',onset_m(.3,2),'h_crit=',find_hc(3,.3,2))
