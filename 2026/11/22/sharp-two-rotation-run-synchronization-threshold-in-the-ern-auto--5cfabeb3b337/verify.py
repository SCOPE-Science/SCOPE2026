#!/usr/bin/env python3
"""Exact finite checks of the abstract block-renormalization theorem."""
from collections import deque

def apply(n, states, word):
    s = set(states)
    for c in word:
        if c == 'a':
            s = {(i+1) % n for i in s}
        elif c == 'b':
            s = {1 if i==0 else i for i in s}
        else:
            raise ValueError(c)
    return s

def witness(n):
    N = n-1
    x = 'ab'
    y = 'aab'
    e = y + x * (N-2)
    return 'b' + e + (x+e) * (N-2)

def check(n):
    N=n-1
    Q=set(range(n)); S=set(range(1,n))
    x='ab';y='aab';e=y+x*(N-2)
    assert apply(n,Q,'b')==S
    for i in S:
        assert apply(n,{i},x)=={i+1 if i<N else 1}
        assert apply(n,{i},e)=={N-1 if i==N else i}
    assert 'aaa' not in witness(n)
    assert len(witness(n))==2*n*n-5*n+1
    assert len(apply(n,Q,witness(n)))==1
    if n<=15:
      # Rank of every admissible word without 'aa' from reachable no-aa states.
      seen={(frozenset(Q),0)}; queue=deque(seen)
      while queue:
        s,prev_a=queue.popleft()
        for ch in 'ab':
          if prev_a and ch=='a':continue
          t=(frozenset(apply(n,s,ch)),int(ch=='a'))
          if t not in seen:
            seen.add(t);queue.append(t)
          assert len(t[0])>=n-1
    return len(witness(n))

if __name__=='__main__':
    for n in range(3,101):
        length=check(n)
        if n<=12: print(n,length)
    print('BLOCK_RENORMALIZATION_OK n=3..100')
