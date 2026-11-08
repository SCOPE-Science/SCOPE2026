"""Finite proofs for the symmetry-fixed matching complexes of two circular ladders.

Uses only the Python standard library. Run: python verify_twisted.py
The main proof is an exhaustive acyclic matching on all simplicial faces.
"""
from collections import Counter, defaultdict, deque


def mobius_edges(k):
    n=2*k
    return [tuple(sorted((i,(i+1)%n))) for i in range(n)] + [(i,i+k) for i in range(k)]


def full_matching_faces(supports):
    faces={0}
    def rec(i,used,mask):
        if i==len(supports):
            faces.add(mask);return
        rec(i+1,used,mask)
        if used&supports[i]==0:
            rec(i+1,used|supports[i],mask|(1<<i))
    rec(0,0,0)
    return faces


def prism_orbit_faces(k,expected_edges):
    n=2*k
    def vid(i,a):return 2*(i%n)+a
    def e(u,v):return tuple(sorted((u,v)))
    def twist(v):
        i,a=divmod(v,2)
        return vid(i+k,1-a)
    full=set()
    for a in [0,1]:
        for i in range(n):
            full.add(e(vid(i,a),vid(i+1,a)))
    for i in range(n):full.add(e(vid(i,0),vid(i,1)))
    assert len(full)==3*n
    orbits=[];seen=set()
    for edge in sorted(full):
        if edge in seen:continue
        image=e(twist(edge[0]),twist(edge[1]))
        assert image in full and image!=edge
        pair={edge,image}
        assert pair.isdisjoint(seen)
        assert len(set(edge+image))==4
        seen.update(pair)
        orbits.append(frozenset(pair))
    assert len(orbits)==3*k and seen==full
    orbit_to_idx={orb:i for i,orb in enumerate(orbits)}
    ordered=[]
    for u,v in expected_edges:
        # Each quotient edge lifts from a top-layer rim edge or a rung.
        if v==(u+k): # canonical chord has u<k
            selected=e(vid(u,0),vid(u,1))
        else:
            selected=e(vid(u,0),vid(v,0))
        image=e(twist(selected[0]),twist(selected[1]))
        ordered.append(orbit_to_idx[frozenset({selected,image})])
    assert sorted(ordered)==list(range(3*k))
    supports=[]
    for idx in ordered:
        endpoints={v for edge in orbits[idx] for v in edge}
        assert len(endpoints)==4
        supports.append(sum(1<<v for v in endpoints))
    return full_matching_faces(supports)


def toggle_morse(faces,nedges):
    remaining=set(faces);matching=[]
    for j in range(nedges):
        bit=1<<j
        pairs=[(f,f|bit) for f in remaining if not f&bit and f|bit in remaining]
        used={a for pair in pairs for a in pair}
        assert len(used)==2*len(pairs)
        remaining.difference_update(used)
        matching.extend(pairs)
    assert len(matching)*2+len(remaining)==len(faces)
    return remaining,matching


def check_acyclic(faces,matching):
    matched={(a,b) for a,b in matching}
    indeg={f:0 for f in faces};out=defaultdict(list);hasse=0
    for face in faces:
        parts=face
        while parts:
            bit=parts&-parts;parts^=bit
            lower=face^bit
            if (lower,face) in matched:src,dst=face,lower
            else:src,dst=lower,face
            out[src].append(dst);indeg[dst]+=1;hasse+=1
    q=deque(f for f in faces if indeg[f]==0);count=0
    while q:
        f=q.popleft();count+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:q.append(g)
    assert count==len(faces),(count,len(faces))
    return hasse


def binary_rank(columns):
    piv={}
    for column in columns:
        while column:
            head=column.bit_length()-1
            if head in piv:column^=piv[head]
            else:piv[head]=column;break
    return len(piv)


def mod2_homology(faces):
    levels=defaultdict(list)
    for face in faces:
        if face:levels[face.bit_count()-1].append(face)
    indices={d:{f:j for j,f in enumerate(fs)} for d,fs in levels.items()}
    ranks={0:1}
    for d in range(1,max(levels)+1):
        cols=[]
        for face in levels[d]:
            c=0;bits=face
            while bits:
                bit=bits&-bits;bits^=bit
                c^=1<<indices[d-1][face^bit]
            cols.append(c)
        ranks[d]=binary_rank(cols)
    return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)
            for d,fs in levels.items() if len(fs)-ranks.get(d,0)-ranks.get(d+1,0)}


def main():
    for k,target,dim in [(6,10,3),(7,16,4)]:
        edges=mobius_edges(k)
        assert len(set(edges))==3*k
        supports=[(1<<u)|(1<<v) for u,v in edges]
        faces=full_matching_faces(supports)
        assert faces==prism_orbit_faces(k,edges), 'Fixed orbit complex mismatch'
        critical,matching=toggle_morse(faces,len(edges))
        assert len(critical)==target
        assert {f.bit_count()-1 for f in critical}=={dim}
        assert 0 not in critical
        hasse=check_acyclic(faces,matching)
        bet=mod2_homology(faces)
        assert bet=={dim:target},(k,bet)
        fvector=dict(sorted(Counter(f.bit_count()-1 for f in faces if f).items()))
        print(f'M_{2*k}: prism edge orbits={3*k}, matching faces={len(faces)},'
              f' fvector={fvector}, Morse pairs={len(matching)},'
              f' unmatched={len(critical)} in dimension {dim},'
              f' Hasse relations={hasse}, reduced mod-2 Betti={bet}')
    print('TWISTED_CIRCULAR_LADDER_FIXED_MOBIUS_MORSE_OK 2')


if __name__=='__main__':main()
