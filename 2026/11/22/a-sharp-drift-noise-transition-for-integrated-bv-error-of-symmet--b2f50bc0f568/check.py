"""Numerical spot checks for the symmetric Stancu sampling theorem.
Run: python stancu_check.py (requires scipy and numpy).
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import binom
from scipy.special import betainc

C = math.sqrt(2/math.pi)

def beta_abs(k,n,s):
    if k == 0: return s
    if k == n+1: return 1-s
    mu=k/(n+1)
    return mu-s+2*(s*betainc(k,n-k+1,s)-mu*betainc(k+1,n-k+1,s))

def sharp(n,b):
    beta=b*math.sqrt(n)
    scores=[]
    for j in range(n+1):
        s=(j+beta/2)/(n+beta)
        scores.append((max(beta_abs(j,n,s),beta_abs(j+1,n,s)),j,s))
    return max(scores)

def numeric_response(n,b,j,which):
    beta=b*math.sqrt(n)
    s=(j+beta/2)/(n+beta)
    k=j+which
    if k==0: return s
    if k==n+1:return 1-s
    val=quad(lambda x: binom.sf(k-1,n,x),0,s,epsabs=2e-10)[0]
    val+=quad(lambda x: binom.cdf(k-1,n,x),s,1,epsabs=2e-10)[0]
    return val

for n in [2,3,7,13,29]:
    for b in [0.0,0.5,0.8,1.5]:
        for j in sorted(set([0,n//3,n//2,n])):
            s=(j+b*math.sqrt(n)/2)/(n+b*math.sqrt(n))
            for d in [0,1]:
                calc=beta_abs(j+d,n,s)
                via=numeric_response(n,b,j,d)
                assert abs(calc-via)<5e-10,(n,b,j,d,calc,via)
print('BETA_VS_DIRECT_BINOMIAL_STEP_INTEGRALS_PASS')
for b in [0,.4,.7,.79,.80,1.,2.]:
    target=max(C,b)/2
    seq=[math.sqrt(n)*sharp(n,b)[0] for n in [200,1000,4000]]
    print('b',b,'target',round(target,8),'n=200/1000/4000',[round(x,8) for x in seq], 'argmax_s',round(sharp(4000,b)[2],5))
    assert abs(seq[-1]-target)<0.035,(b,seq,target)
print('PHASE_TRANSITION_ASYMPTOTICS_PASS')
