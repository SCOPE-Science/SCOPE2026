"""Independent support-block enumeration for three-vertex-path domination on T(n)."""
from itertools import combinations
from math import factorial

def local_paths(labels):
    """All P3 subgraphs whose three K_n edges use exactly four root labels."""
    E = tuple(combinations(labels, 2))
    out = set()
    stars = paths = 0
    for mid in E:
        near = [e for e in E if e != mid and set(e)&set(mid)]
        for ends in combinations(near, 2):
            all_edges = tuple(sorted((mid, *ends)))
            support = frozenset(v for e in all_edges for v in e)
            if len(support) != 4:continue
            # The center edge distinguishes edge-defined P3s.
            q = (mid,tuple(sorted(ends)))
            out.add(q)
            root_deg = {v:sum(v in e for e in all_edges) for v in support}
            if max(root_deg.values()) == 3:stars += 1
            elif sorted(root_deg.values()) == [1,1,2,2]:paths += 1
            else:raise AssertionError("non-tree 4-support")
    assert len(out)==24 and (stars, paths)==(12,12),(len(out),stars,paths)
    return len(out)

def partitions(items):
    """Enumerate unlabelled partitions of items into size-four blocks."""
    items=frozenset(items)
    if not items:
        yield ()
        return
    first=min(items)
    for rest in combinations(sorted(items-{first}),3):
        block=frozenset((first,*rest))
        for p in partitions(items-block):
            yield (block,)+p

assert local_paths((0,1,2,3))==24
for n in (5,9):
    k=(n-1)//4
    block_partitions=sum(1 for hole in range(n) for _ in partitions(set(range(n))-{hole}))
    observed=block_partitions*(24**k)
    expected=factorial(n)//factorial(k)
    assert observed==expected,(n,observed,expected)
    degree=119*k
    print(f"n={n} root_partitions={block_partitions} optimal_P3_collections={observed} degree={degree}")
for k in (3,4,5):
    n=4*k+1
    assert (factorial(n)//factorial(k)) % 24**k == 0
    print(f"n={n} closed_count={factorial(n)//factorial(k)} degree={119*k}")
print("SUPPORT-BLOCK CHECKS PASSED")
