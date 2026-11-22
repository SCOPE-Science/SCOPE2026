"""Finite cross-checks for Singer quotients of projective-plane nonincidence complexes.

Run with Python 3 standard library. The all-prime-power theorem is proved in RESULT.md;
these tests independently check concrete cyclic difference-set incidence models.
"""
from collections import Counter, defaultdict
from itertools import combinations

DATA = {2:(7,{0,1,3}), 3:(13,{0,1,3,9}), 4:(21,{0,1,4,14,16})}

def check_projective_plane(q,n,D):
    assert n==q*q+q+1 and len(D)==q+1
    differences=Counter((b-a)%n for a in D for b in D if a!=b)
    assert set(differences)==set(range(1,n))
    assert all(v==1 for v in differences.values())
    lines=[{(x+d)%n for d in D} for x in range(n)]
    assert len(set(map(frozenset,lines)))==n
    for a,b in combinations(range(n),2):
        assert sum(a in line and b in line for line in lines)==1
    assert sum(len(line)-1 for line in lines)==n*q
    # The star tree is selected equivariantly from a point pair differing by one.
    a,b=next((a,b) for a in D for b in D if (b-a)%n==1)
    trees=[{frozenset(((x+a)%n,(x+d)%n)) for d in D if d!=a} for x in range(n)]
    edges=set().union(*trees)
    assert len(edges)==n*q
    offsets={tuple(sorted(((b-a)%n,(a-b)%n))) for _ in [0]}
    assert (b-a)%n==1
    # A connected cycle of step-one edges is already contained in the forest union.
    assert all(frozenset((x,(x+1)%n)) in edges for x in range(n))
    edge_orbits={frozenset(((y-x)%n,(x-y)%n)) for x,y in (tuple(e) for e in edges)}
    # The actual number of orbits, via translating each unordered edge.
    reps={min(tuple(sorted(((u+k)%n,(v+k)%n))) for k in range(n))
          for u,v in (tuple(e) for e in edges)}
    assert len(reps)==q
    assert len(edges)-n+1==1+n*(q-1)


def check_fano_quotient_chain():
    n=7; points=(1<<7)-1; lines=points<<7; central_bits=(1<<14)|(1<<15)
    D={2,4,5,6} # nonincidence offsets for Fano line difference set {0,1,3}
    incidence_edges=[(i,7+j) for i in range(n) for j in range(n) if (i-j)%n in D]
    def independent(mask):
        return all(not(mask>>u&1 and mask>>v&1) for u,v in incidence_edges)
    faces={mask for mask in range(1,1<<14) if mask not in (points,lines) and independent(mask)}
    for v,shore in ((14,points),(15,lines)):
        faces.update((sub|(1<<v)) for sub in range(shore+1) if sub&~shore==0 and sub!=shore)
    def rotate(mask,k):
        out=mask&central_bits
        for v in range(14):
            if mask>>v&1:out|=1<<(7*(v//7)+(v%7+k)%7)
        return out
    for face in faces:
        assert all(rotate(face,k) in faces for k in range(n))
    rep={f:min(rotate(f,k) for k in range(n)) for f in faces}
    cells={d:sorted({rep[f] for f in faces if f.bit_count()-1==d}) for d in range(7)}
    assert tuple(len(cells[d]) for d in range(7))==(4,11,22,22,16,8,2)
    idcell={d:{f:i for i,f in enumerate(cells[d])} for d in cells}
    def canonical_orientation(mask):
        target=rep[mask]
        k=next(k for k in range(n) if rotate(mask,k)==target)
        vertices=[v for v in range(16) if mask>>v&1]
        moved=[v if v>=14 else 7*(v//7)+(v%7+k)%7 for v in vertices]
        inversions=sum(moved[i]>moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
        return target, -1 if inversions%2 else 1
    # Sparse chain matrices indexed by (row,column), with exact integral coefficients.
    sizes={d:len(cells[d]) for d in cells}
    boundaries={}
    for d in range(1,7):
        b={}
        for j,c in enumerate(cells[d]):
            vertices=[v for v in range(16) if c>>v&1]
            for i,v in enumerate(vertices):
                f,sign=canonical_orientation(c^(1<<v))
                key=(idcell[d-1][f],j)
                b[key]=b.get(key,0)+(-1)**i*sign
        boundaries[d]={k:v for k,v in b.items() if v}
    for d in range(2,7):
        left=defaultdict(list)
        for (i,j),v in boundaries[d-1].items():left[j].append((i,v))
        prod=Counter()
        for (j,k),v in boundaries[d].items():
            for i,w in left[j]:prod[i,k]+=v*w
        assert not any(prod.values()),('boundary square',d)
    expected=(0,3,8,12,10,6,2)
    counts=Counter()
    while True:
        pivot=next(((d,r,c,s) for d in range(1,7) for (r,c),s in sorted(boundaries[d].items()) if abs(s)==1),None)
        if pivot is None:break
        d,r,c,s=pivot
        b=boundaries[d]
        col={i:v for (i,j),v in b.items() if j==c}
        row={j:v for (i,j),v in b.items() if i==r}
        for i,vi in col.items():
            if i==r:continue
            for j,vj in row.items():
                if j==c:continue
                key=(i,j); val=b.get(key,0)-vi*vj*s
                if val:b[key]=val
                else:b.pop(key,None)
        # Remove row and column in this differential, and corresponding neighboring axes.
        boundaries[d]={key:v for key,v in b.items() if key[0]!=r and key[1]!=c}
        if d+1<=6:boundaries[d+1]={key:v for key,v in boundaries[d+1].items() if key[0]!=c}
        if d-1>=1:boundaries[d-1]={key:v for key,v in boundaries[d-1].items() if key[1]!=r}
        sizes[d]-=1;sizes[d-1]-=1;counts[d]+=1
    assert all(not b for b in boundaries.values())
    assert tuple(counts[d] for d in range(7))==expected
    assert tuple(sizes[d] for d in range(7))==(1,0,2,0,0,0,0)

if __name__=='__main__':
    for q,(n,D) in DATA.items():check_projective_plane(q,n,D)
    check_fano_quotient_chain()
    print('SINGER_NONINCIDENCE_QUOTIENT_CHECKS_OK')
