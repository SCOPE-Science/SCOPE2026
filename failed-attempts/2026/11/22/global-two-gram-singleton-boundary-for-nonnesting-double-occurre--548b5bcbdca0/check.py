#!/usr/bin/env python3
"""Reproduce nonnesting double-occurrence two-gram singleton calculations."""
from itertools import permutations, product
from collections import Counter, defaultdict
from math import factorial


def dyck_paths(n):
    def rec(up,down,steps):
        if up == down == n:
            yield tuple(steps)
            return
        if up < n:
            steps.append(1)
            yield from rec(up+1,down,steps)
            steps.pop()
        if down < up:
            steps.append(-1)
            yield from rec(up,down+1,steps)
            steps.pop()
    yield from rec(0,0,[])


def fifo_word(path,order):
    opening=closing=0
    w=[]
    for ch in path:
        if ch == 1:
            w.append(order[opening]); opening+=1
        else:
            w.append(order[closing]); closing+=1
    return tuple(w)


def bigrams(w,n):
    counts = [0]*(n*n)
    for a,b in zip(w,w[1:]):counts[n*a+b]+=1
    return tuple(counts)


def mountain(path):
    height=0; opened=0; closing=False
    for ch in path:
        height+=ch
        if ch == 1:
            if closing: return False
            opened+=1
        else: closing=True
        if height==0:
            opened=0; closing=False
    return height==0


def all_double_occ_words(n):
    used=[0]*n; word=[]
    def rec():
        if len(word)==2*n:
            yield tuple(word); return
        for i in range(n):
            if used[i]<2:
                used[i]+=1;word.append(i)
                yield from rec()
                word.pop();used[i]-=1
    yield from rec()


def arborescence_fiber(w,n):
    # Directed matrix-tree theorem + BEST theorem for trails.
    # Each edge type is indistinguishable: divide by parallel multiplicities.
    adj=[[] for _ in range(n)]
    for a,b in zip(w,w[1:]):adj[a].append(b)
    end=w[-1]
    nonroot=[v for v in range(n) if v!=end]
    count=0
    for choices in product(*(adj[v] for v in nonroot)):
        successor=dict(zip(nonroot,choices))
        works=True
        for v in nonroot:
            seen=set()
            at=v
            while at!=end:
                if at in seen:
                    works=False;break
                seen.add(at)
                at=successor[at]
            if not works:break
        if works:count+=1
    denom=1
    for v in range(n):
        for mult in Counter(adj[v]).values(): denom*=factorial(mult)
    assert count%denom==0,(w,count,denom)
    return count//denom


def brute_truth(n):
    c=Counter(bigrams(w,n) for w in all_double_occ_words(n))
    return c


def check(n, full_brute):
    truth=brute_truth(n) if full_brute else None
    per={};nwords=0; uniques=0; bad=[];factors=Counter()
    for path in dyck_paths(n):
        pred=mountain(path)
        for order in permutations(range(n)):
            w=fifo_word(path,order)
            mult=arborescence_fiber(w,n)
            actual=mult==1
            if truth is not None:
                assert truth[bigrams(w,n)]==mult, (n,w,truth[bigrams(w,n)],mult)
            nwords+=1;uniques+=actual
            factors[mult]+=1
            if actual!=pred:
                bad.append((w,actual,pred,mult))
    assert not bad,bad[:5]
    assert nwords==factorial(n)*sum(1 for _ in dyck_paths(n))
    assert uniques==factorial(n)*2**(n-1)
    print('n=%d nonnest=%d singleton=%d expected=%d profile_fibers=%s'%(
        n,nwords,uniques,factorial(n)*2**(n-1),repr(sorted(factors.items())[:12])))

if __name__=='__main__':
    for n in range(1,7): check(n,full_brute=n<=5)
    print('PASS')
