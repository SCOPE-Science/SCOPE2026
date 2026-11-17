#!/usr/bin/env python3
"""Independent finite checks of signed acyclic-digraph fixed spaces.
Only verifies bounded cases; the theorem's infinite proof is geometric.
"""
import itertools
from collections import defaultdict
from verify_signed_dag import closure, acyclic

def components(n, edges):
    reach=[[i==j or (i,j) in edges for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):reach[i][j]|=reach[i][k] and reach[k][j]
    out=[];unused=set(range(n))
    while unused:
        i=min(unused);c={j for j in unused if reach[i][j] and reach[j][i]};out.append(c);unused-=c
    return out

def rank_real(rows):
    if not rows:return 0
    from fractions import Fraction
    a=[[Fraction(t) for t in row] for row in rows]
    m=len(a);n=len(a[0]);r=0
    for j in range(n):
        p=next((i for i in range(r,m) if a[i][j]!=0),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];d=a[r][j];a[r]=[x/d for x in a[r]]
        for i in range(m):
            if i!=r and a[i][j]:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==m:break
    return r

def pred(n, E, H):
    cs=components(n,E);idx={v:i for i,c in enumerate(cs) for v in c}
    if any(idx[i]!=idx[j] for i,j in E):return {}
    constraints=[]
    for c in cs:constraints.append([int(i in c) for i in range(n)])
    for p,e in H:
        for i in range(n):
            row=[0]*n;row[p[i]]+=1;row[i]-=e;constraints.append(row)
    d=n-rank_real(constraints)
    return {-1:1} if d==0 else {d-1:1}

def check(n,E,H):
    unseen=set(E);orbs=[]
    while unseen:
        a=min(unseen);O={(p[a[0]],p[a[1]]) if e==1 else (p[a[1]],p[a[0]]) for p,e in H}
        assert O<=E
        orbs.append(O);unseen-=O
    m=len(orbs)
    faces=defaultdict(list)
    for mask in range(1<<m):
        edges=set().union(*(orbs[i] for i in range(m) if mask&(1<<i)))
        if acyclic(n,edges):faces[mask.bit_count()-1].append(mask)
    if not faces[0]:hom={-1:1}
    else:
        ranks={0:1}
        for q in sorted(k for k in faces if k>=1):
            idx={s:i for i,s in enumerate(faces[q-1])};pivots={}
            for mask in faces[q]:
                v=0
                for i in range(m):
                    if mask&(1<<i):v^=1<<idx[mask^(1<<i)]
                while v:
                    k=v.bit_length()-1
                    if k not in pivots:pivots[k]=v;break
                    v^=pivots[k]
            ranks[q]=len(pivots)
        hom={q:len(faces[q])-ranks[q]-ranks.get(q+1,0) for q in ranks}
        hom={q:b for q,b in hom.items() if b}
    want=pred(n,E,H)
    assert hom==want,(n,sorted(E),len(H),hom,want)
    return m

def main():
    tested=0;types=defaultdict(int);max_orbits=0
    for n in (2,3,4):
        A=[(i,j) for i in range(n) for j in range(n) if i!=j]
        masks=range(1<<len(A)) if n<4 else list(range(0,1<<len(A),31))+[4095,0,0x5a5,0xa5a]
        for mask in masks:
            E={a for i,a in enumerate(A) if mask&(1<<i)}
            valid=[]
            for p in itertools.permutations(range(n)):
                for e in (1,-1):
                    T={(p[i],p[j]) if e==1 else (p[j],p[i]) for i,j in E}
                    if T==E:valid.append((p,e))
            Hs={closure(n,((p,e),)) for p,e in valid}
            # Include full signed symmetry group, not only cyclic subgroups.
            Hs.add(closure(n,tuple(valid)))
            for H in Hs:
                m=check(n,E,H);tested+=1;max_orbits=max(m,max_orbits)
                cs=components(n,E);cross=any((i not in c or j not in c) for i,j in E for c in cs if i in c)
                types['cross' if cross else 'no_cross']+=1
    print('SIGNED_DAG_GENERAL_DIRECTED_CHECKS_PASS')
    print('checked_pairs',tested,'subclasses',dict(types),'maximum_arc_orbits',max_orbits)
if __name__=='__main__':main()
