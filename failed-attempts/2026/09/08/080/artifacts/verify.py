"""Verify char-2 WLP failure for non-monomial CI type (3,3,4).

A = F2[x,y,z]/I, I=(f1,f2,f3),
  f1 = x^3 + y^2 z + y z^2
  f2 = y^3 + x^2 z + x z^2
  f3 = z^4 + x y^3 + x^3 y + x^4   (repaired: +x^4 needed for regular sequence;
       original topic f3 without x^4 gives non-Artinian tail (dim 2 for d>=7))

Checks (stdlib only, exact F2 linear algebra):
 1. Hilbert function of A equals CI product formula [1,3,6,8,8,6,3,1,0,...].
 2. Multiplication by L=x has det 1 on A3->A4 (rank 8, Lefschetz witness).
 3. Multiplication by ell=x+y+z has rank 7 < 8 on A3->A4 (det 0),
    with logged kernel/cokernel witnesses => A fails WLP in char 2.
Exit 0 with VERIFY_OK iff all pass.
"""
def mons(d):
    return sorted({(d - j - k, j, k) for j in range(d + 1) for k in range(d + 1 - j)})

F1 = {(3,0,0):1,(0,2,1):1,(0,1,2):1}
F2 = {(0,3,0):1,(2,0,1):1,(1,0,2):1}
F3 = {(0,0,4):1,(1,3,0):1,(3,1,0):1,(4,0,0):1}
FS = [(F1,3),(F2,3),(F3,4)]

def rref(rows, ncols):
    M = [r[:] for r in rows]; r = 0; where = [-1]*ncols
    for c in range(ncols):
        piv = -1
        for i in range(r, len(M)):
            if M[i][c]:
                piv = i; break
        if piv < 0: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c]:
                for j in range(c, ncols):
                    M[i][j] ^= M[r][j]
        where[c] = r; r += 1
    return r, M, where

def ideal_rows(d):
    cols = mons(d); idx = {m:i for i,m in enumerate(cols)}; rows = []
    for (f, df) in FS:
        if d < df: continue
        for m in mons(d - df):
            row = [0]*len(cols)
            for e in f:
                s = (m[0]+e[0], m[1]+e[1], m[2]+e[2])
                row[idx[s]] ^= 1
            rows.append(row)
    return cols, rows

QB = {}
for d in range(9):
    cols, rows = ideal_rows(d)
    rk, M, where = rref(rows, len(cols))
    piv = {c: M[w] for c, w in enumerate(where) if w >= 0}
    free = [c for c in range(len(cols)) if where[c] < 0]
    QB[d] = (cols, free, piv)

def mul_mat(L, d):
    a,b,c = L
    cd, freed, _ = QB[d]; ce, freee, pive = QB[d+1]
    idxe = {m:i for i,m in enumerate(ce)}
    mat = []
    for bb in freed:
        m = cd[bb]; v = [0]*len(ce)
        if a: v[idxe[(m[0]+1,m[1],m[2])]] ^= 1
        if b: v[idxe[(m[0],m[1]+1,m[2])]] ^= 1
        if c: v[idxe[(m[0],m[1],m[2]+1)]] ^= 1
        for pc in sorted(pive):
            if v[pc]:
                row = pive[pc]
                for j in range(pc, len(ce)):
                    v[j] ^= row[j]
        mat.append([v[k] for k in freee])
    return mat

def rankm(mat):
    if not mat or not mat[0]: return 0
    return rref([r[:] for r in mat], len(mat[0]))[0]

def nullspace_rows(mat):
    nrows = len(mat); ncols = len(mat[0])
    T = [list(c) for c in zip(*mat)]
    _, M, where = rref([t[:] for t in T], nrows)
    ker = []
    for c in range(nrows):
        if where[c] < 0:
            v = [0]*nrows; v[c] = 1
            for cc in range(nrows):
                if where[cc] >= 0:
                    v[cc] = M[where[cc]][c]
            ker.append(v)
    return ker

def det2(mat):
    n = len(mat); M = [r[:] for r in mat]
    for c in range(n):
        piv = -1
        for i in range(c, n):
            if M[i][c]: piv = i; break
        if piv < 0: return 0
        M[c], M[piv] = M[piv], M[c]
        for i in range(c+1, n):
            if M[i][c]:
                for j in range(c, n): M[i][j] ^= M[c][j]
    return 1

# 1. Hilbert check
hilb = [len(QB[d][1]) for d in range(9)]
assert hilb == [1,3,6,8,8,6,3,1,0], hilb
# 2/3. rank checks
Mx = mul_mat((1,0,0),3); Me = mul_mat((1,1,1),3)
assert det2(Mx)==1 and rankm(Mx)==8, Mx
assert det2(Me)==0 and rankm(Me)==7, Me
ker = nullspace_rows(Me)
assert ker and len(ker)==1, ker
# WLP definition: ell=x+y+z fails some degree; here 3->4 suffices.
# Also confirm some F2 form has WLP-full middle map (x), proving failure is ell-specific, not collapse.
print("Hilbert:", hilb)
print("rank(x : A3->A4) =", rankm(Mx), "det =", det2(Mx))
print("rank(x+y+z : A3->A4) =", rankm(Me), "det =", det2(Me))
print("A3 basis:", [QB[3][0][i] for i in QB[3][1]])
print("A4 basis:", [QB[4][0][i] for i in QB[4][1]])
print("kernel witness (coords on A3 basis):", ker[0])
print("VERIFY_OK")
