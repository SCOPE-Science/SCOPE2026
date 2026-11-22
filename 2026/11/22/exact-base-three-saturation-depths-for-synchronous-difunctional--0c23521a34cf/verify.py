#!/usr/bin/env python3
"""Independent finite checks for synchronous Z-closure of a bipartite relation.

No external packages.  The procedural closure and BFS-distance predictions are
implemented separately.  Run: python3 verify.py
"""
from collections import deque
from itertools import product
from math import ceil, log
import random


def step(mask, a, b):
    # Direct Z-shaped rule over triples of current edges.
    out = mask
    for x in range(a):
        ys = [y for y in range(b) if mask >> (x * b + y) & 1]
        for w in range(a):
            if any(mask >> (w * b + y) & 1 for y in ys):
                for z in ys:
                    out |= 1 << (w * b + z)
    return out


def bfs_distances(mask, a, b):
    graph = [[] for _ in range(a+b)]
    for i in range(a):
        for j in range(b):
            if mask >> (i*b+j) & 1:
                graph[i].append(a+j)
                graph[a+j].append(i)
    dist = [[-1]*(a+b) for _ in range(a+b)]
    for s in range(a+b):
        dist[s][s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if dist[s][v] == -1:
                    dist[s][v] = dist[s][u] + 1
                    queue.append(v)
    return dist


def expected_layer(dist, a, b, radius):
    return sum(1 << (i*b+j)
               for i in range(a) for j in range(b)
               if 0 < dist[i][a+j] <= radius)


def check_instance(mask, a, b):
    D = bfs_distances(mask, a, b)
    current = mask
    radius = 1
    rounds = 0
    while True:
        predicted = expected_layer(D, a, b, radius)
        assert predicted == current, (a, b, mask, rounds, predicted, current)
        new = step(current, a, b)
        if new == current:
            break
        current = new
        radius *= 3
        rounds += 1
        assert rounds <= a+b
    farthest = max((D[i][a+j] for i in range(a) for j in range(b)), default=-1)
    target = 0
    p = 1
    while p < farthest:
        p *= 3
        target += 1
    assert rounds == target, (a,b,mask,rounds,target)
    return rounds



def anchored_step(original, current, a, b):
    # Alternative standard construction: two outer edges held at initial R.
    out = 0
    for x in range(a):
        for y in range(b):
            if original >> (x*b+y) & 1:
                for w in range(a):
                    if current >> (w*b+y) & 1:
                        for z in range(b):
                            if original >> (w*b+z) & 1:
                                out |= 1 << (x*b+z)
    return out


def check_anchored(mask, a, b):
    D = bfs_distances(mask, a, b)
    current = mask
    n=0
    while True:
        assert current == expected_layer(D, a, b, 2*n+1), ('anchored', a,b,mask,n)
        nxt=anchored_step(mask,current,a,b)
        if nxt==current:
            return n
        current=nxt
        n+=1
        assert n<=a+b

def path_mask(k):
    # Alternating path on k vertices in each of two shores: 2k-1 edges.
    # A0-B0-A1-B1-...-A(k-1)-B(k-1)
    result=0
    for i in range(k):
        result |= 1 << (i*k+i)
        if i+1 < k:
            result |= 1 << ((i+1)*k+i)
    return result


def main():
    tested=0
    for a,b in [(1,1),(1,5),(2,3),(3,3),(3,4),(4,4)]:
        max_seen=0
        for mask in range(1 << (a*b)):
            actual = check_instance(mask,a,b)
            max_seen=max(max_seen,actual)
            tested+=1
            if a*b<=12 or (a==4 and b==4 and mask%97==0):
                check_anchored(mask,a,b)
        radius=1
        maximum=0
        while radius < 2*min(a,b)-1:
            radius *=3
            maximum+=1
        assert max_seen==maximum,(a,b,max_seen,maximum)
    for k in range(1,26):
        assert check_instance(path_mask(k),k,k) == next(t for t in range(20) if 3**t>=2*k-1)
        assert check_anchored(path_mask(k),k,k) == k-1
    rng=random.Random(20260922)
    for a,b in [(5,5),(4,7),(8,3),(8,8)]:
        for _ in range(350):
            mask=sum((1 << j) for j in range(a*b) if rng.randrange(7)<rng.randrange(7))
            check_instance(mask,a,b)
            if a*b<=25: check_anchored(mask,a,b)
            tested+=1
    print('VERIFY_OK', tested, 'exhaustive and random matrices; 25 sharp paths; anchored-rule comparison')


if __name__=='__main__':
    main()
