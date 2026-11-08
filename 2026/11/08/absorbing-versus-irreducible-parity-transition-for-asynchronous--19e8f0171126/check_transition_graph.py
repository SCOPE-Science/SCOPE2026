"""Exhaustive transition-graph check for zero-temperature minority on squared cycles.
Uses the closed neighborhood with tie retention, and only Python's standard library.
These finite checks do not replace the all-length argument.
"""
from collections import deque


def predicted(n):
    r = n % 4
    return (4 if r == 0 else n*(n*n+23)//12 if r == 1
            else n*n//2 if r == 2 else 2*n)


def verify(n):
    mask = (1 << n) - 1
    adj = [tuple((i + j) % n for j in (-2, -1, 1, 2)) for i in range(n)]
    edge = [(i, (i+j) % n) for i in range(n) for j in (1,2)]
    def cut(s):
        return sum(((s >> i) ^ (s >> j)) & 1 for i,j in edge)
    def canflip(s,i):
        bit = (s >> i) & 1
        same = sum(((s >> j) & 1) == bit for j in adj[i])
        return same >= 2
    maxcut = -1
    ground = []
    for s in range(1 << n):
        c = cut(s)
        if c > maxcut:
            maxcut = c; ground = [s]
        elif c == maxcut:
            ground.append(s)
    assert len(ground) == predicted(n), (n, len(ground), predicted(n))
    expected_cut = n + ((n//2) if n % 4 == 0 else
                        ((n-3)//2) if n % 4 == 1 else
                        (n-2)//2 if n % 4 == 2 else (n-1)//2)
    assert maxcut == expected_cut, (n,maxcut,expected_cut)
    ground_set = set(ground)
    for s in ground:
        for i in range(n):
            if canflip(s,i):
                assert (s ^ (1 << i)) in ground_set
    if n % 4 == 0:
        assert len(ground)==4
        assert all(not any(canflip(s,i) for i in range(n)) for s in ground)
    else:
        seen={ground[0]}; q=deque([ground[0]])
        while q:
            s=q.popleft()
            for i in range(n):
                if canflip(s,i):
                    t=s^(1 << i)
                    if t in ground_set and t not in seen:
                        seen.add(t); q.append(t)
        assert seen == ground_set, (n,len(seen),len(ground_set))
    # Reverse reachability checks whether every initial state can reach the recurrent region.
    seen=set(ground); q=deque(ground)
    while q:
        s=q.popleft()
        for i in range(n):
            predecessor=s^(1 << i)
            if predecessor not in seen and canflip(predecessor,i):
                seen.add(predecessor);q.append(predecessor)
    assert len(seen)==1 << n, (n,len(seen),1<<n)
    return (n,1<<n,maxcut,len(ground),4 if n%4==0 else 1)

if __name__=='__main__':
    total=0
    for n in range(5,17):
        result=verify(n);total+=result[1]
        print('n=%d states=%d maxcut=%d recurrent_states=%d recurrent_classes=%d'%result)
    print('PASS: %d starting states across n=5..16; exact max-cut counts, all-state reachability, and ground-class topology'%total)
