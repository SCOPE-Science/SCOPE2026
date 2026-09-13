"""Build I,J in longdouble from dp_ld.pkl + mpmath generalized EVP + subspace analysis."""
import numpy as np, pickle, itertools
from math import comb
d = pickle.load(open("output/artifacts/dp_ld.pkl","rb"))
vecs=d["vecs"]; v50=d["v50ld"]; v49=d["v49ld"]
Eidx={v:i for i,v in enumerate(vecs)}
def enum9(D):
    out=[]
    def rec(j,rem,cur):
        if j>9: out.append(tuple(cur)); return
        for e in range(rem//j+1):
            cur.append(e); rec(j+1,rem-j*e,cur); cur.pop()
    rec(1,D,[])
    return out
vecs9=enum9(9); B=len(vecs9); print("B=",B,flush=True)
LD=np.longdouble
I=np.zeros((B,B),dtype=LD); J1=np.zeros((B,B),dtype=LD)
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
        s=LD(0)
        for (ff,c1,a,f) in sublist[i]:
            fv=vecs[ff]
            for (gg,c2,b,g2) in sublist[j]:
                gv=vecs[gg]
                h=tuple(fv[t]+gv[t] for t in range(9))
                s+=LD(c1*c2)*v49[(Eidx[h],a+b+2)]/LD((a+1)*(b+1))
        J1[i,j]=s; J1[j,i]=s
J=LD(50)*J1
np.save("output/artifacts/I_ld.npy", np.array(I,dtype=float))
np.save("output/artifacts/J_ld.npy", np.array(J,dtype=float))
pickle.dump({"I":I,"J":J,"vecs9":vecs9}, open("output/artifacts/IJ_ld.pkl","wb"))
print("const M =", float(J[0,0]/I[0,0]), flush=True)
# conditioning in longdouble precision
s0=I[0,0]; In=I/s0; Jn=J/s0
dd=np.sqrt(np.diag(In)); Is=In/dd[:,None]/dd[None,:]; Js=Jn/dd[:,None]/dd[None,:]
Isf=np.array(Is,dtype=float); Jsf=np.array(Js,dtype=float)
s,U=np.linalg.eigh((Isf+Isf.T)/2)
s=np.array(s,dtype=float)
print("eig(Is) min=%.4e #<1e-12: %d #<1e-15: %d" % (s.min(), (s<1e-12).sum(), (s<1e-15).sum()), flush=True)
print("eig(Is) smallest 10:", s[:10], flush=True)
