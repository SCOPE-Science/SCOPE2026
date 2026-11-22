"""Standalone exact checker for the pentagonal noncrossing-partition orbit theorem.

Python 3 standard library only. No numerical approximations or external datasets.
The finite verifier checks the cellular presentation; classical general
shellability and the orbit-space fundamental-group theorem are used separately.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

N = 5

def set_partitions(n):
    labels = [0] * n
    def extend(i, largest):
        if i == n:
            yield tuple(labels)
            return
        for new_label in range(largest + 2):
            labels[i] = new_label
            yield from extend(i + 1, max(largest, new_label))
    yield from extend(1, 0)

def canonical(labels):
    blocks = {}
    for v, b in enumerate(labels):
        blocks.setdefault(b, []).append(v)
    return tuple(sorted((tuple(vs) for vs in blocks.values()), key=lambda b:b[0]))

def noncrossing(labels, quadruples):
    return not any(labels[a] == labels[c] and labels[b] == labels[d]
                   and labels[a] != labels[b] for a,b,c,d in quadruples)

def transform(partition, permutation):
    return tuple(sorted((tuple(sorted(permutation(v) for v in block))
                        for block in partition), key=lambda b:b[0]))

def refines(finer, coarser):
    block_of = {v:j for j,block in enumerate(coarser) for v in block}
    return all(len({block_of[v] for v in block}) == 1 for block in finer)

def freereduce(word):
    result=[]
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result

def inverse(word):
    return [-a for a in reversed(word)]

def make_faces():
    quadruples=list(combinations(range(N),4))
    parts=sorted({canonical(x) for x in set_partitions(N)
                  if noncrossing(x,quadruples)})
    assert len(parts)==comb(2*N,N)//(N+1)==42
    proper=[p for p in parts if 1<len(p)<N]
    assert len(proper)==40
    rank=lambda p:N-len(p)
    edges=[(p,q) for p in proper for q in proper
           if rank(p)<rank(q) and refines(p,q)]
    triangles=[(p,q,t) for p in proper for q in proper for t in proper
               if rank(p)<rank(q)<rank(t) and refines(p,q) and refines(q,t)]
    faces=[[(p,) for p in proper],edges,triangles]
    assert tuple(map(len,faces)) == (40,150,125)
    return faces

def orbits(faces, operations):
    def rep(face):
        return min(tuple(transform(p,op) for p in face) for op in operations)
    return [sorted({rep(face) for face in level}) for level in faces],rep

def make_operations():
    identity=[lambda v:v]
    rotations=[lambda v,k=k:(v+k)%N for k in range(N)]
    reflections=[lambda v,k=k:(k-v)%N for k in range(N)]
    return {'trivial':identity,'reflection':identity+[reflections[0]],
            'rotations':rotations,'dihedral':rotations+reflections}

def presentation_for_rotations(faces, rotation_ops):
    orbit_faces,representative=orbits(faces,rotation_ops)
    assert tuple(map(len,orbit_faces)) == (8,30,25)
    cell_index=[{cell:j for j,cell in enumerate(level)}
                for level in orbit_faces]
    boundaries=[None,{},{}]
    for d in (1,2):
        for j,cell in enumerate(orbit_faces[d]):
            boundaries[d][j]=[(cell_index[d-1][representative(cell[:k]+cell[k+1:])],
                                (-1)**k) for k in range(d+1)]
    # Explicit integer check d_1 d_2 = 0.
    for triangle in boundaries[2].values():
        chain=defaultdict(int)
        for edge,coef in triangle:
            for vertex,sign in boundaries[1][edge]:
                chain[vertex]+=coef*sign
        assert all(coef==0 for coef in chain.values())
    # Contract a spanning tree of the connected one-skeleton.
    parent=list(range(len(orbit_faces[0])))
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    tree=[]
    generators=[]
    for e,ends in sorted(boundaries[1].items()):
        u,v=[x for x,_ in ends]
        if find(u)!=find(v):
            parent[find(u)]=find(v)
            tree.append(e)
        else:
            generators.append(e)
    assert len(tree)==7 and len(generators)==23
    assert len({find(j) for j in parent})==1
    relators=[]
    for t in sorted(boundaries[2]):
        word=[sign*(e+1) for e,sign in boundaries[2][t] if e in generators]
        relators.append(freereduce(word))
    # An attaching word in which a 1-cell occurs once permits a 1/2-cell
    # cancellation after a homotopy of attaching maps. Substitute the resulting
    # word into every other 2-cell before cancelling. This is a 2-deformation,
    # not an inference from a group presentation alone.
    remaining={e+1 for e in generators}
    cancellations=[]
    while True:
        options=[]
        for ridx,word in enumerate(relators):
            for j,x in enumerate(word):
                if sum(abs(z)==abs(x) for z in word)==1:
                    occurrences=sum(sum(abs(z)==abs(x) for z in w) for w in relators)
                    options.append((len(word),occurrences,ridx,j,abs(x)))
        if not options:
            break
        _,_,ridx,j,g=min(options)
        word=relators.pop(ridx)
        letter=word[j]
        other=word[j+1:]+word[:j]
        replacement=inverse(other) if letter>0 else other
        for i,w in enumerate(relators):
            substituted=[]
            for x in w:
                if x==g:
                    substituted.extend(replacement)
                elif x==-g:
                    substituted.extend(inverse(replacement))
                else:
                    substituted.append(x)
            relators[i]=freereduce(substituted)
        remaining.remove(g)
        cancellations.append((g,ridx,len(replacement)))
    assert len(cancellations)==22
    assert len(remaining)==1 and len(relators)==3
    generator=next(iter(remaining))
    # Two null-attaching maps give independent two-spheres; the degree-five
    # map on the final circle yields M(Z/5,1).
    assert sum(w==[] for w in relators)==2
    nonempty=[w for w in relators if w]
    assert len(nonempty)==1 and len(nonempty[0])==5
    assert all(abs(x)==generator for x in nonempty[0])
    assert abs(sum(1 if x>0 else -1 for x in nonempty[0]))==5
    return generator,relators,cancellations,tree,orbit_faces

def check():
    faces=make_faces()
    actions=make_operations()
    expected={
        'trivial':((40,150,125),15),
        'reflection':((24,81,65),8),
        'rotations':((8,30,25),3),
        'dihedral':((8,21,15),2),
    }
    for name,op in actions.items():
        levels,_=orbits(faces,op)
        counts=tuple(map(len,levels))
        euler=counts[0]-counts[1]+counts[2]
        assert (counts,euler)==expected[name],(name,counts,euler)
        print('%s: cells=%s Euler=%d' % (name,counts,euler))
    # The fivefold action is free on the proper-part complex: a nontrivial
    # rotation fixes neither a vertex nor a chain (rank is preserved).
    proper=[face[0] for face in faces[0]]
    for k in range(1,N):
        assert not any(transform(p,lambda v:(v+k)%N)==p for p in proper)
    # Every pentagon reflection fixes a proper partition of one adjacent pair.
    for k in range(N):
        assert any(transform(p,lambda v:(k-v)%N)==p for p in proper)
    g,rel,cancellations,tree,_=presentation_for_rotations(faces,actions['rotations'])
    print('cyclic_quotient: spanning_tree_edges=%d cancelled_1_2_pairs=%d'
          % (len(tree),len(cancellations)))
    print('terminal_1_cell=%d attaching_words=%s' % (g,rel))
    print('result: M(Z/5,1) wedge S^2 wedge S^2')
    print('VERIFY_OK')

if __name__=='__main__':
    check()
