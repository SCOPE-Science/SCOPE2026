"""Independent template-level degree and connectivity checker.

This checks the finite pattern-overlap identities over many circumferences;
it is supplementary evidence, not a substitute for the general proof.
Run: python3 verify_templates.py
"""
from collections import Counter, deque
from hashlib import sha256
import json

TYPES=('A','B_near','B_far','C_align','C_shift')
EXPECTED={
 'A':{'A':2,'B_near':4,'B_far':2},
 'B_near':{'A':2,'B_near':1,'B_far':2,'C_align':1,'C_shift':2},
 'B_far':{'A':1,'B_near':2,'C_align':1,'C_shift':1},
 'C_align':{'B_near':4,'B_far':4,'C_shift':4},
 'C_shift':{'B_near':4,'B_far':2,'C_align':2}}

def catalogue(n):
    kinds={}
    def insert(vertices,kind):
        s=frozenset(vertices)
        if s in kinds:
            assert kinds[s]==kind, ('collision',n,s,kinds[s],kind)
        kinds[s]=kind
    for base in (0,n):
        opposite=n-base
        def U(j):return base+j%n
        def V(j):return opposite+j%n
        for j in range(n):
            insert((U(j),U(j+1),U(j+2),U(j+3)),'A')
            insert((V(j),U(j),U(j+1),U(j+2)),'B_near')
            insert((V(j),U(j),U(j-1),U(j-2)),'B_near')
            insert((V(j),U(j),U(j+1),U(j-2)),'B_far')
            insert((V(j),U(j),U(j-1),U(j+2)),'B_far')
    for j in range(n):
        for d in (-1,0,1):
            insert((j,(j+1)%n,n+(j+d)%n,n+(j+d+1)%n), 'C_align' if d==0 else 'C_shift')
    return kinds


def one(n):
    kinds=catalogue(n)
    assert Counter(kinds.values())=={'A':2*n,'B_near':4*n,'B_far':4*n,'C_align':n,'C_shift':2*n}
    graph={}
    rows={}
    for s,kind in kinds.items():
        ns=[]
        for leaving in s:
            for arriving in range(2*n):
                if arriving not in s:
                    t=(s-{leaving})|{arriving}
                    if t in kinds:ns.append(t)
        assert len(ns)==len(set(ns))
        graph[s]=ns
        profile=dict(Counter(kinds[t] for t in ns))
        assert profile==EXPECTED[kind],(n,s,profile,EXPECTED[kind])
        rows[kind]=profile
    seen={next(iter(kinds))}
    queue=list(seen)
    for s in queue:
        for t in graph[s]:
            if t not in seen:seen.add(t);queue.append(t)
    assert len(seen)==len(kinds)
    states_sha256=sha256(json.dumps(sorted(tuple(sorted(s)) for s in kinds),separators=(',',':')).encode()).hexdigest()
    return {'n':n,'states':len(kinds),'edges':sum(map(len,graph.values()))//2,'states_sha256':states_sha256}

if __name__=='__main__':
    results=[one(n) for n in range(6,51)]
    print(json.dumps({'range':[6,50], 'all_checks_passed':True, 'samples':[results[0],results[6],results[-1]],
      'type_neighbor_profile':EXPECTED, 'checks_completed':len(results)}, indent=2, sort_keys=True))
