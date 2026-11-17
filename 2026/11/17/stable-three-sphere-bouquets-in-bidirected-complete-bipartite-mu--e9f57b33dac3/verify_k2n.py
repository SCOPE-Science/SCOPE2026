#!/usr/bin/env python3
"""Exact finite checks for bidirected K_{2,n} multipath complexes.

Run: python3 verify_k2n.py. No third-party dependencies.
Faces are four-slot tuples (A,B,C,D), 0 meaning absent; positive entries
are labels in the n-element part. A,C point toward a leaf; B,D away.
"""
from itertools import product, combinations
from collections import Counter, deque


def valid(t):
    a,b,c,d=t
    return not ((a and b and a==b) or (a and c and a==c)
                or (b and d and b==d) or (c and d and c==d)
                or (a and b and c and d and a==d and b==c))


def polynomial(n):
    return n**4-8*n**3+19*n**2-14*n+1


def face_vector(n):
    return (1,4*n,6*n*n-4*n,4*n*(n-1)**2,n*(n-1)**2*(n-2))


def match(n, return_data=False):
    faces={t for t in product(range(n+1),repeat=4) if valid(t)}
    original=set(faces) if return_data else None
    counts=Counter(sum(bool(x) for x in t) for t in faces)
    assert tuple(counts[j] for j in range(5))==face_vector(n)
    pairs={}
    for position in range(4):
        for label in range(1,n+1):
            lower=[f for f in faces if f[position]==0 and
                   f[:position]+(label,)+f[position+1:] in faces]
            for f in lower:
                higher=f[:position]+(label,)+f[position+1:]
                assert f in faces and higher in faces
                if return_data: pairs[f]=higher
                faces.remove(f)
                faces.remove(higher)
    residual=Counter(sum(bool(x) for x in t) for t in faces)
    assert sum(counts.values())==2*(sum(counts.values())-len(faces))//2+len(faces)
    return counts,residual,original,pairs


def graph_face(t):
    # An independent check using actual indegrees, outdegrees and walks.
    n=max(t)
    a,b,c,d=t
    arcs=[]
    if a: arcs.append((0,a+1))
    if b: arcs.append((b+1,0))
    if c: arcs.append((1,c+1))
    if d: arcs.append((d+1,1))
    if len({x for x,y in arcs})!=len(arcs):return False
    if len({y for x,y in arcs})!=len(arcs):return False
    nxt=dict(arcs)
    for start in nxt:
        at=start;seen=set()
        while at in nxt and at not in seen:
            seen.add(at);at=nxt[at]
        if at in seen:return False
    return True


def check_directed_hasse(faces,pairs):
    # Unmatched codimension-one incidence: downward. Matched: upward.
    order=list(faces);ids={t:i for i,t in enumerate(order)}
    adj=[[] for _ in order];degree=[0]*len(order)
    for t in order:
        for j,val in enumerate(t):
            if not val:continue
            low=t[:j]+(0,)+t[j+1:]
            assert low in ids
            if pairs.get(low)==t: src,dst=low,t
            else:src,dst=t,low
            i,k=ids[src],ids[dst];adj[i].append(k);degree[k]+=1
    q=deque(i for i,v in enumerate(degree) if v==0)
    visited=0
    while q:
        i=q.popleft();visited+=1
        for j in adj[i]:
            degree[j]-=1
            if degree[j]==0:q.append(j)
    assert visited==len(faces),(visited,len(faces))
    return sum(map(len,adj))


def main():
    for n in range(6,20):
        counts,remain,_,_=match(n)
        assert remain==Counter({4:polynomial(n)}),(n,remain)
        print('n=%d critical_top=%d total_faces=%d PASS' % (n,remain[4],sum(counts.values())))
    for n in (6,7):
        counts,remain,faces,pairs=match(n,True)
        for t in product(range(n+1),repeat=4):
            assert valid(t)==graph_face(t),(n,t)
        incidences=check_directed_hasse(faces,pairs)
        assert len(pairs)*2+sum(remain.values())==len(faces)
        print('n=%d independent_path_check=%d directed_Hasse_incidences=%d acyclic=PASS'
              %(n,len(faces),incidences))
    print('K2N_MULTIPATH_STABLE_MORSE_EXACT_PASS')

if __name__=='__main__':main()
