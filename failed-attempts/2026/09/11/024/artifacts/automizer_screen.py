"""Bounded fallback attempt: per-class features for all 919 S-centric preimage reps.
Valid eliminations: (S) P=S not proper; (CYC) P cyclic => Aut(P) is a 2-group => Out_F(P)
a 2-group => no strongly 2-embedded subgroup => never essential (any F).
Report survivors; E1,E2,E3 must survive."""
import numpy as np, json, time
from collections import deque
t0=time.time()
E=np.load("output/artifacts/elems.npy"); MT=np.load("output/artifacts/multable.npy")
N=1024
def mul(a,b): return int(MT[a,b])
INV=np.zeros(N,dtype=int)
for n in range(N):
    INV[n]=int(np.where(MT[n,:]==0)[0][0])
idx={tuple(e):n for n,e in enumerate(map(tuple,E.tolist()))}
r=idx[(1,0,0,0,0)]; s=idx[(0,1,0,0,0)]; tt=idx[(0,0,1,0,0)]; u=idx[(0,0,0,1,0)]; v=idx[(0,0,0,0,1)]
Om=np.array(sorted([n for n in range(N) if E[n,3]==0 and E[n,4]==0 and mul(n,n)==0]))
Omset=set(Om.tolist())
cn=np.full(N,-1); reps=[]
for n in range(N):
    found=None
    for i,rr in enumerate(reps):
        if mul(n,INV[rr]) in Omset:
            found=i; break
    if found is None:
        reps.append(n); found=len(reps)-1
    cn[n]=found
Q=len(reps); reps=np.array(reps)
print("Q=",Q)
# Q mult via vectorized lookup: precompute IDX map
QIDX=np.full(Q,-1)
# coset of x: use cn directly
QM=np.zeros((Q,Q),dtype=np.int32)
for a in range(Q):
    ab=np.array([mul(int(reps[a]),int(reps[b])) for b in range(Q)])
    QM[a,:]=cn[ab]
# Q subgroups
def closureQ(genset):
    seen={0}; st=[0]; gl=list(genset)
    while st:
        h=st.pop()
        for g in gl:
            for x in (int(QM[h,g]),int(QM[g,h])):
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
print(f"Qsubs={len(seen)} t={time.time()-t0:.1f}s")
# S-action perms on Q: full 128 perms via BFS on gens
def qmul(a,b): return int(QM[a,b])
# build perm for each generator
import numpy as np
gidx={"r":cn[r],"s":cn[s],"t":cn[tt],"u":cn[u],"v":cn[v]}
# Q-conjugation by q0: need inverse in Q
QINV=np.zeros(Q,dtype=int)
for a in range(Q):
    for b in range(Q):
        if QM[a,b]==0: QINV[a]=b; break
def qconj_perm(q0):
    iq=QINV[q0]
    return np.array([QM[QM[q0,a],iq] for a in range(Q)])
genperms=[qconj_perm(gidx[g]) for g in ("r","s","t","u","v")]
# all Q perms by BFS (words in gens) -> 128 perms
perms=[np.arange(Q)]
got={tuple(np.arange(Q)):0}
from collections import deque as dq
qq=dq([np.arange(Q)])
while qq:
    p=qq.popleft()
    for g in genperms:
        p2=p[g]  # compose? careful: permutations as arrays: (p then conj_g): image of a under p then g: g[p[a]]
        if tuple(p2) not in got:
            got[tuple(p2)]=len(perms); perms.append(p2); qq.append(p2)
perms=np.array(perms)
print("Qconj perms:",len(perms))
print('NOTE: image order',len(perms),'(kernel large; BFS closure still complete)')
# orbits of Q-subs under perms
remaining=set(seen); orbits=[]
while remaining:
    H=remaining.pop()
    Hb=np.zeros(Q,bool); Hb[list(H)]=True
    orb={H}; st=[Hb]
    while st:
        Xb=st.pop()
        for p in perms:
            Yb=Xb[p]
            Y=frozenset(np.where(Yb)[0].tolist())
            if Y in remaining:
                remaining.discard(Y); orb.add(Y); st.append(Yb)
    orbits.append(orb)
print("orbits:",len(orbits))
# E-triple Q-images
Et=json.load(open("output/artifacts/E_triple.json"))
EQ={k:frozenset(cn[n] for n in Et[k]) for k in Et}
print("EQ sizes:",{k:len(v) for k,v in EQ.items()})
# per-class features
Pbool_cache={}
def preimage(H):
    m=np.zeros(N,bool)
    for n in range(N):
        if cn[n] in H: m[n]=True
    return m
rows=[]
for oi,orb in enumerate(orbits):
    H=next(iter(orb))
    Pm=preimage(H)
    P=np.where(Pm)[0]
    C_ok=None
    # centralizer test vectorized: x centralizes P iff MT[x,P]==MT[P,x] elementwise
    # do for all x at once? MT[:,P] vs MT[P,:].T : (1024,k) vs (k,1024).T=(1024,k). compare.
    A1=MT[np.ix_(np.arange(N),P)]; A2=MT[np.ix_(P,np.arange(N))].T
    cent=np.where((A1==A2).all(axis=1))[0]
    centric=set(cent.tolist())<=set(P.tolist())
    if not centric:
        rows.append({"oi":oi,"q":len(H),"p":len(P),"centric":False}); continue
    # features
    sub=MT[np.ix_(P,P)]
    abelian=bool((sub==sub.T).all())
    # cyclic: unique involution: count x with x^2==0
    sq=np.diag(sub)  # MT[p,p]
    ninv=int((sq==0).sum())  # includes identity
    cyclic=(ninv==2)
    # normalizer in Q: q with perm(H)==H
    Hb=np.zeros(Q,bool); Hb[list(H)]=True
    nN=int(sum(1 for p in perms if (Hb[p]==Hb).all()))
    nN_S=8*nN
    index=nN_S//len(P)
    inA=bool((E[P,3]==0).all() and (E[P,4]==0).all())
    pcapA=int(((E[P,3]==0)&(E[P,4]==0)).sum())
    isE=[k for k in EQ if EQ[k]==H]
    rows.append({"oi":oi,"q":len(H),"p":len(P),"centric":True,"abelian":abelian,
      "cyclic":cyclic,"nNS":nN_S,"nout":index,"inA":inA,"pcapA":pcapA,
      "orbsize":len(orb),"isE":isE})
cent=[r_ for r_ in rows if r_.get("centric")]
print("centric:",len(cent))
el_S=[r_ for r_ in cent if r_["p"]==1024]
el_C=[r_ for r_ in cent if r_["p"]<1024 and r_["cyclic"]]
surv=[r_ for r_ in cent if r_["p"]<1024 and not r_["cyclic"]]
print("P=S:",len(el_S),"cyclic-proper:",len(el_C),"survivors:",len(surv))
print("E classes:",[(r_["oi"],r_["q"],r_["p"],r_["isE"]) for r_ in cent if r_["isE"]])
# survivor stats
import collections
print("survivor |P| dist:",dict(sorted(collections.Counter(r_["p"] for r_ in surv).items())))
print("survivors with N_S(P)=S:",sum(1 for r_ in surv if r_["nNS"]==1024))
print("survivors abelian:",sum(1 for r_ in surv if r_["abelian"]))
print("survivor nout dist:",dict(sorted(collections.Counter(r_["nout"] for r_ in surv).items())))
json.dump({"rows":rows,
 "summary":{"centric":len(cent),"elim_S":len(el_S),"elim_cyclic":len(el_C),"survivors":len(surv)}},
 open("output/artifacts/automizer_screen.json","w"))
print("saved")
