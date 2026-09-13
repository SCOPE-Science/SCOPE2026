"""Corrected bottom-up DP with factor C(h,f)*Beta(A+1,r+1), child (f,A+r+1).
Needed sets: need[K]={(h,0)}; children (f, A+r+1). S=W(h)+r grows by W... A+W(f)=W(h) so S_child = W(h)+r+1... wait W(f)+A+r+1 = W(h)+r+1 = S+1. Same sets as before; only values change."""
import numpy as np, math, itertools, pickle

K=50; WMAX=18
def enum_vecs(W):
    vecs=[]
    def rec(j,rem,cur):
        if j>9: vecs.append(tuple(cur)); return
        for e in range(rem//j+1):
            cur.append(e); rec(j+1,rem-j*e,cur); cur.pop()
    rec(1,W,[])
    return vecs
vecs=enum_vecs(WMAX)
Eidx={v:i for i,v in enumerate(vecs)}
E=len(vecs)
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
print("total needed:", sum(len(s) for s in need_at), flush=True)
lg=np.vectorize(math.lgamma)
def beta(a,b):
    return math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
val=[{} for _ in range(K+1)]
for (h,r) in need_at[0]:
    val[0][(h,r)]=1.0 if h==Eidx[(0,)*9] else 0.0
for k in range(1,K+1):
    d={}
    for (h,r) in need_at[k]:
        s=0.0
        for (f,c,A) in subs[h]:
            s+=c*beta(A+1,r+1)*val[k-1][(f,A+r+1)]
        d[(h,r)]=s
    val[k]=d
    if k in (1,2,3,5):
        e0=Eidx[(0,)*9]
        print("k=%d vol=%s want %.10e" % (k, repr(d.get((e0,0))), 1/math.factorial(k)), flush=True)
# full check int S^d
for dd in range(0,7):
    e = tuple(([dd]+[0]*8))
    got = val[K][(Eidx[e],0)]
    want = 1/(math.factorial(K-1)*(K+dd))
    print("d=%d got=%.10e want=%.10e ratio=%.8f" % (dd, got, want, got/want), flush=True)
pickle.dump({"vecs":vecs,"val50":val[50],"val49":val[49]}, open("output/artifacts/dp_corr2.pkl","wb"))
print("saved", flush=True)
