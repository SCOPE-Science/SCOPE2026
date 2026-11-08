#!/usr/bin/env python3
"""Reproduce the unit residue for m-ary partitions at m^r - 1 (stdlib)."""
from math import comb, gcd

cases = [(5,9), (7,7), (11,5), (13,5), (25,4), (35,3), (49,3)]
checks = 0
for m, max_r in cases:
    N = m**max_r
    mod = m**(max_r + 1)
    b = [1]*N
    for n in range(m, N):
        b[n] = (b[n-1] + (b[n//m] if n%m == 0 else 0))%mod
    for r in range(2, max_r+1):
        value = b[m**r - 1]
        unit = (value//m**(r-1)) % m
        target = pow((m+1)//2, r-2, m)
        assert value%m**(r-1) == 0
        assert unit == target, (m,r,unit,target)
        assert gcd(unit,m) == 1
        checks += 1
    print(f'm={m}: r=2..{max_r} verified')

# Independent construction via coin-change generating function (full exact counts).
for m, r in [(5,4),(7,4),(11,3),(25,3)]:
    N = m**r-1
    ways = [0]*(N+1)
    ways[0] = 1
    t=1
    while t<=N:
        for n in range(t,N+1):
            ways[n] += ways[n-t]
        t*=m
    value=ways[N]
    assert value % m**r == (m**(r-1)*pow((m+1)//2,r-2,m))%m**r
    print(f'coin-DP: m={m}, r={r}, value_mod={value%m**r}')

# Check the coefficient identity used in the proof at sampled indices.
for m in [5,7,11,25]:
    for s in range(2,8):
        # Integral falling-difference formula from n=-j, as in cited lemma.
        al=[0]*(s+1)
        for j in range(1,s+1):
            # Generalized binomial for negative top: binom(-u,s)=(-1)^s binom(u+s-1,s).
            from math import comb
            lhs=(-1)**s*comb(m*j, s) if m*j>=s else 0
            # identity: binom(-mj+s-1,s)=(-1)^s * binom(mj,s)
            rhs=sum(al[i]*((-1)**i)*comb(j,i) for i in range(1,j))
            al[j]=((-1)**j)*(lhs-rhs)
        assert al[s]==m**s
        assert al[s-1]==-(s-1)*(m-1)*m**(s-1)//2
        for n in (1,2,3,5):
            assert comb(m*n+s-1,s)==sum(al[i]*comb(n+i-1,i) for i in range(1,s+1))
        if s==3:
            assert al[1] == m*(m-1)*(m-2)//6
        if s==2:
            assert al[1] == -m*(m-1)//2
print('binomial change-of-basis checks: PASS')
print(f'ALL_CHECKS_PASS: {checks} m-adic unit residues, four exact coin-DP checks, 24 integer polynomial identities')
