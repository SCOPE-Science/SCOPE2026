"""Independent exact block-placement accounting, including period wrap."""
from collections import defaultdict
from math import comb

def cat(q,u):
    A=set();B=set();C=set()
    for r in range(q):
        p=tuple((r+i)%q for i in range(q))
        for a in range(q):
            if a==r:A.add(p+(a,))
            elif r<a:B.add(p+(a,))
            else:C.add(p+(a,))
            if a==(r-1)%q:A.add((a,)+p)
            elif (r==0 and a<q-1) or (r>0 and a<r-1):B.add((a,)+p)
            else:C.add((a,)+p)
    assert len(A)==q and len(B)==len(C)==q*(q-1)
    return A,B,C

checks=0; configs=0; repeated=0
for q in range(3,13):
    A,B,C=cat(q,None)
    for n in range(2,12):
        # For a fixed residual word P^(n-1) with its jth letter removed,
        # count distinct q+1 masks formed using a length-q deleted block.
        # Different block placements can give the same mask only when s=j,j+1.
        for j in range(q*(n-1)):
            buckets=defaultdict(set)
            for s in range(q*(n-1)+1):
                block=set(range(s,s+q))
                extra=j if j<s else j+q
                mask=tuple(sorted(block|{extra}))
                label=tuple(k%q for k in mask)
                buckets[label].add(mask)
            for u,masks in buckets.items():
                m=len(masks)
                if u in A: target=n-1 if j%q==u[0] else 0
                elif u in B or u in C:
                    # Count via explicit before/after block cyclic phases, no
                    # appeal to the closed-form deficit formula.
                    target=0
                    for s in range(q*(n-1)+1):
                        x=tuple(k%q for k in range(s,s+q))
                        candidate=x+(j%q,) if s<=j else (j%q,)+x
                        if candidate==u:target+=1
                else:target=0
                if u in A: pass # duplicate s=j,j+1 removed by set
                else:assert m==target,(q,n,j,u,m,target)
                if u in A:assert m==target,(q,n,j,u,m,target)
                checks+=1
                if m>=2:repeated+=1
        configs+=1
print('PASS gap_placement configurations=',configs,'fiber_entries=',checks,'repeated_entries=',repeated)
