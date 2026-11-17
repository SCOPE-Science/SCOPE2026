#!/usr/bin/env python3
"""Independent exhaustive facewise Lefschetz verification of multipartite forest modules."""
from itertools import permutations,product
from math import prod
from collections import defaultdict

def valid_masks(sizes):
    total=sum(sizes); cuts=[sum(sizes[:i]) for i in range(len(sizes)+1)]
    out=[]
    for mask in range(1<<total):
        cs=[(mask>>cuts[i] & ((1<<sizes[i])-1)).bit_count() for i in range(len(sizes))]
        nz=[c for c in cs if c]
        if len(nz)<=1 or len(nz)==2 and min(nz)==1:
            out.append(mask)
    return out

def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def char_face(sizes, all_faces, g):
    ch=-1 # reduced trace including empty face
    for mask in all_faces:
        if not mask: continue
        idx=[i for i in range(len(g)) if mask>>i&1]
        images=[g[i] for i in idx]
        if set(images)==set(idx):
            ch+=parity(images)*(-1 if len(idx)%2==0 else 1)
    return ch

def char_expected(sizes,perm_part,local_perms,g):
    k=len(sizes)
    fixed_parts=sum(perm_part[i]==i for i in range(k))
    # Chain character C1 minus C0 plus C_{-1}: signed oriented edges on K_k
    edge_trace=sum((1 if perm_part[i]==i and perm_part[j]==j else -1 if perm_part[i]==j and perm_part[j]==i else 0) for i in range(k) for j in range(i+1,k))
    h1=edge_trace-fixed_parts+1
    cuts=[sum(sizes[:i]) for i in range(k+1)]
    g2=[g[g[i]] for i in range(len(g))]
    h2=0
    for i in range(k):
        for j in range(i+1,k):
            if perm_part[i]==i and perm_part[j]==j:
                fi=sum(g[v]==v for v in range(cuts[i],cuts[i+1]));fj=sum(g[v]==v for v in range(cuts[j],cuts[j+1]));h2+=(fi-1)*(fj-1)
            elif perm_part[i]==j and perm_part[j]==i:
                h2+=sum(g2[v]==v for v in range(cuts[i],cuts[i+1]))-1
    return h2-h1,(h1,h2)

def all_auts(sizes):
    k=len(sizes);cut=[sum(sizes[:i]) for i in range(k+1)]
    partperms=[p for p in permutations(range(k)) if all(sizes[i]==sizes[p[i]] for i in range(k))]
    local=list(product(*(list(permutations(range(n))) for n in sizes)))
    for p in partperms:
        for loc in local:
            g=tuple(cut[p[i]]+loc[i][v] for i in range(k) for v in range(sizes[i]))
            yield p,loc,g

def run():
    tests=[(2,2),(2,3),(3,3),(2,2,2),(1,2,3),(1,1,2,2),(2,2,2,2),(3,3,3)]
    checks=0
    for sizes in tests:
        faces=valid_masks(sizes)
        auts=0
        for p,loc,g in all_auts(sizes):
            measured=char_face(sizes,faces,g)
            expected,pair=char_expected(sizes,p,loc,g)
            assert measured==expected,(sizes,p,loc,measured,expected,pair)
            auts+=1
        checks+=auts
        print(f'sizes={sizes}; valid_faces_including_empty={len(faces)}; automorphisms={auts}; all_signed_Lefschetz_matches=True')
    print(f'ALL_MULTIPARTITE_FOREST_CHARACTER_CHECKS_PASS; automorphisms={checks}')

if __name__=='__main__': run()

def mod2_ranks(sizes):
    """Separate simplicial boundary elimination over F2; includes all nonempty faces."""
    faces=valid_masks(sizes)
    bydim=defaultdict(list)
    for mask in faces:
        if mask: bydim[mask.bit_count()-1].append(mask)
    ranks={}
    for q in range(1,max(bydim)+1):
        lower={mask:i for i,mask in enumerate(bydim[q-1])}
        piv={};rank=0
        for s in bydim[q]:
            v=0; t=s
            while t:
                bit=t&-t;t-=bit;v^=1<<lower[s^bit]
            while v:
                row=v.bit_length()-1
                if row in piv: v^=piv[row]
                else: piv[row]=v;rank+=1;break
        ranks[q]=rank
    betas={q:len(bydim[q])-ranks.get(q,0)-ranks.get(q+1,0) for q in bydim}
    betas[0]-=1
    k=len(sizes)
    expected={1:(k-1)*(k-2)//2,2:sum((sizes[i]-1)*(sizes[j]-1) for i in range(k) for j in range(i+1,k))}
    for q in set(expected)|set(betas):assert betas.get(q,0)==expected.get(q,0),(sizes,betas,expected)
    return {q:v for q,v in sorted(betas.items()) if v}

if __name__=='__main__':
    for ss in [(2,2),(2,3),(3,3),(2,2,2),(1,1,2,2),(2,2,2,2),(3,3,3)]:
        print(f'F2_BOUNDARY_CHECK sizes={ss}; reduced_bettis={mod2_ranks(ss)}')
    print('ALL_MULTIPARTITE_FOREST_BETTI_CHECKS_PASS')
