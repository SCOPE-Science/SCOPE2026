#!/usr/bin/env python3
"""Exact elementary-collapse verification for one-vertex feedback tournaments."""
from itertools import product
from collections import Counter
import sys

def instance(n, hub, outgoing):
    rest = [i for i in range(n) if i != hub]
    out = set(i for i, b in zip(rest, outgoing) if b)
    incoming = set(rest) - out
    forbidden = {(a,b) for a in out for b in incoming if a < b}
    def circle():
        return bool(out and incoming and max(out)<min(incoming))
    allowed=[]
    for s in range(1, 1<<n):
        if not (s >> hub & 1):
            allowed.append(s)
        elif all(not (s >> a & 1 and s >> b & 1) for a,b in forbidden):
            allowed.append(s)
    return rest,out,incoming,forbidden,set(allowed),circle()

def collapse_pair(faces,small,large):
    assert large in faces and small in faces and large.bit_count()==small.bit_count()+1 and small&large==small
    # Every proper coface of the lower face must be the upper one.
    assert all(t == large for t in faces if t!=small and (t&small)==small),(small,large)
    faces.remove(small); faces.remove(large)

def generated_l_pairs(rest,out,incoming,forbidden):
    faces={s for s in range(1,1<<len(rest)) if all(not (s>>rest.index(a)&1 and s>>rest.index(b)&1) for a,b in forbidden)}
    # Convert local face masks into global vertex bitmasks.
    faces={sum(1<<rest[k] for k in range(len(rest)) if s>>k&1) for s in faces}
    paired=[]
    def perform(F,G):
        collapse_pair(faces,F,G)
        paired.append((F,G))
    def cone_to(z):
        for F in sorted((s for s in faces if not (s>>z&1)),key=lambda s:(-s.bit_count(),-s)):
            if F in faces: perform(F,F|(1<<z))
    if not out:
        z=rest[0];cone_to(z);return paired,faces,False,(z,)
    p=max(out)
    for v in sorted(out-{p}):
        for F in sorted((s for s in faces if (s>>v&1) and not (s>>p&1)),key=lambda s:(-s.bit_count(),-s)):
            if F in faces: perform(F,F|(1<<p))
    early=incoming.intersection(range(p))
    late=incoming.difference(early)
    if early or not late:
        # If no late neighbors, p is isolated; otherwise any early in-neighbor is isolated.
        z=min(early) if early else p
        cone_to(z);return paired,faces,False,(z,)
    # Remaining graph is K_{1, |incoming|}; independence complex = simplex on incoming plus singleton p.
    i=min(incoming)
    for F in sorted((s for s in faces if not (s>>i&1) and not (s>>p&1)),key=lambda s:(-s.bit_count(),-s)):
        if F in faces: perform(F,F|(1<<i))
    return paired,faces,True,(p,i)

def verify(n,hub,outgoing):
    rest,out,incoming,forbidden,faces,is_circle=instance(n,hub,outgoing)
    l_pairs,final_l,predicted,pivots=generated_l_pairs(rest,out,incoming,forbidden)
    assert predicted==is_circle,(n,hub,outgoing,predicted,is_circle)
    h=1<<hub
    for F,G in l_pairs:collapse_pair(faces,F|h,G|h)
    if not predicted:
        (z,)=pivots
        assert final_l=={1<<z},(n,hub,outgoing,final_l)
        collapse_pair(faces,h,h|(1<<z))
        for F in sorted((s for s in faces if not(s&h) and not(s>>z&1)),key=lambda s:(-s.bit_count(),-s)):
            if F in faces: collapse_pair(faces,F,F|(1<<z))
        assert faces=={1<<z},(n,hub,outgoing,faces)
    else:
        p,i=pivots
        assert final_l=={1<<p,1<<i},(n,hub,outgoing,final_l)
        for v in rest:
            if v in (p,i):continue
            for F in sorted((s for s in faces if not(s&h) and (s>>v&1) and not (s>>p&1)),key=lambda s:(-s.bit_count(),-s)):
                if F in faces:collapse_pair(faces,F,F|(1<<p))
        goal={h,1<<p,1<<i,h|(1<<p),h|(1<<i),(1<<p)|(1<<i)}
        assert faces==goal,(n,hub,outgoing,faces,goal)
    return predicted,len(l_pairs)

def run():
    total=0; circles=0; max_pairs=0; per=[]
    for n in range(3,10):
        this=Counter()
        for hub in range(n):
            for bits in product((0,1),repeat=n-1):
                circle,num=verify(n,hub,bits)
                this['checked']+=1;this['circles']+=int(circle)
                total+=1;circles+=int(circle);max_pairs=max(max_pairs,num)
        assert this['circles']==n*(n-2),(n,this)
        per.append((n,dict(this)))
    print('ALL_CERTIFICATES_PASS',total,'instances',circles,'circle cases','max local collapse pairs',max_pairs)
    for n,data in per:print('n',n,'checked',data['checked'],'circles',data['circles'])
    # A strongly connected instance with contractible directed flag complex:
    n=5;hub=4;out={0,2};inn={1,3}
    adj={(i,j): (i<j if i!=hub and j!=hub else (j in out if i==hub else i in inn)) for i in range(n) for j in range(n) if i!=j}
    for a in range(n):
        reached={a};changed=True
        while changed:
            before=len(reached)
            reached.update(j for i in tuple(reached) for j in range(n) if j!=i and adj[i,j])
            changed=len(reached)>before
        assert len(reached)==n
    assert verify(5,4,(1,0,1,0))[0] is False
    print('STRONG_CONNECTIVITY_COUNTEREXAMPLE_PASS: five vertices, outgoing pattern 1010, contractible')
if __name__=='__main__':run()
