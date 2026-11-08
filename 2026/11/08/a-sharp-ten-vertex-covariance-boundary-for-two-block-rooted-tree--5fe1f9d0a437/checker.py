"""Exact, self-contained checker for the two-block tree-attachment theorem.

A rooted unordered tree is encoded as a recursively sorted tuple of its child trees.
Every finite rooted tree has a leaf whose deletion leaves a rooted tree, so
attaching a leaf at every vertex and deduplicating generates every rooted tree.
This program is a finite check; the accompanying proof proves every order.
"""
from fractions import Fraction


def paths(tree, pref=()):
    yield pref
    for i, child in enumerate(tree):
        yield from paths(child, pref + (i,))


def add_leaf(tree, path):
    if not path:
        return tuple(sorted(tree + ((),)))
    j = path[0]
    children = list(tree)
    children[j] = add_leaf(children[j], path[1:])
    return tuple(sorted(children))


def stats(tree):
    # Returns vertices, internal vertices, leaves, internal depth sum, leaf depth sum.
    counts = [0, 0, 0, 0, 0]
    def walk(t, d):
        counts[0] += 1
        if t:
            counts[1] += 1
            counts[3] += d
        else:
            counts[2] += 1
            counts[4] += d
        for sub in t:
            walk(sub, d+1)
    walk(tree, 0)
    return tuple(counts)


def shape_broom(i, ell):
    assert i >= 1 and ell >= 1
    if i == 1:
        return tuple(() for _ in range(ell))
    chain = ()
    for _ in range(i-1):
        chain = (chain,)
    return tuple(sorted((chain,) + tuple(() for _ in range(ell-1))))


def theoretical_g(i, ell):
    return i * (ell * (i-3) - 2*(i-1)) // 2


def direct_covariance(tree):
    # Directly enumerate the uniformly chosen attachment vertex.
    t, i, ell, internal_sum, leaf_sum = stats(tree)
    depths = []
    def walk(sub, d):
        depths.append((d, not bool(sub)))
        for child in sub:
            walk(child, d+1)
    walk(tree, 0)
    vals = [(d+1, 2*ell-int(is_leaf)) for d,is_leaf in depths]
    ed = sum(Fraction(d,t) for d,l in vals)
    el = sum(Fraction(l,t) for d,l in vals)
    edl = sum(Fraction(d*l,t) for d,l in vals)
    return edl - ed*el


def main():
    assert stats(()) == (1,0,1,0,0)
    trees = {()}
    count = 0
    expected_counts = {1:1,2:1,3:2,4:4,5:9,6:20,7:48,8:115,9:286,10:719,11:1842}
    maxima = {}
    for t in range(1,12):
        assert len(trees) == expected_counts[t], (t,len(trees))
        if t >= 2:
            exact_g = []
            for tree in trees:
                n,i,ell,r,q = stats(tree)
                assert n==t and i+ell==t
                g = ell*r-i*q
                assert g <= theoretical_g(i,ell), (t,g,i,ell)
                assert direct_covariance(tree) == Fraction(g,t*t)
                exact_g.append((g,tree,i,ell))
                count += 3
            top = max(k[0] for k in exact_g)
            assert top == max(theoretical_g(i,t-i) for i in range(1,t))
            winners = [(tree,i,ell) for g,tree,i,ell in exact_g if g==top]
            assert any(tree==shape_broom(i,ell) for tree,i,ell in winners)
            maxima[t] = top
            if t <= 8:
                assert top < 0
            if t == 9:
                assert top == 0 and len(winners)==1 and winners[0][1:]==(5,4)
            if t == 10:
                assert top==6 and len(winners)==1 and winners[0][1:]==(6,4)
        if t < 11:
            trees = {add_leaf(tree,p) for tree in trees for p in paths(tree)}
    for t in range(10,101):
        example = shape_broom(5,t-5)
        n,i,ell,r,q=stats(example)
        assert n==t and ell*r-i*q == 5*(t-9)
        assert direct_covariance(example)==Fraction(5*(t-9),t*t)
        count += 2
    print('PASS: rooted tree enumeration 1..11, exact covariance, sharp bounds, cutoffs, broom examples')
    print('shapes_by_order',expected_counts)
    print('sharp_G_by_order',maxima)
    print('assertions_approx',count)
    print('t=10 optimal example',Fraction(6,100))

if __name__ == '__main__':
    main()
