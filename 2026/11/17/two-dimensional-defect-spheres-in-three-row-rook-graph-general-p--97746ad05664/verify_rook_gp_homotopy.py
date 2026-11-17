"""Finite reproducibility checks for three-row rook general-position complexes.

All checks use standard Python; no scientific assertion is inferred from extrapolation.
"""
from collections import defaultdict


def general_position_face(mask, n):
    points = [divmod(i, n) for i in range(3*n) if mask & (1 << i)]
    for a in range(len(points)):
        x, y = points[a]
        for b in range(a+1, len(points)):
            u, v = points[b]
            if x == u or y == v:
                continue
            for c in range(len(points)):
                if c == a or c == b:
                    continue
                w, z = points[c]
                if (w == x and z == v) or (w == u and z == y):
                    return False
    return True


def star_forest_face(mask, n):
    row_neighbors = [set() for _ in range(3)]
    col_neighbors = [set() for _ in range(n)]
    for i in range(3*n):
        if mask & (1 << i):
            r,c = divmod(i,n)
            row_neighbors[r].add(c)
            col_neighbors[c].add(r)
    for r in range(3):
        if len(row_neighbors[r]) >= 2:
            for c in row_neighbors[r]:
                if len(col_neighbors[c]) >= 2:
                    return False
    return True


def predicted_cover_face(mask, n):
    col_rows = []
    for c in range(n):
        rows = {r for r in range(3) if mask & (1 << (r*n+c))}
        col_rows.append(rows)
    thick = [j for j,R in enumerate(col_rows) if len(R) >= 2]
    if not thick: return True
    if len(thick) != 1: return False
    j=thick[0]
    R=col_rows[j]
    if len(R)==3: return all(not col_rows[c] for c in range(n) if c!=j)
    return all(col_rows[c] <= (set(range(3))-R) for c in range(n) if c!=j)


def faces(n):
    f=defaultdict(list)
    for mask in range(1 << (3*n)):
        gp=general_position_face(mask,n)
        sf=star_forest_face(mask,n)
        cv=predicted_cover_face(mask,n)
        assert gp == sf == cv, (n,mask,gp,sf,cv)
        if gp: f[mask.bit_count()].append(mask)
    return f


def binary_rank(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x^=pivots[p]
    return len(pivots)


def reduced_betti(f,n):
    ranks={}
    for k in sorted(f):
        if k==0: continue
        previous={x:i for i,x in enumerate(f[k-1])}
        vectors=[]
        for mask in f[k]:
            boundary=0
            for v in range(3*n):
                if mask & (1<<v):boundary ^= 1<<previous[mask^(1<<v)]
            vectors.append(boundary)
        ranks[k]=binary_rank(vectors)
    return {k-1:len(f[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in f if len(f[k])-ranks.get(k,0)-ranks.get(k+1,0) != 0}


def sign_permutation(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1


def reduced_lefschetz(f,n,rows,cols):
    result=-1 # subtract trace on the unreduced 0-dimensional constants
    for k,masks in f.items():
        if k==0: continue
        for mask in masks:
            indices=[v for v in range(3*n) if mask & (1<<v)]
            images=[rows[v//n]*n+cols[v%n] for v in indices]
            if set(indices) != set(images): continue
            positions={v:i for i,v in enumerate(indices)}
            perm=[positions[v] for v in images]
            result+=((-1)**(k-1))*sign_permutation(perm)
    return result


def theoretical_lefschetz(n,rows,cols):
    tr_aug=sum(rows[i]==i for i in range(3))-1
    sign_cols=sign_permutation(cols)
    seen=set(); top=1
    for j in range(n):
        if j in seen:continue
        c=[];q=j
        while q not in seen:
            seen.add(q);c.append(q);q=cols[q]
        top *= tr_aug if len(c)%2 else 2
    top*=sign_cols
    low=sign_permutation(rows)*sum(cols[j]==j for j in range(n))
    return low + ((-1)**(n-1))*top


def run():
    total_faces=0
    for n in [2,3,4,5]:
        f=faces(n)
        total_faces+=sum(len(v) for v in f.values())-1
        beta=reduced_betti(f,n)
        expected=({1:3,2:1} if n==2 else ({2:n+2**n} if n==3 else {2:n,n-1:2**n}))
        assert beta==expected,(n,beta,expected)
        print('n=',n,'face_vector=',tuple(len(f[k]) for k in sorted(f)), 'reduced_F2_betti=',beta)
        if n>=3:
            sample=[([0,1,2],list(range(n))),([1,0,2],list(range(n))),([1,2,0],list(range(n))),([0,1,2],[1,0]+list(range(2,n))),([0,1,2],list(range(1,n))+[0])]
            for row,col in sample:
                assert reduced_lefschetz(f,n,row,col)==theoretical_lefschetz(n,row,col),(n,row,col)
            print('n=',n,'signed_Lefschetz_checks=',len(sample))
    print('PASS all direct-geodesic/star-forest/cover comparisons and reduced-boundary-rank checks;',total_faces,'nonempty faces; 15 symmetry characters.')

if __name__=='__main__':run()
