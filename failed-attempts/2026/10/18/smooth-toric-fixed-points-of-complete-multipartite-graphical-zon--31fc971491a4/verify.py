#!/usr/bin/env python3
"""Finite cross-check of regular fixed points in complete multipartite graphical fans."""
import itertools
from math import factorial


def orientations(sizes):
    n=sum(sizes); colors=sum(([i]*v for i,v in enumerate(sizes)),[])
    edges=[(i,j) for i in range(n) for j in range(i+1,n) if colors[i]!=colors[j]]
    signatures=set(); total=smooth=0
    for perm in itertools.permutations(range(n)):
        pos={v:i for i,v in enumerate(perm)}
        orientation=tuple(pos[i]<pos[j] for i,j in edges)
        if orientation in signatures: continue
        signatures.add(orientation); total+=1
        runs=[];runcolors=[]
        for v in perm:
            if runcolors and colors[v]==runcolors[-1]:runs[-1]+=1
            else: runcolors.append(colors[v]);runs.append(1)
        if (len(runs)==2 and min(runs)==1) or (len(runs)>=3 and all(t==1 for t in runs[1:-1])):
            smooth+=1
    return total,smooth


def block_counts(sizes):
    k=len(sizes); ctotal=csmooth=0
    def recurse(remaining,last,runs):
        nonlocal ctotal,csmooth
        if sum(remaining)==0:
            if len(runs)<2:return
            freq=[[t for c,t in runs if c==i] for i in range(k)]
            weight=1
            for i in range(k):
                weight*=factorial(sizes[i])
                for z in freq[i]:weight//=factorial(z)
            ctotal+=weight
            if (len(runs)==2 and min(z for c,z in runs)==1) or (
                len(runs)>=3 and all(z==1 for c,z in runs[1:-1])
            ):csmooth+=weight
            return
        for i in range(k):
            if i==last:continue
            for z in range(1,remaining[i]+1):
                temp=list(remaining);temp[i]-=z
                recurse(tuple(temp),i,runs+[(i,z)])
    recurse(tuple(sizes),-1,[])
    return ctotal,csmooth


def main():
    for sizes in [(1,1,1),(1,2,2),(2,2,2),(2,2,3),(1,2,3)]:
        a=orientations(sizes)
        b=block_counts(sizes)
        assert a==b, (sizes,a,b)
        print(sizes, a)
    print('VERIFY_OK')

if __name__=='__main__':main()
