"""float128 (80-bit) vectorized DP rebuild + mpmath high-precision generalized EVP."""
import numpy as np, math, itertools, pickle
LD = np.longdouble
K=50; WMAX=18
def enum_vecs(W):
    vecs=[]
    def rec(j,rem,cur):
        if j>9: vecs.append(tuple(cur)); return
        for e in range(rem//j+1):
            cur.append(e); rec(j+1,rem-j*e,cur); cur.pop()
    rec(1,W,[])
    return vecs
vecs=enum_vecs(WMAX); Eidx={v:i for i,v in enumerate(vecs)}; E=len(vecs)
W=np.array([sum((j+1)*v[j] for j in range(9)) for v in vecs])
from math import comb
subs=[]
for e in vecs:
    L=[]
    for f in itertools.product(*[range(x+1) for x in e]):
        c=1
        for j in range(9): c*=comb(e[j],f[j])
        A=sum((jj+1)*(e[jj]-f[jj]) for jj in range(9))
        L.append((Eidx[f],c,A))
    subs.append(L)
need_at=[set() for _ in range(K+1)]
for h in range(E):
    need_at[K].add((h,0))
    for s in range(2,21):
        need_at[K-1].add((h,s))
for k in range(K,0,-1):
    for (h,r) in need_at[k]:
        for (f,c,A) in subs[h]:
            need_at[k-1].add((f,A+r+1))
print("total:", sum(len(s) for s in need_at), flush=True)
# vectorize: index map (h,r)->pos per level; transitions as arrays
import array as arr
level_idx=[{} for _ in range(K+1)]
for k in range(K+1):
    for i,(h,r) in enumerate(need_at[k]):
        level_idx[k][(h,r)]=i
# precompute beta table in longdouble
btab={}
for A in range(0,19):
    for r in range(0,120):
        btab[(A,r)]=LD(math.exp(math.lgamma(A+1)+math.lgamma(r+1)-math.lgamma(A+r+2)))
val0=np.zeros(len(need_at[0]), dtype=LD)
for (h,r),i in level_idx[0].items():
    val0[i]=LD(1.0) if h==Eidx[(0,)*9] else LD(0.0)
vals=[None]*(K+1); vals[0]=val0
trans=[None]*(K+1)
for k in range(1,K+1):
    nk=len(need_at[k]); keys=list(need_at[k])
    rows=[]; cols=[]; coef=[]
    for ri,(h,r) in enumerate(keys):
        for (f,c,A) in subs[h]:
            ci=level_idx[k-1][(f,A+r+1)]
            rows.append(ri); cols.append(ci); coef.append(LD(c)*btab[(A,r)])
    rows=np.array(rows); cols=np.array(cols); coef=np.array(coef, dtype=LD)
    out=np.zeros(nk, dtype=LD)
    # accumulate: out[rows] += coef*vals[k-1][cols]
    np.add.at(out, rows, coef*vals[k-1][cols])
    vals[k]=out
    if k%10==0: print("level",k,"done", flush=True)
pickle.dump({"vecs":vecs,
             "v50":dict(zip(need_at[K], [float(x) for x in vals[K]])),
             "v49":dict(zip(need_at[K-1], [float(x) for x in vals[K-1]])),
             "v50ld":dict(zip(need_at[K], vals[K])),
             "v49ld":dict(zip(need_at[K-1], vals[K-1]))}, open("output/artifacts/dp_ld.pkl","wb"))
print("saved; vol=", vals[K][level_idx[K][(Eidx[(0,)*9],0)]], flush=True)
