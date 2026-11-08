"""Independent finite-field calculations for three-step graph Lie brackets.

Usage: python checker.py. Standard library only. All tests finite and exploratory;
the unrestricted field statement follows from a separate proof.
"""
import itertools
import random


def echelon_rank(mat, p):
    if not mat: return 0
    rows = [[int(v) % p for v in row] for row in mat]
    n, m, r = len(rows), len(rows[0]), 0
    for col in range(m):
        pivot = next((i for i in range(r, n) if rows[i][col]), None)
        if pivot is None: continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][col], -1, p)
        rows[r] = [(v * inv) % p for v in rows[r]]
        for i in range(n):
            if i != r and rows[i][col]:
                f = rows[i][col]
                rows[i] = [(x - f*y) % p for x,y in zip(rows[i], rows[r])]
        r += 1
        if r == n: break
    return r


def labels(a,b):
    edges = [(i,j) for i in range(a) for j in range(b)]
    paths = ([('Y',j,i,h) for j in range(b) for i in range(a) for h in range(i+1,a)]
        + [('X',i,j,k) for i in range(a) for j in range(b) for k in range(j+1,b)])
    return edges, paths


def kirillov_matrix(a,b, weights, p):
    """Construct from [xi,yj]=edge_ij, two-path brackets, and alternation.

    weights contains edge-evaluation values and path-evaluation values,
    one for each edge and path of the underlying bipartite graph.
    """
    edges, paths = labels(a,b)
    m, n = a+b, len(edges)
    B = [[0]*(m+n) for _ in range(m+n)]
    edgeidx = {edge:k for k,edge in enumerate(edges)}
    for (i,j) in edges:
        value = weights[('E',i,j)] % p
        B[i][a+j] = value
        B[a+j][i] = -value % p
    for label in paths:
        value = weights[label] % p
        if label[0]=='Y':
            _,j,i,h = label
            hits = [(i,(h,j)),(h,(i,j))]
        else:
            _,i,j,k = label
            hits = [(a+j,(i,k)),(a+k,(i,j))]
        for row,edge in hits:
            col = m+edgeidx[edge]
            B[row][col] = value
            B[col][row] = -value % p
    return B


def d_block(a,b,weights,p):
    mat = kirillov_matrix(a,b,weights,p)
    n=a+b
    return [r[n:] for r in mat[:n]]


def zeros(a,b):
    edges,paths=labels(a,b)
    return {**{('E',i,j):0 for (i,j) in edges},**{w:0 for w in paths}}


def witness(a,b):
    """Explicit unimodular mixed-block minor; assumes a>=2,b>=3."""
    assert a>=2 and b>=3
    w=zeros(a,b)
    w[('Y',2,0,1)] = 1
    w[('X',0,1,2)] = 1
    w[('X',1,0,1)] = 1
    selected = [(0,1),(0,2),(1,0),(1,1),(1,2)]
    used = set(selected)
    for newj in range(3,b):
        old = next((e for e in itertools.product(range(2),range(newj)) if e not in used))
        i,j = old
        w[('X',i,j,newj)] = 1
        used.add(old)
        selected.append(old)
    for newi in range(2,a):
        old = next((e for e in itertools.product(range(newi),range(b)) if e not in used))
        i,j = old
        w[('Y',j,i,newi)] = 1
        used.add(old)
        selected.append(old)
    assert len(selected)==a+b and len(set(selected))==len(selected)
    return w,selected


def determinant_bareiss(M):
    A = [list(map(int, r)) for r in M]
    n = len(A)
    if n == 1: return A[0][0]
    sign = 1
    last = 1
    for k in range(n-1):
        if A[k][k] == 0:
            pivot = next((j for j in range(k+1,n) if A[j][k]), None)
            if pivot is None:return 0
            A[k], A[pivot] = A[pivot],A[k]
            sign = -sign
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = A[i][j]*A[k][k] - A[i][k]*A[k][j]
                assert numerator % last == 0
                A[i][j] = numerator//last
            A[i][k] = 0
        last = A[k][k]
    return sign*A[n-1][n-1]


def full_test(a,b,p):
    if a==b==2:
        w=zeros(a,b)
        w[('Y',0,0,1)] = 1
        w[('X',0,0,1)] = 1
        assert echelon_rank(d_block(a,b,w,p),p)==3
        assert echelon_rank(kirillov_matrix(a,b,w,p),p)==6
        return 6
    if b==2: a,b=b,a
    w,selected=witness(a,b)
    D=d_block(a,b,w,p)
    eidx={e:i for i,e in enumerate(labels(a,b)[0])}
    minor=[[row[eidx[e]] for e in selected] for row in D]
    assert abs(determinant_bareiss(minor)) == 1
    assert echelon_rank(minor,p)==a+b
    assert echelon_rank(kirillov_matrix(a,b,w,p),p)==2*(a+b)
    return 2*(a+b)


def census(a,b,p):
    edges,paths=labels(a,b)
    w=zeros(a,b); keys=[('E',*e) for e in edges]+paths
    maxrank=0; total=0
    for vals in itertools.product(range(p),repeat=len(keys)):
        for key,v in zip(keys,vals): w[key]=v
        r=echelon_rank(kirillov_matrix(a,b,w,p),p)
        assert r%2==0
        if r>maxrank:maxrank=r
        total+=1
    return total,maxrank


def run():
    tests=0
    for p in (2,3,5,7):
        for a,b in ((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4),(4,5),(5,5)):
            got=full_test(a,b,p)
            expect=6 if a==b==2 else 2*(a+b)
            assert got==expect
            tests+=1
    census_result=[]
    for a,b,p in ((2,2,2),(2,2,3),(2,3,2)):
        total,maximum=census(a,b,p)
        expected=6 if (a,b)==(2,2) else 2*(a+b)
        assert maximum==expected
        census_result.append((a,b,p,total,maximum))
    print('VERIFY_OK full_witness_tests=',tests,'exhaustive_cases=',census_result)

if __name__=='__main__': run()
