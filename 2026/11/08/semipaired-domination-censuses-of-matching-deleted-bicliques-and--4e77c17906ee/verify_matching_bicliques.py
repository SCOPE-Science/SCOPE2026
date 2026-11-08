#!/usr/bin/env python3
"""Independent direct graph checks of semipaired domination enumerators.

Finite checks corroborate, and do not replace, the combinatorial proof.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from math import comb


def B(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(a, b, t):
    A = Counter({j: B(a, j) for j in range(2, a+1)})
    Bp = Counter({j: B(b, j) for j in range(2, b+1)})
    D = Counter()
    for k, v in A.items():
        for l, w in Bp.items():
            D[k+l] += v*w
    for k, v in Bp.items(): D[k+1] += (a-t)*v
    for k, v in A.items(): D[k+1] += (b-t)*v
    for k in range(1, b): D[k+2] += t*B(b-1, k)
    for k in range(1, a): D[k+2] += t*B(a-1, k)
    D[2] += (a-t)*(b-t)+t
    D[a] += 1
    D[b] += 1
    S = Counter({k: v for k, v in D.items() if k % 2 == 0})
    S[2] -= t
    if S[2]==0: del S[2]
    q4 = B(t,2)*B(b,2)+B(a,2)*B(t,2)-B(t,2)**2
    q4 += t*(B(a-1,2)+B(b-1,2)) + (a+b-2*t)*B(t,3)
    q4 += (a==4)+(b==4)
    M = Counter()
    if (a-t)*(b-t): M[2] += (a-t)*(b-t)
    M[4] += q4
    if a>=6 and a%2==0: M[a] += 1
    if b>=6 and b%2==0: M[b] += 1
    if M[4]==0: del M[4]
    return D, S, M


def direct(a,b,t):
    n=a+b
    adj = [0]*n
    for i in range(a):
        for j in range(b):
            if i==j and i<t: continue
            adj[i] |= 1<<(a+j)
            adj[a+j] |= 1<<i
    compat = [0]*n
    for root in range(n):
        dist=[n+10]*n; dist[root]=0
        q=deque([root])
        while q:
            v=q.popleft()
            for w in range(n):
                if (adj[v]>>w)&1 and dist[w]>dist[v]+1:
                    dist[w]=dist[v]+1;q.append(w)
        for v in range(n):
            if v!=root and dist[v]<=2: compat[root] |= 1<<v
    @lru_cache(None)
    def match(S):
        if not S:return True
        bit=S&-S;v=bit.bit_length()-1
        rest=S^bit
        options=rest&compat[v]
        while options:
            qbit=options&-options
            if match(rest^qbit):return True
            options ^= qbit
        return False
    full=(1<<n)-1
    def dominates(S):
        for v in range(n):
            if not ((S>>v)&1) and not (adj[v]&S): return False
        return True
    semipaired=set()
    D=Counter();S=Counter();M=Counter()
    for mask in range(1,1<<n):
        k=mask.bit_count()
        if dominates(mask):
            D[k]+=1
            if k%2==0 and match(mask):
                semipaired.add(mask);S[k]+=1
    # Inclusion minimal = no proper semipaired subset, not merely one deletion.
    for mask in semipaired:
        sub=(mask-1)&mask
        minimal=True
        while sub:
            if sub in semipaired:
                minimal=False;break
            sub=(sub-1)&mask
        if minimal:M[mask.bit_count()] += 1
    return D,S,M,(1<<n)-1


def run():
    cases=[]
    for a in range(3,6):
        for b in range(3,6):
            for t in range(min(a,b)+1):cases.append((a,b,t))
    cases += [(3,6,t) for t in range(4)]
    cases += [(4,6,t) for t in range(5)]
    cases += [(6,6,t) for t in range(7)]
    cases += [(3,7,3),(3,8,3),(4,7,4),(5,6,5)]
    total=0
    for a,b,t in cases:
        expected=predicted(a,b,t)
        D,S,M,cnt=direct(a,b,t)
        total+=cnt
        actual=[D,S,M]
        for i,(x,y) in enumerate(zip(actual,expected)):
            assert (+x)==(+y),f'{(a,b,t)} distribution {i} actual {x} predicted {y}'
    print('VERIFY_OK instances=%d subsets=%d all_domination_semipaired_minimal_polynomials=PASS'%(len(cases),total))

if __name__=='__main__':run()
