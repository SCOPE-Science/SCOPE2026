#!/usr/bin/env python3
"""Exact finite checks of a gear graph dissociation-complex Morse matching.
Only experimental finite tests; the all-n theorem is supplied by a separate proof.
Standard library only. No internet or external data.
"""
from collections import Counter, deque
import json


def graph(n):
    size = 2*n + 1
    adj = [0]*size
    def edge(a,b):
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    for i in range(n):
        edge(2*i, 2*i+1)
        edge(2*i+1, (2*i+2)%(2*n))
        edge(2*i, 2*n)
    return adj


def all_faces(n):
    adj=graph(n)
    return {m for m in range(1<<(2*n+1))
            if all((adj[i]&m).bit_count()<=1 for i in range(2*n+1) if m>>i&1)}


def pairing_partner(n,mask):
    """Fiber matching: fix central + original rim vertices, toggle subdivision vertices."""
    U={i for i in range(n) if (mask>>(2*i))&1}
    hub=bool(mask&(1<<(2*n)))
    if hub:
        assert len(U)<=1
        forbidden=set()
        if U:
            i=next(iter(U))
            forbidden={(i-1)%n,i}
        isolated=next((j for j in range(n) if j not in forbidden),None)
        assert isolated is not None
        return mask ^ (1<<(2*isolated+1))
    forbidden={i for i in range(n) if i in U and (i+1)%n in U}
    matched_edges=[((i-1)%n,i) for i in sorted(U)
                   if (i-1)%n not in U and (i+1)%n not in U]
    covered={j for a,b in matched_edges for j in (a,b)}
    isolated=next((j for j in range(n) if j not in forbidden and j not in covered),None)
    if isolated is not None:
        return mask ^ (1<<(2*isolated+1))
    if len(U)==n:
        return None
    assert n%2==0 and len(U)==n//2
    for a,b in matched_edges:
        if not mask&(1<<(2*b+1)):
            return mask ^ (1<<(2*a+1))
    return None


def validate(n,acyclic=True,homology=False):
    faces=all_faces(n)
    partners={f:pairing_partner(n,f) for f in faces}
    crit=[f for f,p in partners.items() if p is None]
    for f,p in partners.items():
        if p is not None:
            assert p in faces and partners[p]==f and (f^p).bit_count()==1
            assert (f^p)&sum(1<<(2*i+1) for i in range(n))
    count=1 if n%2 else 3
    assert len(crit)==count and all(f.bit_count()==n for f in crit)
    # Independent check: full-sign Euler characteristic equals c*(-1)^(n-1).
    red_euler=-sum((-1)**f.bit_count() for f in faces)
    assert red_euler == ((-1)**(n-1))*count
    directed_incidences=0
    if acyclic:
        indegree={f:0 for f in faces}
        out={f:[] for f in faces}
        for upper in faces:
            for i in range(2*n+1):
                if upper>>i&1:
                    lower=upper^(1<<i)
                    assert lower in faces
                    if partners[lower]==upper:
                        a,b=lower,upper
                    else:
                        a,b=upper,lower
                    out[a].append(b)
                    indegree[b]+=1
                    directed_incidences+=1
        q=deque(f for f,k in indegree.items() if k==0)
        visited=0
        while q:
            f=q.popleft();visited+=1
            for b in out[f]:
                indegree[b]-=1
                if indegree[b]==0:q.append(b)
        assert visited==len(faces), ('cyclic',n,visited,len(faces))
    betti=None
    if homology:
        levels={}
        for f in faces:
            if f: levels.setdefault(f.bit_count()-1,[]).append(f)
        ranks={}
        for k in range(1,max(levels)+1):
            rows={f:i for i,f in enumerate(levels[k-1])}
            piv={}
            for f in levels[k]:
                v=f;col=0
                while v:
                    b=v&(-v);v^=b
                    col^=1<<rows[f^b]
                while col:
                    top=col.bit_length()-1
                    if top in piv: col^=piv[top]
                    else: piv[top]=col;break
            ranks[k]=len(piv)
        betti={k:len(fs)-ranks.get(k,0)-ranks.get(k+1,0)
               for k,fs in levels.items()}
        betti={k:v for k,v in betti.items() if v}
        assert betti=={0:1,n-1:count},(n,betti)
    return dict(n=n,faces_including_empty=len(faces),matching_pairs=(len(faces)-len(crit))//2,
                critical_faces=len(crit),critical_dimension=n-1,
                reduced_euler=red_euler,hasse_incidences=directed_incidences,
                homology_mod_two=betti)


if __name__=='__main__':
    runs=[validate(n,acyclic=n<=9,homology=n<=7) for n in range(3,10)]
    print(json.dumps({'graph':'gear G_n, 2-independence', 'cases':runs,
           'status':'all finite tests passed'},sort_keys=True,indent=2))
