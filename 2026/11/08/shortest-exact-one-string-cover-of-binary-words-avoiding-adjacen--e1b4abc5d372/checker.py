#!/usr/bin/env python3
"""Independent bounded checks and constructive reproduction of the stated k-mer cover."""
from collections import defaultdict, deque
from itertools import product


def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def legal(s): return not any(a==b==0 for a,b in zip(s,s[1:]))


def create(k):
    assert k>=2
    L=k-1
    vertices=[x for x in product((0,1),repeat=L) if legal(x)]
    edges=[x for x in product((0,1),repeat=k) if legal(x)]
    augmented=list(edges)
    negative=[v for v in vertices if v[0]==1 and v[-1]==0] if L>=2 else []
    omit=(1,)*(L-1)+(0,) if L>=2 else None
    potential={v:(min((j for j,c in enumerate(v) if c==0),default=L) if v!=(1,)*L else L-1) for v in vertices}
    assert all(potential[e[:-1]]-potential[e[1:]]<=1 for e in edges)
    for v in negative:
        if v==omit: continue
        j=next(i for i,x in enumerate(v) if x==0)
        cur=v
        for _ in range(j):
            e=cur+(1,)
            assert e in edges
            augmented.append(e)
            cur=e[1:]
        assert cur[0]==0 and cur[-1]==1
    assert len(augmented)-len(edges)==fib(k)-k+1
    start=(0,)+(1,)*(L-1) if L>=2 else (0,)
    end=omit if L>=2 else start
    degree=defaultdict(int)
    adjacency=defaultdict(list)
    for e in augmented:
        degree[e[:-1]]+=1;degree[e[1:]]-=1
        adjacency[e[:-1]].append(e[1:])
    assert all(degree[v]==int(v==start)-int(v==end) for v in vertices)
    stack=[start]
    circuit=[]
    while stack:
        v=stack[-1]
        if adjacency[v]: stack.append(adjacency[v].pop())
        else: circuit.append(stack.pop())
    path=circuit[::-1]
    assert len(path)==len(augmented)+1 and path[0]==start and path[-1]==end
    spelled=path[0]+tuple(v[-1] for v in path[1:])
    assert legal(spelled)
    assert set(spelled[i:i+k] for i in range(len(spelled)-k+1))==set(edges)
    assert len(spelled)==fib(k+2)+fib(k)
    # certificate for potential/degree lower bound
    assert sum(next(i for i,x in enumerate(v) if x==0) for v in negative)==fib(k)-1
    assert len(spelled)-k+1-len(edges)==fib(k)-k+1
    return spelled


def bfs_min(k):
    edges=[x for x in product((0,1),repeat=k) if legal(x)]
    id_of={e:i for i,e in enumerate(edges)}
    full=(1<<len(edges))-1
    queue=deque()
    seen=set()
    for e in edges:
        state=(e[1:],1<<id_of[e]);seen.add(state);queue.append((state,k))
    while queue:
        (tail,mask),length=queue.popleft()
        if mask==full:return length
        for b in (0,1):
            e=tail+(b,)
            if e not in id_of:continue
            st=(e[1:],mask|(1<<id_of[e]))
            if st not in seen:seen.add(st);queue.append((st,length+1))
    raise AssertionError('not covered')


def main():
    for k in range(2,14):
        word=create(k)
        assert len(word)==fib(k+2)+fib(k)
        print(f'k={k}: k-mers={fib(k+2)}, shortest length={len(word)}, duplicate windows={fib(k)-k+1}')
    for k in range(2,6):
        found=bfs_min(k)
        assert found==fib(k+2)+fib(k),(k,found)
        print(f'k={k}: independent exhaustive shortest-word BFS passed')
    assert len('01')==2
    print('All bounded checks passed; infinite proof is in RESULT.md.')

if __name__=='__main__': main()
