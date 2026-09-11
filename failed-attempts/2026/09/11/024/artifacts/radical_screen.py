"""S-radical screen over all S-centric preimages of Q-subgroups.
For each S-orbit rep H<=Q with preimage P S-centric: compute N_S(P), Out_S(P)=N_S(P)/P (centric),
compute |O_2(Out_S(P))| by brute force (groups of order <= 32ish). Survivors: O_2 trivial."""
import numpy as np, json, pickle, time, itertools
from collections import deque
E=np.load("output/artifacts/elems.npy"); MT=np.load("output/artifacts/multable.npy")
N=1024
def mul(a,b): return int(MT[a,b])
INV=np.zeros(N,dtype=int)
for n in range(N):
    INV[n]=int(np.where(MT[n,:]==0)[0][0])
idx={tuple(e):n for n,e in enumerate(map(tuple,E.tolist()))}
r=idx[(1,0,0,0,0)]; s=idx[(0,1,0,0,0)]; tt=idx[(0,0,1,0,0)]; u=idx[(0,0,0,1,0)]; v=idx[(0,0,0,0,1)]
Om=sorted([n for n in range(N) if E[n,3]==0 and E[n,4]==0 and mul(n,n)==0])
Omset=set(Om)
# rebuild Q reps + subgroups (recompute quickly using saved? recompute)
cn=np.full(N,-1); reps=[]
for n in range(N):
    found=None
    for i,rr in enumerate(reps):
        if mul(n,INV[rr]) in Omset:
            found=i; break
    if found is None:
        reps.append(n); found=len(reps)-1
    cn[n]=found
Q=len(reps)
print("Q=",Q)
QM=np.zeros((Q,Q),dtype=int)
for a in range(Q):
    for b in range(Q):
        q=mul(reps[a],reps[b])
        for i,rr in enumerate(reps):
            if mul(q,INV[rr]) in Omset:
                QM[a,b]=i; break
def closureQ(genset):
    seen={0}; st=[0]; gl=list(genset)
    while st:
        h=st.pop()
        for g in gl:
            for x in (QM[h,g],QM[g,h]):
                if x not in seen: seen.add(x); st.append(x)
    return frozenset(seen)
seen={frozenset([0])}; queue=deque([frozenset([0])])
while queue:
    H=queue.popleft()
    for g in range(Q):
        if g in H: continue
        H2=closureQ(set(H)|{g})
        if H2 not in seen:
            seen.add(H2); queue.append(H2)
print("Q subs:",len(seen))
# S-action on Q
def qconj(qidx, by):
    return cn[mul(mul(by,reps[qidx]),INV[by])]
conj={g:np.array([qconj(q,gn) for q in range(Q)]) for g,gn in [("r",r),("s",s),("t",tt),("u",u),("v",v)]}
def apply_sub(H, perm): return frozenset(int(perm[x]) for x in H)
remaining=set(seen); orbits=[]
while remaining:
    H=remaining.pop()
    orb={H}; st=[H]
    while st:
        X=st.pop()
        for p in conj.values():
            Y=apply_sub(X,p)
            if Y in remaining:
                remaining.discard(Y); orb.add(Y); st.append(Y)
    orbits.append(orb)
print("orbits:",len(orbits))
# E-triple Q-images for identification
Et=json.load(open("output/artifacts/E_triple.json"))
EQ={}
for name in ("E1","E2","E3"):
    P=set(Et[name])
    H=frozenset(cn[n] for n in P)
    EQ[name]=H
    print(name,"Q-size:",len(H))
# analyze each orbit rep
def normalizer(Pset):
    S_=Pset
    return [x for x in range(N) if all(mul(mul(x,p),INV[x]) in S_ for p in Pset)]
def centralizer_of_set(P):
    return [x for x in range(N) if all(mul(x,p)==mul(p,x) for p in P)]
def o2_order_of_quotient(Nlist, Pset):
    # G = N/P as abstract group via cosets; compute its maximal normal 2-subgroup order.
    # Since G is a 2-group quotient... N,P are 2-groups so G is a 2-group; O_2(G)=G always!
    # NOTE: O_2(N_S(P)/P) is trivial iff N_S(P)=P. The S-radical condition O_2(Out_S(P))=1
    # with Out_S(P)=N_S(P)/P (centric) means N_S(P)=P, i.e., P self-normalizing!
    return len(Nlist)//len(Pset)
t0=time.time()
ncentric=0
selfnorm=[]
nonself=[]
e_classes=set()
for oi,orb in enumerate(orbits):
    H=next(iter(orb))
    P=sorted([n for n in range(N) if cn[n] in H])
    Pset=set(P)
    C=centralizer_of_set(P)
    if not all(c in Pset for c in C):
        continue
    ncentric+=1
    Nor=normalizer(Pset)
    q=len(Nor)//len(P)
    isE = any(H==EQ[k] for k in EQ)
    if isE:
        e_classes.add(oi)
    if q==1:
        selfnorm.append((oi,len(H),len(P),len(orb),[k for k in EQ if H==EQ[k]]))
    else:
        nonself.append((oi,len(H),len(P),len(orb),q))
print(f"centric orbit reps: {ncentric}, self-normalizing (N=P): {len(selfnorm)}, N>P: {len(nonself)}")
print("E-class orbit idx:",e_classes)
print("selfnorm (oi,qsize,psize,orbsize,isE):")
for row in selfnorm: print(row)
json.dump({"ncentric":ncentric,"selfnorm":selfnorm,"nonself_n":[r for r in nonself],
 "e_orbits":sorted(e_classes)},
 open("output/artifacts/radical_screen.json","w"),indent=1)
print("saved")
