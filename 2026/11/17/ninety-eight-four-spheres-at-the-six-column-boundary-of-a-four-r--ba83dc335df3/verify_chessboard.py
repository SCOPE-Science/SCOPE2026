"""Exact finite certificate for a four-row, six-column multiple chessboard complex.

Python 3 standard library only.  Nonempty faces use 24-bit masks, bit (4*c+r)
represents row r, column c.  Vertices and columns are zero-based internally.
"""
from collections import Counter, deque
from itertools import combinations
from random import Random
from hashlib import sha256

M=6
CAP=(1,2,2,2)
N=4*M


def faces_by_columns():
    states={(0,(0,0,0,0))}
    for c in range(M):
        nxt=set()
        for mask,counts in states:
            nxt.add((mask,counts))
            for r in range(4):
                if counts[r]<CAP[r]:
                    k=list(counts);k[r]+=1
                    nxt.add((mask|(1<<(4*c+r)),tuple(k)))
        states=nxt
    faces={mask for mask,_ in states}
    assert len(faces)==len(states)
    return faces


def faces_by_rows():
    result=set()
    def rec(r,used,mask):
        if r==4:
            result.add(mask)
            return
        remaining=[c for c in range(M) if not ((used>>c)&1)]
        for size in range(min(CAP[r],len(remaining))+1):
            for chosen in combinations(remaining,size):
                add=sum(1<<(4*c+r) for c in chosen)
                other=sum(1<<c for c in chosen)
                rec(r+1,used|other,mask|add)
    rec(0,0,0)
    return result


def lexicographic_matching(faces):
    remaining=set(faces)-{0}
    pairs=[]
    order=list(range(N)); Random(427).shuffle(order)
    # In each pass the used bit is toggled whenever both faces survive.
    for v in order:
        bit=1<<v
        for f in sorted(remaining):
            if f not in remaining or f&bit: continue
            g=f|bit
            if g in remaining:
                remaining.remove(f)
                remaining.remove(g)
                pairs.append((f,g))
    return order,pairs,remaining


def check_acyclicity(faces,pairs):
    nonempty=faces-{0}
    matching_top={top:lower for lower,top in pairs}
    assert len(matching_top)==len(pairs)
    indeg={f:0 for f in nonempty}
    succ={f:[] for f in nonempty}
    edges=0
    for top in nonempty:
        b=top
        while b:
            bit=b&-b; b-=bit
            lower=top^bit
            if lower==0: continue
            assert lower in nonempty
            if matching_top.get(top)==lower:
                src,dst=lower,top
            else:
                src,dst=top,lower
            succ[src].append(dst);indeg[dst]+=1;edges+=1
    queue=deque(f for f in nonempty if indeg[f]==0)
    seen=0
    while queue:
        f=queue.popleft();seen+=1
        for g in succ[f]:
            indeg[g]-=1
            if indeg[g]==0: queue.append(g)
    assert seen==len(nonempty), ('directed Hasse cycle',seen,len(nonempty))
    return edges,seen


def mod2_rank(cols):
    basis={}
    for c in cols:
        while c:
            i=c.bit_length()-1
            if i in basis:c ^= basis[i]
            else:
                basis[i]=c
                break
    return len(basis)


def mod2_chain_ranks(faces):
    by_dim={d: sorted(f for f in faces if f and f.bit_count()-1==d)
            for d in range(6)}
    ranks={0:1} # rank of augmentation C_0 -> Z
    for d in range(1,6):
        index={f:i for i,f in enumerate(by_dim[d-1])}
        cols=[]
        for f in by_dim[d]:
            b=f; col=0
            while b:
                bit=b&-b;b-=bit
                col^=1<<index[f^bit]
            cols.append(col)
        ranks[d]=mod2_rank(cols)
    ranks[6]=0
    betti={d: len(by_dim[d])-ranks[d]-ranks[d+1] for d in range(6)}
    return ranks,betti


def main():
    faces=faces_by_columns()
    assert faces==faces_by_rows(), 'independent face enumeration disagreement'
    assert len(faces)==6310
    fv=Counter(f.bit_count()-1 for f in faces if f)
    assert dict(sorted(fv.items()))=={0:24,1:225,2:1020,3:2250,4:2160,5:630}
    assert sum((-1)**d*n for d,n in fv.items())==99
    order,pairs,critical=lexicographic_matching(faces)
    assert len(pairs)==3105
    assert Counter(f.bit_count()-1 for f in critical)=={0:1,4:98}
    assert len(critical)==99
    assert all(x in faces and y in faces and (x&y)==x and
               y.bit_count()==x.bit_count()+1 for x,y in pairs)
    assert len(set(x for pair in pairs for x in pair))==2*len(pairs)
    edges,seen=check_acyclicity(faces,pairs)
    assert seen==6309
    ranks,betti=mod2_chain_ranks(faces)
    assert betti=={0:0,1:0,2:0,3:0,4:98,5:0}
    print('CHESSBOARD_4X6_1222_EXACT_PASS')
    print('face_dimensions=',dict(sorted(fv.items())))
    print('matching_order=',order)
    print('matched_pairs=',len(pairs))
    print('critical_dimensions=',dict(sorted(Counter(f.bit_count()-1 for f in critical).items())))
    print('directed_hasse_edges=',edges,'topologically_sorted_faces=',seen)
    print('mod_two_differential_ranks=',ranks)
    print('mod_two_reduced_betti=',betti)
    data=';'.join(f'{u},{v}' for u,v in pairs).encode()
    print('matching_pair_list_sha256=',sha256(data).hexdigest())

if __name__=='__main__':main()
