#!/usr/bin/env python3
"""Standalone exact orbit-CW and attaching-word verifier for a binary rank-three building.

Uses only Python 3 standard library. A word is a signed list of edge generators.
Elementary eliminations use Tietze substitutions of generators occurring once
in the attaching word of a chosen two-cell; empty attaching maps give spheres.
"""
from itertools import combinations
from collections import Counter


def times_x(v):
    w = v << 1
    return w ^ (0b10011 if (w & 0b10000) else 0)


def field_mul(a, b):
    out = 0
    for j in range(4):
        if (b >> j) & 1:
            out ^= a
        a = times_x(a)
    return out


def span(vectors):
    s = {0}
    for v in vectors:
        s.update({x ^ v for x in tuple(s)})
    return frozenset(s)


def reduce_word(w):
    stack = []
    for x in w:
        if stack and stack[-1] == -x:
            stack.pop()
        else:
            stack.append(x)
    # Cyclic reduction conjugates an attaching loop, hence preserves the
    # homotopy type of the two-dimensional presentation complex.
    while len(stack) > 1 and stack[0] == -stack[-1]:
        stack = stack[1:-1]
    return tuple(stack)


def inverse(w):
    return tuple(-x for x in reversed(w))


def substitute(w, x, replacement):
    out = []
    for v in w:
        if v == x:
            out.extend(replacement)
        elif v == -x:
            out.extend(inverse(replacement))
        else:
            out.append(v)
    return reduce_word(out)


def solve_relator(w, j):
    signed = w[j]
    # a*x*b = 1 yields x=(b*a)^(-1), and a*x^(-1)*b=1 yields x=b*a.
    remainder = w[j+1:] + w[:j]
    return abs(signed), inverse(remainder) if signed > 0 else remainder


def construct():
    spaces = {}
    for k in (1, 2, 3):
        spaces[k] = sorted({s for tup in combinations(range(1,16), k)
                            if len(s := span(tup)) == (1 << k)},
                           key=lambda s: tuple(sorted(s)))
    assert tuple(len(spaces[k]) for k in (1,2,3)) == (15,35,15)
    vertices = [s for k in (1,2,3) for s in spaces[k]]
    pos = {s:i for i,s in enumerate(vertices)}
    faces = {0:[(s,) for s in vertices],1:[],2:[]}
    for j,s in enumerate(vertices):
        for t in vertices[j+1:]:
            if s < t:
                faces[1].append((s,t))
    for p in spaces[1]:
        for l in spaces[2]:
            if p < l:
                for h in spaces[3]:
                    if l < h:
                        faces[2].append((p,l,h))
    assert tuple(map(lambda i:len(faces[i]),(0,1,2))) == (65,315,315)
    powers = [1]
    for k in range(1,15):
        powers.append(times_x(powers[-1]))
    assert len(set(powers)) == 15 and times_x(powers[-1]) == 1
    def act(s, scalar):
        return frozenset(field_mul(v,scalar) for v in s)
    # The full order-three subgroup fixes precisely five two-planes,
    # and no element of order five or fifteen fixes a proper subspace.
    assert {i:sum(act(s,powers[i]) == s for s in vertices)
            for i in (1,3,5,10)} == {1:0,3:0,5:5,10:5}
    return faces,vertices,pos,powers,act


def run_subgroup(order, shared):
    faces,vertices,pos,fullpowers,act = shared
    powers = fullpowers[::15//order]
    assert len(powers) == order
    def orbit(t):
        return min(tuple(pos[act(vertices[v],u)] for v in t) for u in powers)
    representatives = {}
    index = {}
    for dim,ff in faces.items():
        representatives[dim] = sorted({min(tuple(pos[act(s,u)] for s in f)
                                             for u in powers) for f in ff})
        index[dim] = {t:i for i,t in enumerate(representatives[dim])}
    counts = tuple(len(representatives[d]) for d in (0,1,2))
    assert counts == {1:(65,315,315),3:(25,105,105),5:(13,63,63),15:(5,21,21)}[order]
    # Quotient graph: a spanning tree reduces vertices to a single vertex.
    edges = []
    for t in representatives[1]:
        edges.append((index[0][orbit((t[0],))],index[0][orbit((t[1],))]))
    parent = list(range(counts[0]))
    def root(t):
        while parent[t] != t:
            t = parent[t]
        return t
    tree = []
    for j,(a,b) in enumerate(edges):
        ra,rb = root(a),root(b)
        if ra != rb:
            parent[ra] = rb
            tree.append(j)
    assert len(tree) == counts[0]-1
    tree_set = set(tree)
    edge_names = {e:i+1 for i,e in enumerate(j for j in range(counts[1]) if j not in tree_set)}
    relations = []
    for p,l,h in representatives[2]:
        oriented = (index[1][orbit((p,l))]+1,
                    index[1][orbit((l,h))]+1,
                    -(index[1][orbit((p,h))]+1))
        w = [(1 if a>0 else -1)*edge_names[abs(a)-1]
             for a in oriented if abs(a)-1 in edge_names]
        relations.append(reduce_word(w))
    generators = set(edge_names.values())
    steps = []
    # Purely algebraic Tietze eliminations of elementary two-cell/one-cell pairs.
    while generators:
        choices = []
        for i,w in enumerate(relations):
            multiplicities = Counter(abs(a) for a in w)
            for j,a in enumerate(w):
                if multiplicities[abs(a)] == 1:
                    x,replacement = solve_relator(w,j)
                    uses = sum(sum(abs(z)==x for z in t)
                               for k,t in enumerate(relations) if k != i)
                    choices.append(((len(replacement)*uses,len(w),uses,i,j),i,j))
        assert choices, 'No eligible elementary cancellation; cannot certify wedge'
        _,i,j = min(choices)
        w = relations[i]
        x,repl = solve_relator(w,j)
        assert x in generators and sum(abs(a)==x for a in w) == 1
        relations = [substitute(t,x,repl) for k,t in enumerate(relations) if k!=i]
        generators.remove(x)
        steps.append((i,x,len(w),len(repl)))
        if len(generators) == 0:break
        # When one generator remains and all attaching maps are powers of it,
        # retaining it is the complete reduced presentation.
        if len(generators)==1 and all((not t or abs(sum(1 if a>0 else -1 for a in t)) == 5) for t in relations) and any(t for t in relations):
            break
    assert counts[2] - len(steps) == len(relations)
    assert counts[1]-len(tree)-len(steps) == len(generators)
    if generators:
        assert len(generators) == 1
        gen = next(iter(generators))
        degrees = [sum(1 if a==gen else -1 for a in t) for t in relations]
        assert all(abs(t) in (0,5) for t in degrees)
        # All nonzero maps have degree five on the same circle. Elementary
        # changes of two-cell bases leave one degree-five attachment and
        # make the other degree-five attachments null-homotopic.
        moore_count = 1
        sphere_count = len(relations)-1
        assert sum(abs(t)==5 for t in degrees) >= 1
    else:
        assert all(not w for w in relations)
        degrees = []
        moore_count = 0
        sphere_count = len(relations)
    expected = {1:(0,64),3:(0,24),5:(1,12),15:(1,4)}[order]
    assert (moore_count,sphere_count)==expected
    print(f'C{order}: cells={counts}, tree_edges={len(tree)}, '
          f'elementary_cancellations={len(steps)}, residual_generators={len(generators)}, '
          f'degree_counts={dict(sorted(Counter(degrees).items()))}, '
          f'Moore_summands={moore_count}, sphere_summands={sphere_count}')
    return counts,steps,degrees


def main():
    shared = construct()
    for order in (1,3,5,15):
        run_subgroup(order,shared)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
