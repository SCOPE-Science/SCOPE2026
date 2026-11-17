#!/usr/bin/env python3
"""Dependency-free integer Newton identity certificate for a clock transfer."""
from itertools import product
N = 81
letters = tuple(product(range(3), repeat=2))
adj = [[] for _ in range(N)]
for a,b,c in product(range(9),repeat=3):
    left,cur,right=letters[a],letters[b],letters[c]
    # Check both vertices of the middle column, using separate boolean clauses.
    ok = True
    for r in range(2):
        target=(cur[r]+1)%3
        if not(any(e==target for e in left)
                or any(e==target for e in right)
                or cur[1-r]==target):
            ok=False
    if ok:
        adj[9*a+b].append(9*b+c)

# P <- P*T, starting from I. Each step is wholly integer arithmetic.
P=[[int(i==j) for j in range(N)] for i in range(N)]
traces=[0]
for k in range(1,N+1):
    new=[[0]*N for _ in range(N)]
    for i in range(N):
        row=P[i]
        out=new[i]
        for j in range(N):
            v=row[j]
            if v:
                for h in adj[j]: out[h]+=v
    P=new
    traces.append(sum(P[i][i] for i in range(N)))

# Newton identities for monic characteristic polynomial.
coefs=[1]
for k in range(1,N+1):
    num=sum(coefs[k-i]*traces[i] for i in range(1,k+1))
    assert num%k==0
    coefs.append(-num//k)
# Multiply x^74 (x^2+3x+9)^2 (x^3-6x^2-9x-18)
poly=[1]
for f in ([1,3,9],[1,3,9],[1,-6,-9,-18]):
    p=[0]*(len(poly)+len(f)-1)
    for i,a in enumerate(poly):
        for j,b in enumerate(f):p[i+j]+=a*b
    poly=p
poly += [0]*74
assert len(poly)==N+1
assert coefs==poly, (coefs,poly)
print('certificate_method=Newton_identites_of_all_81_exact_traces')
print('matrix_dimension=',N,'edge_count=',sum(map(len,adj)))
print('nonzero_coefficients=',[(i,c) for i,c in enumerate(coefs) if c])
for n in range(3,11): print('n=',n,'three_clock_states=',traces[n])
print('all_charpoly_coefficients_verified=true')
