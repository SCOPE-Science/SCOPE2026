"""Reconstructs the type-B4 Kreweras orbit complex and its 2-CW presentation.

Python 3 standard library only. Run: python3 verify.py
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from hashlib import sha256

N = 4
IDENTITY = (1, 2, 3, 4)
COXETER = (2, 3, 4, -1)


def multiply(a, b):
    """Signed composition a after b."""
    return tuple((1 if x > 0 else -1) * a[abs(x)-1] for x in b)


def inverse(a):
    out = [0]*N
    for i, x in enumerate(a):
        out[abs(x)-1] = (1 if x > 0 else -1)*(i+1)
    return tuple(out)


def reflection_length(w):
    """Codimension of the fixed subspace in the signed permutation representation."""
    seen = set()
    positive_cycles = 0
    for i in range(N):
        if i in seen:
            continue
        j, sign = i, 1
        while j not in seen:
            seen.add(j)
            v = w[j]
            sign *= 1 if v > 0 else -1
            j = abs(v)-1
        positive_cycles += (sign == 1)
    return N - positive_cycles


def all_signed():
    return sorted(tuple(p[i]*s[i] for i in range(N))
                  for p in permutations((1,2,3,4))
                  for s in product((-1,1), repeat=N))


def reflection_generators():
    gens = []
    for i in range(N):
        g = list(IDENTITY)
        g[i] *= -1
        gens.append(tuple(g))
    for i, j in combinations(range(N), 2):
        for s in (1, -1):
            g = list(IDENTITY)
            g[i], g[j] = s*(j+1), s*(i+1)
            gens.append(tuple(g))
    return sorted(gens)


def check_group():
    group = all_signed()
    assert len(group) == 384 and len(set(group)) == 384
    gens = reflection_generators()
    assert len(gens) == 16
    assert all(multiply(g, g) == IDENTITY for g in gens)
    distance = {IDENTITY: 0}
    frontier = [IDENTITY]
    while frontier:
        fresh = []
        for w in frontier:
            for t in gens:
                v = multiply(w, t)
                if v not in distance:
                    distance[v] = distance[w]+1
                    fresh.append(v)
        frontier = fresh
    assert len(distance) == 384
    assert all(distance[w] == reflection_length(w) for w in group)
    assert reflection_length(COXETER) == 4
    c_power = IDENTITY
    for j in range(1,9):
        c_power = multiply(c_power, COXETER)
        assert (c_power == IDENTITY) == (j == 8)
    return group


def kreweras(w):
    return multiply(inverse(w), COXETER)


def build_original_complex(group):
    ell = reflection_length
    interval = [w for w in group if ell(w)+ell(multiply(inverse(w), COXETER)) == 4]
    assert Counter(map(ell, interval)) == {0:1, 1:16, 2:36, 3:16, 4:1}
    proper = sorted(w for w in interval if 0 < ell(w) < 4)
    assert len(proper) == 68
    at = {w: i for i, w in enumerate(proper)}
    def below(x, y):
        return ell(x)+ell(multiply(inverse(x), y)) == ell(y)
    ranks = {r:[w for w in proper if ell(w)==r] for r in (1,2,3)}
    faces = {(i,) for i in range(len(proper))}
    for r in (1,2):
        for s in range(r+1,4):
            for x in ranks[r]:
                for y in ranks[s]:
                    if below(x,y):
                        faces.add(tuple(sorted((at[x], at[y]))))
    for a in ranks[1]:
        for b in ranks[2]:
            if below(a,b):
                for c in ranks[3]:
                    if below(b,c):
                        faces.add(tuple(sorted((at[a],at[b],at[c]))))
    assert Counter(map(len, faces)) == {1:68, 2:288, 3:256}
    vertex_perm = [at[kreweras(w)] for w in proper]
    def on_face(face):
        return tuple(sorted(vertex_perm[i] for i in face))
    assert all(on_face(f) in faces for f in faces)
    powers = []
    for i in range(len(proper)):
        x = i
        period = 0
        while True:
            x = vertex_perm[x]
            period += 1
            if x == i:
                break
        powers.append(period)
    assert max(powers) == 8 and all(8 % m == 0 for m in powers)
    invc = inverse(COXETER)
    for w in group:
        assert kreweras(kreweras(w)) == multiply(multiply(invc,w),COXETER)
        x=w
        for j in range(8):
            x=kreweras(x)
        assert x==w
    return faces, on_face


def quotient_simplices(faces, on_face):
    """Take barycentric subdivision to eliminate all simplex inversions."""
    original_faces = sorted(faces, key=lambda f:(len(f),f))
    fid = {face: i for i,face in enumerate(original_faces)}
    induced = [fid[on_face(face)] for face in original_faces]
    def subset(a,b):
        return len(a)<len(b) and set(a).issubset(b)
    sizegroups = {d: [i for i,f in enumerate(original_faces) if len(f)==d]
                  for d in (1,2,3)}
    chains = {(i,) for i in range(len(original_faces))}
    for d in (1,2):
        for e in range(d+1,4):
            for i in sizegroups[d]:
                for j in sizegroups[e]:
                    if subset(original_faces[i], original_faces[j]):
                        chains.add((i,j))
    for i in sizegroups[1]:
        for j in sizegroups[2]:
            if subset(original_faces[i], original_faces[j]):
                for k in sizegroups[3]:
                    if subset(original_faces[j],original_faces[k]):
                        chains.add((i,j,k))
    assert Counter(map(len,chains)) == {1:612, 2:2112, 3:1536}
    def shift(ch):
        return tuple(induced[i] for i in ch)
    assert all(shift(ch) in chains for ch in chains)
    orbit_of = {}
    representatives = {}
    groups = defaultdict(list)
    for ch in sorted(chains, key=lambda t:(len(t),t)):
        if ch in orbit_of:
            continue
        orbit = []
        temp = ch
        while temp not in orbit:
            orbit.append(temp)
            temp = shift(temp)
        assert temp == ch and 8 % len(orbit) == 0
        oi = len(representatives)
        representatives[oi] = ch
        for a in orbit:
            assert a not in orbit_of
            orbit_of[a] = oi
        groups[len(ch)].append(oi)
    assert {d:len(groups[d]) for d in (1,2,3)} == {1:77,2:264,3:192}
    return orbit_of, representatives, groups


def relator_presentation(orbit_of, reps, groups):
    """Triangulated-2-complex CW presentation from a maximal tree."""
    vert = groups[1]
    vertloc = {x:i for i,x in enumerate(vert)}
    edges = groups[2]
    tri = groups[3]
    parent = list(range(len(vert)))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    tree = set()
    for oi in edges:
        a,b = reps[oi]
        u = vertloc[orbit_of[(a,)]]
        v = vertloc[orbit_of[(b,)]]
        ru,rv = root(u),root(v)
        if ru != rv:
            parent[ru] = rv
            tree.add(oi)
    assert len(tree) == 76 and len({root(i) for i in range(77)}) == 1
    labels = {oi:i+1 for i,oi in enumerate(x for x in edges if x not in tree)}
    assert len(labels) == 188
    def freereduce(word):
        stack = []
        for x in word:
            if stack and stack[-1] == -x:
                stack.pop()
            else:
                stack.append(x)
        return stack
    relators = []
    for oi in tri:
        a,b,c = reps[oi]
        boundary = ((a,b),(b,c),(a,c))
        word = []
        for j,edge in enumerate(boundary):
            edge_orb = orbit_of[edge]
            label = labels.get(edge_orb)
            if label is not None:
                word.append(label if j<2 else -label)
        relators.append(freereduce(word))
    assert len(relators) == 192
    return relators, set(labels.values())


def eliminate_generators(relators, active):
    """Exact 2-CW generator/2-cell eliminations, preserving the empty 2-cells."""
    def invert(w):
        return [-g for g in reversed(w)]
    def free_reduce(w):
        stack=[]
        for v in w:
            if stack and stack[-1] == -v:
                stack.pop()
            else:
                stack.append(v)
        return stack
    initial = len(active)
    trace = []
    while True:
        counts = Counter(abs(g) for rel in relators for g in rel)
        candidates=[]
        for i,rel in enumerate(relators):
            if len(rel)>8:
                continue
            within=Counter(abs(g) for g in rel)
            for gen,multiplicity in within.items():
                if multiplicity == 1:
                    candidates.append((len(rel),counts[gen],gen,i))
        if not candidates:
            break
        _,_,gen,i = min(candidates)
        old = relators.pop(i)
        j = next(j for j,g in enumerate(old) if abs(g)==gen)
        cyclic = old[j:]+old[:j]
        expr = invert(cyclic[1:]) if cyclic[0]>0 else cyclic[1:]
        assert gen not in set(map(abs,expr))
        relators = [free_reduce([y for x in word for y in
                    (expr if x==gen else invert(expr) if x==-gen else [x])])
                    for word in relators]
        active.remove(gen)
        trace.append((gen,tuple(expr)))
        assert len(relators) + len(trace) == 192
    assert initial == 188 and len(trace) == 187
    assert len(active)==1 and len(relators)==5
    surviving = next(iter(active))
    assert sorted(abs(sum(1 if g==surviving else -1 for g in rel))
                  for rel in relators) == [0,0,4,4,4]
    assert all(all(abs(g)==surviving for g in rel) for rel in relators)
    assert all(free_reduced(r) for r in relators)
    trace_text='\n'.join('%s:%s'%(g,','.join(map(str,w))) for g,w in trace)
    trace_hash=sha256(trace_text.encode('ascii')).hexdigest()
    return trace_hash, sorted([tuple(rel) for rel in relators])


def free_reduced(w):
    return not any(w[i]==-w[i+1] for i in range(len(w)-1))


def main():
    group=check_group()
    faces,on_face=build_original_complex(group)
    orbit,reps,grouped=quotient_simplices(faces,on_face)
    relators,active=relator_presentation(orbit,reps,grouped)
    trace_hash,last=eliminate_generators(relators,active)
    print('B4_KREWERAS_WEDGE_CERTIFICATE_OK')
    print('signed_permutations=384 rank_distribution=1,16,36,16,1')
    print('original_simplices=68,288,256')
    print('barycentric_orbit_cells=77,264,192')
    print('one_cell_eliminations=187 remaining_generator=1 remaining_2cells=5')
    print('remaining_attaching_degrees=0,0,4,4,4')
    print('homotopy_type=Moore(Z/4,1) wedge four S2')
    print('elimination_trace_sha256='+trace_hash)

if __name__ == '__main__':
    main()
