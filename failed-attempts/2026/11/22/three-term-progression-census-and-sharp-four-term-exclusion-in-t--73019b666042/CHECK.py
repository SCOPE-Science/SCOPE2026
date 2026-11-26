#!/usr/bin/env python3
"""Exact digit-automaton and polynomial certificate for Baum–Sweet progression counts."""
from collections import deque, defaultdict

# The ten reachable states are (addition carries, zero-run parity, d_seen).
STATES = [
 ((0,0),(0,0,0),0),
 ((0,0),(1,1,1),0),
 ((0,1),(1,0,1),1),
 ((1,1),(0,1,0),1),
 ((1,1),(1,0,0),1),
 ((1,1),(0,0,1),1),
 ((0,0),(0,0,0),1),
 ((1,2),(0,0,0),1),
 ((0,0),(1,1,1),1),
 ((1,2),(1,1,1),1),
]
# Columns correspond to input bits (a,b) = (0,0),(0,1),(1,0),(1,1).
EDGES = [
 [1,2,0,3],
 [0,-1,-1,-1],
 [-1,-1,-1,-1],
 [-1,4,5,-1],
 [6,3,-1,-1],
 [-1,-1,3,7],
 [8,2,6,3],
 [2,9,3,7],
 [6,-1,-1,-1],
 [-1,7,-1,-1],
]
# P(z) = (1-z-z^2)(1-z-3z^2+2z^4), coefficients low to high.
P = [1,-2,-3,4,5,-2,-2]
# Each row is coefficients low to high of P(z)*F_i(z), where F_i is
# the generating function of accepting paths beginning at state i.
H = [
 [0,0,0,1,1],
 [0,0,0,0,1,1],
 [0],
 [0,0,1,0,-2,-1],
 [0,1,0,-3,-2,1,1],
 [0,0,0,1,1,-1,-1],
 [1,0,-4,-2,3,2],
 [0,0,0,1,1],
 [1,-1,-3,0,3,1],
 [0,0,0,0,1,1],
]

def transition(st,a,b,t=3):
    carries, parity, seen=st
    total=[a+i*b+(0 if i==0 else carries[i-1]) for i in range(t)]
    bits=[v%2 for v in total]
    if any(bit and old for bit,old in zip(bits,parity)):
        return None
    return (tuple(total[i]//2 for i in range(1,t)),
            tuple(0 if bit else 1-old for bit,old in zip(bits,parity)),
            seen|b)

def add(A,B):
    n=max(len(A),len(B));return [(A[i] if i<len(A) else 0)+(B[i] if i<len(B) else 0) for i in range(n)]

def shift(A): return [0]+A

checks=0
# Independently rediscover the transition graph, including reachability closure.
start=STATES[0]
seen={start};queue=deque([start]);graph={}
while queue:
    s=queue.popleft()
    edges=[]
    for a,b in ((0,0),(0,1),(1,0),(1,1)):
        nxt=transition(s,a,b)
        edges.append(nxt)
        if nxt is not None and nxt not in seen:
            seen.add(nxt);queue.append(nxt)
    graph[s]=edges
assert set(STATES)==seen and len(STATES)==len(set(STATES))==10
checks+=1
for i,s in enumerate(STATES):
    for j,expected in enumerate(EDGES[i]):
        actual=graph[s][j]
        assert actual==(STATES[expected] if expected>=0 else None), (i,j,actual)
        checks+=1

# Every F_i is formally determined by F_i = accept_i + z*sum_{edges i->j}F_j.
# The displayed H polynomials verify P*F_i=H_i without external symbolic software.
for i,s in enumerate(STATES):
    rhs=([x if s[2] and s[0]==(0,0) else 0 for x in P])
    for j in EDGES[i]:
        if j>=0:rhs=add(rhs,shift(H[j]))
    lhs=H[i]+[0]*(len(rhs)-len(H[i]))
    rhs=rhs+[0]*(len(lhs)-len(rhs))
    assert lhs==rhs,(i,lhs,rhs)
    checks+=1
assert H[0]==[0,0,0,1,1]

# Completely independent zero-run predicate.
def good(n):
    if n==0:return True
    return all(len(z)%2==0 for z in bin(n)[2:].split('1'))

def count_dfa(L):
    curr={start:1}
    for _ in range(L):
        nxt=defaultdict(int)
        for state,weight in curr.items():
            for a in (0,1):
                for b in (0,1):
                    x=transition(state,a,b)
                    if x is not None:nxt[x]+=weight
        curr=nxt
    return sum(v for (cs,qs,seen_d),v in curr.items() if seen_d and cs==(0,0))

# Exact GF coefficient extraction from P(z)G(z)=z^3+z^4.
def gf_coeffs(N):
    out=[]
    for k in range(N+1):
        target=int(k==3 or k==4)
        out.append(target-sum(P[j]*out[k-j] for j in range(1,min(k,len(P)-1)+1)))
    return out
coeff=gf_coeffs(24)
for L in range(25):
    assert count_dfa(L)==coeff[L],(L,count_dfa(L),coeff[L])
    checks+=1

for L in range(13):
    B=[n for n in range(1<<L) if good(n)]
    S=set(B)
    brute3=sum(1 for x in B for y in B if y>x and (2*y-x) in S)
    assert brute3==coeff[L],(L,brute3,coeff[L])
    # Four points would force x,y,2y-x,3y-2x all in the set.
    brute4=sum(1 for x in B for y in B if y>x and (2*y-x) in S and (3*y-2*x) in S)
    assert brute4==0,(L,brute4)
    checks+=2

# Directly test defining recurrences on a separate range.
for n in range(30000):
    assert good(4*n)==good(n)
    assert good(2*n+1)==good(n)
    assert not good(4*n+2)
    checks+=3

print('CHECK_OK',checks,'exact assertions')
print('T_0..T_12',coeff[:13])
print('No nonconstant four-term progressions: digit descent proof; independent finite cross-check passed.')
