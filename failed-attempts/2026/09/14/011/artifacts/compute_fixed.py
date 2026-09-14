import sympy as sp
from itertools import permutations, product

def perm_op(p):
    M = sp.zeros(27,27)
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                src = (i0,i1,i2)
                dst = (src[p[0]], src[p[1]], src[p[2]])
                s = i0*9+i1*3+i2
                d = dst[0]*9+dst[1]*3+dst[2]
                M[d,s] = 1
    return M

I = sp.eye(27)
P12 = perm_op((1,0,2))
P13 = perm_op((2,1,0))
C = (I+P12)*(I-P13)
print("rank C =", C.rank(), flush=True)
col_basis = C.columnspace()
print("dim =", len(col_basis), flush=True)
B = sp.Matrix.hstack(*col_basis)
BTB = B.T*B
BTBinv = BTB.inv()

def kron3(A):
    K = sp.zeros(27,27)
    for i0 in range(3):
        for i1 in range(3):
            for i2 in range(3):
                for j0 in range(3):
                    for j1 in range(3):
                        for j2 in range(3):
                            r = i0*9+i1*3+i2
                            c = j0*9+j1*3+j2
                            K[r,c] = A[i0,j0]*A[i1,j1]*A[i2,j2]
    return K

def hook_mat(A):
    Am = A if isinstance(A, sp.Matrix) else sp.Matrix(A)
    K = kron3(Am)
    return BTBinv*(B.T*K*B)

def fixed_dim(mats):
    rows = [hook_mat(M)-sp.eye(8) for M in mats]
    Mall = sp.Matrix.vstack(*rows)
    return 8 - Mall.rank()

gens = []
for i in range(3):
    for j in range(3):
        if i==j: continue
        for s in (1,-1):
            E = sp.eye(3); E[i,j]=s
            gens.append(E)
print("(a) SL(3,Z) invariants dim =", fixed_dim(gens), flush=True)

verts = [[0,0,0],[1,0,0],[0,1,0],[0,0,1]]
mats_T3 = []
for perm in permutations(range(4)):
    b = verts[perm[0]]
    cols = []
    for k in (perm[1],perm[2],perm[3]):
        cols.append([verts[k][r]-b[r] for r in range(3)])
    A = sp.Matrix(cols).T
    if A.det()==1:
        mats_T3.append(A)
print("num T3+ :", len(mats_T3), flush=True)
print("(d) T3 stabilizer fixed dim =", fixed_dim(mats_T3), flush=True)

cands_seg = []
for entries in product(range(-1,2), repeat=9):
    A = sp.Matrix(3,3,entries)
    if A.det()!=1: continue
    c0 = (A[0,0],A[1,0],A[2,0])
    if c0==(1,0,0) or c0==(-1,0,0):
        cands_seg.append(A)
print("num seg-bounded:", len(cands_seg), flush=True)
print("(b) seg-dir bounded fixed dim =", fixed_dim(cands_seg), flush=True)

cands_plane = []
for entries in product(range(-1,2), repeat=9):
    A = sp.Matrix(3,3,entries)
    if A.det()!=1: continue
    if (A[2,0],A[2,1])==(0,0) and A[2,2] in (1,-1):
        cands_plane.append(A)
print("num plane-bounded:", len(cands_plane), flush=True)
print("(c) plane bounded fixed dim =", fixed_dim(cands_plane), flush=True)
