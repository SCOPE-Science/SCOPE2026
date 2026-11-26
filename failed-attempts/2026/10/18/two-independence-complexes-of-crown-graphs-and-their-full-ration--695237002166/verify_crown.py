"""Independent finite checks for the crown-graph higher-independence theorem.

Standard-library-only. All labels and calculations are described in RESULT.md.
"""
import itertools
import json
from collections import Counter, deque


def faces_from_graph(n):
    adj = [set() for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    ans = set()
    for mask in range(1, 1 << (2*n)):
        remaining = {i for i in range(2*n) if (mask >> i) & 1}
        good = True
        while remaining:
            component = {remaining.pop()}
            queue = list(component)
            while queue:
                v = queue.pop()
                for w in adj[v] & remaining:
                    remaining.remove(w)
                    component.add(w)
                    queue.append(w)
            if len(component) > 2:
                good = False
                break
        if good:
            ans.add(mask)
    return ans


def structural_faces(n):
    ans = set()
    for mask in range(1, 1 << (2*n)):
        A = {i for i in range(n) if (mask >> i) & 1}
        B = {i for i in range(n) if (mask >> (i+n)) & 1}
        if not A or not B:
            ans.add(mask)
        elif len(A) == len(B) == 2 and A == B:
            ans.add(mask)
        elif len(A) == 1 and len(B) == 1:
            ans.add(mask)
        elif len(A) == 2 and len(B) == 1 and B <= A:
            ans.add(mask)
        elif len(A) == 1 and len(B) == 2 and A <= B:
            ans.add(mask)
    return ans


def matching(F, n):
    available = set(F)
    pairs = []
    for pivot in list(range(n)) + [n]:
        for small in sorted(available):
            big = small | (1 << pivot)
            if not ((small >> pivot) & 1) and big in available:
                available.remove(small)
                available.remove(big)
                pairs.append((small, big))
    return available, pairs


def verify_acyclic(F, pairs, n):
    pairset = set(pairs)
    adjacency = {m: [] for m in F}
    indeg = {m: 0 for m in F}
    count = 0
    for big in F:
        for v in range(2*n):
            if (big >> v) & 1:
                small = big ^ (1 << v)
                if small not in F:
                    continue
                if (small, big) in pairset:
                    src, dst = small, big
                else:
                    src, dst = big, small
                adjacency[src].append(dst)
                indeg[dst] += 1
                count += 1
    q = deque(m for m in F if indeg[m] == 0)
    visited = 0
    while q:
        p = q.popleft()
        visited += 1
        for t in adjacency[p]:
            indeg[t] -= 1
            if indeg[t] == 0:
                q.append(t)
    assert visited == len(F), 'acyclicity failure'
    return count


def rank_mod_two(vectors):
    pivots = {}
    for x in vectors:
        while x:
            k = x.bit_length() - 1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return len(pivots)


def homology_mod_two(F):
    by_dim = {}
    for m in F:
        by_dim.setdefault(m.bit_count()-1, []).append(m)
    maxd = max(by_dim)
    ranks = {}
    for d in range(1, maxd+1):
        lower = sorted(by_dim[d-1])
        pos = {m:i for i,m in enumerate(lower)}
        columns = []
        for big in by_dim.get(d, []):
            boundary = 0
            for v in range(big.bit_length()):
                if (big >> v) & 1:
                    boundary |= 1 << pos[big ^ (1 << v)]
            columns.append(boundary)
        ranks[d] = rank_mod_two(columns)
    ranks[0] = 0
    ranks[maxd+1] = 0
    return {d: len(by_dim[d])-ranks[d]-ranks[d+1]-(d == 0)
            for d in by_dim if len(by_dim[d])-ranks[d]-ranks[d+1]-(d == 0)}


def permutation_sign(order):
    parity = 0
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            parity ^= order[i] > order[j]
    return 1 if parity == 0 else -1


def reduced_lefschetz(F, n, perm, swap):
    p = [perm[i] + (n if swap else 0) for i in range(n)] + [perm[i] + (0 if swap else n) for i in range(n)]
    trace = -1  # Remove the always-fixed augmented empty simplex.
    for m in F:
        v = [i for i in range(2*n) if (m >> i) & 1]
        image = [p[i] for i in v]
        if sorted(image) == v:
            index = [v.index(j) for j in image]
            trace += (-1)**(len(v)-1)*permutation_sign(index)
    return trace


def expected_character(perm, swap):
    n = len(perm)
    f = sum(perm[i] == i for i in range(n))
    c2 = sum(perm[perm[i]] == i and perm[i] > i for i in range(n))
    wedge = (f*f-3*f+2)//2-c2
    return (-1 if swap else 1)*wedge


def check():
    output = {'cases': [], 'character_cases': []}
    for n in range(3, 9):
        F = faces_from_graph(n)
        assert F == structural_faces(n)
        critical, pairs = matching(F, n)
        expected = {1 << 0} | {
            (1 << n) | (1 << (n+i)) | (1 << (n+j))
            for i in range(1, n) for j in range(i+1, n)
        }
        assert critical == expected
        assert 2*len(pairs)+len(critical) == len(F)
        edges = verify_acyclic(F, pairs, n)
        hom = homology_mod_two(F)
        assert hom == {2: (n-1)*(n-2)//2}
        output['cases'].append({
            'n': n, 'faces': len(F), 'f_vector': [
                sum(m.bit_count()-1 == d for m in F) for d in range(n)
            ], 'matched_pairs': len(pairs),
            'covering_relations': edges,
            'critical': {'degree_0': 1, 'degree_2': (n-1)*(n-2)//2},
            'reduced_mod2_homology': hom,
        })
        if n <= 6:
            tests = 0
            for p in itertools.permutations(range(n)):
                for swap in [False, True]:
                    assert reduced_lefschetz(F, n, p, swap) == expected_character(p, swap)
                    tests += 1
            output['character_cases'].append({'n': n, 'group_elements_checked': tests})
    print(json.dumps(output, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    check()
