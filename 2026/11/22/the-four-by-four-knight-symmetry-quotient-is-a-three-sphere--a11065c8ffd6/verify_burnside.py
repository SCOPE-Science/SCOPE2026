from collections import defaultdict
n=4;N=n*n;E=[];A=[0]*N
for i in range(N):
 for j in range(i+1,N):
  if sorted((abs(i//n-j//n),abs(i%n-j%n)))==[1,2]:A[i]|=1<<j;A[j]|=1<<i;E.append((i,j))
faces=[m for m in range(1,1<<N) if all(not (A[i]&m) for i in range(N) if m>>i&1)]
assert len(faces)==1364 and len(E)==24
by_size=sorted(faces,key=lambda f:(f.bit_count(),f))
perm=[]
for k in range(8):
 p=[]
 for i in range(N):
  r,c=divmod(i,n)
  if k>=4:c=n-1-c
  for z in range(k%4):r,c=c,n-1-r
  p.append(n*r+c)
 perm.append(p)
assert len(set(tuple(p) for p in perm))==8
sums=[0]*8
for p in perm:
 fixed=set(f for f in faces if sum(1<<p[i] for i in range(N) if f>>i&1)==f)
 C={}
 for f in by_size:
  if f not in fixed:continue
  v=[1]+[0]*7
  sub=(f-1)&f
  while sub:
   if sub in C:
    for k in range(1,8):v[k]+=C[sub][k-1]
   sub=(sub-1)&f
  C[f]=v
  for k in range(8):sums[k]+=v[k]
assert all(t%8==0 for t in sums),sums
quot=[s//8 for s in sums]
assert quot==[217,4801,35910,126666,239340,249840,136080,30240],quot
print('KNIGHT4_D4_BURNSIDE_OK',len(E),len(faces),quot)
