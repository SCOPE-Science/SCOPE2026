"""Independent finite checks for general-position complexes of three-row rook graphs.
Standard library only; execute python verify.py.
"""
from itertools import combinations,product

def iter_subsets(mask):
    sub=mask
    while True:
        yield sub
        if sub==0:return
        sub=(sub-1)&mask

def constructed_faces(n):
    V=3*n
    facets=[]
    for rows in product(range(3),repeat=n):
        facets.append(sum(1<<(r*n+j) for j,r in enumerate(rows)))
    bases=[]
    for j in range(n):
        for r,s in combinations(range(3),2):
            t=3-r-s
            b=(1<<(r*n+j))|(1<<(s*n+j))
            full=b|sum(1<<(t*n+k) for k in range(n) if k!=j)
            facets.append(full); bases.append((j,(r,s),b,full))
        facets.append(sum(1<<(r*n+j) for r in range(3)))
    out=set()
    for f in facets:out.update(iter_subsets(f))
    # The common intersection of two separate thickening simplices
    # is a face of the one-cell-per-column join.
    for i,(_,_,_,fi) in enumerate(bases):
        for _,_,_,fj in bases[:i]:
            w=fi&fj
            assert all(sum(bool(w&(1<<(r*n+j))) for r in range(3))<=1 for j in range(n)),(n,fi,fj)
    return out

def shortest_path_faces(n):
    N=3*n
    d=[[0 if a==b else (1 if a//n==b//n or a%n==b%n else 2) for b in range(N)] for a in range(N)]
    violating=[]
    for i,j,k in combinations(range(N),3):
        if d[i][j]+d[j][k]==d[i][k] or d[i][k]+d[k][j]==d[i][j] or d[j][i]+d[i][k]==d[j][k]:
            violating.append((1<<i)|(1<<j)|(1<<k))
    # direct incremental enumeration, independent of star-forest model
    bad_by_max=[[] for _ in range(N)]
    for x in violating:bad_by_max[x.bit_length()-1].append(x)
    valid=bytearray(1<<N)
    valid[0]=1
    out={0}
    for s in range(1,1<<N):
        top=s.bit_length()-1
        parent=s^(1<<top)
        if valid[parent] and not any((s&t)==t for t in bad_by_max[top]):
            valid[s]=1;out.add(s)
    return out,len(violating)

def rank_mod2(columns):
    piv={}
    for c in columns:
        while c:
            p=c.bit_length()-1
            if p in piv:c^=piv[p]
            else:
                piv[p]=c
                break
    return len(piv)

def betti_reduced(faces):
    dims={}
    for f in faces:
        if f:dims.setdefault(f.bit_count()-1,[]).append(f)
    # boundary into degree one lower
    ranks={}
    for k in sorted(dims):
        if k==0:continue
        target={f:i for i,f in enumerate(dims[k-1])}
        columns=[]
        for f in dims[k]:
            col=0
            s=f
            while s:
                bit=s&-s;s-=bit
                col^=1<<target[f^bit]
            columns.append(col)
        ranks[k]=rank_mod2(columns)
    b={k:len(vals)-ranks.get(k,0)-ranks.get(k+1,0) for k,vals in dims.items()}
    b[0]-=1
    return {k:v for k,v in b.items() if v},[len(dims.get(k,[])) for k in range(max(dims)+1)]

if __name__=='__main__':
    for n in range(3,7):
        faces=constructed_faces(n)
        direct,viol=shortest_path_faces(n)
        assert faces==direct,(n,sorted(faces^direct)[:5])
        betti,vec=betti_reduced(faces)
        predicted={n-1:2**n,2:n}
        if n==3:predicted={2:2**n+n}
        assert betti==predicted,(n,betti,predicted)
        print(f'n={n}: forbidden_geodesic_triples={viol}, faces={len(faces)}, f_vector={vec}, reduced_mod2_Betti={betti}, PASS')
    print('VERIFY_OK')
