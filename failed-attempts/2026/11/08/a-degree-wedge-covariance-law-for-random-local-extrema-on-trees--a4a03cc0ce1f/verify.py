"""Independent exact checks for local-extrema covariance on fixed trees.

Run: python verify.py
Uses only Python standard library. All arithmetic is exact.
"""
from fractions import Fraction
from itertools import permutations, combinations
from math import comb


def f(a, b):
    if min(a, b) < 1:
        raise ValueError('positive degrees required')
    return (Fraction(a + b + 1, a * b * (a + 1) * (b + 1))
            - Fraction(1, a * b * comb(a + b, a)))


def theoretical_cov(adj):
    n = len(adj)
    deg = list(map(len, adj))
    ans = -sum((Fraction(1, (d + 1) ** 2) for d in deg), Fraction())
    for u in range(n):
        for v in adj[u]:
            if u < v:
                ans += 2 * f(deg[u], deg[v])
    for w in range(n):
        for u, v in combinations(adj[w], 2):
            ans -= 2 * f(deg[u], deg[v]) / (deg[u] + deg[v] + 1)
    return ans


def empirical_cov(adj):
    n = len(adj)
    nm = nv = nprod = 0
    trials = 0
    for labels in permutations(range(n)):
        peaks = sum(all(labels[u] > labels[v] for v in adj[u]) for u in range(n))
        troughs = sum(all(labels[u] < labels[v] for v in adj[u]) for u in range(n))
        nm += peaks
        nv += troughs
        nprod += peaks * troughs
        trials += 1
    return Fraction(nprod, trials) - Fraction(nm * nv, trials ** 2), trials


def canonical_trees(n):
    """Generate exactly one labeled representative of each unlabeled tree.

    Prüfer codes enumerate all n^(n-2) labeled trees. To avoid an
    external graph library, use a reversible degree-preserving invariant:
    recursively delete leaves and encode sorted rooted branch signatures
    at the final one/two centers. Representatives only; enumeration exact.
    """
    from itertools import product
    def signature(adj):
        alive = set(range(n))
        while len(alive) > 2:
            leaves = {v for v in alive if sum(w in alive for w in adj[v]) <= 1}
            alive -= leaves
        def rooted(v, parent):
            return '('+''.join(sorted(rooted(w, v) for w in adj[v] if w != parent))+')'
        return min(rooted(c, -1) for c in alive) if len(alive) == 1 else \
               '('+''.join(sorted(rooted(c, next(iter(alive-{c}))) for c in alive))+')'
    seen = set()
    for code in product(range(n), repeat=n-2):
        deg = [1]*n
        for x in code: deg[x] += 1
        adj = [set() for _ in range(n)]
        for x in code:
            leaf = next(i for i in range(n) if deg[i]==1)
            adj[leaf].add(x); adj[x].add(leaf)
            deg[leaf]-=1; deg[x]-=1
        u, v = [i for i in range(n) if deg[i] == 1]
        adj[u].add(v); adj[v].add(u)
        sig = signature(adj)
        if sig not in seen:
            seen.add(sig)
            yield tuple(tuple(sorted(v)) for v in adj)


def path(n):
    return tuple(tuple(v for v in (i-1, i+1) if 0<=v<n) for i in range(n))


def star(n):
    return (tuple(range(1,n)),)+tuple((0,) for _ in range(1,n))


def main():
    checks = 0
    for a in range(1,40):
        for b in range(1,40):
            assert f(a,b) > 0
            # Mixed distance-two covariance is exactly negative adjacent
            # covariance divided by sum of endpoint degrees plus one.
            from math import factorial
            beta = Fraction(factorial(a)*factorial(b),factorial(a+b+1))
            direct = (beta-Fraction(1,(a+1)*(b+1)))/(a*b)
            assert direct == -f(a,b)/(a+b+1)
            checks += 2
    # All nonisomorphic fixed trees through seven vertices, in exact arithmetic.
    # 8-vertex path/star and selected branched shapes also checked exhaustively.
    for n in range(2,8):
        shapes = list(canonical_trees(n))
        for adj in shapes:
            obs, trials = empirical_cov(adj)
            assert obs == theoretical_cov(adj), (n,adj,obs,theoretical_cov(adj))
            checks += 1
        print('n =',n,'nonisomorphic-tree samples =',len(shapes))
    for n in range(3,9):
        adj=path(n)
        obs, trials=empirical_cov(adj)
        assert obs==theoretical_cov(adj)
        if n>=4: assert obs==Fraction(8*n-37,180)
        checks += 2
    for n in range(3,9):
        adj=star(n)
        obs,trials=empirical_cov(adj)
        expect=Fraction(-(n-2)*(n**3+2*n*n-9*n-6),12*n*n)
        assert obs==theoretical_cov(adj)==expect
        checks += 1
    assert theoretical_cov(path(4)) < 0 < theoretical_cov(path(5))
    assert all(theoretical_cov(star(n))<0 for n in range(3,101))
    checks+=2
    print('PASS',checks,'exact checks')

if __name__=='__main__':
    main()
