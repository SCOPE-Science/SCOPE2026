"""Check the power-sum DP 'weight' fix: compare exact int p1^d over Dx_k(1) vs DP values."""
import numpy as np, math, itertools

def enum_vecs(W, J=9):
    vecs = []
    def rec(j, rem, cur):
        if j > J:
            vecs.append(tuple(cur)); return
        for e in range(rem // j + 1):
            cur.append(e); rec(j+1, rem - j*e, cur); cur.pop()
    rec(1, W, [])
    return vecs

def dp_moments(k, wmax=18, rset=(0,)):
    vecsW = enum_vecs(wmax)
    Eidx = {v:i for i,v in enumerate(vecsW)}
    E=len(vecsW)
    W = np.array([sum((j+1)*v[j] for j in range(9)) for v in vecsW])
    from math import comb
    rows,cols,Cs,AAs,WFs=[],[],[],[],[]
    for ei,e in enumerate(vecsW):
        for f in itertools.product(*[range(x+1) for x in e]):
            c=1
            for j in range(9): c*=comb(e[j],f[j])
            A=sum(e[j]-f[j] for j in range(9))
            rows.append(ei);cols.append(Eidx[f]);Cs.append(c);AAs.append(A);WFs.append(W[Eidx[f]])
    rows=np.array(rows);cols=np.array(cols);Cs=np.array(Cs);AAs=np.array(AAs);WFs=np.array(WFs)
    lg=np.vectorize(math.lgamma)
    v={s:np.zeros(E) for s in rset}
    for s in rset: v[s][Eidx[(0,)*9]]=1.0
    for kk in range(1,k+1):
        vn={}
        for s in rset:
            A1=AAs+1;B1=(kk-1)+WFs+s+1
            co=Cs*np.exp(lg(A1)+lg(B1)-lg(A1+B1))
            out=np.zeros(E); np.add.at(out,rows,co*v[s][cols]); vn[s]=out
        v=vn
    return vecsW, Eidx, v

def exact_int_p1d(k, d):
    # Laplace: int_{Dx_k} (t_1+...+t_k)^d = d!/(k+d)!
    return math.factorial(d)/math.factorial(k+d)

for k in [2,3,5]:
    vecsW, Eidx, v = dp_moments(k, wmax=10)
    print("k=",k)
    for d in range(0,7):
        e = tuple(([d]+[0]*8))
        got = v[0][Eidx[e]]; want = exact_int_p1d(k,d)
        print("  d=%d got=%.10e want=%.10e ratio=%.6f" % (d, got, want, got/want))
