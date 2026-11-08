#!/usr/bin/env python3
"""Independent adjacency-neighborhood simulator and complete small-n check."""

def graph(n):
    adj = [list(range(1,n+1))]
    for i in range(n):
        adj.append([0,1+((i-1)%n),1+((i+1)%n)])
    return adj

def next_state(s, adj):
    n = len(adj)-1
    out = [0]*(n+1)
    tally = sum(s[v] for v in adj[0])
    out[0] = 1 if 2*tally<n else (0 if 2*tally>n else s[0])
    for i in range(1,n+1):
        out[i] = int(sum(s[v] for v in adj[i]) >= 2)
    return tuple(out)

def num_eight(n):
    adj = graph(n)
    ans = 0
    for state in range(1<<(n+1)):
        original = tuple((state>>i)&1 for i in range(n+1))
        cur = original
        for _ in range(4):
            cur = next_state(cur,adj)
        if cur == original:
            continue
        for _ in range(4):
            cur = next_state(cur,adj)
        ans += cur == original
    return ans

if __name__ == '__main__':
    data=[]
    for n in range(3,13):
        v=num_eight(n)
        assert v==(288 if n==12 else 0)
        data.append((n,v))
    print('graph_based_primitive_eight_by_rim_size=' + repr(data))
    print('INDEPENDENT_GRAPH_EXHAUSTIVE_OK')
