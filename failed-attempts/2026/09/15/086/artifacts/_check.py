import itertools
import numpy as np
# W0 for G2
import numpy as np
S1 = np.array([[-1,3],[0,1]], dtype=int)
S2 = np.array([[1,0],[1,-1]], dtype=int)
# generate group
def gen():
    els = {tuple(np.eye(2,dtype=int).flatten()): np.eye(2,dtype=int)}
    mats = [S1,S2]
    # BFS words
    from collections import deque
    # store mat -> word
    seen = {tuple(np.eye(2).flatten()): []}
    q=[np.eye(2,dtype=int)]
    while q:
        m=q.pop()
        for i,S in enumerate(mats):
            n = S@m  # left mult?
            # action: group acts on column vectors; composition left mult
            t=tuple(n.flatten())
            if t not in seen:
                seen[t]=seen[tuple(m.flatten())]+[i+1]
                q.append(n)
    return seen
seen=gen()
print(len(seen))
# check product order
P=S1@S2
print("s1s2=\n",P, "order?", end=" ")
M=np.eye(2,dtype=int)
for k in range(1,13):
    M=M@P
    if np.array_equal(M,np.eye(2)): print(k); break
