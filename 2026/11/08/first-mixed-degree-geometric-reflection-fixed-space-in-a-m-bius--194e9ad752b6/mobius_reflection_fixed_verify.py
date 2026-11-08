"""Exact verification of edge-/vertex-axis geometric fixed complexes on M_{2n} for 2 <= n <= 8.
Run: python3 mobius_reflection_fixed_verify.py
No external packages or files required.
"""
from collections import Counter, defaultdict
from functools import lru_cache


def mobius_edges(n):
    m = 2*n
    return tuple(sorted({tuple(sorted((i, (i+j) % m)))
                         for i in range(m) for j in (1, n)}))


def perfect_matchings(n, edges):
    adj = [[] for _ in range(2*n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i)); adj[v].append((u, i))
    @lru_cache(None)
    def walk(mask):
        if mask == 0:
            return (frozenset(),)
        u = (mask & -mask).bit_length() - 1
        result = []
        for v, ei in adj[u]:
            if mask & (1 << v):
                for p in walk(mask ^ (1 << u) ^ (1 << v)):
                    result.append(p | {ei})
        return tuple(result)
    p = walk((1 << (2*n)) - 1)
    assert len(p) == len(set(p))
    assert all(len(t) == n for t in p)
    return p


def orbit_complex(n, a):
    E = mobius_edges(n)
    P = perfect_matchings(n, E)
    ix = {e: i for i, e in enumerate(E)}
    trans = []
    for u, v in E:
        trans.append(ix[tuple(sorted(((a-u) % (2*n), (a-v) % (2*n))))])
    assert all(trans[trans[j]] == j for j in range(len(E)))
    orbits = []
    seen = set()
    for j in range(len(E)):
        if j in seen: continue
        ob = tuple(sorted({j, trans[j]})); seen.update(ob)
        endpoints = [u for i in ob for u in E[i]]
        if len(set(endpoints)) == 2*len(ob):
            orbits.append(ob)
    assert seen == set(range(len(E)))
    F = set()
    for p in P:
        avail = [k for k, ob in enumerate(orbits) if set(ob) <= p]
        for mask in range(1 << len(avail)):
            F.add(tuple(avail[j] for j in range(len(avail)) if mask & (1 << j)))
    # Independently derive every invariant original face from perfect matchings.
    fixed_original = set()
    for p in P:
        seq = sorted(p)
        for mask in range(1 << len(seq)):
            q = frozenset(seq[j] for j in range(len(seq)) if mask & (1 << j))
            if {trans[j] for j in q} == q:
                fixed_original.add(q)
    from_orbits = {frozenset(j for k in sig for j in orbits[k]) for sig in F}
    assert fixed_original == from_orbits
    return E, P, orbits, F


def elementary_collapse(F):
    faces = set(F)
    pairs = []
    while True:
        cofaces = defaultdict(list)
        for sig in faces:
            for i in range(len(sig)):
                cofaces[sig[:i]+sig[i+1:]].append(sig)
        choices = [(len(sig), sig, cofaces[sig][0])
                   for sig in faces if len(sig) >= 1 and len(cofaces[sig]) == 1]
        if not choices:
            break
        _, sig, sup = min(choices, key=lambda t: (-t[0], t[1], t[2]))
        assert sig in faces and sup in faces and len(sup) == len(sig)+1
        assert all(not(set(sig)<set(s) and s not in (sig,sup)) for s in faces)
        faces.remove(sig); faces.remove(sup)
        pairs.append((sig, sup))
    assert len(faces)+2*len(pairs) == len(F)
    return faces, pairs


def graph_betti_one(core):
    v = [t[0] for t in core if len(t) == 1]
    e = [t for t in core if len(t) == 2]
    nbr = {x: set() for x in v}
    for x,y in e:
        nbr[x].add(y); nbr[y].add(x)
    comp = 0; seen = set()
    for x in v:
        if x in seen: continue
        comp += 1; st=[x]; seen.add(x)
        while st:
            for y in nbr[st.pop()]:
                if y not in seen:
                    seen.add(y);st.append(y)
    return comp, len(e)-len(v)+comp


def freely_reduce(word):
    reduced = []
    for x in word:
        if reduced and reduced[-1] == -x:
            reduced.pop()
        else:
            reduced.append(x)
    return tuple(reduced)


def circle_two_cell_model(core):
    vertices = sorted(t[0] for t in core if len(t) == 1)
    edges = sorted(t for t in core if len(t) == 2)
    tris = sorted(t for t in core if len(t) == 3)
    assert len(vertices)==8 and len(edges)==15 and len(tris)==8
    parent = {x:x for x in vertices}
    def root(x):
        while parent[x] != x: x=parent[x]
        return x
    tree = set()
    for e in edges:
        x,y=e
        if root(x) != root(y):
            parent[root(x)] = root(y);tree.add(e)
    assert len(tree) == 7
    gen={e:i+1 for i,e in enumerate(e for e in edges if e not in tree)}
    assert len(gen) == 8
    def oriented_edge(x,y):
        key=tuple(sorted((x,y)))
        if key in tree: return []
        return [gen[key]*(1 if x<y else -1)]
    words=[freely_reduce(oriented_edge(x,y)+oriented_edge(y,z)+oriented_edge(z,x))
           for x,y,z in tris]
    original = words[:]
    elimination=[]
    while True:
        choices = [(len(w),i,g) for i,w in enumerate(words)
                   for g in sorted({abs(x) for x in w})
                   if sum(abs(x)==g for x in w)==1]
        if not choices: break
        _,i,g=min(choices)
        w=words.pop(i)
        k=next(k for k,x in enumerate(w) if abs(x)==g)
        A=list(w[:k]);B=list(w[k+1:])
        inv=lambda seq:[-x for x in reversed(seq)]
        sub=inv(A)+inv(B) if w[k] == g else B+A
        new=[]
        for rel in words:
            changed=[]
            for x in rel:
                if x==g:changed.extend(sub)
                elif x==-g:changed.extend(inv(sub))
                else:changed.append(x)
            new.append(freely_reduce(changed))
        words=new
        elimination.append((g,w,tuple(sub)))
    assert len(elimination)==7
    assert words == [()], (original,words,elimination)
    assert len(set(range(1,9)) - {rec[0] for rec in elimination}) == 1
    return original, elimination, words


def main():
    data=[]
    for n in range(2,9):
        for a in (0,1):
            _, pms, orbits, complex_ = orbit_complex(n,a)
            core,steps=elementary_collapse(complex_)
            if a==0 or (a==1 and n==3):
                assert len(core) == 2 and {len(x) for x in core} == {0,1}
                kind='point'
            elif a==1 and n==2:
                assert all(len(q) < 2 for q in core) and len(core) == 4
                kind='three points'
            elif a==1 and n<=7:
                assert max(map(len,core)) == 2
                comp, b1 = graph_betti_one(core)
                target=(2,1) if n==4 else (1,2)
                assert (comp,b1)==target
                kind='S1 + point' if n==4 else 'wedge 2 S1'
            else:
                assert (n,a)==(8,1)
                rel,elim,remaining=circle_two_cell_model(core)
                kind='S1 wedge S2'
                print('M16_EDGE_REFLECTION_CW_PRESENTATION',rel)
                print('M16_EDGE_REFLECTION_SEVEN_CANCELLATIONS',elim)
                print('M16_EDGE_REFLECTION_RESIDUAL_WORDS',remaining)
            count=Counter(len(f)-1 for f in complex_ if f)
            print('n=',n,'axis=',a,'perfect_matchings=',len(pms),
                  'orbit_vertices=',len(orbits),'f_vector=',[count[i] for i in range(max(count)+1)],
                  'free_pairs=',len(steps),'core_nonempty=',len(core)-1,'type=',kind)
            data.append((n,a,kind))
    assert len(data)==14
    print('MOBIUS_REFLECTION_FIRST_MIXED_FIXED_TYPE_OK')
if __name__ == '__main__':
    main()
