"""Finite-round, orbit-reduced cross-checks for Hamming-graph finite-variable logic.

This experiment is not used as a proof of unrestricted equivalence.
The general mathematical proof uses coordinate patterns and permanent pebble games.
"""
import itertools
import json
from collections import defaultdict


def rgs(words):
    unique={}
    out=[]
    for x in words:
        if x not in unique:
            unique[x]=len(unique)
        out.append(unique[x])
    return tuple(out)


def parts(k,q):
    return sorted(set(rgs(t) for t in itertools.product(range(q),repeat=k)))


def states(d,q,k):
    ps=parts(k,q)
    return list(itertools.combinations_with_replacement(ps,d))


def signatures_orbit(d,q,k):
    profiles=states(d,q,k)
    look={p:i for i,p in enumerate(profiles)}
    vertices=list(itertools.product(range(q),repeat=d))
    atomic=[]; succ=[]
    for ps in profiles:
        distances=tuple(sum(row[i]!=row[j] for row in ps) for i in range(k) for j in range(i+1,k))
        atomic.append(tuple((v==0,v==1) for v in distances))
        nxt=[]
        for i in range(k):
            cases=set()
            for w in vertices:
                ns=[]
                for c,p in enumerate(ps):
                    t=list(p);t[i]=w[c]
                    ns.append(rgs(t))
                cases.add(look[tuple(sorted(ns))])
            nxt.append(tuple(sorted(cases)))
        succ.append(tuple(nxt))
    return profiles,atomic,succ


def compare(dq1,dq2,k):
    data=[signatures_orbit(*dq,k) for dq in (dq1,dq2)]
    atoms=data[0][1]+data[1][1]
    offsets=(0,len(data[0][0]))
    successors=[]
    for idx,(_,_,sucs) in enumerate(data):
        off=offsets[idx]
        successors.extend(tuple(tuple(v+off for v in s) for s in row) for row in sucs)
    colors=[None]*len(atoms)
    def relabel(sigs):
        mapping={};out=[]
        for s in sigs:
            if s not in mapping:
                mapping[s]=len(mapping)
            out.append(mapping[s])
        return out
    colors=relabel(atoms)
    rounds=0
    while True:
        signatures=[(atoms[i],tuple(frozenset(colors[j] for j in successors[i][p]) for p in range(k))) for i in range(len(atoms))]
        updated=relabel(signatures)
        rounds+=1
        if updated==colors:
            break
        assert rounds<50, 'no color stability'
        colors=updated
    left=set(colors[:offsets[1]]);right=set(colors[offsets[1]:])
    return {'k':k,'left':dq1,'right':dq2,'equivalent':left==right,
            'states_left':offsets[1],'states_right':len(atoms)-offsets[1],
            'rounds':rounds,'color_classes_left':len(left),'color_classes_right':len(right),
            'difference_left':len(left-right),'difference_right':len(right-left)}


def main():
    cases=[((1,2),(1,5),2,True),((2,2),(2,5),2,True),((2,2),(3,3),2,True),
           ((1,5),(2,2),2,False),((2,2),(2,3),3,False),((2,3),(2,4),3,True),
           ((2,4),(3,4),3,False),((1,3),(1,4),3,True),((1,3),(1,4),4,False),
           ((2,3),(2,4),4,False),((2,4),(2,5),4,True),
           ((2,2),(2,4),4,False),((3,2),(3,3),3,False),((3,3),(3,5),3,True)]
    results=[]
    for a,b,k,expected in cases:
        r=compare(a,b,k)
        assert r['equivalent']==expected,(a,b,k,r)
        results.append(r)
    print(json.dumps({'cases':len(results),'discrepancies':0,'results':results},sort_keys=True,indent=2))

if __name__=='__main__':main()
