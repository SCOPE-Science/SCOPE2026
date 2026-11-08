#!/usr/bin/env python3
"""Exact finite-stage checks and scalar inequalities for the Cantor–Bergman theorem.
Use Python 3 standard library only. Finite computations corroborate the written proof.
"""
from fractions import Fraction as Q
import math
checks = 0
def check(condition, explanation):
    global checks
    checks += 1
    if not condition: raise AssertionError(explanation)
# Exact Jensen certificate: no floating point used.
jset = (0,2,6,8)
lower = sum((1/(1+Q(j)+Q(1,6))**2 + 1/(1+Q(j)+Q(5,6))**2)/2 for j in jset)
check(lower == Q(253146344807189721168,402458387931340458025),'exact Jensen sum')
check(lower > Q(629,1000),'vacuum lower bound')
# Conservative inequalities (verified numerically, backed by elementary series in proof).
delta = math.log(2)/math.log(3)
check(0.6309 < delta < 0.6310,'Cantor dimension interval')
check(3.14159 < math.pi < 3.14160,'pi interval')
# Rigorous alternating-Taylor sine enclosure from rational endpoint bounds.
x_lo=Q(314159,100000)*(1-Q(6310,10000))
x_hi=Q(314160,100000)*(1-Q(6309,10000))
sin_lower=x_lo-x_hi**3/6+x_lo**5/120-x_hi**7/5040
check(sin_lower>Q(915,1000),'rational sine lower bound')
check(math.sin(math.pi*delta)>.915,'independent sine numerical check')
# The exact rational upper bound on J_1 uses monotonicity of d^2(1-d)
# for 0<d<2/3 and the preceding sin lower bound.
j1_upper=Q(314160,100000)*Q(6310,10000)**2*(1-Q(6310,10000))/Q(915,1000)
check(j1_upper<Q(505,1000),'rational beta-integral upper bound')
j1 = math.pi*delta**2*(1-delta)/math.sin(math.pi*delta)
j2=(1+delta)*j1/2
a1=(8/27)*2**(-delta)
q1=(2*delta/(delta+1))*2**(-1-delta)/(1.5**3)
check(j1<.505 and j2<.412,'beta integral bound')
check(a1<.192 and q1>.073,'first-mode bounds')
check(a1+j1-q1<.624,'first-mode upper threshold')
check(Q(3,16)+Q(412,1000)<Q(600,1000),'higher-mode upper threshold')
# Independent exact finite-stage spectral integration in each ternary component.
for m in range(1,6):
    s=3**m
    ternary=[0]
    for _ in range(2*m):
        ternary=[3*v+d for v in ternary for d in (0,2)]
    # g_k(t)dt integrates to (t/(1+t))^(k+1).
    L=[]
    for k in range(5):
        exact=sum((Q(q+1,s+q+1)**(k+1)-Q(q,s+q)**(k+1)) for q in ternary)*Q(3,2)**m
        L.append(exact)
        check(exact>0,'positive eigenvalue')
    if m>=2:
        check(L[0]>lower,'finite-stage vacuum bound')
        check(all(L[0]>e for e in L[1:]),'finite-stage first modes')
    print('m=',m,'normalized eigenvalues=',[round(float(e),9) for e in L])
print('CANTOR_BERGMAN_CHECKS_PASS',checks)
