"""Exact-rational finite-prefix checks for unilateral contraction-shift orbit frame energy identities.
Finite checks corroborate algebra only. Infinite statements use the mathematical proof.
"""
from fractions import Fraction as F
from itertools import product

def calc(w2, cutoff):
    # w2 = squared weights, eventually equal 1; canonical finite-prefix and tail booster.
    n=len(w2)
    p2=F(1)
    for a in w2[cutoff+1:]: p2*=a
    booster = F(1)/p2 - w2[cutoff]
    assert booster>=0
    q=[F(0)]*(n+1)
    q[0]=F(1)
    for j in range(cutoff):q[j+1]=1-w2[j]
    q[cutoff+1]+=booster
    s=[]
    for k in range(n+1):
        if k==0:s.append(q[0])
        else:s.append(w2[k-1]*s[-1]+q[k])
    assert all(x>=1 for x in s)
    assert all(s[k]==1 for k in range(cutoff+1))
    assert s[n]==1
    E=sum(q)
    minimum=F(1)+sum(1-x for x in w2)
    assert E>=minimum
    tail=sum(1-x for x in w2[cutoff+1:])
    assert E-minimum==F(1)/p2-F(1)-tail
    # identity for diagonal Stein equation at each finite coordinate
    assert all(q[k]==s[k]-(w2[k-1]*s[k-1] if k else 0) for k in range(n+1))
    return 7

checks=0
pool=[F(1),F(2,3),F(3,4),F(5,6)]
for length in range(1,7):
    for w2 in product(pool,repeat=length):
        for cutoff in range(length):
            checks+=calc(list(w2),cutoff)
# nontrivial infinite tail family squared weights 1-1/(n+2)^2
for N in range(200):
    t=F(N+2,N+3)  # infinite squared tail product after edge N
    w2=F((N+1)*(N+3),(N+2)**2)
    booster=1/t-w2
    assert booster==F(N+3,(N+2)**2)
    # the positive gap to the infinite minimum is the positive higher-order tail correction
    assert booster>=0
    checks+=2
# vanishing product test example: w_j^2=(j+1)/(j+2)
for N in range(1,200):
    prod=F(1,N+1)
    direct=F(1)
    for j in range(N):direct*=F(j+1,j+2)
    assert prod==direct
    checks+=1
print('SHIFT_ORBIT_ENERGY_EXACT_OK',checks)
