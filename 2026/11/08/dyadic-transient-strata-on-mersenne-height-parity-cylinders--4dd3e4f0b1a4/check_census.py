#!/usr/bin/env python3
"""Exhaustive state-graph census, independent of matrix ranks or symbolic factorization."""
from collections import Counter, deque

def step(x,n):
    y = 0
    for a in range(3):
        for b in range(n):
            v = 0
            if a > 0: v ^= (x >> ((a-1)*n+b)) & 1
            if a < 2: v ^= (x >> ((a+1)*n+b)) & 1
            v ^= (x >> (a*n+(b+1)%n)) & 1
            v ^= (x >> (a*n+(b-1)%n)) & 1
            y |= v << (a*n+b)
    return y

def expected(n):
    h=n&-n
    if h==1: return [3]
    k=h//2
    if k<4: return ([4]*(2*(k-1)))+([4-k]*2)
    return [k]*6

def main():
    checked = 0
    for n in range(3,7):
        size = 1 << (3*n)
        succ = [step(x,n) for x in range(size)]
        indeg = [0]*size
        for y in succ:indeg[y]+=1
        q=deque(i for i in range(size) if indeg[i]==0)
        removal=[]
        while q:
            x=q.popleft();removal.append(x)
            y=succ[x];indeg[y]-=1
            if indeg[y]==0:q.append(y)
        time = [-1]*size
        for x in range(size):
            if indeg[x]>0:time[x]=0
        for x in reversed(removal):time[x]=1+time[succ[x]]
        hist=Counter(time)
        assert -1 not in hist
        dim=3*n
        blocks=expected(n)
        kernel=[sum(min(t,b) for b in blocks) for t in range(max(blocks)+1)]
        periodic=1 << (dim-sum(blocks))
        counts=[periodic * (1 << v) for v in kernel]
        got=[sum(t<=j for t in time) for j in range(max(blocks)+1)]
        assert counts==got,(n,counts,got)
        assert max(time)==max(blocks)
        checked+=size
        print('n=%d: %d states, max T=%d, periodic=%d' % (n,size,max(time),hist[0]))
    print('PASS: %d labelled binary states exhaustively classified' % checked)
if __name__=='__main__':main()
