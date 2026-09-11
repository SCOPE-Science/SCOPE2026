"""Subgroup census mod socle: Q=S/Om (order 128), lift candidates, S-conjugacy, centricity, Glauberman screen."""
import numpy as np, json, itertools, time
E=np.load("output/artifacts/elems.npy"); MT=np.load("output/artifacts/multable.npy")
N=1024
def mul(a,b): return int(MT[a,b])
INV=np.zeros(N,dtype=int)
for n in range(N):
    INV[n]=int(np.where(MT[n,:]==0)[0][0])
def comm(a,b): return mul(mul(mul(a,b),INV[a]),INV[b])
idx={tuple(e):n for n,e in enumerate(map(tuple,E.tolist()))}
r=idx[(1,0,0,0,0)]; s=idx[(0,1,0,0,0)]; tt=idx[(0,0,1,0,0)]; u=idx[(0,0,0,1,0)]; v=idx[(0,0,0,0,1)]
Om=sorted([n for n in range(N) if E[n,3]==0 and E[n,4]==0 and mul(n,n)==0])
Omset=set(Om)
assert len(Om)==8
# cosets of Om
cn=np.full(N,-1); reps=[]
for n in range(N):
    c=min(mul(n,h) for h in Om)
    if cn[c]==-1 and c not in reps:
        pass
    # assign
    found=None
    for rr in reps:
        if mul(n,INV[rr]) in Omset:
            found=rr; break
    if found is None:
        reps.append(n); found=n
    # map rep->index
    cn[n]=reps.index(found)
Q=len(reps)
print("Q order:",Q, "num reps:",len(reps))
assert Q==128
QM=np.zeros((Q,Q),dtype=int)
for a in range(Q):
    for b in range(Q):
        q=mul(reps[a],reps[b])
        # find coset
        for i,rr in enumerate(reps):
            if mul(q,INV[rr]) in Omset:
                QM[a,b]=i; break
QINV=np.zeros(Q,dtype=int)
for a in range(Q):
    for b in range(Q):
        if QM[a,b]==0: QINV[a]=b; break
# enumerate all subgroups of Q by DFS over elements (128 elts, feasible with pruning? use cyclic-extension DFS)
# Q has presentation: generators images of r,s,t,u,v with orders in Q: r:4? s:4? t:2? u:2 v:2
pass
def qord(a):
    x=a; k=1
    while x!=0:
        x=QM[x,a]; k+=1
    return k
print("orders:",qord(cn[r]),qord(cn[s]),qord(cn[tt]),qord(cn[u]),qord(cn[v]))
# subgroup enumeration via standard algorithm: iterate subsets closed... use recursive closure DFS with canonical min to dedupe
subs=set()
count=[0]
def closure(genset):
    seen={0}; st=[0]
    gl=list(genset)
    while st:
        h=st.pop()
        for g in gl:
            for x in (QM[h,g],QM[g,h]):
                if x not in seen: seen.add(x); st.append(x)
    return frozenset(seen)
# seed DFS: standard subgroup lattice enumeration: for each subgroup, try adding each element > max? Use BFS:
from collections import deque
seen_subs={frozenset([0])}
queue=deque([frozenset([0])])
while queue:
    H=queue.popleft()
    m=max(H) if H else -1
    for g in range(Q):
        if g in H: continue
        H2=closure(set(H)|{g})
        if H2 not in seen_subs:
            seen_subs.add(H2); queue.append(H2)
print("num subgroups of Q:",len(seen_subs))
# order distribution
from collections import Counter
od=Counter(len(H) for H in seen_subs)
print("Q order dist:",dict(sorted(od.items())))
# lift to S: preimage sizes *8
# For each Q-subgroup H, preimage P = union of cosets. Compute properties:
# S-conjugacy: action of S on Q-subgroups by conjugation (via reps). Compute orbits.
# First compute conjugation perm of Q induced by each generator
def qconj(qidx, by):
    # lift rep, conjugate, project
    x=mul(mul(by,reps[qidx]),INV[by])
    return cn[x]
conj={}
for g,gn in [("r",r),("s",s),("t",tt),("u",u),("v",v)]:
    conj[g]=np.array([qconj(q,gn) for q in range(Q)])
# orbit representatives of Q-subgroups under group generated: BFS with all 1024? use gens
def apply_sub(H, perm):
    return frozenset(perm[x] for x in H)
# orbits via greedy extraction
parent={H:H for H in seen_subs}
# simpler: greedy orbit extraction
remaining=set(seen_subs); orbits=[]
while remaining:
    H=remaining.pop()
    # orbit BFS
    orb={H}; st=[H]
    while st:
        X=st.pop()
        for g in conj.values():
            Y=apply_sub(X,g)
            if Y in remaining:
                remaining.discard(Y); orb.add(Y); st.append(Y)
            elif Y not in orb:
                # Y might be in another... but remaining-based: check
                pass
    # note: Y could be outside remaining but in orb already handled; but Y not in remaining and not in orb means it was consumed in earlier orbit -> merge? That can't happen since we pop orbits fully: if Y in a previous orbit, then H would have been there. Since action is group action and previous orbits are unions of orbits, Y in previous orbit implies H in same orbit, contradiction. So fine.
    orbits.append(orb)
print("num S-orbits on Q-subgroups:",len(orbits))
# For each orbit rep, compute preimage P props: order, S-centric?, contains Om?
def centralizer_S(Pset):
    P=Pset
    return [x for x in range(N) if all(mul(x,p)==mul(p,x) for p in P)]
results=[]
for orb in orbits:
    H=next(iter(orb))
    P=sorted([n for n in range(N) if cn[n] in H])
    Pset=set(P)
    # centric: C_S(P) <= P i.e. centralizer subset of P
    C=centralizer_S(P)
    centric=all(c in Pset for c in C)
    results.append({"qorder":len(H),"por der":len(P),"centric":centric,"orbit_size":len(orb),
      "qsize":len(H),"cmembers":len(C)})
# summarize
import collections
print("orbit reps:",len(results))
for d in sorted(results,key=lambda d:(d["qsize"],-d["centric"]))[:40]:
    print(d)
# centric orbit reps
cent=[d for d in results if d["centric"]]
print("centric orbit reps:",len(cent))
print(sorted([(d["qsize"],d["por der"],d["orbit_size"]) for d in cent]))
json.dump({"num_Qsubs":len(seen_subs),"Q_order_dist":dict(od),
 "num_orbits":len(orbits),
 "centric_reps":sorted([(d["qsize"],d["por der"],d["orbit_size"]) for d in cent])},
 open("output/artifacts/quotient_census.json","w"),indent=1)
# save orbit reps (Q-subgroup sorted lists) for replay
reps_out=[sorted(next(iter(o))) for o in orbits]
json.dump(reps_out,open("output/artifacts/quotient_orbit_reps.json","w"))
print("saved")
