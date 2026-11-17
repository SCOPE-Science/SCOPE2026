"""Exact finite corroboration of sign-robust prime-cyclic Gabor windows.

All nonvanishing decisions use integer autocorrelation and the minimal
polynomial of a primitive prime root. No floating-point threshold is used.
"""
from itertools import combinations, product
from random import Random


def overlap(p, S, u):
    return [x for x in S if (x + u) % p in S]


def robust_criterion(p, S):
    return all(len(overlap(p, S, u)) % 2 == 1 for u in range(1, p))


def ambiguity_zero(p, S, signing):
    g = [signing.get(i, 0) for i in range(p)]
    for u in range(p):
        c = [g[(x + u) % p] * g[x] for x in range(p)]
        # k=0 gives the integer sum; for k != 0 cyclotomic
        # irreducibility gives a zero iff the coefficient row is constant.
        if sum(c) == 0 or min(c) == max(c):
            return (u, 0 if sum(c) == 0 else 1)
    return None


def defeating_signing(p, S, u):
    """Realize half positive and half negative overlaps via path propagation."""
    edges = overlap(p, S, u)
    assert len(edges) % 2 == 0
    target = {x: -1 if j < len(edges) // 2 else 1
              for j, x in enumerate(edges)}
    adj = {x: [] for x in S}
    for x in edges:
        y = (x + u) % p
        adj[x].append((y, target[x]))
        adj[y].append((x, target[x]))
    signing = {}
    for root in S:
        if root in signing:
            continue
        signing[root] = 1
        stack = [root]
        while stack:
            x = stack.pop()
            for y, edgeprod in adj[x]:
                if y not in signing:
                    signing[y] = signing[x] * edgeprod
                    stack.append(y)
                else:
                    assert signing[y] == signing[x] * edgeprod
    assert sum(signing[x] * signing[(x + u) % p] for x in edges) == 0
    return signing


def exhaustive(p):
    sets_checked = signs_checked = universal_sets = 0
    for size in range(1, p):
        for tpl in combinations(range(p), size):
            S = set(tpl)
            sets_checked += 1
            expected = robust_criterion(p, S)
            passes_every_signing = True
            for assignment in product((-1, 1), repeat=size):
                signs_checked += 1
                if ambiguity_zero(p, S, dict(zip(tpl, assignment))) is not None:
                    passes_every_signing = False
            assert expected == passes_every_signing, (p, S)
            if expected:
                universal_sets += 1
            else:
                bad_u = next(u for u in range(1,p) if len(overlap(p,S,u))%2==0)
                failing_signing = defeating_signing(p,S,bad_u)
                assert ambiguity_zero(p,S,failing_signing) is not None
    return sets_checked, signs_checked, universal_sets


def examples():
    for p, S in [(7, {1,2,4}), (13, {0,1,3,9}),
                 (23,{i*i%23 for i in range(1,23)}),
                 (31,{i*i%31 for i in range(1,31)})]:
        overlaps = [len(overlap(p,S,u)) for u in range(1,p)]
        assert len(set(overlaps)) == 1 and overlaps[0]%2==1
        assert ambiguity_zero(p,S,{x:1 for x in S}) is None
        lower = 1
        while lower*(lower-1) < p-1:
            lower += 1
        if p in (7,13):
            assert len(S) == lower
        print('EXAMPLE',p,'support',len(S),'overlap',overlaps[0],
              'sharp_sparsity_bound',lower)

if __name__ == '__main__':
    for p in (3,5,7):
        print('EXHAUSTIVE',p,*exhaustive(p))
    examples()
    random = Random(1729)
    samples = 0
    p = 11
    for _ in range(300):
        S = {i for i in range(p) if random.randrange(2)}
        if not S or len(S) == p:
            continue
        expected = robust_criterion(p,S)
        if expected:
            for _ in range(30):
                sg = {x:random.choice((-1,1)) for x in S}
                assert ambiguity_zero(p,S,sg) is None
                samples+=1
        else:
            u = next(u for u in range(1,p) if len(overlap(p,S,u))%2==0)
            sg = defeating_signing(p,S,u)
            assert ambiguity_zero(p,S,sg) is not None
            samples+=1
    print('RANDOM_P11_SIGNINGS',samples)
    print('ROBUST_SIGNING_GABOR_PASS')
