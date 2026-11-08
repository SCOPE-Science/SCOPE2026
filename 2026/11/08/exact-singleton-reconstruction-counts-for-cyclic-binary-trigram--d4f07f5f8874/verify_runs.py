"""Independent run-necklace and rational-series checks.

Run: python3 verify_runs.py
"""
from itertools import combinations
from math import comb

def compositions(s, k):
    if k == 1:
        yield (s,)
        return
    for cuts in combinations(range(1, s), k - 1):
        vals = tuple(b - a for a, b in zip((0,)+cuts, cuts+(s,)))
        yield vals

def cyclic_orbit(v):
    return {v[i:]+v[:i] for i in range(len(v))}

def expected_individual(k,s,a):
    j=k-a
    if k==1:
        return True
    if j==0:
        return s==k
    if s<a+2*j:
        return False
    e=s-(a+2*j)
    return j==1 or (j==k and e in (0,1)) or (j==k-1 and e==0)

# Check individual transitivity without relying on the counting formula.
for k in range(1, 8):
    for s in range(k, 18):
        by_a={}
        for v in compositions(s,k):
            a=v.count(1)
            by_a.setdefault(a, []).append(v)
        for a,seq in by_a.items():
            actual = len(cyclic_orbit(seq[0])) == len(seq)
            assert actual == expected_individual(k,s,a), (k,s,a,actual)
            if actual:
                assert cyclic_orbit(seq[0]) == set(seq)
print('RUN_TRANSITIVITY_OK')

# A profile is a pair of run-length vectors modulo simultaneous rotation.
# Compare the direct cyclic orbit test with the one-rigid-side condition.
for k in range(2, 6):
    for zs in range(k, min(13,2*k+5)):
        zby={}
        for z in compositions(zs,k): zby.setdefault(z.count(1),[]).append(z)
        for os in range(k,min(13,2*k+5)):
            oby={}
            for o in compositions(os,k):oby.setdefault(o.count(1),[]).append(o)
            for az,Z in zby.items():
                for ao,O in oby.items():
                    # If the number of pairs exceeds k, transitivity is impossible.
                    if len(Z)*len(O)>k: actual=False
                    else:
                        first=(Z[0],O[0]); orbit=set()
                        for i in range(k):
                            orbit.add((first[0][i:]+first[0][:i],first[1][i:]+first[1][:i]))
                        actual=len(orbit)==len(Z)*len(O)
                    rigid_z=len(Z)==1
                    rigid_o=len(O)==1
                    predicted=(rigid_z and expected_individual(k,os,ao)) or (rigid_o and expected_individual(k,zs,az))
                    assert actual==predicted, (k,zs,os,az,ao)
print('PAIRED_TRANSITIVITY_OK')

# Count coefficients two independent ways: direct composition of rigid/flexible
# descriptor classes, and a polynomial rational-function recurrence.
limit=120
nmax=limit
coeff=[0]*(nmax+1)
for n in range(1,nmax+1):coeff[n]+=2
for n in range(2,nmax+1):coeff[n]+=n-1
for k in range(2,nmax+1):
    R=[k,2*k]
    F=[k+1+j for j in range(0,max(0,nmax-k))]
    if k>=3:F.append(2*k-1)
    F.append(2*k+1)
    for a in R:
        for b in R:
            if a+b<=nmax:coeff[a+b]+=1
        for b in F:
            if a+b<=nmax:coeff[a+b]+=2

# Numerator of the proposed closed rational function, ascending powers.
p={1:2,2:3,3:4,4:4,5:3,6:5,7:6,8:7,9:5,11:-1,12:-4,14:-2}
recur=[0]*(nmax+1)
for n in range(1,nmax+1):
    recur[n]=p.get(n,0)+(recur[n-3] if n>=3 else 0)+(recur[n-4] if n>=4 else 0)-(recur[n-7] if n>=7 else 0)
    assert recur[n]==coeff[n],(n,recur[n],coeff[n])
print('RATIONAL_SERIES_OK')
