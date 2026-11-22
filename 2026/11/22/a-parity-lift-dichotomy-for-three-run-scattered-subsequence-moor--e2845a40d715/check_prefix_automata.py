#!/usr/bin/env python3
"""Independent full-prefix subsequence DP, reachable states, and Moore minimization."""
from collections import deque
from itertools import product

def full_update(s, pattern, x):
    out=list(s)
    for j in range(len(pattern)-1, -1, -1):
        if pattern[j]==x:
            out[j] ^= (1 if j==0 else s[j-1])
    return tuple(out)

def states(a,b):
    pattern = '0'*a+'1'*b+'0'
    z=(0,)*len(pattern)
    todo=deque([z]); seen={z}
    while todo:
        s=todo.popleft()
        for x in '01':
            t=full_update(s,pattern,x)
            if t not in seen:
                seen.add(t);todo.append(t)
    return pattern,seen

def predict(a,b):
    h=a.bit_length()
    return 2**(h+b+1 if b>=2 or a%2==0 else h+b)

def refine(pattern, reachable):
    # Repeated Moore partition refinement from the actual output, not assumed signatures.
    nodes=list(reachable)
    idx={s:i for i,s in enumerate(nodes)}
    trans=[tuple(idx[full_update(s,pattern,x)] for x in '01') for s in nodes]
    parts=[s[-1] for s in nodes]
    while True:
        signatures=[(parts[i],parts[t[0]],parts[t[1]]) for i,t in enumerate(trans)]
        labels={k:j for j,k in enumerate(sorted(set(signatures)))}
        fresh=[labels[v] for v in signatures]
        if len(set(fresh))==len(set(parts)):
            return len(set(fresh))
        parts=fresh

cases=0; total_states=0; minimizations=0
for a in range(1,12):
    for b in range(1,7):
        p,S=states(a,b)
        expected=predict(a,b)
        assert len(S)==expected,(a,b,len(S),expected)
        cases+=1;total_states+=len(S)
        if a<=5 and b<=4:
            assert refine(p,S)==expected,('minimize',a,b)
            minimizations+=1
# Independent literal positional counting, checked against full DP.
comparisons=0
for a in range(1,5):
    for b in range(1,5):
        p='0'*a+'1'*b+'0'
        for n in range(0,12):
            for t in product('01',repeat=n):
                s=(0,)*len(p)
                for x in t:s=full_update(s,p,x)
                # Count embeddings via recursive list of index-tuples, not prefix counter recurrence.
                combos=[()]
                for ch in p:
                    combos=[inds+(i,) for inds in combos for i in range(inds[-1]+1 if inds else 0,n) if t[i]==ch]
                assert s[-1] == (len(combos)%2),(a,b,n,t)
                comparisons+=1
print(f'PASS orbit_cases={cases} visited_states={total_states} minimized_cases={minimizations} literal_checks={comparisons}')
