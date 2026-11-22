"""Exact, standalone integral chain certificates for ordinary three-cut complexes.

For C_n^5, n=13,...,20, construct the simplicial Alexander dual K of
Delta_3(C_n^5), then perform elementary chain contractions over Z.
All arithmetic is exact; no external libraries or saved certificate required.
The separate GF(2) calculation uses full, unreduced boundary matrices.
"""
from collections import defaultdict
from itertools import combinations

EXPECTED = {13:(5,1),14:(5,1),15:(3,21),16:(3,101),
            17:(3,52),18:(3,19),19:(3,1),20:(2,4)}


def dual_faces(n):
    def edge(a,b):
        return min((a-b)%n,(b-a)%n) <= 5
    forbidden = [sum(1 << x for x in t) for t in combinations(range(n),3)
                 if sum(edge(a,b) for a,b in combinations(t,2)) < 2]
    levels = {0:[0]}
    for k in range(1,n+1):
        prev = levels[k-1]
        nxt=[]
        for m in prev:
            for j in range(m.bit_length(),n):
                s=m | (1<<j)
                if all((s & b)!=b for b in forbidden):
                    nxt.append(s)
        if not nxt:
            break
        assert len(set(nxt)) == len(nxt)
        levels[k] = nxt
    return levels,forbidden


def signed_boundaries(levels,n):
    # q is chain dimension; include augmentation C_{-1}=Z.
    matrices = {}
    for k in range(1,max(levels)+1):
        columns = {}
        for s in levels[k]:
            columns[s] = {s^(1<<j): (-1)**u for u,j in
                          enumerate(v for v in range(n) if (s>>v)&1)}
        matrices[k-1] = columns
    return matrices


def check_chain(matrices):
    for q in range(1,max(matrices)+1):
        low = matrices[q-1]
        for c,v in matrices[q].items():
            res=defaultdict(int)
            for mid,a in v.items():
                for r,b in low[mid].items():
                    res[r] += a*b
            assert all(x==0 for x in res.values()), (q,c,res)


def integral_unit_contractions(levels,n):
    ds=signed_boundaries(levels,n)
    check_chain(ds)
    remaining={k-1:set(fs) for k,fs in levels.items()}
    summary={}
    # Each unit pivot is an exact integral chain-homotopy cancellation.
    for q in sorted(ds,reverse=True):
        cols=ds[q]
        rows=defaultdict(dict)
        for c,v in cols.items():
            for r,a in v.items():rows[r][c]=a
        count=0
        while True:
            best=None
            for r,inc in rows.items():
                if r not in remaining[q-1]:continue
                for c,a in inc.items():
                    if abs(a)!=1:continue
                    cost=(len(inc)-1)*(len(cols[c])-1)
                    if best is None or cost<best[0]:best=(cost,r,c,a)
                    if cost==0:break
                if best is not None and best[0]==0:break
            if best is None:break
            _,r,c,pivot=best
            pv=cols[c].copy()
            for oc,coef in list(rows[r].items()):
                if oc==c:continue
                factor=coef//pivot
                col=cols[oc]
                for rr,b in pv.items():
                    new=col.get(rr,0)-factor*b
                    if new:
                        col[rr]=new
                        rows[rr][oc]=new
                    else:
                        col.pop(rr,None)
                        rows[rr].pop(oc,None)
            for rr in list(cols[c]):rows[rr].pop(c,None)
            del cols[c]
            remaining[q].remove(c)
            remaining[q-1].remove(r)
            if q+1 in ds:
                for higher in ds[q+1].values(): higher.pop(c,None)
            if q-1 in ds:
                ds[q-1].pop(r,None)
            count += 1
        summary[q] = count
    assert not remaining[-1], (n,'augmentation survives')
    for q,cols in ds.items():
        assert all(not col for col in cols.values()), (n,q,'nonzero remaining boundary')
    critical = {q:len(cs) for q,cs in remaining.items() if q>=0 and cs}
    q,b = EXPECTED[n]
    assert critical == {q:b},(n,critical)
    assert sum(2*v for v in summary.values())+b == sum(map(len,levels.values()))
    return critical,summary


def mod2_betti(levels):
    ranks={0:1}  # augmented boundary rank C_0 -> C_{-1}
    for k in range(1,max(levels)+1):
        rowindex={s:i for i,s in enumerate(levels[k-1])}
        pivots={}
        for s in levels[k]:
            col=0
            for j in range(s.bit_length()):
                if (s>>j)&1:col |= 1<<rowindex[s^(1<<j)]
            while col:
                i=col.bit_length()-1
                if i not in pivots:
                    pivots[i]=col
                    break
                col ^= pivots[i]
        ranks[k]=len(pivots)
    return {k-1:len(levels[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in levels if k>0}


def run():
    for n,expected in EXPECTED.items():
        levels,bad=dual_faces(n)
        critical,steps=integral_unit_contractions(levels,n)
        fb={q:v for q,v in mod2_betti(levels).items() if v}
        assert fb==critical=={expected[0]:expected[1]}
        m=max(levels)
        # Small faces (all vertices, edges, and triangles) of Delta_3 exist,
        # because their complements are too large to be faces of K.
        assert m<n-3
        print('n=%d forbidden_triples=%d dual_faces=%d max_dual_face=%d '
              'integral_dual_betti=%s mod2_dual_betti=%s unit_pairs=%d '
              'ordinary_cut_homotopy=vee_%d_S^%d' %
              (n,len(bad),sum(map(len,levels.values())),m,critical,fb,
               sum(steps.values()),expected[1],n-expected[0]-3))
    print('PASS: all eight integral chain contractions and independent full GF(2) boundary computations')

if __name__=='__main__':run()

# Theorem's complete dihedral-character table, expressed by full vectors:
# rotation r(j)=j+1, reflection s(j)=-j, and s_k(j)=k-j.
CHARACTERS = {
    13:([1]*13,[-1]*13),
    14:([(-1)**k for k in range(14)],[(-1)**(k+1) for k in range(14)]),
    15:([21 if k==0 else 6 if k%5==0 else 1 for k in range(15)],[-3]*15),
    16:([101,-1,1,-1,-3,-1,1,-1,5,-1,1,-1,-3,-1,1,-1],[-3 if k%2==0 else 7 for k in range(16)]),
    17:([52]+[1]*16,[4]*17),
    18:([19]+[(-1)**k for k in range(1,18)],[1 if k%2==0 else -3 for k in range(18)]),
    19:([1]*19,[-1]*19),
    20:([4 if k%10==0 else -4 if k%10==5 else -1 if k%2==0 else 1 for k in range(20)],[0]*20),
}
INVARIANTS = {13:0,14:0,15:0,16:4,17:4,18:0,19:0,20:0}
ROTATION_INVARIANTS = {13:1,14:0,15:3,16:6,17:4,18:1,19:1,20:0}


def orientation_sign(vertex_images):
    return (-1)**sum(vertex_images[a]>vertex_images[b]
                     for a in range(len(vertex_images))
                     for b in range(a+1,len(vertex_images)))


def from_dual_lefschetz(n,levels,d,perm):
    """Equivariant Alexander duality: sign on vertices times dual trace."""
    ambient_sign=orientation_sign([perm(j) for j in range(n)])
    reduced_lefschetz=-1  # empty face in augmented C_{-1}
    for k,faces in levels.items():
        if k==0:continue
        for mask in faces:
            vertices=[j for j in range(n) if mask>>j&1]
            images=[perm(j) for j in vertices]
            if set(vertices)==set(images):
                reduced_lefschetz += (-1)**(k-1)*orientation_sign(images)
    return ambient_sign * ((-1)**d) * reduced_lefschetz


def from_original_lefschetz(n,levels,degree,perm):
    """Independent trace on original (large) cut complex via invariant faces."""
    dual={v for f in levels.values() for v in f}
    full=(1<<n)-1
    seen=set()
    orbit_masks=[]
    for j in range(n):
        if j in seen:continue
        orbit=0
        x=j
        while x not in seen:
            orbit |= 1<<x
            seen.add(x)
            x=perm(x)
        assert x==j
        orbit_masks.append(orbit)
    # Every invariant simplex is a union of whole vertex orbits.
    lefschetz=-1
    for b in range(1<<len(orbit_masks)):
        mask=0
        for t,orbit in enumerate(orbit_masks):
            if (b>>t)&1:mask |= orbit
        # Original faces are exactly complements of NONfaces of dual.
        if not mask or (full^mask) in dual:continue
        vertices=[j for j in range(n) if mask>>j&1]
        lefschetz += (-1)**(len(vertices)-1)*orientation_sign([perm(j) for j in vertices])
    return (-1)**degree*lefschetz


def check_characters():
    for n,(d,rank) in EXPECTED.items():
        levels,bad=dual_faces(n)
        degree=n-d-3
        rotations=[]
        reflections=[]
        for k in range(n):
            for is_reflection in (False,True):
                perm=(lambda j,k=k:(k-j)%n) if is_reflection else (lambda j,k=k:(j+k)%n)
                via_dual=from_dual_lefschetz(n,levels,d,perm)
                via_original=from_original_lefschetz(n,levels,degree,perm)
                assert via_dual==via_original,(n,k,is_reflection,via_dual,via_original)
                (reflections if is_reflection else rotations).append(via_dual)
        assert (rotations,reflections)==CHARACTERS[n],(n,rotations,reflections)
        assert rotations[0]==rank
        assert sum(rotations)//n == ROTATION_INVARIANTS[n]
        assert (sum(rotations)+sum(reflections))//(2*n)==INVARIANTS[n]
        assert sum(rotations)%n==0
        assert (sum(rotations)+sum(reflections))%(2*n)==0
        print('dihedral n=%d rotations=%s reflections=%s rotation_invariants=%d full_invariants=%d' %
              (n,rotations,reflections,ROTATION_INVARIANTS[n],INVARIANTS[n]))
    print('PASS: all 264 dihedral character values match independent Lefschetz computations on original and dual complexes')

if __name__=='__main__':check_characters()
