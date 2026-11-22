#!/usr/bin/env python3
"""Finite checks for a rotation-run constrained Černý reset theorem."""
from collections import deque

def letters(n):
    return tuple((i + 1) % n for i in range(n)),tuple(0 if i == n-1 else i for i in range(n))

def constructed_word(n):
    assert n % 2 == 0 and n >= 4
    m = n // 2
    chunks = []
    for j in range(1,n-1):
        if j % 2:
            lengths = [2]*(m-1) + [1]
        else:
            r = j//2
            lengths = [2]*(r-1)+[1]+[2]*(m-r)
        assert sum(lengths) == n-1
        chunks.append(''.join('a'*s+'b' for s in lengths))
    return 'b'+''.join(chunks)

def apply(n,S,word):
    a,b=letters(n)
    for c in word:
        f=a if c=='a' else b
        S={f[i] for i in S}
    return S

def optimal_length(n):
    assert n%2==0
    m=n//2
    return 6*m*m-8*m+3

def bfs(n):
    """Exact shortest path on subset x run-state graph."""
    A,B=letters(n)
    full=(1<<n)-1
    def image(s,fn):
        v=0
        while s:
            x=s&-s
            v |= 1<<fn[x.bit_length()-1]
            s-=x
        return v
    ta=[image(s,A) for s in range(1<<n)]
    tb=[image(s,B) for s in range(1<<n)]
    seen={(full,0):0}
    todo=deque([(full,0)])
    while todo:
        s,run=todo.popleft()
        d=seen[(s,run)]
        if s.bit_count()==1: return d
        nxt=[(ta[s],run+1),(tb[s],0)]
        for z in nxt:
            if z[1]>2 or z in seen: continue
            seen[z]=d+1;todo.append(z)
    raise AssertionError('No permitted reset word')

def verify():
    for n in range(4,102,2):
        w=constructed_word(n)
        assert 'aaa' not in w
        assert len(w)==optimal_length(n)
        assert apply(n,set(range(n)),w)=={0}
        m=n//2
        S=apply(n,set(range(n)),'b')
        assert S==set(range(n-1))
        blocks=w[1:].split('b')
        # One final b follows each run; boundary grouping by n-1 rotations.
        chunks=[];a_count=0;chunk=''
        for c in w[1:]:
            chunk+=c
            if c=='a':a_count+=1
            if c=='b' and a_count%(n-1)==0:
                chunks.append(chunk);chunk=''
        assert len(chunks)==n-2 and not chunk
        for j,chunk in enumerate(chunks,1):
            S=apply(n,S,chunk)
            if j%2:
                r=(j+1)//2
                target={0}|set(range(1,n-2*r,2))
            else:
                r=j//2
                target=set(range(0,n-2*r,2))
            assert S==target,(n,j,S,target)
    for n in (4,6,8,10,12,14,16):
        d=bfs(n)
        assert d==optimal_length(n),(n,d,optimal_length(n))
    print('VERIFY_OK even n=4..100, independent exact BFS n=4..16')
if __name__=='__main__': verify()
