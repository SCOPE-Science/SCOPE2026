#!/usr/bin/env python3
"""Exact checks for Boolean connected-vertex-set convolution on open ladders.

The checker is supplementary: the general theorem is proved by a recurrence
and a four-state periodic signed construction in RESULT.md.
"""
from itertools import product


def adjacency(n):
    graph = [[] for _ in range(2*n)]
    for col in range(n):
        a, b = col, n+col
        graph[a].append(b)
        graph[b].append(a)
        for v in (a, b):
            if col:
                graph[v].append(v-1)
                graph[v-1].append(v)
    return graph


def connected(mask, graph):
    if not mask:
        return False
    start = (mask & -mask).bit_length()-1
    found = 1 << start
    stack = [start]
    while stack:
        u = stack.pop()
        for v in graph[u]:
            bit = 1 << v
            if mask & bit and not found & bit:
                found |= bit
                stack.append(v)
    return found == mask


def fwht(values):
    a = values[:]
    size = len(a)
    h = 1
    while h < size:
        for block in range(0, size, 2*h):
            for k in range(block, block+h):
                x, y = a[k], a[k+h]
                a[k], a[k+h] = x+y, x-y
        h *= 2
    return a


def signed_transfer(signs, initial=(0,0,0,0)):
    t,b,d,z=initial
    for alpha,beta in signs:
        nt=alpha*(1+t+d)
        nb=beta*(1+b+d)
        nd=alpha*beta*(1+t+b+d)
        z += nt+nb+nd
        t,b,d=nt,nb,nd
    return (t,b,d,z)


def signs_from_freq(freq,n):
    return [(-1 if freq>>i & 1 else 1,
             -1 if freq>>(n+i)&1 else 1) for i in range(n)]


def certified_signs(n):
    seed = [(1,-1), (1,1), (1,-1)]
    period = [(1,-1), (1,-1), (-1,1), (-1,-1)]
    return (seed+period*((max(0,n-3)+3)//4))[:n]


def pell_count(n):
    a = [0,3,7]
    for k in range(3,n+1):
        a.append(2*a[-1]+a[-2])
    return sum((n-k+1)*a[k] for k in range(1,n+1))


def expected_special(n):
    if n in (1,2):return -1
    return {3:0,0:0,1:1,2:-1}[n%4]


def main():
    checks = 0
    for n in range(1,9):
        graph=adjacency(n)
        f=[int(connected(mask,graph)) for mask in range(1<<(2*n))]
        C=sum(f)
        assert C == pell_count(n), (n,C,pell_count(n)); checks+=1
        spectrum=fwht(f)
        assert spectrum[0] == C;checks+=1
        assert (C % 2 == n*(n+1)//2 % 2);checks+=1
        for freq,actual in enumerate(spectrum):
            predicted=signed_transfer(signs_from_freq(freq,n))[3]
            assert actual == predicted, (n,freq,actual,predicted)
            checks+=1
            if n%4 in (1,2):
                assert actual != 0;checks+=1
        sign=certified_signs(n)
        z=signed_transfer(sign)[3]
        assert z==expected_special(n), (n, z)
        checks+=1
        freq = sum((1<<i if a==-1 else 0) | (1<<(n+i) if b==-1 else 0)
                   for i,(a,b) in enumerate(sign))
        assert spectrum[freq]==z;checks+=1
        if n%4 in (1,2):
            assert min(abs(x) for x in spectrum)==1;checks+=1
        else:
            assert 0 in spectrum;checks+=1
        print('rungs',n,'connected_sets',C,'zeros',spectrum.count(0),
              'min_nonzero',min(abs(x) for x in spectrum if x),'special',z)

    assert signed_transfer(certified_signs(3)) == (2,0,-1,0);checks+=1
    period = [(1,-1), (1,-1), (-1,1), (-1,-1)]
    states = [(2,0,-1,0),(2,0,-2,0),(1,1,-1,1),(-1,1,-2,-1)]
    for k in range(1,5):
        actual=signed_transfer(period[:k],states[0])
        assert actual == states[k%4], (k,actual,states[k%4])
        checks+=1
    for n in range(1,401):
        result=signed_transfer(certified_signs(n))
        assert result[3]==expected_special(n), (n,result)
        checks+=1
        if n>=3:
            assert result==states[(n-3)%4], (n,result,states[(n-3)%4])
            checks+=1
        assert pell_count(n)%2==n*(n+1)//2%2
        checks+=1
    print('PASS',checks,'exact assertions')


if __name__=='__main__':
    main()
