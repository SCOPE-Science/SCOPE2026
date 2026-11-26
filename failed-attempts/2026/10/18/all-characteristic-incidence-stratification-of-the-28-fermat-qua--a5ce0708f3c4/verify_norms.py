from itertools import combinations
from collections import Counter

# tuples a0..a3 for Z[t]/(t^4+1)
def add(u,v):return tuple(a+b for a,b in zip(u,v))
def neg(u):return tuple(-a for a in u)
def sub(u,v):return add(u,neg(v))
def mul(u,v):
 out=[0]*4
 for i,a in enumerate(u):
  for j,b in enumerate(v):
   x=i+j;out[x%4]+= (-1 if x>=4 else 1)*a*b
 return tuple(out)
zero=(0,0,0,0);one=(1,0,0,0)
def pw(x,j):
 y=one
 for _ in range(j):y=mul(x,y)
 return y
t=(0,1,0,0)
L=[]
for i in range(4):
 for j in range(4):L.append((pw(t,2*i),pw(t,2*j),one))
for j in range(3):
 for k in (1,3,5,7):
  v=[zero]*3;a,b=[x for x in range(3) if x!=j];v[a]=one;v[b]=neg(pw(t,k));L.append(tuple(v))
assert len(L)==28
def det(v,w,y):
 return add(sub(mul(v[0],sub(mul(w[1],y[2]),mul(w[2],y[1]))),mul(v[1],sub(mul(w[0],y[2]),mul(w[2],y[0])))),mul(v[2],sub(mul(w[0],y[1]),mul(w[1],y[0]))))
def norm(d):
 a,b,c,e=d;return (a*a-c*c+2*b*e)**2+(2*a*c-b*b+e*e)**2
zeros=0; cnt=Counter(); norms=Counter()
for ids in combinations(range(28),3):
 d=det(*(L[i] for i in ids))
 if d==zero:zeros+=1;continue
 v=norm(d);norms[v]+=1;remainder=v
 for prime in (2,3,5,17):
  if remainder%prime==0:
   cnt[prime]+=1
   while remainder%prime==0:remainder//=prime
 assert remainder==1
assert zeros==60
assert norms==Counter({4:864,16:560,8:384,1:384,64:192,36:192,17:192,9:192,32:96,256:64,2:64,400:32})
assert set(cnt)=={2,3,5,17}
# All nonzero triple determinants have norm supported on these four primes;
# hence outside them the characteristic-zero concurrence pattern is preserved.
print('NORM_OK',zeros,dict(sorted(norms.items())),dict(sorted(cnt.items())))
