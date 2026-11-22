#!/usr/bin/env python3
"""Exact finite witness and 16-state transfer checks for a theorem on self-looped symmetric forests."""
from itertools import combinations, product


def forest(n, edges):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for a, b in edges:
        ra, rb = root(a), root(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def agree_by_semantics(n, edges, loops):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    candidates = []
    for mask in range(1 << n):
        members = {i for i in range(n) if mask & (1 << i)}
        if members & loops or any(u in members and v in members for u,v in edges):
            continue
        # Check defense explicitly, not by using symmetry in the implementation.
        attacks = {v for u in members for v in adj[u]}
        attackers = {u for v in members for u in adj[v]} | (members & loops)
        if not attackers <= attacks:
            continue
        stable = all(v in members or v in attacks for v in range(n))
        candidates.append((members, stable))
    preferred = [(s, good) for s, good in candidates
                 if not any(s < other for other,_ in candidates)]
    return all(good for _, good in preferred)


def agree_by_local_condition(n, edges, loops):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    unlooped = set(range(n)) - loops
    forced = {u for u in unlooped if not (adj[u] & unlooped)}
    return all(bool(adj[s] & forced) for s in loops)


def good_path(bits):
    n=len(bits)
    unlooped={i for i,x in enumerate(bits) if x == 0}
    forced={u for u in unlooped
            if (u == 0 or bits[u-1] == 1)
            and (u == n-1 or bits[u+1] == 1)}
    return all(i == 0 and 1 in forced or i > 0 and i-1 in forced
               or i+1 in forced for i,x in enumerate(bits) if x == 1)

# Independent exhaustive comparison with Dung semantics, on every labelled
# simple forest of order <=5 with every choice of self-attacking vertices.
forests = marks = 0
for n in range(6):
    possibilities=list(combinations(range(n), 2))
    for bits in product((0,1),repeat=len(possibilities)):
        edges=[e for e,k in zip(possibilities,bits) if k]
        if not forest(n,edges):
            continue
        forests += 1
        for mask in range(1<<n):
            S={i for i in range(n) if mask & (1<<i)}
            assert agree_by_semantics(n,edges,S) == agree_by_local_condition(n,edges,S)
            marks+=1

# 16-state exact transfer, in lexicographic binary-state order.
states=list(product((0,1),repeat=4))
index={s:i for i,s in enumerate(states)}

def permitted(a,b,c,d,e):
    return c==0 or (b==0 and a==1) or (d==0 and e==1)

T=[[0]*16 for _ in range(16)]
for i,s in enumerate(states):
    for e in (0,1):
        if permitted(*s,e):
            T[i][index[s[1:]+(e,)]]+=1
B=[int(permitted(*s,1) and permitted(*s[1:],1,1)) for s in states]
# Note: s[1:] gives (b,c,d), and the two-step check is (b,c,d,1,1).
assert B==[1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0]
alpha=[int(s[:2]==(1,1)) for s in states]

def matvec(x):
    return [sum(T[i][j]*x[j] for j in range(16)) for i in range(16)]

v0=B; v1=matvec(v0);v2=matvec(v1);v3=matvec(v2)
v4=matvec(v3);v5=matvec(v4)
assert [v5[i]-v4[i]-v3[i]+v1[i]-v0[i] for i in range(16)] == [0]*16

# From P(T)B=0 follows the fifth-order recurrence at every order >=7.
F=[1,1]
v=B
for n in range(2,45):
    F.append(sum(alpha[i]*v[i] for i in range(16)))
    v=matvec(v)
assert F[:13]==[1,1,3,3,6,9,13,22,32,51,79,121,190]
for n in range(7,len(F)):
    assert F[n] == F[n-1]+F[n-2]-F[n-4]+F[n-5]
for n in range(15):
    assert F[n]==sum(good_path(w) for w in product((0,1),repeat=n))
# Exact characteristic polynomial via the Faddeev-LeVerrier identity.
def matmul(A,C):
    return [[sum(A[i][k]*C[k][j] for k in range(16)) for j in range(16)]
            for i in range(16)]
ident=[[int(i==j) for j in range(16)] for i in range(16)]
M=[r[:] for r in ident]
coeff=[1]
for k in range(1,17):
    TM=matmul(T,M)
    trace=sum(TM[i][i] for i in range(16))
    assert trace % k==0
    ck=-trace//k
    coeff.append(ck)
    for i in range(16):
        TM[i][i]+=ck
    M=TM
assert coeff == [1,-1,-1,0,1,-1]+[0]*11

# One aperiodic nontrivial strongly connected component, all others transient.
reach=[[bool(T[i][j]) or i==j for j in range(16)] for i in range(16)]
for k in range(16):
    for i in range(16):
        for j in range(16):
            if reach[i][k] and reach[k][j]:reach[i][j]=True
core={0,1,2,4,5,6,8,9,10,11,13}
assert all(reach[i][j] and reach[j][i] for i in core for j in core)
assert not any(reach[i][j] and reach[j][i] for i in core for j in set(range(16))-core)
assert T[0][0] == 1  # cycle length one in the irreducible core
assert all(T[i][i]==0 for i in set(range(16))-core)
print('VERIFY_OK forests=%d loop_markings=%d path_orders=0..14 transfer_order=44 exact_PTB=zero' % (forests,marks))
print('FIRST',F[:18])
