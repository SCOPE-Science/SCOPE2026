#!/usr/bin/env python3
"""Independent finite trace and online mistake-tree tests of Hamming-neighborhood dimensions.

Usage: python3 verify_mixed_hamming.py
The unrestricted mathematical arguments are separate from these finite tests.
"""
from itertools import product, combinations
from functools import lru_cache
import json


def concept_matrices(q, inclusive):
    vertices = tuple(product(*(range(size) for size in q)))
    masks = []
    for center in vertices:
        mask = 0
        for j, query in enumerate(vertices):
            dist = sum(a != b for a, b in zip(center, query))
            if dist <= 1 if inclusive else dist == 1:
                mask |= 1 << j
        masks.append(mask)
    return vertices, tuple(masks)


def vc_dimension(masks, count):
    last = 0
    for k in range(1, min(4, count) + 1):
        found = False
        for chosen in combinations(range(count), k):
            traces = set()
            for mask in masks:
                t = sum(((mask >> i) & 1) << j for j, i in enumerate(chosen))
                traces.add(t)
                if len(traces) == (1 << k):
                    found = True
                    break
            if found:
                break
        if not found:
            break
        last = k
    return last


def online_dimension(masks, count):
    @lru_cache(None)
    def rank(hypotheses):
        best = 0
        for query_mask in masks:
            positive = hypotheses & query_mask
            negative = hypotheses & ~query_mask
            if positive and negative:
                best = max(best, 1 + min(rank(positive), rank(negative)))
            if best == 3:
                break
        return best
    return rank((1 << count) - 1), rank.cache_info().currsize


def expected(q, inclusive):
    q = tuple(sorted(q)); dim = len(q)
    if inclusive:
        if dim == 1:
            return 0, 0
        if dim == 2 and q == (2, 2):
            return 1, 1
        if dim == 2 and q[0] == 2:
            return 2, 2
        if dim == 2 and q == (3, 3):
            return 2, 3
        return 3, 3
    if dim == 1 or (dim == 2 and q == (2, 2)):
        return 1, 1
    if dim == 2 and q == (2, 3):
        return 2, 2
    if dim == 2 and q == (3, 3):
        return 2, 3
    if dim == 3 and q == (2, 2, 2):
        return 2, 2
    return 3, 3


def verify_tree(q, inclusive, tree):
    vertices, masks = concept_matrices(q, inclusive)
    def visit(node, constraints, depth):
        if 'center' in node:
            assert depth == 3
            center = tuple(node['center'])
            assert center in vertices
            for query,bit in constraints:
                d = sum(a != b for a,b in zip(center,query))
                got = int(d<=1 if inclusive else d==1)
                assert got == bit, (center, query, bit, got)
            return 1
        assert 'query' in node and 'zero' in node and 'one' in node
        query = tuple(node['query'])
        assert query in vertices
        return visit(node['zero'],constraints+[(query,0)],depth+1)+visit(node['one'],constraints+[(query,1)],depth+1)
    assert visit(tree, [], 0) == 8


def first_tree(q, inclusive, depth):
    vertices, masks = concept_matrices(q,inclusive)
    @lru_cache(None)
    def go(hyp,k):
        if k == 0:
            return {'center': vertices[(hyp & -hyp).bit_length()-1]}
        for j,querymask in enumerate(masks):
            lo= hyp&~querymask; hi = hyp&querymask
            if lo and hi:
                x=go(lo,k-1); y=go(hi,k-1)
                if x is not None and y is not None:
                    return {'query':vertices[j], 'zero':x,'one':y}
        return None
    tree = go((1<<len(vertices))-1,depth)
    assert tree is not None
    return tree


def main():
    test_vectors = [
        (2,), (3,), (2,2), (2,3), (2,4), (2,5),
        (3,3), (3,4), (4,4),
        (2,2,2), (2,2,3), (2,3,3), (2,2,2,2),
    ]
    total = 0
    for q in test_vectors:
        for inclusive in (False, True):
            vertices, masks = concept_matrices(q,inclusive)
            observed = (vc_dimension(masks,len(vertices)), online_dimension(masks,len(vertices))[0])
            exp = expected(q,inclusive)
            assert observed == exp, (q,inclusive,observed,exp)
            total += 1
            print('DIMENSIONS',q,'closed' if inclusive else 'open',*observed)
    for inclusive in (False,True):
        tree = first_tree((3,3),inclusive,3)
        verify_tree((3,3),inclusive,tree)
        print('EIGHT_LEAF_TREE', 'closed' if inclusive else 'open',json.dumps(tree,separators=(',',':')))
    print('ALL_MIXED_HAMMING_CHECKS_PASS',total,'grid/concept families and two eight-leaf trees')

if __name__=='__main__':
    main()
