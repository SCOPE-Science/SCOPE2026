"""Direct finite-field checks of ordered commuting tuples in positive Witt nilradicals."""
from itertools import product


def elements(p):
    return list(product(range(p), repeat=p - 2))


def commute(a, b, p):
    # Coefficients are indexed by monomials x^(2+i) d/dx.
    for d in range(2, p):
        val = 0
        for i in range(p - 2):
            ai = a[i]
            if not ai:
                continue
            for j in range(p - 2):
                if i + j + 3 == d:
                    val += (j - i) * ai * b[j]
        if val % p:
            return False
    return True


def predicted(p, q, r):
    m = (p - 1) // 2
    return q ** (m * r) + (q ** r - 1) * sum(q ** (p - r + s * (r - 2)) for s in range(2, m + 1))


def direct_counts(p, max_r):
    el = elements(p)
    n = len(el)
    neighbor = [list() for _ in range(n)]
    for i, a in enumerate(el):
        for j, b in enumerate(el):
            if commute(a, b, p):
                neighbor[i].append(j)
    assert all(i in neighbor[i] for i in range(n))
    total_two = sum(len(x) for x in neighbor)
    print(f'p={p} q={p}: r=2 direct={total_two} formula={predicted(p,p,2)}')
    assert total_two == predicted(p, p, 2)
    if max_r >= 3:
        # For a fixed first entry, count all ordered adjacent pairs in its centralizer.
        # This directly tests every triple of original elements, not a proof identity.
        adj = [set(x) for x in neighbor]
        total_three = sum(sum(len(adj[j].intersection(adj[i])) for j in neighbor[i]) for i in range(n))
        print(f'p={p} q={p}: r=3 direct={total_three} formula={predicted(p,p,3)}')
        assert total_three == predicted(p,p,3)
    return neighbor


if __name__ == '__main__':
    n5 = direct_counts(5,3)
    # For r=4, count all ordered commuting triples in each first-element centralizer.
    # Direct adjacency triple enumeration with local neighbor intersections.
    A = [set(x) for x in n5]
    four = 0
    for i, neigh in enumerate(n5):
        mask = A[i]
        for j in neigh:
            common = mask.intersection(A[j])
            for k in common:
                four += len(common.intersection(A[k]))
    print(f'p=5 q=5: r=4 direct={four} formula={predicted(5,5,4)}')
    assert four == predicted(5,5,4)
    # A second prime: full independent rank-based centralizer counting.
    # For each f, count the solutions to the original linear equations [f,g]=0.
    p = 7
    dim = p-2
    basis = [tuple(int(j==i) for j in range(dim)) for i in range(dim)]
    def rank_mod(rows,p):
        v=[list(x) for x in rows]
        pivot=0
        for col in range(len(v[0])):
            i=next((i for i in range(pivot,len(v)) if v[i][col]%p),None)
            if i is None: continue
            v[pivot],v[i]=v[i],v[pivot]
            inv=pow(v[pivot][col],-1,p)
            v[pivot]=[(z*inv)%p for z in v[pivot]]
            for j in range(pivot+1,len(v)):
                a=v[j][col]%p
                if a:
                    v[j]=[(x-a*y)%p for x,y in zip(v[j],v[pivot])]
            pivot+=1
            if pivot==len(v):break
        return pivot
    total=0
    ranks={}
    for f in product(range(p),repeat=dim):
        matrix=[]
        images=[]
        for b in basis:
            coeff=[0]*(p-2)
            for i,fi in enumerate(f):
                for j,bj in enumerate(b):
                    t=i+j+3
                    if t<p:coeff[t-2]+=fi*bj*(j-i)
            images.append([x%p for x in coeff])
        matrix=list(zip(*images))
        r=rank_mod(matrix,p)
        ranks[r]=ranks.get(r,0)+1
        total += p**(dim-r)
    print(f'p=7 q=7: r=2 direct-rank={total} formula={predicted(p,p,2)} ranks={ranks}')
    assert total==predicted(p,p,2)
    print('WITT_NILRADICAL_COMMUTING_TUPLES_DIRECT_CHECK_PASS')


def gaussian(n,d,q):
    if d<0 or d>n:return 0
    # Calculate the Gaussian coefficient as an exact integer product.
    import math
    num=math.prod(q**(n-i)-1 for i in range(d))
    den=math.prod(q**(d-i)-1 for i in range(d))
    return num//den


def abelian_subspace_formula(p,q,d):
    m=(p-1)//2
    if d==0:return 1
    if d>m:return 0
    return gaussian(m,d,q) + sum(gaussian(s-1,d-1,q)*q**(p-s-d) for s in range(max(2,d),m+1))


def verify_p5_subspaces():
    p=5; es=elements(p)
    # Every plane is the span of independent vectors; normalize a basis in F_5^3.
    def canon_two(a,b):
        rows=[list(a),list(b)]
        r=0
        for col in range(3):
            i=next((i for i in range(r,2) if rows[i][col] % p),None)
            if i is None:continue
            rows[i],rows[r]=rows[r],rows[i]
            inv=pow(rows[r][col],-1,p)
            rows[r]=[(z*inv)%p for z in rows[r]]
            for j in range(2):
                if j!=r:
                    c=rows[j][col];rows[j]=[(x-c*y)%p for x,y in zip(rows[j],rows[r])]
            r+=1
            if r==2:break
        return tuple(map(tuple,rows)) if r==2 else None
    planes=set(); abelian=set()
    for a in es[1:]:
        for b in es[1:]:
            v=canon_two(a,b)
            if v is not None:
                planes.add(v)
                if commute(v[0],v[1],p): abelian.add(v)
    counts={0:1,1:(p**3-1)//(p-1),2:len(abelian),3:0}
    print(f'p=5 q=5: all planes={len(planes)}; abelian subspace dimensions={counts}')
    assert len(planes)==gaussian(3,2,5)
    assert all(counts[d]==abelian_subspace_formula(5,5,d) for d in range(4))
    print('WITT_ABELIAN_SUBSPACE_SPECTRUM_DIRECT_CHECK_PASS')

if __name__=='__main__':
    verify_p5_subspaces()

if __name__=='__main__':
    for p in (5,7,11):
        m=(p-1)//2
        for r in (2,3,4):
            total=sum(abelian_subspace_formula(p,p,d)*__import__('math').prod(p**r-p**i for i in range(d)) for d in range(m+1))
            assert total==predicted(p,p,r)
    print('GAUSSIAN_SPANNING_IDENTITY_CHECK_PASS')
