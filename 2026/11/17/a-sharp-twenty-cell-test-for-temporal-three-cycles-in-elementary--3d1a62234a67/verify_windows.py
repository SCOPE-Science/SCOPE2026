"""Exact finite graph certificate for primitive temporal-three ECA points."""
from collections import Counter, deque
import json


def local3(rule, word):
    a = [(word >> i) & 1 for i in range(6, -1, -1)]
    for _ in range(3):
        a = [(rule >> (4*a[i] + 2*a[i+1] + a[i+2])) & 1
             for i in range(len(a)-2)]
    return a[0]


def minimal_cycle(rule):
    adj = [[] for _ in range(64)]
    for word in range(128):
        initial = (word >> 3) & 1
        if local3(rule, word) != initial:
            continue
        first = (rule >> ((word >> 2) & 7)) & 1
        adj[word >> 1].append((word & 63, first != initial, word))
    optimum = None
    for source in range(64):
        for target, marked, firstword in adj[source]:
            if not marked:
                continue
            queue = deque([target]); distance = {target:0}; parent = {}
            while queue and source not in distance:
                vertex = queue.popleft()
                for nex, _, word in adj[vertex]:
                    if nex not in distance:
                        distance[nex] = distance[vertex]+1
                        parent[nex] = (vertex, word)
                        queue.append(nex)
            if source in distance:
                path = []
                vertex = source
                while vertex != target:
                    vertex, word = parent[vertex]
                    path.append(word)
                edgewords = [firstword]+path[::-1]
                if optimum is None or len(edgewords) < len(optimum):
                    optimum = edgewords
    return optimum


def global_step(rule, word):
    n = len(word)
    return ''.join(str((rule >> (4*int(word[(i-1)%n])+2*int(word[i])+int(word[(i+1)%n]))) & 1)
                   for i in range(n))


def produce():
    minima = []
    witnesses = {}
    for rule in range(256):
        path = minimal_cycle(rule)
        if path is None:
            minima.append(None)
            continue
        n = len(path)
        x = ''.join(str((word >> 3) & 1) for word in path)
        if global_step(rule,global_step(rule,global_step(rule,x))) != x:
            raise AssertionError((rule,'false three-return',x))
        if global_step(rule,x) == x:
            raise AssertionError((rule,'fixed',x))
        minima.append(n)
        witnesses[str(rule)] = x
    counts=Counter(minima)
    result={'minimum_ring_length':minima,
            'distribution':{str(k):counts[k] for k in sorted(counts,key=lambda x:(x is None,x or 0))},
            'max_finite_minimum':max(k for k in minima if k is not None),
            'maximizers':[i for i,m in enumerate(minima) if m == max(k for k in minima if k is not None)],
            'rule_105_witness':witnesses['105'],
            'number_witnessed_rules':len(witnesses)}
    return result

if __name__=='__main__':
    print(json.dumps(produce(),sort_keys=True,separators=(',',':')))
