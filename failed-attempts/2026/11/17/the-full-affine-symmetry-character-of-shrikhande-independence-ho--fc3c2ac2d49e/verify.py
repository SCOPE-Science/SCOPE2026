#!/usr/bin/env python3
"""Exact finite verification for the Shrikhande independence-complex character.
Usage: python3 verify.py (with character_table.csv in the same directory).
Requires Python 3 standard library only.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
import csv

Q = tuple((a, b) for a in range(4) for b in range(4))
index = {x: i for i, x in enumerate(Q)}
D = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
ZERO = (0, 0)
IDENTITY = (1, 0, 0, 1)


def add(x, y):
    return ((x[0] + y[0]) % 4, (x[1] + y[1]) % 4)


def is_edge(v, w, kind):
    x, y = Q[v], Q[w]
    if kind == 'shrikhande':
        return ((x[0]-y[0]) % 4, (x[1]-y[1]) % 4) in D
    return x[0] == y[0] or x[1] == y[1]


def adj_masks(kind):
    adj = [0]*16
    for i in range(16):
        for j in range(i+1, 16):
            if is_edge(i,j,kind):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    assert all(m.bit_count()==6 for m in adj)
    assert all((adj[i]&adj[j]).bit_count()==2
               for i in range(16) for j in range(i+1,16))
    return adj


def all_faces(adj):
    # Independent complete enumeration: every 16-bit subset, no recursion.
    f = [m for m in range(1<<16) if all(not ((m&(1<<v)) and (m & adj[v]))
                                              for v in range(16))]
    return sorted(f, key=lambda x: (x.bit_count(), x))


def morse_check(faces, order):
    # Greedy vertex-toggling face-poset matching, with the empty cell excluded.
    all_nonzero = [s for s in faces if s]
    unmatched = set(all_nonzero)
    matching = {}
    for v in order:
        for s in all_nonzero:
            t = s | (1 << v)
            if not (s & (1<<v)) and s in unmatched and t in unmatched:
                unmatched.remove(s)
                unmatched.remove(t)
                matching[s] = t
    # Every Hasse incidence, directed low->high if matched, high->low otherwise.
    arcs = defaultdict(list)
    indeg = {s:0 for s in all_nonzero}
    total = 0
    for high in all_nonzero:
        if high.bit_count() == 1:
            continue
        for v in range(16):
            if high & (1<<v):
                low = high & ~(1<<v)
                if matching.get(low)==high:
                    src,dst=low,high
                else:
                    src,dst=high,low
                arcs[src].append(dst)
                indeg[dst] += 1
                total += 1
    q=deque(s for s in all_nonzero if indeg[s]==0)
    count=0
    while q:
        s=q.popleft();count+=1
        for t in arcs[s]:
            indeg[t]-=1
            if indeg[t]==0:q.append(t)
    assert count==len(all_nonzero)
    return len(matching), Counter(s.bit_count()-1 for s in unmatched), total


def boundary_rank_mod2(faces, degree):
    # columns in degree d, rows in degree d-1; integer matrices reduced mod 2.
    cols = [s for s in faces if s.bit_count() == degree+1]
    lowers = [s for s in faces if s.bit_count() == degree]
    lower_index = {s:i for i,s in enumerate(lowers)}
    pivots = {}
    for s in cols:
        vec = 0
        for v in range(16):
            if s & (1 << v):
                vec ^= 1 << lower_index[s & ~(1<<v)]
        while vec:
            k=vec.bit_length()-1
            if k not in pivots:
                pivots[k]=vec;break
            vec ^= pivots[k]
    return len(pivots)


def make_affine_linear():
    out=[]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    mat=(a,b,c,d)
                    images = {apply_matrix(mat,v) for v in D}
                    if images == D:
                        out.append(mat)
    assert len(out)==12
    return out


def apply_matrix(A, v):
    a,b,c,d=A;x,y=v
    return ((a*x+b*y)%4,(c*x+d*y)%4)


def affine_perm(A,t):
    return tuple(index[add(apply_matrix(A,v),t)] for v in Q)


def mask_image(mask,perm):
    out=0
    for v in range(16):
        if mask & (1<<v): out|=1<<perm[v]
    return out


def inversion_sign(mask,perm):
    im=[perm[v] for v in range(16) if mask & (1<<v)]
    return -1 if sum(im[i] > im[j] for i in range(len(im)) for j in range(i+1,len(im)))%2 else 1


def lefschetz(faces,perm):
    # Augmented trace; H_2 is the only reduced homology.
    tr=-1
    for face in faces:
        if face and mask_image(face,perm)==face:
            tr += (-1 if face.bit_count()%2==0 else 1)*inversion_sign(face,perm)
    return tr


def cyclic_lefschetz(adj,perm):
    # Independent check via permutation cycles of the sixteen vertices.
    unseen=set(range(16)); cycles=[]
    while unseen:
        v=min(unseen);cy=[];w=v
        while w in unseen:
            unseen.remove(w);cy.append(w);w=perm[w]
        assert w==v
        cycles.append(sum(1<<x for x in cy))
    tr=-1
    for subset in range(1,1<<len(cycles)):
        mask=0
        for i,c in enumerate(cycles):
            if subset & (1<<i):mask |= c
        if all(not (mask&(1<<v) and mask&adj[v]) for v in range(16)):
            # A cyclic permutation of length L has sign (-1)^(L-1).
            # With k included cycles, combined Lefschetz sign is (-1)^(k-1).
            tr += 1 if subset.bit_count()%2 else -1
    return tr


def rmat(A,B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%4,(a*f+b*h)%4,(c*e+d*g)%4,(c*f+d*h)%4)


def main():
    shr_adj=adj_masks('shrikhande')
    rook_adj=adj_masks('rook')
    F=all_faces(shr_adj); R=all_faces(rook_adj)
    sh_counts=Counter(s.bit_count() for s in F)
    ro_counts=Counter(s.bit_count() for s in R)
    assert sh_counts=={0:1,1:16,2:72,3:96,4:16},sh_counts
    assert ro_counts=={0:1,1:16,2:72,3:96,4:24},ro_counts
    assert len(F)==201 and len(R)==209
    pairs,critical,arcs=morse_check(F, list(range(16)))
    assert (pairs,critical,arcs)==(88,Counter({2:23,0:1}),496),(pairs,critical,arcs)
    rook_order=[7,9,5,6,14,10,12,8,1,2,13,15,4,11,0,3]
    rp,rc,ra=morse_check(R,rook_order)
    assert (rp,rc,ra)==(96,Counter({2:15,0:1}),528),(rp,rc,ra)
    assert [boundary_rank_mod2(F,k) for k in range(4)]==[1,15,57,16]
    assert [boundary_rank_mod2(R,k) for k in range(4)]==[1,15,57,24]
    print('FACES_SHRIKHANDE',len(F)-1,'FACES_ROOK',len(R)-1)
    print('MORSE_SHRIKHANDE',pairs,sorted(critical.items()),arcs)
    print('MOD2_RANKS_SHRIKHANDE',1,15,57,16)
    # Known coclique classification rechecked without using its published enumeration.
    H0={(0,0),(2,0),(0,2),(2,2)}
    H1={(0,0),(1,2),(2,0),(3,2)}
    H2={(0,0),(2,1),(0,2),(2,3)}
    H3={(0,0),(1,3),(2,2),(3,1)}
    cocliques={sum(1<<index[add(t,x)] for x in H) for t in Q for H in (H0,H1,H2,H3)}
    assert cocliques == {f for f in F if f.bit_count()==4}
    assert len(cocliques)==16
    print('COCLIQUE_COSETS',len(cocliques))
    Aset=make_affine_linear()
    assert IDENTITY in Aset
    # Aut graph size <=16*12, because a neighbor set is a 6-cycle. The
    # stabilizer of each vertex injects into Aut(C6), of order 12.
    neighbors=[v for v in range(16) if shr_adj[0]&(1<<v)]
    assert len(neighbors)==6
    assert all((shr_adj[v]&sum(1<<x for x in neighbors)).bit_count()==2 for v in neighbors)
    # The nine non-neighbors of zero have pairwise distinct intersections
    # with its six neighbors, so a vertex stabilizer acts faithfully on C6.
    nmask=sum(1<<x for x in neighbors)
    other=[v for v in range(1,16) if not (shr_adj[0] & (1<<v))]
    assert len(other)==9
    assert len({shr_adj[v]&nmask for v in other})==9
    allperms=set()
    table=[]
    for A in Aset:
        for tx in range(4):
            for ty in range(4):
                p=affine_perm(A,(tx,ty))
                assert p not in allperms
                allperms.add(p)
                assert all(is_edge(v,w,'shrikhande')==is_edge(p[v],p[w],'shrikhande')
                           for v in range(16) for w in range(v+1,16))
                trace1=lefschetz(F,p)
                trace2=cyclic_lefschetz(shr_adj,p)
                assert trace1==trace2
                table.append((*A,tx,ty,trace1))
    assert len(table)==192
    # Reconstruct signed boundary equivariance on all 192 automorphisms.
    checked_incidence = 0
    for perm in allperms:
        for face in F:
            if face.bit_count()<2:
                continue
            imface=mask_image(face,perm)
            orient=inversion_sign(face,perm)
            lhs={}
            for pos,v in enumerate(u for u in range(16) if imface & (1<<u)):
                lhs[imface & ~(1<<v)] = orient*(-1 if pos%2 else 1)
            rhs={}
            for pos,v in enumerate(u for u in range(16) if face & (1<<u)):
                sub=face & ~(1<<v)
                image_sub=mask_image(sub,perm)
                rhs[image_sub]=(-1 if pos%2 else 1)*inversion_sign(sub,perm)
                checked_incidence += 1
            assert lhs==rhs
    assert checked_incidence==192*496
    print('SIGNED_CHAIN_EQUIVARIANCE_IDENTITIES',checked_incidence)
    # Check the actual independent CSV against all newly computed characters.
    with (Path(__file__).with_name('character_table.csv')).open(newline='',encoding='utf-8') as inp:
        rows=list(csv.DictReader(inp))
    assert len(rows)==192
    parsed=[tuple(int(z[k]) for k in ('a','b','c','d','tx','ty','trace')) for z in rows]
    assert parsed==table
    # Rational Fourier multiplicities as Gaussian integers (no float roundoff).
    transchar={(tx,ty):t[-1] for t in table if t[:4]==IDENTITY for tx,ty in [(t[4],t[5])]}
    def complex_i(k): return [(1,0),(0,1),(-1,0),(0,-1)][k%4]
    mult={}
    for p in range(4):
        for q in range(4):
            real=imag=0
            for (a,b),char in transchar.items():
                re,im=complex_i(-p*a-q*b)
                real+=char*re;imag+=char*im
            assert imag==0 and real%16==0
            mult[p,q]=real//16
            assert mult[p,q]>=0
    expected=((2,1,1,1),(1,2,2,1),(1,2,1,2),(1,1,2,2))
    assert tuple(tuple(mult[p,q] for q in range(4)) for p in range(4))==expected
    assert sum(mult.values())==23
    assert mult[0,0]==2
    print('TRANSLATION_FOURIER_MATRIX',expected)
    print('TRANSLATION_FIXED_DIMENSION',mult[0,0])
    # Check the two-dimensional T-fixed module under the complementary D12.
    avg={A:sum(t[-1] for t in table if t[:4]==A)//16 for A in Aset}
    assert all(sum(t[-1] for t in table if t[:4]==A)%16==0 for A in Aset)
    r=(0,1,3,1);s=(0,1,1,0)
    assert rmat(rmat(s,r),s)==rmat(rmat(rmat(r,r),r),rmat(r,r))
    powers=[IDENTITY]
    for i in range(1,6):powers.append(rmat(powers[-1],r))
    assert rmat(powers[-1],r)==IDENTITY
    assert {rmat(s,p) for p in powers}|set(powers)==set(Aset)
    for i,p in enumerate(powers):
        assert avg[p]==1+(-1)**i
        assert avg[rmat(s,p)]==-1-(-1)**i
    assert sum(t[-1] for t in table)==0
    print('T_FIXED_DIHEDRAL_MODULE','rho(r)=+1,rho(s)=-1; rho(r)=-1,rho(s)=-1')
    print('FULL_AUTOMORPHISM_FIXED_DIMENSION',0)
    # Rook graph comparison with same translation action; no novelty claimed.
    rookchars={}
    for tx in range(4):
        for ty in range(4):
            perm=affine_perm(IDENTITY,(tx,ty))
            rookchars[(tx,ty)]=lefschetz(R,perm)
            assert rookchars[(tx,ty)]==cyclic_lefschetz(rook_adj,perm)
    assert sum(rookchars.values())==16
    print('ROOK_TRANSLATION_FIXED_DIMENSION',1)
    print('FULL_SHRIKHANDE_CHARACTER_VERIFIED_192_PASS')

if __name__ == '__main__': main()
