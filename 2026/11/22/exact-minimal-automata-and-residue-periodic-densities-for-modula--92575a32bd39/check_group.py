#!/usr/bin/env python3
"""Independent finite checks for modular ordered-two-subsequence neutral languages."""
from collections import deque,Counter
from itertools import product


def states(q,m):
    pairs=[(i,j) for i in range(q) for j in range(i+1,q)]
    dim=q+len(pairs)
    zero=(0,)*dim
    def step(s,letter):
        t=list(s)
        for k,(i,j) in enumerate(pairs):
            if j==letter:
                t[q+k]=(s[q+k]+s[i])%m
        t[letter]=(s[letter]+1)%m
        return tuple(t)
    items=[zero];idx={zero:0};delta=[]
    for x in items:
        succ=[]
        for a in range(q):
            y=step(x,a)
            if y not in idx:
                idx[y]=len(items);items.append(y)
            succ.append(idx[y])
        delta.append(succ)
    finals={i for i,s in enumerate(items) if all(s[q+k]==0 and (s[a]*s[b])%m==0 for k,(a,b) in enumerate(pairs))}
    return items,delta,finals


def minimize(delta,finals):
    n=len(delta)
    # Partition refinement, with residual signatures of arbitrary suffixes.
    classes=[int(i in finals) for i in range(n)]
    while True:
        keys=[(classes[i],)+tuple(classes[t] for t in delta[i]) for i in range(n)]
        labels={};new=[]
        for key in keys:
            if key not in labels: labels[key]=len(labels)
            new.append(labels[key])
        if len(set(new))==len(set(classes)):
            return len(labels)
        classes=new


def direct(q,m,upto=7):
    counts=Counter()
    # Brute-force all length <= upto and independently calculate all scattered length-two counts.
    for n in range(upto+1):
        yes=0
        for w in product(range(q),repeat=n):
            pair=Counter()
            for i in range(n):
                for j in range(i+1,n):
                    if w[i]!=w[j]: pair[w[i],w[j]]+=1
            if all(v%m==0 for v in pair.values()): yes+=1
        counts[n]=yes
    return counts

if __name__=='__main__':
    for q,m in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)]:
        allstates,d,fs=states(q,m)
        predicted=m**(q+q*(q-1)//2)
        assert len(allstates)==predicted,(q,m,len(allstates),predicted)
        small=minimize(d,fs)
        assert small==predicted,(q,m,small,predicted)
        print(f'q={q} m={m} reachable={len(allstates)} minimized={small} accepting={len(fs)} PASS')
    for q,m in [(2,2),(2,3),(3,2)]:
        its,delta,finals=states(q,m)
        x=0;hist=[int(x in finals)]
        curr=Counter({x:1})
        for n in range(1,9):
            nxt=Counter()
            for state,c in curr.items():
                for y in delta[state]: nxt[y]+=c
            curr=nxt;hist.append(sum(v for k,v in curr.items() if k in finals))
        d=direct(q,m,8)
        assert all(hist[n]==d[n] for n in range(9)),(q,m,hist,d)
        print(f'q={q} m={m} length0to8={hist} direct-words PASS')
