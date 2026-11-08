#!/usr/bin/env python3
"""Independent verification of vertex-query shattering in rooted-tree frontiers.

Run: python3 check_frontiers.py
Uses only Python's standard library. Enumerations are finite checks,
not proofs of arbitrary-size theorems.
"""
from itertools import product
from functools import lru_cache
from math import floor, log2
import random


def frontiers(children):
    @lru_cache(None)
    def visit(v):
        if not children[v]:
            return frozenset({1 << v})
        acc = {0}
        for c in children[v]:
            acc = {a | b for a in acc for b in visit(c)}
        return frozenset({1 << v} | acc)
    return set(visit(0))


def conflict_pairs(children):
    n = len(children)
    parent = [-1] * n
    for v, sons in enumerate(children):
        for w in sons:
            parent[w] = v
    def ancestor(x, y):
        while y >= 0:
            if x == y:
                return True
            y = parent[y]
        return False
    C = set()
    for x in range(n):
        for y in range(x + 1, n):
            bad = ancestor(x,y) or ancestor(y,x)
            if not children[x] and ancestor(parent[x],y) and not ancestor(x,y):
                bad = True
            if not children[y] and ancestor(parent[y],x) and not ancestor(y,x):
                bad = True
            if bad:
                C.add((x,y))
    return C


def terminal_internal_count(children):
    internal = [v for v in range(len(children)) if children[v]]
    return sum(not any(children[c] for c in children[v]) for v in internal)


def inspect_tree(children):
    n = len(children)
    F = frontiers(children)
    C = conflict_pairs(children)
    count = [0] * (n+1)
    max_size = 0
    for mask in range(1 << n):
        expected = all(not (mask >> x & 1 and mask >> y & 1) for x,y in C)
        actual = len({f & mask for f in F}) == (1 << mask.bit_count())
        assert actual == expected, (children,mask,actual,expected)
        if actual:
            k = mask.bit_count()
            count[k] += 1
            max_size = max(max_size, k)
    assert max_size == terminal_internal_count(children) or (n == 1 and max_size == 0)
    return count


def complete_tree(branching,height):
    children = [[]]
    levels = [0]
    for _ in range(height):
        next_level = []
        for v in levels:
            for _ in range(branching):
                c = len(children)
                children.append([])
                children[v].append(c)
                next_level.append(c)
        levels = next_level
    return children


def comb(m):
    children = [[] for _ in range(m)]
    for i in range(m-1):
        leaf = len(children)
        children.append([])
        children[i].append(leaf)
        children[i].append(i+1)
    for _ in range(2):
        leaf = len(children)
        children.append([])
        children[m-1].append(leaf)
    return children


def ldim_of_frontiers(children):
    F = sorted(frontiers(children))
    n = len(children)
    masks = [sum(1 << i for i,f in enumerate(F) if (f >> v) & 1) for v in range(n)]
    @lru_cache(None)
    def rank(s):
        best = 0
        for q in masks:
            a = s & q
            b = s & ~q
            if a and b:
                best = max(best,1+min(rank(a),rank(b)))
        return best
    return rank((1 << len(F))-1)


def main():
    checked = 0
    # Every increasing-parent rooted tree (parent(v)<v) on up to 8 vertices.
    # This includes every unlabeled rooted-tree shape in that range.
    for n in range(2,9):
        for parents in product(*(range(i) for i in range(1,n))):
            children = [[] for _ in range(n)]
            for i,p in enumerate(parents,1):
                children[p].append(i)
            inspect_tree(children)
            checked += 1
    # Additional trees outside the exhaustive order range.
    random.seed(22319)
    for n in (9,10,11):
        for _ in range(100):
            children = [[] for _ in range(n)]
            for i in range(1,n):
                children[random.randrange(i)].append(i)
            inspect_tree(children)
            checked += 1
    complete_cases = 0
    for b,h in ((2,1),(2,2),(2,3),(3,1),(3,2),(4,1)):
        c = inspect_tree(complete_tree(b,h))
        p=[1,b+1]
        for _ in range(2,h+1):
            # z + P(z)^b
            new=[0] * (b*(len(p)-1)+1)
            new[0]=1
            poly=[1]
            for i in range(b):
                nxt=[0]*(len(poly)+len(p)-1)
                for j,a in enumerate(poly):
                    for k,v in enumerate(p):nxt[j+k]+=a*v
                poly=nxt
            poly[1]+=1
            p=poly
        assert c[:len(p)]==p and not any(c[len(p):]),(b,h,c,p)
        complete_cases += 1
    comb_cases = 0
    for m in range(1,10):
        C=comb(m)
        f=frontiers(C)
        assert len(f)==m+1
        assert terminal_internal_count(C)==1
        assert ldim_of_frontiers(C)==int(log2(m+1))
        if m<=6:
            coeff=inspect_tree(C)
            assert coeff==[1,2*m+1]+[0]*(2*m)
        comb_cases+=1
    print('FRONTIER_SHATTERING_PASS', 'rooted_trees',checked, 'complete_cases',complete_cases, 'comb_online',comb_cases)

if __name__ == '__main__':
    main()
