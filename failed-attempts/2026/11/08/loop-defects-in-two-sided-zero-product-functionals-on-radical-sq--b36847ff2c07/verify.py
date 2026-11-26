"""Finite exact tests of the two-sided-zero-product tensor defect of quiver algebras."""
from itertools import product

def rank(rows, prime):
    pivots = {}
    for row in rows:
        v = list(row)
        while True:
            k = next((i for i, z in enumerate(v) if z % prime), None)
            if k is None:
                break
            if k not in pivots:
                inv = pow(v[k] % prime, -1, prime)
                pivots[k] = [(z * inv) % prime for z in v]
                break
            factor = v[k] % prime
            w = pivots[k]
            v = [(a - factor * b) % prime for a, b in zip(v, w)]
    return len(pivots)

def test(vertices, arrows, p):
    n = vertices; m = len(arrows); N = n + m
    basis = [[[0] * N for _ in range(N)] for _ in range(N)]
    for i in range(n):
        basis[i][i][i] = 1
    for j, (src, tgt) in enumerate(arrows):
        a = n+j
        basis[src][a][a] = 1
        basis[a][tgt][a] = 1
    def mul(x, y):
        z = [0]*N
        for i, a in enumerate(x):
            if a:
                for j, b in enumerate(y):
                    if b:
                        for k, c in enumerate(basis[i][j]):
                            z[k] += a*b*c
        return tuple(v%p for v in z)
    B = [tuple(int(i==j) for i in range(N)) for j in range(N)]
    image_rows = []
    for x in B:
        for y in B:
            image_rows.append(mul(x,y)+mul(y,x))
    p_rank = rank(image_rows,p)
    zero_tensors=[]
    elems=list(product(range(p),repeat=N))
    for x in elems:
        for y in elems:
            if not any(mul(x,y)) and not any(mul(y,x)):
                zero_tensors.append([a*b%p for a in x for b in y])
    annihilator_span = rank(zero_tensors,p)
    loops=sum(src==tgt for src,tgt in arrows)
    expected_functional_dimension=n+2*m
    assert annihilator_span==N*N-expected_functional_dimension, (n,arrows,p,annihilator_span)
    assert p_rank==n+2*m-loops, (n,arrows,p,p_rank)
    assert (N*N-p_rank)-annihilator_span==loops
    # Directly test each loop obstruction form without using product-map equations.
    for j,(src,tgt) in enumerate(arrows):
        if src==tgt:
            for x in elems:
                for y in elems:
                    if not any(mul(x,y)) and not any(mul(y,x)):
                        assert x[src]*y[n+j]%p==0
    print('OK',{'p':p,'vertices':n,'arrows':arrows,'tensor_dim':N*N,
                'product_rank':p_rank,'zero_tensor_span':annihilator_span,'defect':loops})

for pp in (2,3):
    for verts, arrows in [
        (1,[]), (1,[(0,0)]), (1,[(0,0),(0,0)]),
        (2,[(0,1)]), (2,[(0,1),(1,0)]), (2,[(0,1),(0,1)]),
        (2,[(0,0),(0,1)]),(2,[(0,0),(0,1),(1,0)]),
        (2,[(0,0),(1,1),(0,1)]),
        (3,[(0,1),(1,2),(2,0)]),
    ]:
        test(verts,arrows,pp)
print('VERIFY_OK')
