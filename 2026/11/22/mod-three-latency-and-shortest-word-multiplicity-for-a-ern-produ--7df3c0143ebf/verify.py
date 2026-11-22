#!/usr/bin/env python3
"""Independent finite checks for the simultaneous Cerny reset formula.
Python standard library only; prints a certificate of tested ranges.
"""
from collections import deque

def step(s, n, ch):
    if ch == 'a':
        return ((s << 1) & ((1 << n) - 1)) | (s >> (n-1))
    return (s & ~1) | (2 if s & 1 else 0)

def apply_full(n, w):
    s=(1<<n)-1
    for ch in w: s=step(s,n,ch)
    return s

def canonical(n):
    return 'b'+('a'*(n-1)+'b')*(n-2)

def additional(n):
    return 'b'+('a'*(n-1)+'b')*(n-3)+'a'*(n-3)+'b'+'aa'+'b'

def predicted(n):
    if n%3==0: return (n-1)**2,1
    if n%3==1:
        k=(n-1)//3
        return (n-1)**2+1,2*k*(3*k-2)
    k=(n-2)//3
    return (n-1)**2+1,k*(3*k-1)

def exact_bfs(n):
    # all nonempty subset pairs for C_n and C_3; no mathematical reductions
    size=1 << (n+3)
    d=[-1]*size
    ways=[0]*size
    start=((1<<n)-1)|(7<<n)
    d[start]=0; ways[start]=1
    queue=deque([start]); goal_depth=None; total=0; visited=0
    while queue:
        state=queue.popleft()
        depth=d[state]
        if goal_depth is not None and depth>goal_depth:break
        visited+=1
        x=state & ((1<<n)-1); y=state>>n
        if x.bit_count()==1 and y.bit_count()==1:
            if goal_depth is None:goal_depth=depth
            if depth==goal_depth:total+=ways[state]
            continue
        if goal_depth is not None:continue
        for ch in 'ab':
            nxt=step(x,n,ch)|(step(y,3,ch)<<n)
            if d[nxt]<0:
                d[nxt]=depth+1;ways[nxt]=ways[state];queue.append(nxt)
            elif d[nxt]==depth+1:
                ways[nxt]+=ways[state]
    return goal_depth,total,visited

def classified(n):
    """Check the known one-letter-slack family independently by replay."""
    w=canonical(n); a=[('a'+w), (w+'a'),(w+'b')]
    for j in range(1,n-1):
        for t in range(n-1):
            if t==j:continue
            a.append('b'+('a'*(n-1)+'b')*(j-1)+'a'*t+'b'+'a'*(n-1-t)+'b'+('a'*(n-1)+'b')*(n-2-j))
    assert len(a)==len(set(a))==(n-2)**2+3
    assert all(len(x)==(n-1)**2+1 and apply_full(n,x).bit_count()==1 for x in a)
    return sum(apply_full(3,x).bit_count()==1 for x in a)

if __name__=='__main__':
    for n in range(3,17):
        L,count,visited=exact_bfs(n)
        exp_L,exp_count=predicted(n)
        assert (L,count)==(exp_L,exp_count),(n,L,count,exp_L,exp_count)
        assert len(canonical(n))==(n-1)**2
        assert apply_full(n,canonical(n)).bit_count()==1
        assert len(additional(n))==(n-1)**2+1
        assert apply_full(n,additional(n)).bit_count()==1
        assert apply_full(3,additional(n)).bit_count()==1
        if n%3==0:assert apply_full(3,canonical(n)).bit_count()==1
        else:assert apply_full(3,canonical(n)).bit_count()>1
        if n<=13 and n%3!=0:assert classified(n)==count
        print(f'n={n:2d} shortest={L:3d} count={count:4d} explored={visited:6d}')
    for n in range(17,201):
        assert apply_full(n,canonical(n)).bit_count()==1
        assert apply_full(n,additional(n)).bit_count()==1
        assert apply_full(3,additional(n)).bit_count()==1
        assert (apply_full(3,canonical(n)).bit_count()==1)==(n%3==0)
    print('CHECK_OK: exhaustive subset-pair shortest-path counting n=3..16; explicit word checks n=3..200')
