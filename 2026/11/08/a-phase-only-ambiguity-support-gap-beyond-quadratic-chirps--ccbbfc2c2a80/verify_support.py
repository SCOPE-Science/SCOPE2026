#!/usr/bin/env python3
"""Exact cyclotomic support checks for periodic phase-only self ambiguity.
No third-party packages. All zero decisions are exact integer arithmetic.
For prime p, sum of p roots of unity vanishes iff every residue
appears once in the sum; this follows from Phi_p=1+...+T^(p-1).
This independently enumerates short p-ary phase codes, not arbitrary
unimodular complex phases; the general theorem is proven analytically.
"""
from itertools import product, combinations
from collections import Counter

ASSERTIONS = 0

def check(ok, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(msg)

def iszero(p, exponents):
    bins = [0] * p
    for x in exponents:
        bins[x % p] += 1
    return len(set(bins)) == 1

def count_ambiguity(p, phase):
    byrow = []
    for delay in range(p):
        row = 0
        for freq in range(p):
            exps = [phase[t] - phase[(t-delay)%p] - freq*t for t in range(p)]
            row += not iszero(p, exps)
        byrow.append(row)
    return sum(byrow), byrow

def chirp(p, phase):
    inv2 = pow(2, -1, p)
    b_minus_a = (phase[1]-phase[0]) % p
    delta2 = (phase[2]-2*phase[1]+phase[0]) % p
    a = delta2*inv2 % p
    b = (b_minus_a - a) % p
    return all((phase[t]-phase[0]-a*t*t-b*t) % p == 0 for t in range(p))

# Exact singleton-difference witnesses for all 2/3-character supports.
for p in (5, 7, 11, 13):
    for size in (2, 3):
        for S in combinations(range(p), size):
            counts = Counter((a-b)%p for a in S for b in S if a!=b)
            check(any(m == 1 for m in counts.values()), (p,S,counts))

# Exhaustive modulo global phase for every 5th-root phase code at p=5.
from collections import defaultdict
hist = defaultdict(int)
for phases in product(range(5), repeat=4):
    phase = (0,)+phases
    s, rows = count_ambiguity(5, phase)
    c = chirp(5, phase)
    hist[s]+=1
    check((s==5)==c, ('classification',phase,s,rows))
    check(s==5 or s>=17, ('forbidden',phase,s,rows))
    check(rows[0]==1, ('zero delay',phase,s,rows))
    if not c:
        check(all(r>=4 for r in rows[1:]), ('row gap',phase,rows))
check(sum(hist.values())==625, 'phase enumeration')
sharp=(1,0,0,0,0)
s,rows=count_ambiguity(5,sharp)
check(s==17 and rows==[1,4,4,4,4], (s,rows))

# Additional exact prime-alphabet tests at p=7 and p=11, including
# non-chirps and every quadratic chirp modulo a global phase.
for p in (7, 11):
    for a in range(p):
        for b in range(p):
            phase=tuple((a*t*t+b*t)%p for t in range(p))
            s, rows=count_ambiguity(p,phase)
            check(s==p and all(r==1 for r in rows), ('chirp',p,a,b,s,rows))
    for u in range(1,p):
        for v in range(1,p):
            phase=[0]*p
            phase[0]=u
            phase[1]=v
            s,rows=count_ambiguity(p,phase)
            if not chirp(p,phase):
                check(s>=4*p-3 and all(r>=4 for r in rows[1:]), ('nonchirp',p,u,v,s,rows))
print('PHASE_AMBIGUITY_EXACT_CHECKS_PASS', ASSERTIONS, 'p5_histogram', sorted(hist.items()))
