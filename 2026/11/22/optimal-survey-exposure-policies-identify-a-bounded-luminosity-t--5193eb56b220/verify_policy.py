"""Checks for the explicit inverse-exposure theorem in a bounded-horizon survey.
Only standard-library arithmetic; numerical checks supplement the symbolic proof.
"""
from math import isclose
GAMMA=0.75

def density(t):
    return 6.0*(t-1.0)*(2.0-t) if 1 < t < 2 else 0.0

def primitive(t):
    return -2*t**3+9*t*t-12*t+5

def anti_weight(t):
    g=GAMMA
    return -6*t**(3-g)/(3-g)+18*t**(2-g)/(2-g)-12*t**(1-g)/(1-g)

def tail(t):
    return anti_weight(2.0)-anti_weight(max(1.0,min(t,2.0)))

def H(t):
    if t<=0:return 0.0
    if t>=2:return 1.0
    return (primitive(t) if t>=1 else 0.0)+t**GAMMA*tail(t)

def Hp(t):
    if t>=2:return 0.0
    return GAMMA*t**(GAMMA-1)*tail(t)

def Hpp(t):
    g=GAMMA
    return g*(g-1)*t**(g-2)*tail(t)-g*density(t)/t

def overhead(t):
    return H(t)/Hp(t)-t

def overhead_prime(t):
    return -H(t)*Hpp(t)/Hp(t)**2

def policy(tau):
    lo,hi=1e-9,2.0
    for _ in range(90):
        mid=(lo+hi)/2
        if (mid+tau)*Hp(mid)-H(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def inferred_f(t):
    v=t+overhead(t)
    return H(t)*(t*overhead_prime(t)-(1-GAMMA)*v)/(GAMMA*v*v)

def run():
    count=0
    def check(c,message):
        nonlocal count
        assert c,message
        count+=1
    check(abs(H(2)-1)<1e-14,'normalization')
    check(abs(H(.4)/(.4**GAMMA)-H(.8)/(.8**GAMMA))<1e-12,'small-t power law')
    for i in range(1,20):
        t=1+i/20
        check(abs(inferred_f(t)-density(t))<5e-10,f'inversion at {t}')
        check(t*overhead_prime(t)>(1-GAMMA)*(t+overhead(t)),f'curvature at {t}')
        check(Hpp(t)<0,f'concavity at {t}')
        check(overhead_prime(t)>0,f'monotone overhead at {t}')
    for i in range(1,16):
        t=i/16
        check(abs(overhead(t)-(1-GAMMA)/GAMMA*t)<1e-11,'below-support linear overhead')
        check(abs(inferred_f(t))<1e-11,'zero density below support')
    for tau in [0.03,0.1,0.2,0.4,0.7,1.,1.5,3.,6.,10.,25.,100.]:
        t=policy(tau)
        check(abs(overhead(t)-tau)<1e-7,f'optimality equation {tau}')
        check(all(H(t)/(t+tau)>=H(x)/(x+tau)-1e-11 for x in [1e-5,.05,.25,.5,.75,1,1.25,1.5,1.75,2,3,4]),'global optimum sampled')
        if tau<1/3:check(abs(t-3*tau)<1e-7,'boundary phase')
    check(abs(overhead(0.5)-(1-GAMMA)*0.5/GAMMA)<1e-12,'exact low-exposure inverse policy')
    for tau in [1000.0, 10000.0, 100000.0]:
        t=policy(tau)
        ratio=(2-t)/( (8.0/(9.0*tau))**0.5 )
        check(abs(ratio-1)<0.12, f'large-overhead endpoint law {tau}: {ratio}')
    for tau in [0.1,1.,10.]:print('overhead=',tau,'optimal dwell=',round(policy(tau),10),'detection fraction=',round(H(policy(tau)),10))
    print('PASS',count,'assertions')
if __name__=='__main__':run()
