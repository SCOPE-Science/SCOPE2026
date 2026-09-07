"""Independent trace cross-check: count closed walks by word enumeration
(no linear algebra) and compare to Tr(A^k) from adjacency powers.
Also verifies Tr(A^2)=16n and Tr(A^4)=152n (i.e. 38 closed 4-walks per vertex)."""
import itertools, json

def mul(p,q,n):
    N=2*n
    e1,k1=p; e2,k2=q
    if e1==0 and e2==0: return (0,(k1+k2)%N)
    if e1==0 and e2==1: return (1,(k2-k1)%N)
    if e1==1 and e2==0: return (1,(k1+k2)%N)
    return (0,(n+k2-k1)%N)

def count_closed(n, L):
    N=2*n
    S=[(0,1),(0,N-1),(1,0),(1,n)]
    ident=(0,0)
    c=0
    for w in itertools.product(range(4), repeat=L):
        p=ident
        for i in w: p=mul(p,S[i],n)
        if p==ident: c+=1
    return c

rows=[]
for n in [3,4,5,6,7,8,9,10,12,30]:
    c2=count_closed(n,2)
    c4=count_closed(n,4)
    # adjacency trace via group law matrix (integer)
    # build adjacency as ints for exactness
    els=[(e,k) for e in (0,1) for k in range(2*n)]
    idx={g:i for i,g in enumerate(els)}
    S=[(0,1),(0,2*n-1),(1,0),(1,n)]
    Nv=len(els)
    import numpy as np
    A=np.zeros((Nv,Nv),dtype=int)
    for g in els:
        i=idx[g]
        for s in S:
            A[i,idx[mul(g,s,n)]]+=1
    tr2=int(np.trace(A@A))
    tr4=int(np.trace(np.linalg.matrix_power(A,4)))
    assert c2==4, (n,c2)
    assert c4==38, (n,c4)
    assert tr2==16*n==Nv*c2, (n,tr2)
    assert tr4==152*n==Nv*c4, (n,tr4)
    # fourth-moment upper bound on lam2 (weak, honest)
    import math
    ub=(tr4-256)**0.25
    print(f"n={n} closed2={c2} closed4={c4} Tr2={tr2} Tr4={tr4} 152n={152*n} ub_lam2<={ub:.3f}")
    rows.append({"n":n,"closed2":c2,"closed4":c4,"tr2":tr2,"tr4":tr4,"ub_lam2":ub})
with open("/srv/scope-research/rounds/2026-09-07-pilot-01/workspaces/research/lane-03/output/artifacts/trace_counts.json","w") as f:
    json.dump(rows,f,indent=2)
print("TRACE CHECKS PASSED")
