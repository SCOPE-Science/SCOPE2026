"""Independent enumerator: symmetric-difference components and formal species recurrence.
No construction or traversal of a reconfiguration graph.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from math import comb, factorial

@lru_cache(None)
def pairings(vertices):
    if not vertices:
        return ((),)
    a = vertices[-1]
    return tuple(((a, b),) + rest for i, b in enumerate(vertices[:-1])
                 for rest in pairings(vertices[:i] + vertices[i+1:-1]))

def polynomial(m):
    # C_t: cycle components and unchanged matched pairs.
    C = [{0: 1}]
    for t in range(1, m + 1):
        row = defaultdict(int)
        for exponent, count in C[t-1].items():
            row[exponent] += count
        for j in range(2, t+1):
            multiplier = comb(t-1, j-1) * 2**(j-1) * factorial(j-1)
            for exponent, count in C[t-j].items():
                row[exponent + j+1] += multiplier * count
        C.append(dict(row))
    out = defaultdict(int)
    for k in range(m+1):
        multiplier = comb(m, k)*2**k*factorial(k)
        for exponent, count in C[m-k].items():
            out[exponent+k] += multiplier*count
    return [out[i] for i in range(max(out)+1)]

def component_distance(source, target):
    sm, tm = set(map(frozenset, source)), set(map(frozenset, target))
    xor = sm ^ tm
    graph = defaultdict(set)
    for e in xor:
        a,b = tuple(e)
        graph[a].add(b);graph[b].add(a)
    seen=set();cycle_count=0
    for v in graph:
        if v in seen:continue
        todo=[v];seen.add(v);comp=[]
        while todo:
            x=todo.pop();comp.append(x)
            for y in graph[x]:
                if y not in seen:
                    seen.add(y);todo.append(y)
        if all(len(graph[x])==2 for x in comp):cycle_count += 1
        else:assert len([x for x in comp if len(graph[x])==1])==2
    return len(sm-tm)+cycle_count

def verify(m):
    n=2*m+1
    source = tuple((2*i, 2*i+1) for i in range(m))
    hist=Counter()
    for h in range(n):
        others=tuple(x for x in range(n) if x != h)
        for P in pairings(others):
            hist[component_distance(source,P)] +=1
    direct=[hist[i] for i in range(max(hist)+1)]
    species=polynomial(m)
    assert direct==species,(m,direct,species)
    assert sum(species)==factorial(n)//(2**m*factorial(m))
    assert len(species)-1==m+m//2
    print(f'm={m} n={n} component_distance_layers={direct} '
          f'species_layers={species} diameter={len(species)-1}')

if __name__ == '__main__':
    for m in range(1, 6):verify(m)
