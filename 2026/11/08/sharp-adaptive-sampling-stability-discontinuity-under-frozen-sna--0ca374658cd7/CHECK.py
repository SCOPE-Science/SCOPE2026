"""Exact reproducible checks for the frozen-snapshot Kaczmarz theorem.
Run with Python 3: python CHECK.py; uses only the standard library.
These finite tests corroborate, but do not substitute for, the all-dimension proof.
"""
from fractions import Fraction as F
from itertools import product
from math import exp, log, isclose

checks = 0

def require(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

for m in range(2, 5):
    for T in range(1, 5 if m <= 3 else 3):
        for beta in [F(1, 4), F(1, 2), F(3, 4), F(1), F(2)]:
            for ell in [0, 1, 2]:
                for x0 in product([F(0), F(1), F(2)], repeat=m):
                    if all(x == 0 for x in x0):
                        continue
                    weights = [abs(x)**ell for x in x0] if ell else [F(1) for _ in x0]
                    sw = sum(weights)
                    probs = [w/sw for w in weights]
                    e2 = sum(x*x for x in x0)
                    a = sum(p*x*x for p,x in zip(probs,x0))
                    b = sum(p*(1+(T-1)*p)*x*x for p,x in zip(probs,x0))
                    calculated = e2-2*beta*T*a+beta*beta*T*b
                    exact = F(0)
                    for seq in product(range(m),repeat=T):
                        prob = F(1)
                        counts = [0]*m
                        for i in seq:
                            prob *= probs[i]
                            counts[i] += 1
                        resulting = sum(x*x*(1-beta*counts[i])**2 for i,x in enumerate(x0))
                        exact += prob*resulting
                    require(exact==calculated, (m,T,beta,ell,x0,exact,calculated))
                    if ell==0:
                        q = 1-beta*T/F(m)*(2-beta*(1+F(T-1,m)))
                        require(exact == q*e2, (m,T,beta,x0))
                    if ell>0 and beta*T<2:
                        q = 1-beta*T/F(m)*(2-beta*T)
                        require(exact<=q*e2, (m,T,beta,ell,x0,exact,q*e2))

# Independent check of the positive-probability all-collision event.
for T in (3, 4, 5):
    beta=1
    growth=abs(1-beta*T)
    for ell in (0.25, 0.5, 1.0, 2.0):
        for c in (0.01, 0.5, 3.0, 10.0):
            lower=exp(-T*c/(1-growth**(-ell)))
            log_prod=-T*sum(log(1+c*growth**(-ell*k)) for k in range(400))
            require(log_prod+1e-12>=log(lower), (T,ell,c,log_prod,lower))
            require(log_prod<0, (T,ell,c,log_prod))

print(f'PASS: {checks} exact-enumeration and collision-product assertions')
