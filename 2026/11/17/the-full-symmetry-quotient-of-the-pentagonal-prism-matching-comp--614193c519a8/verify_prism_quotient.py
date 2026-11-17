#!/usr/bin/env python3
"""Integral orbit-chain and fundamental-group certificate for a prism matching quotient.
Python 3 standard library only. Use --create-certificate to generate a new certificate;
normal execution independently reconstructs and checks the supplied certificate.
"""
import collections
import hashlib
import itertools
import json
import pathlib
import sys

N = 5

def graph_edges():
    v = lambda i, layer: 5 * layer + (i % 5)
    out = [tuple(sorted((v(i, l), v(i+1, l)))) for l in range(2) for i in range(N)]
    out += [tuple(sorted((v(i, 0), v(i, 1)))) for i in range(N)]
    return tuple(sorted(out))

EDGES = graph_edges()
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}

def group():
    res = []
    for rotation in range(5):
        for reflected in (0, 1):
            for layer_swap in (0, 1):
                def vertex(x):
                    return 5 * ((x // 5) ^ layer_swap) + (((-x % 5) if reflected else x % 5) + rotation) % 5
                res.append(tuple(EDGE_INDEX[tuple(sorted((vertex(a), vertex(b))))] for a,b in EDGES))
    assert len(set(res)) == 20
    return tuple(res)

GROUP = group()

def translate(mask, permutation):
    ans = 0
    while mask:
        lowbit = mask & -mask
        mask -= lowbit
        ans |= 1 << permutation[lowbit.bit_length()-1]
    return ans

def canonical(flag):
    return min(tuple(translate(mask, g) for mask in flag) for g in GROUP)

def construct():
    masks = [sum(1<<v for v in e) for e in EDGES]
    faces = {}
    for m in range(1, 1<<15):
        occupied = 0
        feasible = True
        for i, vertex_mask in enumerate(masks):
            if (m >> i) & 1:
                if occupied & vertex_mask:
                    feasible = False
                    break
                occupied |= vertex_mask
        if feasible:
            faces[m] = m.bit_count()
    assert [sum(k==j for k in faces.values()) for j in range(1,6)] == [15,75,145,95,11]
    flags = [set() for _ in range(5)]
    memo = {}
    def chains(top):
        if top not in memo:
            chains_here = [(top,)]
            sub = (top-1) & top
            while sub:
                if sub in faces:
                    chains_here.extend(c+(top,) for c in chains(sub))
                sub = (sub-1) & top
            memo[top] = chains_here
        return memo[top]
    for top in faces:
        for flag in chains(top):
            flags[len(flag)-1].add(flag)
    assert [len(x) for x in flags] == [341,2680,5940,4920,1320]
    orbit = [sorted({canonical(f) for f in fset}) for fset in flags]
    assert [len(x) for x in orbit] == [35,188,357,276,72]
    # Burnside calculation uses a distinct loop from orbit canonicalization.
    for d,fset in enumerate(flags):
        fixed = sum(sum(all(translate(mask,g)==mask for mask in f) for f in fset) for g in GROUP)
        assert fixed == 20*len(orbit[d]), (d,fixed)
    return orbit

def boundaries(orbit):
    B = {}
    for d in range(1,5):
        lower = {f: i for i,f in enumerate(orbit[d-1])}
        mat = {}
        for j,flag in enumerate(orbit[d]):
            c = collections.Counter()
            for i in range(len(flag)):
                face = canonical(flag[:i]+flag[i+1:])
                c[lower[face]] += (-1)**i
            mat[j] = {i:x for i,x in c.items() if x}
        B[d] = mat
    assert boundary_squared_zero(B)
    return B

def boundary_squared_zero(B):
    for d in range(2,5):
        for j,col in B[d].items():
            out = collections.Counter()
            for i,v in col.items():
                for k,w in B[d-1][i].items():
                    out[k] += v*w
            if any(out.values()):
                return False
    return True

def spanning_tree(orbit):
    vindex = {f:i for i,f in enumerate(orbit[0])}
    eends = [(vindex[canonical((e[0],))],vindex[canonical((e[1],))]) for e in orbit[1]]
    parent = list(range(len(vindex)))
    def find(i):
        while i != parent[i]:
            i = parent[i]
        return i
    tree = []
    for i,(a,b) in enumerate(eends):
        ra,rb = find(a),find(b)
        if ra != rb:
            parent[rb] = ra
            tree.append(i)
    assert len(tree) == 34
    return tree

def relators(orbit, tree):
    index = {f:i for i,f in enumerate(orbit[1])}
    rels = []
    for tri in orbit[2]:
        es = (canonical((tri[0],tri[1])), canonical((tri[1],tri[2])), canonical((tri[0],tri[2])))
        word = tuple(sign*(index[e]+1) for e,sign in zip(es,(1,1,-1)) if index[e] not in tree)
        rels.append(word)
    return rels

def free_reduce(word):
    out = []
    for x in word:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    while len(out)>1 and out[0]==-out[-1]:
        out = out[1:-1]
    return out

def generate_pi1(orbit):
    tree = spanning_tree(orbit)
    rels = relators(orbit, set(tree))
    remain = set(range(len(orbit[1]))) - set(tree)
    rounds = []
    while remain:
        available = {}
        for j,w in enumerate(rels):
            reduced = free_reduce([x for x in w if abs(x)-1 in remain])
            if len(reduced)==1:
                available.setdefault(abs(reduced[0])-1,j)
        if not available:
            raise AssertionError('The relation elimination did not finish')
        pairs = sorted([e,j] for e,j in available.items())
        rounds.append(pairs)
        remain.difference_update(available)
    assert [len(r) for r in rounds] == [97,36,17,4]
    return {'tree_edges':tree, 'trivialization_rounds':rounds}

def check_pi1(orbit, pi1):
    assert pi1['tree_edges'] == spanning_tree(orbit)
    tree = set(pi1['tree_edges'])
    rels = relators(orbit,tree)
    remain = set(range(len(orbit[1]))) - tree
    for pairs in pi1['trivialization_rounds']:
        removed = set()
        for e,j in pairs:
            assert e in remain and e not in removed
            assert 0 <= j < len(rels)
            reduced = free_reduce([x for x in rels[j] if abs(x)-1 in remain])
            assert len(reduced)==1 and abs(reduced[0])==e+1, (e,j,reduced)
            removed.add(e)
        remain.difference_update(removed)
    assert not remain
    return [len(x) for x in pi1['trivialization_rounds']]

def create_reduction(orbit):
    mat = boundaries(orbit)
    cells = {i:set(range(len(orbit[i]))) for i in range(5)}
    pivots = []
    for d in (4,3,2,1):
        while True:
            rows = collections.Counter(i for col in mat[d].values() for i in col)
            choices = [(len(c)*rows[i],len(c)+rows[i],i,j,u)
                       for j,c in mat[d].items() for i,u in c.items() if abs(u)==1]
            if not choices:
                break
            _,__,i,j,u=min(choices)
            pivots.append([d,i,j,u])
            cancel(mat,cells,d,i,j,u)
    assert [len(cells[i]) for i in range(5)] == [1,0,0,1,0]
    assert all(all(not c for c in m.values()) for m in mat.values())
    return pivots

def cancel(mat,cells,d,i,j,u):
    M = mat[d]
    assert i in cells[d-1] and j in cells[d] and M[j][i]==u and abs(u)==1
    pivot = dict(M[j])
    for k,col in list(M.items()):
        if k == j or i not in col:
            continue
        ratio = col[i]//u
        for a,b in pivot.items():
            v = col.get(a,0)-ratio*b
            if v:
                col[a]=v
            else:
                col.pop(a,None)
    del M[j]
    for col in M.values():
        col.pop(i,None)
    cells[d].remove(j)
    cells[d-1].remove(i)
    if d+1 in mat:
        for col in mat[d+1].values():
            col.pop(j,None)
    if d-1 in mat:
        mat[d-1].pop(i,None)

def check_reduction(orbit,pivots):
    mat = boundaries(orbit)
    cells = {i:set(range(len(orbit[i]))) for i in range(5)}
    counts = collections.Counter()
    for d,i,j,u in pivots:
        assert 1<=d<=4
        cancel(mat,cells,d,i,j,u)
        counts[d]+=1
    assert boundary_squared_zero(mat)
    assert [counts[d] for d in (1,2,3,4)] == [34,154,203,72]
    assert [len(cells[d]) for d in range(5)] == [1,0,0,1,0]
    assert all(not c for M in mat.values() for c in M.values())
    return [counts[d] for d in (1,2,3,4)]

def main():
    orbit = construct()
    if len(sys.argv)==3 and sys.argv[1]=='--create-certificate':
        obj={'schema_version':1,'cell_counts':[len(x) for x in orbit],
             'pi1':generate_pi1(orbit),'unit_pivots':create_reduction(orbit)}
        pathlib.Path(sys.argv[2]).write_text(json.dumps(obj,separators=(',',':'))+'\n',encoding='utf-8')
        print('CERTIFICATE_CREATED')
        return
    path = pathlib.Path(__file__).with_name('certificate.json')
    if len(sys.argv)==2:
        path = pathlib.Path(sys.argv[1])
    obj = json.loads(path.read_text(encoding='utf-8'))
    assert obj['schema_version'] == 1
    assert obj['cell_counts'] == [len(x) for x in orbit]
    round_counts = check_pi1(orbit,obj['pi1'])
    pivot_counts = check_reduction(orbit,obj['unit_pivots'])
    print('graph_edges=15; matching_faces=341; group_order=20')
    print('orbit_cells='+str(obj['cell_counts']))
    print('fundamental_group_trivialization='+str(round_counts))
    print('integer_unit_cancellations='+str(pivot_counts))
    print('remaining_cells_by_dimension=[1,0,0,1,0]')
    print('INTEGRAL_PRISM_QUOTIENT_VERIFY_OK')

if __name__=='__main__':
    main()
