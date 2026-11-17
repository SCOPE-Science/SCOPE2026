#!/usr/bin/env python3
"""Exhaustive finite quotient certificate for a four-colour cyclic network."""
from itertools import product
from collections import Counter
from math import factorial

Q = 4
VALUES = range(3)

def cap_add(a,b):
    return min(2,a+b)

def initial(a,b):
    return (tuple(a),tuple(b),tuple(i if a[i] else -1 for i in range(Q)),
            tuple(i if b[i] else -1 for i in range(Q)))

def advance(state):
    a,b,ta,tb=state
    nxt_counts=[]
    nxt_tags=[]
    for vec,opp,tags in ((a,b,ta),(b,a,tb)):
        updated=[0]*Q
        for c,amount in enumerate(vec):
            goal=(c+1)%Q
            dest=goal if opp[goal]>=2 else c
            updated[dest]=cap_add(updated[dest],amount)
        updated_tags=tuple(-1 if c<0 else ((c+1)%Q if opp[(c+1)%Q]>=2 else c) for c in tags)
        nxt_counts.append(tuple(updated))
        nxt_tags.append(updated_tags)
    return nxt_counts[0],nxt_counts[1],nxt_tags[0],nxt_tags[1]

def orbit(state):
    first={}
    steps=[]
    while state not in first:
        first[state]=len(steps)
        steps.append(state)
        state=advance(state)
        assert len(steps)<64, 'unexpected long symbolic orbit'
    return first[state],len(steps)-first[state]

def rotate(a,k):
    out=[0]*Q
    for i,v in enumerate(a):out[(i+k)%Q]=v
    return tuple(out)

CANONICAL=[
 ((0,2,2,2),(2,2,0,2)),
 ((0,2,2,2),(2,2,1,2)),
 ((1,2,2,2),(2,2,0,2)),
 ((1,2,2,2),(2,2,1,2)),
 ((1,1,2,2),(2,2,1,1)),
]
EXPECTED={(rotate(a,k),rotate(b,k)) for a,b in CANONICAL for k in range(4)}
assert len(EXPECTED)==20

def signatures():
    for bits in product(VALUES,repeat=8):
        a,b=bits[:4],bits[4:]
        if any(a) and any(b):yield tuple(a),tuple(b)

def composition(n):
    for a in range(n+1):
     for b in range(n+1-a):
      for c in range(n+1-a-b):
       yield (a,b,c,n-a-b-c)

def multinomial(vec):
    return factorial(sum(vec))//__import__('math').prod(factorial(v) for v in vec)

def U(n):
    return sum(multinomial((0,a,b,n-a-b)) for a in range(2,n+1)
        for b in range(2,n+1-a) if n-a-b>=2)

def V(n):
    return sum(multinomial((1,a,b,n-1-a-b)) for a in range(2,n)
        for b in range(2,n-a) if n-1-a-b>=2)

def W(n):
    return sum(multinomial((1,1,a,n-2-a)) for a in range(2,n) if n-2-a>=2)

def formula(m,n):
    return 4*(U(m)+V(m))*(U(n)+V(n))+4*W(m)*W(n)

def main():
    periods=Counter();entries=Counter();six=set();sharp=None
    for a,b in signatures():
        s=initial(a,b)
        d,p=orbit(s)
        periods[p]+=1;entries[d]+=1
        if p==6:
            assert d in (0,1)
            six.add((a,b))
        if d==5 and sharp is None:sharp=(a,b)
        t=s
        for j in range(17):
            if j==5:at5=t
            t=advance(t)
        assert at5==t, (a,b)
        assert p in (1,4,6) and d<=5
    assert periods=={1:6141,4:239,6:20},periods
    assert six==EXPECTED,(six^EXPECTED)
    on_cycle={(a,b) for a,b in six if orbit(initial(a,b))[0]==0}
    assert on_cycle=={(rotate(CANONICAL[0][0],k),rotate(CANONICAL[0][1],k)) for k in range(4)}
    assert sum(entries.values())==6400 and entries[5]>0
    assert orbit(initial((0,1,2,2),(2,2,1,1)))==(5,1)
    weighted={}
    for m,n in ((6,6),(6,7),(7,7),(8,9)):
        count=0
        for a in composition(m):
            aa=tuple(min(2,x) for x in a)
            for b in composition(n):
                bb=tuple(min(2,x) for x in b)
                if (aa,bb) in EXPECTED:
                    count+=multinomial(a)*multinomial(b)
        assert count==formula(m,n)
        weighted[f'{m},{n}']=count
    print('abstract_states=6400',flush=True)
    print('period_signature_counts='+str(dict(sorted(periods.items()))),flush=True)
    print('entry_signature_counts='+str(dict(sorted(entries.items()))),flush=True)
    print('universal_identity=F^17=F^5',flush=True)
    print('period_six_signatures=20=4_rotations_of_5_patterns',flush=True)
    print('period_six_on_cycle_signatures=4;one_step_basin_signatures=16',flush=True)
    print('sharp_entry_5=(0,1,2,2);(2,2,1,1)',flush=True)
    print('weighted_period_six_counts='+str(weighted),flush=True)
    print('PASS',flush=True)
if __name__=='__main__':main()
