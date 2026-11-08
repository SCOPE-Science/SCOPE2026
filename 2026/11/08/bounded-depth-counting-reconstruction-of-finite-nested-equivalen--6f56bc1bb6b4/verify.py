#!/usr/bin/env python3
"""Finite tests for counting refinement of nested equivalence partitions.
No external dependencies. A sample is not an exhaustive argument for arbitrary orders.
"""
import random
from collections import Counter, defaultdict

def canon(ids, colors):
    m=len(ids); n=len(colors)
    def class_tree(level, members):
        if level==0:
            return tuple(sorted(colors[x] for x in members))
        groups=defaultdict(list)
        for x in members: groups[ids[level-1][x]].append(x)
        return tuple(sorted(class_tree(level-1,v) for v in groups.values()))
    groups=defaultdict(list)
    for x in range(n): groups[ids[-1][x]].append(x)
    return tuple(sorted(class_tree(m-1,v) for v in groups.values()))

def orbit_labels(ids, colors):
    m=len(ids); n=len(colors)
    def class_tree(level, members):
        if level==0:
            return tuple(sorted(colors[x] for x in members))
        groups=defaultdict(list)
        for x in members: groups[ids[level-1][x]].append(x)
        return tuple(sorted(class_tree(level-1,v) for v in groups.values()))
    ans=[]
    for x in range(n):
        chain=[colors[x]]
        for level in range(m):
            members=[y for y in range(n) if ids[level][y]==ids[level][x]]
            chain.append(class_tree(level,members))
        ans.append(tuple(map(repr,chain)))
    return ans

def simultaneous_refinement(batch, max_rounds):
    # Each structure: (list of levels containing block IDs, unary colors).
    universe=sorted({c for _,col in batch for c in col})
    names={v:i for i,v in enumerate(universe)}
    old=[[names[c] for c in col] for _,col in batch]
    for step in range(max_rounds):
        keys=[]
        for (ids,col),cs in zip(batch,old):
            n=len(col); m=len(ids)
            kk=[]
            for x in range(n):
                profiles=[]
                for lev in range(m):
                    counts=Counter(cs[y] for y in range(n) if ids[lev][x]==ids[lev][y])
                    profiles.append(tuple(sorted(counts.items())))
                kk.append((cs[x],tuple(profiles)))
            keys.append(kk)
        all_keys=sorted({key for ks in keys for key in ks})
        ix={k:i for i,k in enumerate(all_keys)}
        old=[[ix[k] for k in ks] for ks in keys]
    return old

def random_structure(n,m,rng):
    # Build nested partitions, retaining positive block sizes.
    colors=[rng.randrange(3) for _ in range(n)]
    blocks=[[x] for x in range(n)]
    ids=[]
    for lev in range(m):
        rng.shuffle(blocks)
        new=[]
        while blocks:
            size=rng.randint(1,min(len(blocks),4))
            taken=blocks[:size]; del blocks[:size]
            new.append([x for b in taken for x in b])
        levels=[None]*n
        for block_id,b in enumerate(new):
            for x in b: levels[x]=block_id
        ids.append(levels)
        blocks=new
    return (ids,colors)

def rooted_pattern(patterns):
    e1=[]; e2=[]; current=0; coarse=0
    for pattern in patterns:
        for size in pattern:
            e1.extend([current]*size)
            e2.extend([coarse]*size)
            current += 1
        coarse += 1
    return ([e1,e2],[0]*len(e1))

def check_depth_witness():
    # Two 16-point nested structures have the same rank-1 colors but differ at rank 2.
    left=rooted_pattern([[1,1,2,2,2],[1,1,1,1,1,1,2]])
    right=rooted_pattern([[1,1,1,1,2,2],[1,1,1,1,2,2]])
    assert len(left[1])==len(right[1])==16
    c1=simultaneous_refinement([left,right],1)
    c2=simultaneous_refinement([left,right],2)
    assert Counter(c1[0])==Counter(c1[1])
    assert Counter(c2[0])!=Counter(c2[1])
    assert canon(*left)!=canon(*right)
    print('DEPTH_WITNESS_OK 16 2')

def main():
    rng=random.Random(17291)
    total=0
    pairs=0
    for m in range(1,5):
        for n in range(1,11):
            batch=[random_structure(n,m,rng) for _ in range(110)]
            # Extend sample by uniformly monochrome cases.
            batch += [(ids,[0]*n) for ids,_ in batch[:25]]
            refined=simultaneous_refinement(batch,m)
            by_signature={}
            for (ids,colors),cs in zip(batch,refined):
                invariant=tuple(sorted(Counter(cs).items()))
                iso=canon(ids,colors)
                if invariant in by_signature:
                    assert by_signature[invariant]==iso,(m,n,iso,by_signature[invariant])
                    pairs+=1
                else: by_signature[invariant]=iso
                orbit=orbit_labels(ids,colors)
                for i in range(n):
                    for j in range(n):
                        assert (cs[i]==cs[j]) == (orbit[i]==orbit[j]),(m,n,i,j)
                total+=1
    check_depth_witness()
    print('VERIFY_OK nested_partitions',total,'repeated_signatures',pairs,'levels_1_to_4','sizes_1_to_10')
if __name__=='__main__': main()
