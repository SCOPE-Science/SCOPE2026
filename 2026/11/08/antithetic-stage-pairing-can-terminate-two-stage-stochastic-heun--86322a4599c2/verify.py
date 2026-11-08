"""Exact-arithmetic regression checks for a two-stage finite-sum gradient update.

Run with: python3 verify.py
These finite checks supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product

count = 0

def check(ok, what):
    global count
    assert ok, what
    count += 1

def amplification(u, v):
    return 1 - (u+v)/2 + u*v/2

def moments(t, d, mismatch_probability):
    low = t*(1-d)
    high = t*(1+d)
    same = (amplification(low,low)**2 + amplification(high,high)**2)/2
    different = amplification(low,high)**2
    return (1-mismatch_probability)*same + mismatch_probability*different

# Fundamental exact identities for all rational test points.
for t in [Q(i,8) for i in range(1,49)]:
    for d in [Q(j,10) for j in range(1,10)]:
        low = t*(1-d)
        high = t*(1+d)
        same = (amplification(low,low)**2+amplification(high,high)**2)/2
        mixed = amplification(low,high)**2
        delta = d*d*t*t*(2*t*t-4*t+3)
        check(same - mixed == delta,"factorization")
        check(delta>0,"strict ordering")
        check(moments(t,d,Q(0))==same,"same-sample coupling")
        check(moments(t,d,Q(1,2))==(same+mixed)/2,"independent coupling")
        check(moments(t,d,Q(1))==mixed,"antithetic coupling")
        for mismatch in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            check(moments(t,d,mismatch)==mixed+(1-mismatch)*delta,"affine coupling law")
# Rational exact termination and separation example.
a,b,h=Q(2,7),Q(12,7),Q(7,3)
u,v=h*a,h*b
check((u,v)==(Q(2,3),Q(4)),"example curvatures")
check(amplification(u,v)==0 and amplification(v,u)==0,"antithetic annihilation")
check(amplification(u,u)==Q(5,9),"same low")
check(amplification(v,v)==Q(5),"same high")
check(moments(h,Q(5,7),Q(0))==Q(1025,81),"shared risk")
check(moments(h,Q(5,7),Q(1,2))==Q(1025,162),"iid risk")
check(moments(h,Q(5,7),Q(1))==Q(0),"antithetic risk")
check(1-h+h*h/2==Q(25,18),"full gradient deterministic Heun amplification")
# Enumerate every length-3 two-stage oracle history for each extremal coupling.
for q in [Q(0),Q(1,2),Q(1)]:
    pair_probs = {(u,u):(1-q)/2,(v,v):(1-q)/2,
                  (u,v):q/2,(v,u):q/2}
    for k in range(1,4):
        exact = Q(0)
        for history in product(pair_probs.items(),repeat=k):
            prob=Q(1)
            amp=Q(1)
            for (ua,ub),p in history:
                prob *= p
                amp *= amplification(ua,ub)
            exact += prob*amp**2
        check(exact==moments(h,Q(5,7),q)**k,"finite epoch second-moment product")
print(f"PASS: {count} exact checks")
