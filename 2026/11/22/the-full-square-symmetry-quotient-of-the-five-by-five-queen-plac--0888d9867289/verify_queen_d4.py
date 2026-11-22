#!/usr/bin/env python3
"""Exact finite verification of the geometric D4 quotient of the 5x5 queen complex.

Only the Python standard library is used.  The code verifies the face list,
regular flag-orbit CW structure, elementary collapses, and a finite
presentation simplification of the fundamental group.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product

N=5
SQUARES=tuple(product(range(N),repeat=2))


def symmetries():
    group=[]
    for turns in range(4):
        for mirror in (False,True):
            permutation=[]
            for x0,y0 in SQUARES:
                x,y=x0,y0
                if mirror:y=4-y
                for _ in range(turns):x,y=y,4-x
                permutation.append(SQUARES.index((x,y)))
            group.append(tuple(permutation))
    assert len(set(group))==8
    assert tuple(range(25)) in group
    for s in group:
        for t in group:
            assert tuple(s[t[i]] for i in range(25)) in group
    return group


def faces():
    # Lexicographically unique legal queen sets.  A queen attacks along any
    # shared row, shared column, or shared (slope +/-1) diagonal.
    comp=[0]*25
    for j,(r,c) in enumerate(SQUARES):
        for k,(s,t) in enumerate(SQUARES):
            if j!=k and r!=s and c!=t and abs(r-s)!=abs(c-t):
                comp[j]|=1<<k
    d=defaultdict(list)
    def extend(mask,avail):
        if mask:d[mask.bit_count()-1].append(mask)
        while avail:
            bit=avail&-avail
            v=bit.bit_length()-1
            avail^=bit
            extend(mask|bit, avail&comp[v])
    extend(0,(1<<25)-1)
    assert [len(d[i]) for i in range(5)] == [25,140,204,82,10]
    assert not d.get(5)
    return [f for k in range(5) for f in d[k]]


def image(face,p):
    out=0
    while face:
        bit=face&-face
        out|=1<<p[bit.bit_length()-1]
        face^=bit
    return out


def orbit_flag_data(faces,group):
    F=set(faces)
    for s in group:
        assert {image(f,s) for f in F}==F
    # All nonempty flags, not only saturated flags; enumerate uniquely by
    # recursively inserting any strictly smaller nonempty face at the front.
    flags=defaultdict(list)
    proper={f:[] for f in faces}
    for f in faces:
        g=(f-1)&f
        while g:
            proper[f].append(g)
            g=(g-1)&f
    def chains(chain):
        flags[len(chain)-1].append(chain)
        for sf in proper[chain[0]]:
            chains((sf,)+chain)
    for f in faces:chains((f,))
    assert [len(flags[k]) for k in range(5)] == [461,2952,5676,4368,1200]

    @lru_cache(None)
    def canonical(flag):
        return min(tuple(image(f,s) for f in flag) for s in group)

    orbit=[]; index=[]
    for d in range(5):
        reps=sorted(set(canonical(flag) for flag in flags[d]))
        orbit.append(reps)
        index.append({flag:j for j,flag in enumerate(reps)})
    assert list(map(len,orbit))==[63,373,711,546,150]

    # A chain has one face of each given rank, hence no nontrivial symmetry
    # can permute its vertices.  Orbiting these chains gives regular cells.
    def which(flag):return index[len(flag)-1][canonical(flag)]
    bounds={}
    for d in range(1,5):
        for j,flag in enumerate(orbit[d]):
            row=Counter()
            for k in range(d+1):
                faceflag=flag[:k]+flag[k+1:]
                row[which(faceflag)]+=(-1)**k
            # Distinct dimension-tags on omitted flags imply no face
            # identifications inside the boundary of one orbit cell.
            assert len(row)==d+1 and all(abs(x)==1 for x in row.values())
            bounds[d,j]=dict(row)
    for d in range(2,5):
        for j in range(len(orbit[d])):
            twice=Counter()
            for k,c in bounds[d,j].items():
                for l,b in bounds[d-1,k].items():
                    twice[l]+=c*b
            assert not any(twice.values())
    return orbit,which,bounds


def elementary_collapses(orbit,bounds):
    live={d:set(range(len(orbit[d]))) for d in range(5)}
    above=defaultdict(set)
    for (d,j),bd in bounds.items():
        for k,val in bd.items():
            if val:above[d-1,k].add((d,j))
    queue=deque((d,j) for d in range(5) for j in range(len(orbit[d])))
    pairs=[]
    while queue:
        d,j=queue.popleft()
        if j not in live[d]:continue
        cofaces=[x for x in above[d,j] if x[1] in live[x[0]]]
        if len(cofaces)!=1 or cofaces[0][0]!=d+1:continue
        c=cofaces[0]
        assert abs(bounds[c][j])==1
        # A free face must meet a maximal coface, not a cell that remains
        # inside a higher-dimensional cell.
        assert not any(k in live[d+2] for dim,k in above.get(c,set()) if dim==d+2) if d+2<5 else True
        live[d].remove(j)
        live[d+1].remove(c[1])
        pairs.append(((d,j),c))
        for k in bounds[c]:
            if k in live[d]:queue.append((d,k))
        if d:
            for k in bounds[d,j]:
                if k in live[d-1]:queue.append((d-1,k))
    assert len(pairs)==823
    assert [len(live[d]) for d in range(5)]==[30,96,71,0,0]
    assert sum((-1)**d*len(live[d]) for d in range(5))==5
    return pairs


def cyclic_reduce(word):
    stack=[]
    for letter in word:
        if stack and stack[-1]==-letter:stack.pop()
        else:stack.append(letter)
    while len(stack)>1 and stack[0]==-stack[-1]:
        stack=stack[1:-1]
    return tuple(stack)


def fundamental_group(orbit,which):
    verts=[(f[0],) for f in orbit[0]]
    assert len(verts)==63
    edges=[(which((f[0],)),which((f[1],))) for f in orbit[1]]
    adjacency=defaultdict(list)
    for j,(a,b) in enumerate(edges):
        adjacency[a].append((b,j));adjacency[b].append((a,j))
    visited={0};tree=set();q=deque([0])
    while q:
        v=q.popleft()
        for w,j in adjacency[v]:
            if w not in visited:
                visited.add(w);tree.add(j);q.append(w)
    assert len(visited)==63 and len(tree)==62
    generator={j:idx+1 for idx,j in enumerate(j for j in range(len(edges)) if j not in tree)}
    assert len(generator)==311
    relators=[]
    for flag in orbit[2]:
        word=[]
        for two,sgn in [((flag[0],flag[1]),1),
                         ((flag[1],flag[2]),1),
                         ((flag[0],flag[2]),-1)]:
            e=which(two)
            if e in generator:word.append(sgn*generator[e])
        relators.append(cyclic_reduce(word))
    assert Counter(map(len,relators))==Counter({1:94,2:190,3:427})
    relators=[r for r in relators if r]
    active=set(generator.values());steps=[]
    while True:
        candidate=None
        # A Tietze elimination can solve for a generator occurring exactly
        # once (with exponent +1 or -1) in a cyclic relator.
        for i in sorted(range(len(relators)),key=lambda i:(len(relators[i]),i)):
            word=relators[i]
            counts=Counter(abs(x) for x in word)
            for j,letter in enumerate(word):
                if counts[abs(letter)]==1:
                    candidate=(i,j);break
            if candidate:break
        if candidate is None:break
        i,j=candidate
        word=relators[i]
        letter=word[j]
        other=word[j+1:]+word[:j]
        # The cyclic relator letter*other=1 is equivalent to replacing
        # the positive generator by the inverse of 'other' (if letter>0).
        rhs=tuple(-x for x in reversed(other)) if letter>0 else tuple(other)
        g=abs(letter)
        assert g in active
        new=[]
        for k,relator in enumerate(relators):
            if k==i:continue
            expanded=[]
            for x in relator:
                if x==g:expanded.extend(rhs)
                elif x==-g:expanded.extend(-y for y in reversed(rhs))
                else:expanded.append(x)
            rr=cyclic_reduce(expanded)
            if rr:new.append(rr)
        relators=new
        active.remove(g)
        steps.append((g,letter,tuple(rhs)))
    assert len(steps)==311 and not active and not relators
    return steps


def burnside_euler(faces, group):
    # Independent Euler check using invariant nonempty face posets rather than
    # orbit enumeration: no inversions after barycentric subdivision.
    fixed_eulers=[]
    for p in group:
        fixed=sorted((f for f in faces if image(f,p)==f), key=int.bit_count)
        contribution={}
        for f in fixed:
            contribution[f]=1-sum(v for s,v in contribution.items() if s&f==s)
        fixed_eulers.append(sum(contribution.values()))
    assert fixed_eulers==[17,5,1,5,1,5,1,5]
    assert sum(fixed_eulers)==8*5
    return fixed_eulers


def main():
    G=symmetries()
    X=faces()
    eulers=burnside_euler(X,G)
    orbit,which,bounds=orbit_flag_data(X,G)
    drops=elementary_collapses(orbit,bounds)
    eliminated=fundamental_group(orbit,which)
    # By the collapses the quotient is homotopy-equivalent to a connected
    # 2-complex. Its computed fundamental group is trivial, and Euler
    # characteristic 5 implies H_2 = Z^4 (H_2 is a subgroup of free C_2).
    # The simply-connected homology version of Whitehead's theorem gives
    # the wedge of four 2-spheres as the exact homotopy type.
    print('QUEENS5_D4_QUOTIENT_VERIFIED')
    print('face_counts=(25,140,204,82,10)')
    print('flag_orbit_cells=(63,373,711,546,150)')
    print('Burnside_fixed_Euler=',tuple(eulers))
    print('elementary_collapse_pairs=',len(drops))
    print('remaining_cell_counts=(30,96,71,0,0)')
    print('Tietze_generator_eliminations=',len(eliminated))
    print('pi1=1, Euler_characteristic=5, homotopy_type=vee_4_S2')

if __name__=='__main__':main()
