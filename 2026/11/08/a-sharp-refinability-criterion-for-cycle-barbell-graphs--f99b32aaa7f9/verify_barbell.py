#!/usr/bin/env python3
"""Exact finite checks for color-refinement orbit rigidity of cycle barbells.

Only standard-library imports. Each graph is two vertex-disjoint cycles of
length m,n joined at designated vertices by an edge-path of length d.
"""
from collections import Counter


def barbell(m, n, d):
    assert m >= 3 and n >= 3 and d >= 1
    size = m + n + d - 1
    adj = [set() for _ in range(size)]
    def edge(u,v):
        assert u != v and v not in adj[u]
        adj[u].add(v); adj[v].add(u)
    for i in range(m): edge(i, (i+1) % m)
    for i in range(n): edge(m+i, m+(i+1)%n)
    path = [0] + list(range(m+n, size)) + [m]
    for u,v in zip(path,path[1:]): edge(u,v)
    assert sum(len(a) for a in adj) == 2 * (m+n+d)
    return adj


def refine(adj):
    colors = (0,) * len(adj)
    steps = 0
    while True:
        keys = [(colors[v], tuple(sorted(Counter(colors[w] for w in adj[v]).items())))
                for v in range(len(adj))]
        code = {x: i for i,x in enumerate(sorted(set(keys)))}
        next_colors = tuple(code[k] for k in keys)
        if len(set(next_colors)) == len(set(colors)):
            return colors, steps
        colors = next_colors
        steps += 1
        assert steps < len(adj)


def predicted_orbits(m,n,d):
    L = []
    tag_l = 'L' if m != n else 'C'
    tag_r = 'R' if m != n else 'C'
    for i in range(m): L.append((tag_l, min(i,m-i)))
    for i in range(n): L.append((tag_r, min(i,n-i)))
    for i in range(1,d): L.append(('P', i if m!=n else min(i,d-i)))
    return L


def predicted_stable(m,n,d):
    # All subdivided paths of degree-3 to degree-3 are indistinguishable
    # precisely when all three lengths agree.
    if m != n or d != m:
        return predicted_orbits(m,n,d)
    L = []
    for i in range(m): L.append(('B', min(i,m-i)))
    for i in range(n): L.append(('B', min(i,n-i)))
    for i in range(1,d): L.append(('B', min(i,d-i)))
    return L


def partition_equal(a,b):
    assert len(a)==len(b)
    ax = {}
    bx = {}
    for i,(x,y) in enumerate(zip(a,b)):
        if x in ax:
            if ax[x] != y:return False
        else:ax[x]=y
        if y in bx:
            if bx[y] != x:return False
        else:bx[y]=x
    return True


def orbit_count(m,n,d):
    if m != n:
        return d + 1 + m//2 + n//2
    return 1 + m//2 + d//2


def stable_count(m,n,d):
    if m==n==d:
        return 1 + m//2
    return orbit_count(m,n,d)



def exact_automorphism_orbits(adj, colors):
    """Enumerate all adjacency-preserving permutations, with safe color pruning."""
    size = len(adj)
    buckets = {}
    for i, c in enumerate(colors):
        buckets.setdefault(c, []).append(i)
    assignment = {}
    taken = set()
    seen_orbits = list(range(size))
    def find(x):
        while seen_orbits[x] != x:
            x = seen_orbits[x]
        return x
    seen = [0]
    def search():
        if len(assignment) == size:
            seen[0] += 1
            for v, w in assignment.items():
                seen_orbits[find(v)] = find(w)
            return
        best = None
        choices = None
        for v in range(size):
            if v in assignment: continue
            cands = [w for w in buckets[colors[v]] if w not in taken
                     and all(((u in adj[v]) == (x in adj[w]))
                             for u,x in assignment.items())]
            if not cands: return
            if choices is None or len(cands) < len(choices):
                best,choices = v,cands
        for w in choices:
            assignment[best] = w
            taken.add(w)
            search()
            taken.remove(w)
            del assignment[best]
    search()
    assert seen[0] > 0
    return [find(i) for i in range(size)]


def run():
    cases = 0
    defects = []
    max_stabilization = 0
    for m in range(3,18):
        for n in range(m,18):
            for d in range(1,24):
                adj = barbell(m,n,d)
                colors, steps = refine(adj)
                orbits = predicted_orbits(m,n,d)
                stable = predicted_stable(m,n,d)
                assert partition_equal(colors,stable), (m,n,d,colors,stable)
                assert len(set(colors)) == stable_count(m,n,d), (m,n,d)
                assert len(set(orbits)) == orbit_count(m,n,d), (m,n,d)
                # A refinement color class cannot split an automorphism orbit.
                for i in range(len(colors)):
                    for j in range(i):
                        assert orbits[i]!=orbits[j] or colors[i]==colors[j]
                nonrefinable = not partition_equal(colors,orbits)
                assert nonrefinable == (m==n==d), (m,n,d)
                if nonrefinable: defects.append((m,n,d))
                max_stabilization = max(max_stabilization, steps)
                cases += 1
    print('VERIFIED_CASES', cases)
    print('NONREFINABLE_PARAMETERS', defects)
    print('MAX_STRICT_ROUNDS', max_stabilization)
    # Independent basic automorphism property: explicit flip involutions.
    # For symmetric length m=n=d, color-equivalent near-hub vertices of
    # bridge and cycle have different bridge memberships (cut vs non-cut).
    for k in range(3,18):
        adj=barbell(k,k,k)
        colors,_=refine(adj)
        assert colors[1]==colors[2*k]  # bridge interior adjacent to left hub
    automorphism_cases = 0
    for m in range(3,7):
        for n in range(m,7):
            for d in range(1,8):
                adj = barbell(m,n,d)
                colors, _ = refine(adj)
                exact = exact_automorphism_orbits(adj, colors)
                assert partition_equal(exact,predicted_orbits(m,n,d)), (m,n,d)
                automorphism_cases += 1
    print('EXACT_AUTOMORPHISM_CASES',automorphism_cases)
    print('VERIFY_OK')

if __name__=='__main__':run()
