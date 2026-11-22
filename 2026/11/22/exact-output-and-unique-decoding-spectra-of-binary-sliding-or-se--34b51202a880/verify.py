import itertools,collections,math

def yof(x,h): return tuple(int(any(x[i:i+h])) for i in range(len(x)-h+1))
def f(h,L):
 if L<h: return 0
 if L==h: return 1
 d=L-h
 C=[0]*(d+1); C[0]=1
 for k in range(1,d+1): C[k]=sum(C[max(0,k-h):k])
 return C[d]
def g(h,L):
 if L==0:return 1
 return sum(1 for t in itertools.product((0,1),repeat=L-1) if not any(t[i:i+h]==(0,)*h for i in range(0,len(t)-h+1)))
def formula(y,h):
 m=len(y)
 if 0 not in y:return None
 runs=[]; t=0
 while t<m:
  if y[t]==0:t+=1;continue
  j=t
  while j<m and y[j]==1:j+=1
  runs.append((t,j))
  t=j
 z=1
 for a,b in runs:
  if a==0 or b==m: z*=g(h,b-a)
  else: z*=f(h,b-a)
 return z

def gfR(m,h):
 # via combinatorial grammar DP use power series operations dictionary
 def mul(a,b):
  c=[0]*(m+1)
  for i in range(m+1):
   for j in range(m-i+1):c[i+j]+=a[i]*b[j]
  return c
 def inv(a):
  c=[0]*(m+1); c[0]=1
  for j in range(1,m+1):c[j]=-sum(a[i]*c[j-i] for i in range(1,j+1))
  return c
 one=[1]*(m+1)
 denom=[1,-2,1]+[0]*max(0,m-2)
 if h+1<=m:denom[h+1]-=1
 z=[0,1]+[0]*(m-1)
 R=mul(inv([1,-1]+[0]*(m-1)),[1]+[0]*m)
 term=mul(mul(z,inv([1,-1]+[0]*(m-1))),inv(denom[:m+1]))
 return R[m]+term[m]
def gfU(m,h):
 den=[1,-1]+[0]*max(0,m-1)
 for e in (h+1,h+2):
  if e<=m:den[e]-=1
 c=[0]*(m+1); c[0]=1
 for j in range(1,m+1):c[j]=-sum(den[i]*c[j-i] for i in range(1,j+1))
 return (c[m-1]+(2*c[m-2] if m>=2 else 0)+(c[m-3] if m>=3 else 0))

count=0
for h in range(2,7):
 for m in range(1,11):
  n=m+h-1
  if n>16: continue
  d=collections.Counter(yof(x,h) for x in itertools.product((0,1),repeat=n))
  u=sum(v==1 for v in d.values())
  assert len(d)==gfR(m,h),(h,m,'R',len(d),gfR(m,h))
  assert u==gfU(m,h),(h,m,'U',u,gfU(m,h))
  for y,v in d.items():
   if 0 in y: assert formula(y,h)==v,(h,m,y,v,formula(y,h))
  count+=1
  print('PASS',h,m,'images',len(d),'singletons',u)
print('ALL PASS',count)
