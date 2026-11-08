#!/usr/bin/env python3
"""Exhaustive small-ring and explicit-witness checks for rank thresholds."""
from collections import deque

def step(s, letter, n):
    if letter == 'r':
        return ((s << 1) & ((1 << n) - 1)) | (s >> (n - 1))
    if letter == 'd':
        return (s & ~1) | 2 if (s & 1) else s
    raise ValueError(letter)

def target_rank(n):
    initial=(1<<n)-1
    queue=deque([initial]); distance={initial:0}
    while queue:
        s=queue.popleft()
        if s.bit_count() <= n//2-1:
            return distance[s],len(distance)
        for letter in 'rd':
            t=step(s,letter,n)
            if t not in distance:
                distance[t]=distance[s]+1
                queue.append(t)
    raise AssertionError('No compressed set')

def witness(m):
    return 'd'+'rrrd'+('rrd'*(m-2))+'rrrd'

def run_witness(n,w):
    s=(1<<n)-1
    for letter in w:
        s=step(s,letter,n)
    return s.bit_count()

def main():
    for n in range(6,19,2):
        t,states=target_rank(n)
        m=n//2
        assert t==3*m+3,(n,t)
        w=witness(m)
        assert len(w)==t and run_witness(n,w)==m-1,(n,w)
        print(f'BFS_OK n={n} threshold={t} visited={states}')
    for m in range(3,501):
        assert len(witness(m))==3*m+3
        assert run_witness(2*m,witness(m))==m-1
    print('VERIFY_OK bfs_n=6..18_even witnesses_m=3..500')
if __name__=='__main__':main()
