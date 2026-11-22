"""Exact independent feasibility and integer-congruence check for the seven-vertex wheel."""
from collections import Counter
n=7
edges={tuple(sorted((0,i))) for i in range(1,7)}
edges.update(tuple(sorted((i, (i%6)+1))) for i in range(1,7))
tri=[]
for a in range(n):
 for b in range(a+1,n):
  for c in range(b+1,n):
   if all((x,y) in edges for x,y in ((a,b),(a,c),(b,c))):
    tri.append((1<<a)|(1<<b)|(1<<c))
assert len(edges)==12 and len(tri)==6
N=1<<n
f=[int(not any((s&t)==t for t in tri)) for s in range(N)]
M=[[f[s&t] for t in range(N)] for s in range(N)]
# Apply the exact inverse of the Boolean-zeta matrix on both sides.
for i in range(n):
 bit=1<<i
 for s in range(N):
  if s&bit:
   row=M[s]; prior=M[s^bit]
   for t in range(N):row[t]-=prior[t]
for i in range(n):
 bit=1<<i
 for t in range(N):
  if t&bit:
   p=t^bit
   for s in range(N):M[s][t]-=M[s][p]
for s in range(N):
 for t in range(N):
  if s!=t: assert M[s][t]==0
hist=Counter(M[s][s] for s in range(N))
assert hist==Counter({0:105,-1:12,1:10,2:1}),hist
assert M[N-1][N-1]==2
print('WHEEL_TRIANGLES',len(tri))
print('WHEEL_INTEGER_CONGRUENCE',dict(sorted(hist.items())))
print('WHEEL_SMITH nonzero=1^22,2^1 zeros=105')
print('WHEEL_RANK_Q=23 RANK_F2=22 RANK_F3=23')
print('WHEEL_VERIFY_OK')
