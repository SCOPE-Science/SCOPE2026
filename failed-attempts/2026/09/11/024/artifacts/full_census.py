"""Full subgroup census of S (order 1024) by cyclic-extension BFS, then S-conjugacy orbits,
centricity, normalizers, and essential-necessary filters. Pure stdlib+numpy."""
import numpy as np, json, time
from collections import deque
E=np.load("output/artifacts/elems.npy"); MT=np.load("output/artifacts/multable.npy")
N=1024
def mul(a,b): return int(MT[a,b])
INV=np.zeros(N,dtype=int)
for n in range(N):
    INV[n]=int(np.where(MT[n,:]==0)[0][0])
t0=time.time()
def closure(genset):
    seen={0}; st=[0]; gl=list(genset)
    while st:
        h=st.pop()
        for g in gl:
            x=mul(h,g)
            if x not in seen: seen.add(x); st.append(x)
            y=mul(g,h)
            if y not in seen: seen.add(y); st.append(y)
    return frozenset(seen)
seen={frozenset([0])}; queue=deque([frozenset([0])])
while queue:
    H=queue.popleft()
    # candidate generators: elements >= max(H)? standard canonical to reduce dupes: try all g not in H
    for g in range(N):
        if g in H: continue
        H2=closure(set(H)|{g})
        if H2 not in seen:
            seen.add(H2); queue.append(H2)
print(f"total subgroups: {len(seen)} in {time.time()-t0:.1f}s")
from collections import Counter
od=Counter(len(H) for H in seen)
print("order dist:",dict(sorted(od.items())))
json.dump({"num_subgroups":len(seen),"order_dist":{str(k):v for k,v in sorted(od.items())}},
  open("output/artifacts/full_subgroup_count.json","w"),indent=1)
# save all subgroups as sorted lists (for downstream)
import pickle
with open("output/artifacts/all_subgroups.pkl","wb") as f:
    pickle.dump([sorted(H) for H in seen],f)
print("saved pkl")
