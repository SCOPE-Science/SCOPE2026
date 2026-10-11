#!/usr/bin/env python3
from itertools import combinations
from math import comb, gcd

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def ppow(a,n):
    out=[1]
    for _ in range(n): out=conv(out,a)
    return out

def A(s):
    out=[0]*(s+1)
    for j in range(2,s+1,2): out[j]=comb(s,j)
    return out

def B(s):
    out=[0]*(2*s+1)
    for j in range(1,s+1): out[2*j]=comb(s,j)**2
    return out

def formula(q,s,char2):
    return ppow(A(s),q) if char2 else conv(A(s), ppow(B(s),(q-1)//2))

def reconstruct(P):
    nz=[i for i,c in enumerate(P) if c]
    order=nz[0]; deg=nz[-1]; lc=P[deg]
    if lc==1:
        q=order//2; s=deg//q; c2=True
    else:
        s=lc; q=order-1; c2=False
        assert deg+1==q*s
    return q,s,c2

def perfect_matching(S,adj):
    S=set(S)
    if not S: return True
    if len(S)%2: return False
    v=next(iter(S))
    for u in sorted(adj[v]&S):
        if perfect_matching(S-{v,u},adj): return True
    return False

def brute_ring_Zn(n):
    V=list(range(n))
    Z={a for a in V if a==0 or gcd(a,n)>1}
    adj=[set() for _ in V]
    for i,a in enumerate(V):
        for j in range(i+1,n):
            b=V[j]
            if (a+b)%n in Z:
                adj[i].add(j); adj[j].add(i)
    P=[0]*(n+1)
    for mask in range(1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        if not all(v in S or bool(adj[v]&S) for v in range(n)): continue
        if perfect_matching(S,adj): P[len(S)]+=1
    return P

for n,q,s,c2 in [(4,2,2,True),(8,2,4,True),(9,3,3,False)]:
    got=brute_ring_Zn(n)
    want=formula(q,s,c2)
    assert got==want,(n,got,want)
    assert reconstruct(want)==(q,s,c2)

# Structural profiles beyond brute ring enumeration.
for q,s,c2 in [(4,4,True),(8,8,True),(3,9,False),(5,5,False),(7,7,False)]:
    P=formula(q,s,c2)
    assert reconstruct(P)==(q,s,c2)

print('VERIFY_OK')
print('actual_rings=Z4,Z8,Z9')
print('bruteforce_subsets=16,256,512')
print('additional_profiles=(4,4,char2),(8,8,char2),(3,9,odd),(5,5,odd),(7,7,odd)')
print('reconstruction_from_lowest_degree_and_leading_coefficient=passed')
