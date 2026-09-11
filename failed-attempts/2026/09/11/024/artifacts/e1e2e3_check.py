import numpy as np, json
E=np.load("output/artifacts/elems.npy"); MT=np.load("output/artifacts/multable.npy")
N=1024
def mul(a,b): return int(MT[a,b])
INV=np.zeros(N,dtype=int)
for n in range(N):
    INV[n]=int(np.where(MT[n,:]==0)[0][0])
idx={tuple(e):n for n,e in enumerate(map(tuple,E.tolist()))}
r=idx[(1,0,0,0,0)]; s=idx[(0,1,0,0,0)]; tt=idx[(0,0,1,0,0)]; u=idx[(0,0,0,1,0)]; v=idx[(0,0,0,0,1)]
def closure(gens):
    seen={0}; st=[0]; gl=list(gens)
    while st:
        h=st.pop()
        for g in gl:
            for x in (mul(h,g),mul(g,h)):
                if x not in seen: seen.add(x); st.append(x)
    return sorted(seen)
def is_subgroup(L):
    S=set(L)
    return all(mul(a,b) in S for a in L for b in L)
E1=closure([r,s,tt,u]); E2=closure([r,s,tt,v])
r2=mul(r,r); s2=mul(s,s)
E3=closure([r2,s2,tt,u,v])
print("orders:",len(E1),len(E2),len(E3))
# check subgroups
print("sub:",is_subgroup(E1),is_subgroup(E2),is_subgroup(E3))
# Om containment
Om=sorted([n for n in range(N) if E[n,3]==0 and E[n,4]==0 and mul(n,n)==0])
Z=[n for n in range(N) if all(mul(n,g)==mul(g,n) for g in [r,s,tt,u,v])]
print("Z==Om:",sorted(Z)==sorted(Om))
for name,EE in [("E1",E1),("E2",E2),("E3",E3)]:
    S_=set(EE)
    print(name,"contains Om:",all(o in S_ for o in Om))
    # centric?
    C=[x for x in range(N) if all(mul(x,p)==mul(p,x) for p in EE)]
    print(name,"|C|=",len(C),"centric:",all(c in S_ for c in C))
    # normalizer
    Nor=[x for x in range(N) if all(mul(mul(x,p),INV[x]) in S_ for p in EE)]
    print(name,"|N|=",len(Nor))
json.dump({"E1":E1,"E2":E2,"E3":E3},open("output/artifacts/E_triple.json","w"))
print("saved")
