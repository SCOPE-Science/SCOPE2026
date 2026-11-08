"""Finite checks for static and adaptive edge-membership shattering on wheel cycles.

Usage: python verify_wheel.py wheel_r5_tree.json
This verification script is self-contained and uses only Python's standard library.
Finite checks corroborate, but do not establish, the infinite-family theorem.
"""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
import sys


def graph_cycles(r):
    # Enumerate elementary cycles independently from adjacency, not a cycle formula.
    n = r + 1
    hub = r
    edges = [(i, (i + 1) % r) for i in range(r)] + [(hub, i) for i in range(r)]
    adjacency = [[] for _ in range(n)]
    for e, (a,b) in enumerate(edges):
        adjacency[a].append((b,e))
        adjacency[b].append((a,e))
    found = set()
    for start in range(n):
        def explore(u, visited, used_edges):
            for v,e in adjacency[u]:
                if v == start and len(used_edges) >= 2:
                    found.add(sum(1 << f for f in used_edges + [e]))
                elif v not in visited and v > start:
                    explore(v, visited | {v}, used_edges + [e])
        explore(start, {start}, [])
    return sorted(found)


def vc_dimension(cycles, ground):
    counts = {}
    last = 0
    for size in range(1, min(5, ground+1)):
        count = 0
        for support in combinations(range(ground), size):
            traces = {sum(((c >> e)&1) << j for j,e in enumerate(support)) for c in cycles}
            if len(traces) == (1 << size):
                count += 1
        counts[size] = count
        if count:
            last = size
        else:
            break
    return last, counts


def littlestone(cycles, ground):
    masks = [sum(1 << i for i,c in enumerate(cycles) if (c >> e)&1) for e in range(ground)]
    @lru_cache(None)
    def recur(S):
        best=0
        for m in masks:
            left = S & m
            right = S & ~m
            if left and right:
                best = max(best, 1 + min(recur(left), recur(right)))
        return best
    return recur((1 << len(cycles))-1)


def verify_tree(tree, cycles, height, path=()):
    if not height:
        assert isinstance(tree, dict) and set(tree) == {'witness'}
        witness = tree['witness']
        assert witness in cycles, (witness, 'not a wheel cycle')
        assert all(((witness >> query)&1) == answer for query,answer in path)
        return [witness]
    assert set(tree)=={'query','zero','one'}
    query=tree['query']
    assert isinstance(query,int) and 0<=query<10
    assert query not in [q for q,a in path]
    zeros=verify_tree(tree['zero'],cycles,height-1,path+((query,0),))
    ones=verify_tree(tree['one'],cycles,height-1,path+((query,1),))
    return zeros+ones


def main():
    certificate_path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('wheel_r5_tree.json')
    certificate=json.loads(certificate_path.read_text())
    assert certificate['r']==5 and certificate['depth']==4
    confirmed={}
    for r in range(3,9):
        cycles=graph_cycles(r)
        assert len(cycles)==1+r*(r-1), (r,len(cycles))
        vc, counts = vc_dimension(cycles,2*r)
        assert vc == (2 if r==3 else 3), (r,vc)
        online=littlestone(cycles,2*r)
        if r in (3,4,5,6,7,8):
            assert online == {3:2,4:3,5:4,6:4,7:5,8:5}[r], (r,online)
        confirmed[r]={'concepts':len(cycles),'vc':vc,'ldim':online,'shattered_counts':counts}
    leaves=verify_tree(certificate['tree'],graph_cycles(5),4)
    assert len(leaves)==16 and len(set(leaves))==16
    assert confirmed[5]['ldim']==4
    print(json.dumps(confirmed,sort_keys=True))
    print('WHEEL_CYCLE_SHATTERING_CHECKS_PASS; W6_tree_depth=4; leaf_witnesses=16')

if __name__=='__main__':
    main()
