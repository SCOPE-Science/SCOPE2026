"""Finite checks for the super-domination/irredundance correspondence and cyclic enumerator.
Run: python3 verification_check.py
"""
from collections import Counter
from itertools import combinations, product


def neighbors(n, edges):
    out = [set() for _ in range(n)]
    for a, b in edges:
        out[a].add(b)
        out[b].add(a)
    return out


def irredundant(subset, adj):
    return all(any((adj[j] | {j}) & subset == {i}
                   for j in adj[i] | {i}) for i in subset)


def super_dominating(selected, adj):
    omitted = set(range(len(adj))) - selected
    return all(any(adj[j] & omitted == {i} for j in selected)
               for i in omitted)


def clique_blowup(n, edges, m):
    edge_set = {frozenset(e) for e in edges}
    out = [set() for _ in range(n*m)]
    for a in range(n*m):
        for b in range(n*m):
            if a != b and (a//m == b//m or
                           frozenset((a//m,b//m)) in edge_set):
                out[a].add(b)
    return out


def cyclic_admissible(bits):
    n = len(bits)
    for i in range(n):
        s = tuple(bits[(i+j) % n] for j in range(4))
        if s[:3] == (1,1,1) or s in ((1,1,0,1), (1,0,1,1)):
            return False
    return True


def transfer_counts(n):
    # A triple-state directed transfer counts cyclic words without 111,1101,1011.
    states = list(product((0,1), repeat=3))
    trans = {}
    for abc in states:
        trans[abc] = []
        for d in (0,1):
            s = abc + (d,)
            if s[1:] != (1,1,1) and s not in ((1,1,0,1),(1,0,1,1)):
                trans[abc].append((abc[1:] + (d,), d))
    out = Counter()
    for start in states:
        dp = Counter({(start,0):1})
        for _ in range(n):
            new = Counter()
            for (state,k), count in dp.items():
                for nxt, bit in trans[state]:
                    new[(nxt,k+bit)] += count
            dp = new
        for (state,k), count in dp.items():
            if state == start:
                out[k] += count
    return out


def minimum_word_count(n):
    if n % 2 == 0:
        return 6 if n % 4 == 0 else 2
    return n * ((n+3)//4)


def run():
    tests = 0
    graph_profiles = 0
    # Every labeled simple graph of order at most four, with allowed m as below.
    for n in range(1,5):
        pairs = list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            edges = [e for j,e in enumerate(pairs) if mask>>j & 1]
            adj = neighbors(n,edges)
            for m in ((2,3) if n <= 3 else (2,)):
                blown = clique_blowup(n,edges,m)
                for omitted_mask in range(1<<(n*m)):
                    omitted = {i for i in range(n*m) if omitted_mask>>i & 1}
                    fibers = {i//m for i in omitted}
                    predicted = (len(fibers) == len(omitted) and
                                 irredundant(fibers,adj))
                    actual = super_dominating(set(range(n*m))-omitted,blown)
                    assert predicted == actual, (n,edges,m,omitted_mask)
                    tests += 1
                graph_profiles += 1
    cycle_words = 0
    for n in range(3,18):
        edges = [(i,(i+1)%n) for i in range(n)]
        adj = neighbors(n,edges)
        counts = Counter()
        for bits in product((0,1),repeat=n):
            subset = {i for i,b in enumerate(bits) if b}
            assert irredundant(subset,adj) == cyclic_admissible(bits)
            if cyclic_admissible(bits): counts[len(subset)] += 1
            cycle_words += 1
        assert counts == transfer_counts(n)
        assert max(counts) == n//2
        assert counts[n//2] == minimum_word_count(n)
    cycle_blowup_subsets = 0
    for n,m in [(3,2),(4,2),(5,2),(6,2),(7,2),(3,3),(4,3),(5,3)]:
        edges = [(i,(i+1)%n) for i in range(n)]
        adj = clique_blowup(n,edges,m)
        counts = Counter()
        for mask in range(1<<(n*m)):
            chosen = {j for j in range(n*m) if mask>>j & 1}
            if super_dominating(chosen,adj): counts[len(chosen)] += 1
            cycle_blowup_subsets += 1
        predicted = Counter({m*n-k: c*m**k for k,c in transfer_counts(n).items()})
        assert counts == predicted, (n,m,counts,predicted)
        assert counts[m*n-n//2] == m**(n//2)*minimum_word_count(n)
    print('VERIFY_OK labeled_graph_profiles=%d labeled_graph_subsets=%d cycle_words=%d direct_cycle_blowup_subsets=%d irredundance_correspondence=PASS cyclic_transfer=PASS minimum_count=PASS' % (graph_profiles,tests,cycle_words,cycle_blowup_subsets))


if __name__ == '__main__':
    run()
