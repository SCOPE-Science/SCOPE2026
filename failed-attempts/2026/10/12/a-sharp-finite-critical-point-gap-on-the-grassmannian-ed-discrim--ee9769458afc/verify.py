#!/usr/bin/env python3
from math import comb

def C(n, k):
    if k < 0 or k > n:
        return 0
    return comb(n, k)

# Exact arithmetic for the symmetric nilpotent witness N=[[i,1],[1,-i]].
# Represent a+bi as (a,b).
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
ZERO=(0,0); ONE=(1,0); I=(0,1); MINUS_I=(0,-1)
N=[[I,ONE],[ONE,MINUS_I]]
assert N[0][1] == N[1][0]
N2=[[ZERO,ZERO],[ZERO,ZERO]]
for r in range(2):
    for c in range(2):
        s=ZERO
        for j in range(2):
            s=add(s,mul(N[r][j],N[j][c]))
        N2[r][c]=s
assert N2 == [[ZERO,ZERO],[ZERO,ZERO]]
assert N != [[ZERO,ZERO],[ZERO,ZERO]]

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part=n
    for p in range(max_part,0,-1):
        for rest in partitions(n-p,p):
            yield (p,)+rest

def coefficient(part, k):
    dp=[0]*(k+1)
    dp[0]=1
    for s in part:
        for j in range(k, s-1, -1):
            dp[j] += dp[j-s]
    return dp[k]

for n in range(2,19):
    all_ones=(1,)*n
    for k in range(1,n):
        target=C(n-2,k)+C(n-2,k-2)
        for part in partitions(n):
            if part == all_ones:
                continue
            assert coefficient(part,k) <= target, (n,k,part,coefficient(part,k),target)
        assert target == C(n,k)-2*C(n-2,k-1)

# Direct coefficientwise split test:
# (1+x^a)(1+x^b) = (1+x^(a+b)) + x^a + x^b.
for a in range(1,8):
    for b in range(1,8):
        m=a+b
        lhs=[0]*(m+1)
        rhs=[0]*(m+1)
        lhs[0]=1; lhs[a]+=1; lhs[b]+=1; lhs[m]+=1
        rhs[0]=1; rhs[m]=1
        assert all(lhs[j] >= rhs[j] for j in range(m+1))
        diff=[lhs[j]-rhs[j] for j in range(m+1)]
        expected=[0]*(m+1)
        expected[a]+=1
        expected[b]+=1
        assert diff == expected

print("witness_symmetric_nilpotent=OK")
print("partition_extremum_stress_n<=18=OK")
print("binomial_gap_identity=OK")
print("coefficientwise_refinement=OK")
print("VERIFY_OK")
