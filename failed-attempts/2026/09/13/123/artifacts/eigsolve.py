"""Build I,J (float, from corrected DP) + stable generalized eigensolve in long double."""
import numpy as np, pickle, itertools
from math import comb
d = pickle.load(open("output/artifacts/dp_corr2.pkl","rb"))
vecs = d["vecs"]; v50=d["val50"]; v49=d["val49"]
Eidx={v:i for i,v in enumerate(vecs)}
def enum9(D):
    out=[]
    def rec(j,rem,cur):
        if j>9: out.append(tuple(cur)); return
        for e in range(rem//j+1):
            cur.append(e); rec(j+1,rem-j*e,cur); cur.pop()
    rec(1,D,[])
    return out
vecs9 = enum9(9); B=len(vecs9); print("B=",B, flush=True)
Bidx={v:i for i,v in enumerate(vecs9)}
I=np.zeros((B,B)); J1=np.zeros((B,B))
sublist=[]
for vv in vecs9:
    L=[]
    for f in itertools.product(*[range(x+1) for x in vv]):
        c=1
        for j in range(9): c*=comb(vv[j],f[j])
        a=sum((jj+1)*(vv[jj]-f[jj]) for jj in range(9))
        L.append((Eidx[f],c,a,f))
    sublist.append(L)
for i in range(B):
    ei=vecs9[i]
    for j in range(i,B):
        ej=vecs9[j]
        g=tuple(ei[t]+ej[t] for t in range(9))
        val=v50[(Eidx[g],0)]
        I[i,j]=val; I[j,i]=val
        s=0.0
        for (ff,c1,a,f) in sublist[i]:
            fv=vecs[ff]
            for (gg,c2,b,g2) in sublist[j]:
                gv=vecs[gg]
                h=tuple(fv[t]+gv[t] for t in range(9))
                s+=c1*c2*v49[(Eidx[h],a+b+2)]/((a+1)*(b+1))
        J1[i,j]=s; J1[j,i]=s
J=50*J1
np.save("output/artifacts/I_mat.npy",I); np.save("output/artifacts/J_mat.npy",J)
print("const M =",J[0,0]/I[0,0], flush=True)
# long double scaled solve
Il=I.astype(np.longdouble); Jl=J.astype(np.longdouble)
dd=np.sqrt(np.diag(Il)); Is=Il/dd[:,None]/dd[None,:]; Js=Jl/dd[:,None]/dd[None,:]
L=np.linalg.cholesky(Is)
Y=np.linalg.solve(L,Js); Y=np.linalg.solve(L,Y.T).T; Y=(Y+Y.T)/2
w,V=np.linalg.eigh(Y)
print("top 12:", w[-12:], flush=True)
print("max M =", w[-1], flush=True)
np.save("output/artifacts/eigvals.npy", np.array(w, dtype=float))
c=np.array(V[:,-1],dtype=float)/np.array(dd,dtype=float)
np.save("output/artifacts/coeff_float.npy", c)
print("Rayleigh:", (c@J@c)/(c@I@c), flush=True)
