"""Reproduce the quaternary span-four orientable-cycle bound; requires numpy and scipy (HiGHS).
No downloaded data or private state is required.
"""
from itertools import product
from collections import defaultdict, Counter
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

q=4
W=[''.join(p) for p in product('0123',repeat=4)]
O=[(w,w[::-1]) for w in W if w<w[::-1]]
assert len(O)==120
V=[''.join(p) for p in product('0123',repeat=3)]
J={v:i for i,v in enumerate(V)}
E=[e for orb in O for e in orb]
A=np.zeros((64+120,240),dtype=np.int64)
for j,e in enumerate(E):
    A[J[e[:3]],j]+=1
    A[J[e[1:]],j]-=1
    A[64+j//2,j]+=1
assert np.max(abs(A))<=1
con=LinearConstraint(A,np.zeros(184),np.r_[np.zeros(64),np.ones(120)])
res=milp(-np.ones(240),integrality=np.ones(240),bounds=Bounds(0,1),constraints=con,options={'mip_rel_gap':0.0,'time_limit':50.0})
assert res.success and res.mip_gap==0 and abs(res.fun+106)<1e-7, (res.message, res.fun)
chosen=sorted(E[i] for i,x in enumerate(res.x) if x>.5)
assert len(chosen)==106 and len({min(w,w[::-1]) for w in chosen})==106
# Verify the exact, integer-valued primal independently of MILP feasibility tolerance.
assert np.all(A @ np.rint(res.x).astype(np.int64) >= np.zeros(184,dtype=int))
assert np.all(A @ np.rint(res.x).astype(np.int64) <= np.r_[np.zeros(64,dtype=int),np.ones(120,dtype=int)])
# Reconstruct Euler circuit without a graph library.
g=defaultdict(list)
for w in chosen: g[w[:3]].append((w[1:],w))
for v in g: g[v].sort(reverse=True)
start=min(g)
stack=[(start,'')]; circuit=[]
while stack:
    v=stack[-1][0]
    if g[v]:
        t,w=g[v].pop()
        stack.append((t,w))
    else:
        circuit.append(stack.pop()[1])
assert len(circuit)==107 and circuit[-1]==''
seq=''.join(w[0] for w in circuit[-2::-1]);assert len(seq)==106
windows=[''.join(seq[(i+j)%106] for j in range(4)) for i in range(106)]
assert sorted(windows)==chosen
assert len(set(min(w,w[::-1]) for w in windows))==106
# Independent 120-variable necessary relaxation, with exact integral antisymmetric conservation and quotient parity.
C=sorted({min(v,v[::-1]) for v in V})
N=[v for v in C if v!=v[::-1]]
B=np.zeros((len(N),120),dtype=np.int64)
P=np.zeros((len(C),120),dtype=np.int64)
for j,(a,rev) in enumerate(O):
    u=a[:3];v=a[1:]
    for i,p in enumerate(N):
        B[i,j]=int(u==p)-int(v==p)-int(u==p[::-1])+int(v==p[::-1])
    P[C.index(min(u,u[::-1])),j]+=1
    P[C.index(min(v,v[::-1])),j]+=1
T=np.block([[B,np.zeros((len(N),len(C)),dtype=int)],[P,-2*np.eye(len(C),dtype=int)]])
rr=milp(np.r_[-np.ones(120),np.zeros(len(C))],integrality=np.ones(120+len(C)),bounds=Bounds(0,np.r_[np.ones(120),np.full(len(C),10)]),constraints=LinearConstraint(T,np.zeros(len(T)),np.zeros(len(T))),options={'mip_rel_gap':0.0,'time_limit':50.0})
assert rr.success and rr.mip_gap==0 and abs(rr.fun+106)<1e-7,(rr.message,rr.fun)
print('DIRECT_OPTIMUM',106,'RELAXATION_OPTIMUM',106,'WITNESS',seq,'VERIFY_OK')
