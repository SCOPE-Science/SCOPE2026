"""Phase B: save I,J matrices from double DP for high-precision eigensolve."""
import numpy as np, math, itertools

K = 50; DMAX = 9; WMAX = 18
RSET = [0] + list(range(2, 21))

def enum_vecs(W):
    vecs = []
    def rec(j, rem, cur):
        if j > 9:
            vecs.append(tuple(cur)); return
        for e in range(rem // j + 1):
            cur.append(e); rec(j+1, rem - j*e, cur); cur.pop()
    rec(1, W, [])
    return vecs

vecs18 = enum_vecs(WMAX); vecs9 = enum_vecs(DMAX)
Eidx = {v: i for i, v in enumerate(vecs18)}
E = len(vecs18); B = len(vecs9)
W = np.array([sum((j+1)*v[j] for j in range(9)) for v in vecs18])
from math import comb
rows, cols, Cs, AAs, WFs = [], [], [], [], []
for ei, e in enumerate(vecs18):
    for f in itertools.product(*[range(x+1) for x in e]):
        c = 1
        for j in range(9):
            c *= comb(e[j], f[j])
        A = sum(e[j]-f[j] for j in range(9))
        rows.append(ei); cols.append(Eidx[f]); Cs.append(c); AAs.append(A); WFs.append(W[Eidx[f]])
rows=np.array(rows); cols=np.array(cols); Cs=np.array(Cs); AAs=np.array(AAs); WFs=np.array(WFs)
lg = np.vectorize(math.lgamma)
v = {s: np.zeros(E) for s in RSET}
for s in RSET:
    v[s][Eidx[(0,)*9]] = 1.0
snap49 = None
for k in range(1, K+1):
    vn = {}
    for s in RSET:
        A1 = AAs + 1; B1 = (k-1) + WFs + s + 1
        co = Cs*np.exp(lg(A1)+lg(B1)-lg(A1+B1))
        out = np.zeros(E)
        np.add.at(out, rows, co*v[s][cols])
        vn[s] = out
    v = vn
    if k == K-1:
        snap49 = {s: x.copy() for s, x in v.items()}
v50 = v; v49 = snap49
I = np.zeros((B,B)); J1 = np.zeros((B,B))
sublist = []
for vv in vecs9:
    L = []
    for f in itertools.product(*[range(x+1) for x in vv]):
        c = 1
        for j in range(9):
            c *= comb(vv[j], f[j])
        a = sum((j+1)*(vv[j]-f[j]) for j in range(9))
        L.append((Eidx[f], c, a, f))
    sublist.append(L)
for i in range(B):
    ei = vecs9[i]
    for j in range(i, B):
        ej = vecs9[j]
        g = tuple(ei[t]+ej[t] for t in range(9))
        val = v50[0][Eidx[g]]
        I[i,j] = val; I[j,i] = val
        ssum = 0.0
        for (ff, c1, a, f) in sublist[i]:
            fv = vecs18[ff]
            for (gg, c2, b, g2) in sublist[j]:
                gv = vecs18[gg]
                h = tuple(fv[t]+gv[t] for t in range(9))
                ssum += c1*c2*v49[a+b+2][Eidx[h]]/((a+1)*(b+1))
        J1[i,j] = ssum; J1[j,i] = ssum
J = K*J1
np.save("output/artifacts/I_mat.npy", I)
np.save("output/artifacts/J_mat.npy", J)
print("saved. I[0,0]=%.6e J[0,0]=%.6e" % (I[0,0], J[0,0]))
print("diag I range:", np.diag(I).min(), np.diag(I).max())
print("diag J range:", np.diag(J).min(), np.diag(J).max())
