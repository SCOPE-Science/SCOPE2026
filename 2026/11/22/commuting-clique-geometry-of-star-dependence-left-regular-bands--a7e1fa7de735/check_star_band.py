"""Direct finite enumeration of a left regular band with one dependent hub.

Usage: python3 check_star_band.py
Requires Python 3.9+ and only the standard library.
"""
from itertools import combinations
from collections import Counter
from math import comb


def all_elements(n):
    leaves = range(n)
    out = [('L', tuple(s), ()) for r in range(n + 1)
           for s in combinations(leaves, r)]
    for k in range(3 ** n):
        states = []
        t = k
        for _ in range(n):
            states.append(t % 3)
            t //= 3
        a = tuple(i for i in leaves if states[i] == 1)
        b = tuple(i for i in leaves if states[i] == 2)
        out.append(('H', a, b))
    assert len(set(out)) == len(out) == 2 ** n + 3 ** n
    return out


def canonical(raw, hub):
    seen, before, after, found = set(), [], [], False
    for c in raw:
        if c in seen:
            continue
        seen.add(c)
        if c == hub:
            found = True
        elif found:
            after.append(c)
        else:
            before.append(c)
    return ('H' if found else 'L', tuple(sorted(before)), tuple(sorted(after)))


def word(e, hub):
    typ, a, b = e
    if typ == 'L':
        return a
    return a + (hub,) + b


def prod(e, f, hub):
    return canonical(word(e, hub) + word(f, hub), hub)


def expected_centralizer(n, e):
    if e[0] == 'L':
        return 2 ** n + 3 ** (n - len(e[1]))
    return 2 ** len(e[1]) + 2 ** (n - len(e[1]))


def expected_cliques(n):
    out=Counter()
    for k in range(n+1):
        out[2**k+2**(n-k)] += comb(n,k)
    return out


def run(n):
    es = all_elements(n)
    e_set = set(es)
    hub = n
    # product rule is implemented by concatenation and deletion, independent of pair labels.
    for e in es:
        assert prod(e,e,hub)==e
    neighborhoods = {}
    pairs=0
    for e in es:
        neighbors = {f for f in es if prod(e,f,hub) == prod(f,e,hub)}
        neighborhoods[e] = neighbors
        assert len(neighbors) == expected_centralizer(n,e),(n,e,len(neighbors))
        pairs += len(neighbors)
    assert pairs == 3 * 4 ** n + 5 ** n, (n,pairs)
    expected_families=[]
    for k in range(2**n):
        aa = {i for i in range(n) if k >> i & 1}
        family = {('L', tuple(s), ()) for r in range(len(aa)+1)
                  for s in combinations(sorted(aa), r)}
        family.update(('H',tuple(sorted(aa)),tuple(s))
                      for r in range(n-len(aa)+1)
                      for s in combinations(sorted(set(range(n))-aa),r))
        assert family <= e_set
        for e in family:
            assert family <= neighborhoods[e]
            for f in family:
                assert prod(e,f,hub) in family
        for e in e_set - family:
            assert not (family <= neighborhoods[e])
        expected_families.append(frozenset(family))
    assert len(set(expected_families)) == 2**n
    if n<=4:
        # Direct Bron--Kerbosch search using only sets of actual multiplication results.
        def maximal_cliques():
            out = set()
            def visit(r,p,x):
                if not p and not x:
                    out.add(frozenset(r))
                    return
                pivot = max(p | x, key=lambda u:len(p & (neighborhoods[u]-{u})),default=None)
                avoid = neighborhoods[pivot]-{pivot} if pivot is not None else set()
                for u in list(p - avoid):
                    nu = neighborhoods[u]-{u}
                    visit(r|{u},p & nu,x & nu)
                    p.remove(u)
                    x.add(u)
            visit(set(),set(es),set())
            return out
        actual=maximal_cliques()
        assert actual==set(expected_families),(n,len(actual),len(expected_families))
        if n<=3:
            clique_counts=Counter()
            # Exact direct enumeration of every nonempty clique in vertex order.
            def enumerate_cliques(prefix,candidates):
                for idx,u in enumerate(candidates):
                    clique_counts[len(prefix)+1]+=1
                    rest=[v for v in candidates[idx+1:] if v in neighborhoods[u]]
                    enumerate_cliques(prefix+(u,),rest)
            enumerate_cliques(tuple(),es)
            def choose(a,b):
                return comb(a,b) if 0 <= b <= a else 0
            maxsize=2**n+1
            for d in range(1,maxsize+1):
                predicted=choose(2**n,d)+sum(comb(n,k)*(
                    choose(2**k+2**(n-k),d)-choose(2**k,d)) for k in range(n+1))
                assert clique_counts[d]==predicted,(n,d,clique_counts[d],predicted)
    counts=Counter(map(len,expected_families))
    assert counts==expected_cliques(n)
    return n,len(es),pairs,len(expected_families),dict(sorted(counts.items()))

if __name__=='__main__':
    for n in range(1,7):
        print('m,order,commuting_ordered,maximal_families,clique_size_counts:',run(n))
    print('ALL CHECKS PASSED')
