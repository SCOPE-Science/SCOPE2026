"""Independent generator-matrix check for the five-person book-network example.

Requires NumPy, Python >=3.9. States: 0 susceptible, 1 infectious, 2 removed.
"""
from collections import deque
import numpy as np

E = [(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(3,4)]
N = 5
RATE = 100


def transitions(state):
    result=[]
    for v in range(N):
        if state[v] == 1:
            new=list(state);new[v]=2
            result.append((tuple(new),1))
        elif state[v] == 0:
            k=sum(1 for a,b in E if (a==v and state[b]==1) or (b==v and state[a]==1))
            if k:
                new=list(state);new[v]=1
                result.append((tuple(new),k*RATE))
    return result

start=(0,0,0,1,0)
seen={start:0}
queue=deque([start])
while queue:
    state=queue.popleft()
    for new,_ in transitions(state):
        if 1 in new and new not in seen:
            seen[new]=len(seen)
            queue.append(new)

M=np.zeros((len(seen),len(seen)),dtype=float)
for state,j in seen.items():
    for target,rate in transitions(state):
        M[j,j]+=rate
        if 1 in target:
            M[j,seen[target]]-=rate
sol=np.linalg.solve(M,np.ones(len(seen)))
h5=sum(1/k for k in range(1,6))
assert len(seen)>1
assert abs(sol[seen[start]]-2.283380168162515)<1e-10
assert sol[seen[start]]>h5+4e-5
print('PASS independent generator-matrix check:',len(seen),'transient states')
print('Expected extinction time at rate 100:',format(sol[0],'.15f'))
print('Limit:',format(h5,'.15f'))
