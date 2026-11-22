from itertools import combinations
n=7
full=(1<<n)-1
V=[a for a in range(1,full) if a&1 and 2<=a.bit_count()<=n-2]
N=len(V)
id={a:i for i,a in enumerate(V)}
def compatible(a,b):
    return not all((x&y) for x,y in ((a,b),(a,full^b),(full^a,b),(full^a,full^b)))
f=[[(i,) for i in range(N)]]
for k in range(2,5):
    f.append([s+(j,) for s in f[-1] for j in range(s[-1]+1,N) if all(compatible(V[i],V[j]) for i in s)])
print('original f-vector:',*[len(x) for x in f])
total=0
traces=[]
for sign in (1,-1):
  for offset in range(n):
    p=[(sign*i+offset)%n for i in range(n)]
    perm=[]
    for a in V:
      b=sum(1<<p[i] for i in range(n) if a & (1<<i))
      if not b&1:b=full^b
      perm.append(id[b])
    trace=0
    for d,faces in enumerate(f):
      for face in faces:
        mapped=tuple(perm[i] for i in face)
        if set(mapped)!=set(face):continue
        inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
        trace+=(-1)**(d+inversions)
    traces.append(trace)
    total+=trace
print('Lefschetz Euler traces:',traces,'total',total,'orbit Euler',total//14)
assert total==-168
print('BURNSIDE_7_TREE_LINK_EULER_OK')
