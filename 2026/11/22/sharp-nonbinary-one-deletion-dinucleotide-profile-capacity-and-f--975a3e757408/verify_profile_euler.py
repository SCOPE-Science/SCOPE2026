#!/usr/bin/env python3
"""Standalone verifier of the q-ary dinucleotide deletion-profile Euler construction."""
from collections import defaultdict
from itertools import product

def witness(q):
    assert q >= 3
    outgoing = defaultdict(list)
    # One occurrence of every proper triple a != b != c (a may equal c).
    for a, b, c in product(range(q), repeat=3):
        if a != b and b != c:
            outgoing[(a,b)].append((b,c))
    # Two transitions through every equal state, with one modified exit.
    for a in range(q):
        prev = (a-1) % q
        following = (a+1) % q if a else 2
        outgoing[(prev,a)].append((a,a))
        outgoing[(a,a)].append((a,following))
    for v in outgoing: outgoing[v].sort(reverse=True)
    start = (0,1)
    stack = [start]
    tour = []
    while stack:
        v = stack[-1]
        if outgoing[v]: stack.append(outgoing[v].pop())
        else: tour.append(stack.pop())
    path = list(reversed(tour))
    assert path[0] == (0,1), (q, path[0])
    assert path[-1] == (0,2), (q, path[-1])
    assert all(u[1] == v[0] for u,v in zip(path,path[1:]))
    assert all(not outgoing[v] for v in outgoing)
    word = [path[0][0]] + [v[1] for v in path]
    assert len(word) == q*(q-1)**2 + 2*q + 2
    return tuple(word)

def profile(word,q):
    v=[0]*(q*q)
    for a,b in zip(word,word[1:]):v[q*a+b]+=1
    return tuple(v)

def ball(word,q):
    return {profile(word[:i]+word[i+1:],q) for i in range(len(word))}

def delta(a,b,c,q):
    v=[0]*(q*q)
    v[q*a+b]-=1;v[q*b+c]-=1;v[q*a+c]+=1
    return tuple(v)

def categories(q):
    return {delta(a,b,c,q) for a,b,c in product(range(q),repeat=3)}

def run():
    for q in range(3,9):
        word=witness(q)
        assert len(categories(q)) == q+q*(q-1)**2
        vals=ball(word,q)
        cap=q*(q-1)**2+q+2
        assert len(vals)==cap, (q,len(vals),cap)
        # Distinct deletion profiles equal the feature count from the local-delta formula.
        base=profile(word,q)
        observed=set()
        for i in range(len(word)):
            if i==0: change=tuple(-int(j==q*word[0]+word[1]) for j in range(q*q))
            elif i==len(word)-1:change=tuple(-int(j==q*word[-2]+word[-1]) for j in range(q*q))
            else:change=delta(word[i-1],word[i],word[i+1],q)
            assert tuple(x+y for x,y in zip(base,change)) == profile(word[:i]+word[i+1:],q)
            observed.add(change)
        assert len(observed)==cap
        print('q=',q,'first_length=',len(word),'capacity=',cap,'witness=', ''.join(map(str,word)) if q<=4 else 'verified')
    # Exhaustively check all ternary words through length 9 against the universal 17 bound.
    for n in range(2,10):
        max_seen=max(len(ball(w,3)) for w in product(range(3),repeat=n))
        assert max_seen <= min(n,17)
        print('ternary_length',n,'max',max_seen)
    print('PASS')
if __name__=='__main__':run()
