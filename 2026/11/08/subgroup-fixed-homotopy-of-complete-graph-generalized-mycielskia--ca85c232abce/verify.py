#!/usr/bin/env python3
"""Finite checks for subgroup-fixed independence complexes of generalized Mycielskians.
Only Python 3 standard library is required. Exact exhaustive checks on stated finite ranges.
"""
from itertools import combinations


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for k in range(minimum, n+1):
        for rest in partitions(n-k, k):
            yield (k,)+rest


def build(n, ell, part):
    # Explicit original graph; labels 0..n-1, levels 0..ell, plus an apex.
    vertices = [('w', -1)] + [(j,a) for j in range(ell+1) for a in range(n)]
    ed = set()
    for j in range(ell):
        for a in range(n):
            for b in range(n):
                if a != b:
                    ed.add(frozenset(((j,a),(j+1,b))))
    for a,b in combinations(range(n),2):
        ed.add(frozenset(((ell,a),(ell,b))))
    for a in range(n):
        ed.add(frozenset((('w',-1),(0,a))))
    # One explicit cyclic permutation on each prescribed label orbit.
    cycles=[]; start=0
    for s in part:
        cycles.append(tuple(range(start,start+s)))
        start+=s
    assert start==n
    orbitsets=[frozenset((('w',-1),))]
    for j in range(ell+1):
        for cy in cycles:
            orbitsets.append(frozenset((j,a) for a in cy))
    # Remove orbits containing an internal edge: barycentric orbit weight cannot be positive.
    orbitsets=[o for o in orbitsets if not any(e <= o for e in ed)]
    idx=[next(iter(o)) for o in orbitsets]
    neighbors=[set() for _ in orbitsets]
    for i,j in combinations(range(len(orbitsets)),2):
        if any(e <= (orbitsets[i]|orbitsets[j]) for e in ed):
            neighbors[i].add(j);neighbors[j].add(i)
    return orbitsets,neighbors,ed,vertices


def predicted(n,ell,part):
    f=sum(1 for x in part if x==1)
    ids=[('w',-1)]
    for j in range(ell+1):
        for t,s in enumerate(part):
            if j<ell or s==1: ids.append((j,t))
    nb=[set() for _ in ids]
    for i,u in enumerate(ids):
        for z,v in enumerate(ids[:i]):
            if u[0]=='w' or v[0]=='w':
                edge = (v[0]==0 if u[0]=='w' else u[0]==0)
            elif u[0]==v[0]==ell:
                edge=u[1]!=v[1]
            elif abs(u[0]-v[0])==1:
                edge=(u[1]!=v[1] or part[u[1]]>1)
            else:edge=False
            if edge:nb[i].add(z);nb[z].add(i)
    return ids,nb,f


def independent_faces(nb):
    # bitmask enumeration; used only for small quotient graphs
    faces=[0]
    for i,neighbors in enumerate(nb):
        bad=sum(1<<j for j in neighbors)
        faces += [s|(1<<i) for s in faces if not s&bad]
    return faces


def homology_mod2(nb):
    fs=independent_faces(nb)
    bydim=[[] for _ in range(1+max(s.bit_count() for s in fs))]
    for mask in fs:bydim[mask.bit_count()].append(mask)
    ranks=[0]*len(bydim)
    for k in range(1,len(bydim)):
        ix={mask:j for j,mask in enumerate(bydim[k-1])}
        pivots={}
        for mask in bydim[k]:
            x=0
            t=mask
            while t:
                low=t&(-t);t^=low;x ^= 1<<ix[mask^low]
            while x:
                col=x.bit_length()
                if col in pivots:x ^= pivots[col]
                else:pivots[col]=x;break
        ranks[k]=len(pivots)
    return {k-1:len(bydim[k])-ranks[k]- (ranks[k+1] if k+1<len(ranks) else 0)
            for k in range(1,len(bydim)) if len(bydim[k])-ranks[k]- (ranks[k+1] if k+1<len(ranks) else 0) >0},len(fs)


def expected(ell,f):
    k,r=divmod(ell,3)
    if not f:
        return {} if r==0 else {k:1}
    if f==1:return {}
    if r==0:return {2*k:f*(f-1)**k}
    return {2*k+1:(f-1)**(k+1)}


def fold_check(ids,nb,part,ell,f):
    current=set(range(len(ids)))
    cnt=0
    for i,v in enumerate(ids):
        if v[0]=='w':continue
        j,t=v
        if part[t]==1:continue
        if j==ell:raise AssertionError('large orbit survived in last clique layer')
        if f:
            # Any fixed label at the same level witnesses domination.
            u=next(k for k,x in enumerate(ids) if x[0]==j and part[x[1]]==1)
        else:
            # Retain the first orbit as the path representative in each level.
            t0=0
            if t==t0:continue
            u=next(k for k,x in enumerate(ids) if x==(j,t0))
        assert u in current and i in current and u not in nb[i]
        assert (nb[u]&current) <= (nb[i]&current), (ids[i], ids[u])
        current.remove(i);cnt+=1
    kept=[ids[i] for i in sorted(current)]
    # Compare remaining graph with its stated explicit model.
    if f:
        fixed=[t for t,s in enumerate(part) if s==1]
        target=[('w',-1)]+[(j,t) for j in range(ell+1) for t in fixed]
    else:target=[('w',-1)]+[(j,0) for j in range(ell)]
    assert set(kept)==set(target),(kept,target)
    return cnt


def main():
    cases=checks=folds=mod2cases=faces=0
    for n in range(2,7):
        for p in partitions(n):
            for ell in range(1,7):
                os,actual,edges,vertices=build(n,ell,p)
                ids,model,f=predicted(n,ell,p)
                # Canonical orbit order equals model order by construction.
                assert len(os)==len(ids)
                for o,v in zip(os,ids):
                    if v[0]=='w':assert o==frozenset((('w',-1),))
                    else:
                        j,t=v; start=sum(p[:t]); assert o==frozenset((j,a) for a in range(start,start+p[t]))
                assert actual==model
                checks+=len(ids)*(len(ids)-1)//2
                folds+=fold_check(ids,model,p,ell,f)
                cases+=1
                if len(ids)<=15 and ell<=5:
                    b,num=homology_mod2(model)
                    assert b==expected(ell,f),(n,p,ell,b,expected(ell,f))
                    faces+=num;mod2cases+=1
    print(f'ALL_FIXED_MYC_CHECKS_OK partitions_levels={cases} edge_pair_checks={checks} verified_dominance_deletions={folds} mod2_cases={mod2cases} faces_enumerated={faces}')

if __name__=='__main__':main()
