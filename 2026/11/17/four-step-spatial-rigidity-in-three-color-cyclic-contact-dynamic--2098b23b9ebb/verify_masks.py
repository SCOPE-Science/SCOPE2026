"""Independent 4-step transfer computation using successor masks, not time-step simulation.
Standard-library only; run: python3 verify_masks.py
"""
from collections import Counter

# A trace is specified by its starting color and the single non-updating time.
traces=[]
for initial in range(3):
    for hold in range(4):
        v=initial
        word=[]
        for t in range(4):
            word.append(v)
            v=(v + (t!=hold))%3
        assert v==initial
        traces.append(tuple(word))
assert len(set(traces))==12
cols=[(a,b) for a in range(12) for b in range(12)]
want=[]
contact=[]
selfmask=[]
for B in cols:
    need=0
    own=0
    for row in (0,1):
        word=traces[B[row]]
        other=traces[B[1-row]]
        for t in range(4):
            if word[(t+1)%4]!=word[t]:need|=1<<(4*row+t)
            if other[t]==(word[t]+1)%3:own|=1<<(4*row+t)
    want.append(need)
    selfmask.append(own)
    masks=[]
    for A in cols:
        mask=0
        for row in (0,1):
            for t in range(4):
                if any(traces[A[r]][t]==(traces[B[row]][t]+1)%3 for r in (0,1)):
                    mask|=1<<(4*row+t)
        masks.append(mask)
    contact.append(masks)

V=144*144
forward=[[] for _ in range(V)]
backward=[[] for _ in range(V)]
edges=0
for mid in range(144):
    required=want[mid]
    own=selfmask[mid]
    for left in range(144):
        partial=own|contact[mid][left]
        for right in range(144):
            if partial|contact[mid][right] == required:
                u=left*144+mid
                v=mid*144+right
                forward[u].append(v)
                backward[v].append(u)
                edges+=1
# A second Kosaraju traversal, implemented without external graph packages.
visited=bytearray(V)
order=[]
for start in range(V):
    if visited[start]:
        continue
    visited[start]=1
    stack=[(start,0)]
    while stack:
        v,j=stack[-1]
        if j<len(forward[v]):
            w=forward[v][j]
            stack[-1]=(v,j+1)
            if not visited[w]:
                visited[w]=1
                stack.append((w,0))
        else:
            order.append(v)
            stack.pop()
component=[-1]*V
all_components=[]
for start in reversed(order):
    if component[start]>=0:
        continue
    ident=len(all_components)
    stack=[start]
    component[start]=ident
    chunk=[]
    while stack:
        v=stack.pop()
        chunk.append(v)
        for w in backward[v]:
            if component[w]<0:
                component[w]=ident
                stack.append(w)
    all_components.append(chunk)
cyclic=[]
for chunk in all_components:
    if len(chunk)>1 or any(w==chunk[0] for w in forward[chunk[0]]):
        cyclic.append(chunk)
assert edges==20340
assert sorted(map(len,cyclic))==[4]*6
assert all(sum(component[v]==component[w] for v in chunk for w in forward[v])==4 for chunk in cyclic)
print('independent_mask_edges=',edges)
print('independent_cycle_scc_size_histogram=',dict(Counter(map(len,cyclic))))
print('independent_cyclic_vertices=',sum(map(len,cyclic)))
print('status=PASS')
