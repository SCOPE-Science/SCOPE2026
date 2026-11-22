from collections import Counter
MOD={2:0x7,4:0x13,6:0x43,8:0x11B,10:0x409,12:0x1053}

def mul(a,b,n):
 m=MOD[n]; top=1<<n;mask=top-1;r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&top:a^=m
 return r

def square(a,n):return mul(a,a,n)
def fourth(a,n):return square(square(a,n),n)
def powr(a,e,n):
 out=1
 while e:
  if e&1:out=mul(out,a,n)
  a=square(a,n);e//=2
 return out

def add4(u,v):return tuple(a^b for a,b in zip(u,v))
def smul(k,u,n):return tuple(mul(k,a,n) for a in u)
def frob(u,n):return tuple(square(a,n) for a in u)
def polyF(A,u,n):
 acc=0
 for i in range(4):
  for j in range(4):
   if A>>(4*i+j)&1:acc^=mul(square(u[i],n),u[j],n)
 return acc

def matmul(a,b):
 return sum((sum((sum((((a>>(4*i+j))&1) & ((b>>(4*j+k))&1)) for j in range(4))&1)<<k for k in range(4)))<<(4*i) for i in range(4))
def transpose(a):return sum(((a>>(4*j+i))&1)<<(4*i+j) for i in range(4) for j in range(4))
def rows(a):return [(a>>(4*i))&15 for i in range(4)]
def rank(a):
 k=0;b=rows(a)
 for j in range(4):
  i=next((i for i in range(k,4) if (b[i]>>j)&1),None)
  if i is None:continue
  b[i],b[k]=b[k],b[i]
  for t in range(4):
   if t!=k and (b[t]>>j)&1:b[t]^=b[k]
  k+=1
 return k

def inverse(A):
 aug=[(rows(A)[i]|(1<<(4+i))) for i in range(4)]
 for j in range(4):
  k=next(k for k in range(j,4) if aug[k]>>j&1)
  aug[k],aug[j]=aug[j],aug[k]
  for k in range(4):
   if k!=j and aug[k]>>j&1:aug[k]^=aug[j]
 return sum((a>>4)<<(4*i) for i,a in enumerate(aug))
def matv(A,u):return tuple(__import__('functools').reduce(int.__xor__,(u[j] for j in range(4) if A>>(4*i+j)&1),0) for i in range(4))

def kernel(A,n):
 B=matmul(inverse(transpose(A)),A)
 dim=4*n; images=[]
 for k in range(dim):
  u=tuple(1<<(k%n) if i==k//n else 0 for i in range(4))
  v=add4(tuple(fourth(z,n) for z in u),matv(B,u))
  images.append(sum(v[i]<<(i*n) for i in range(4)))
 # row reduce images (columns) with coordinate tracking of each linear combination
 piv={};deps=[]
 for k,val in enumerate(images):
  vec=1<<k
  while val:
   j=val.bit_length()-1
   if j not in piv:
    piv[j]=(val,vec);break
   val^=piv[j][0];vec^=piv[j][1]
  else:deps.append(vec)
 assert len(deps)==8,(n,A,len(deps))
 basis=[tuple((v>>(i*n))&((1<<n)-1) for i in range(4)) for v in deps]
 out=[(0,0,0,0)]
 for b in basis:out+= [add4(v,b) for v in out]
 assert len(set(out))==256
 return out

def canonical(v,n,third):return min(v,smul(third,v,n),smul(third^1,v,n))

def spectrum(A,n):
 roots=kernel(A,n)
 third=next(a for a in range(2,1<<n) if a!=1 and powr(a,3,n)==1)
 pts=set()
 for v in roots:
  if v!=(0,0,0,0) and polyF(A,v,n)==0:pts.add(canonical(v,n,third))
 assert len(pts)==45,(len(pts),hex(A))
 unseen=set(pts);cycs=[]
 while unseen:
  v=min(unseen);w=v;k=0
  while True:
   assert w in unseen or w==v
   unseen.discard(w);k+=1
   w=canonical(frob(w,n),n,third)
   if w==v:break
  cycs.append(k)
 assert sum(cycs)==45
 return dict(sorted(Counter(cycs).items())),pts

reps=[0x1468,0x126b,0x1486,0x1469,0x126c,0x1249,0x128d,0x128c,0x124a,0x1248]
orders=[3,2,5,3,4,1,6,3,2,1]

def lines(A,pts,n):
 stars=sorted(pts);index={s:i for i,s in enumerate(stars)}
 third=next(a for a in range(2,1<<n) if a!=1 and powr(a,3,n)==1)
 def mix(u,v):
  w=matv(A,v)
  return __import__('functools').reduce(int.__xor__,(mul(square(u[i],n),w[i],n) for i in range(4)),0)
 def onspan(u,v,r):
  i,j=next((i,j) for i in range(4) for j in range(i+1,4) if (d:=mul(u[i],v[j],n)^mul(v[i],u[j],n))!=0)
  d=mul(u[i],v[j],n)^mul(v[i],u[j],n)
  a=mul(mul(r[i],v[j],n)^mul(v[i],r[j],n),powr(d,(1<<n)-2,n),n)
  b=mul(mul(u[i],r[j],n)^mul(r[i],u[j],n),powr(d,(1<<n)-2,n),n)
  return all(mul(a,u[k],n)^mul(b,v[k],n)==r[k] for k in range(4))
 coll=set()
 for i in range(len(stars)):
  for j in range(i+1,len(stars)):
   if mix(stars[i],stars[j])!=0 or mix(stars[j],stars[i])!=0:continue
   line=tuple(k for k,r in enumerate(stars) if onspan(stars[i],stars[j],r))
   assert len(line)==5,(hex(A),i,j,len(line),line)
   coll.add(line)
 assert len(coll)==27,(hex(A),len(coll))
 fperm={i:index[canonical(frob(s,n),n,third)] for i,s in enumerate(stars)}
 lc=set(coll);cycles=[]
 while lc:
  l=min(lc);v=l;ncy=0
  while True:
   lc.remove(v);ncy+=1
   v=tuple(sorted(fperm[i] for i in v))
   if v==l:break
   assert v in lc,(v,l)
  cycles.append(ncy)
 return dict(sorted(Counter(cycles).items()))


# The ten representatives are row-packed binary matrices.  Their canonical
# order here is by increasing pair (number of rational points, rational lines).
EXPECTED={
 0x1468:(1120,3,0,3,{1:3,3:4,6:5},{3:5,6:2}),
 0x126b:(420,3,1,3,{1:3,2:1,4:10},{1:1,2:3,4:5}),
 0x1486:(4032,5,0,0,{5:3,10:3},{2:1,5:3,10:1}),
 0x1469:(3360,7,0,1,{1:1,2:1,3:2,6:6},{3:1,6:4}),
 0x126c:(5040,7,1,1,{1:1,4:3,8:4},{1:1,2:1,8:3}),
 0x1249:(420,7,3,7,{1:7,2:19},{1:3,2:12}),
 0x128d:(3360,9,1,0,{2:1,3:1,4:1,12:3},{1:1,4:2,6:1,12:1}),
 0x128c:(1120,9,3,0,{2:3,3:5,6:4},{1:3,2:3,3:4,6:1}),
 0x124a:(1260,11,5,3,{1:3,2:1,4:10},{1:5,2:1,4:5}),
 0x1248:(28,15,15,15,{1:15,2:15},{1:15,2:6})
}

def binary_star_count(A):
 return sum(1 for u in range(1,16)
            if not ((matv(A,(u>>0&1,u>>1&1,u>>2&1,u>>3&1)))))

def invariant(A):
 def bitmul(u,v): return ((u&v).bit_count()&1)
 def val(u,v):return (u&sum(((A>>(4*i+j))&1)<<j for j in range(4) for i in range(4) if u>>i&1)).bit_count()&1
 def form(u):return (sum(bitmul((A>>(4*i))&15,u) * ((u>>i)&1) for i in range(4))&1)
 def matb(u):return sum((bitmul((A>>(4*i))&15,u)<<i) for i in range(4))
 def matbt(u):return sum((sum(((A>>(4*j+i))&1)*((u>>j)&1) for j in range(4))&1)<<i for i in range(4))
 pts=[i for i in range(1,16) if form(i)==0]
 lns={tuple(sorted((u,v,u^v))) for u in range(1,16) for v in range(1,16) if u!=v}
 lcount=sum(1 for u,v,w in lns if u in pts and v in pts and bitmul(matb(u),v)==0 and bitmul(matb(v),u)==0)
 scount=sum(1 for u in pts if matb(u)==matbt(u))
 return (len(pts),lcount,scount)

def swap_add(A,mode,i):
 rows=[(A>>(4*j))&15 for j in range(4)]
 if mode=='s':
  rows[i],rows[i+1]=rows[i+1],rows[i]
  for j in range(4):
   if (rows[j]>>i&1)!=(rows[j]>>(i+1)&1):rows[j]^=(1<<i)|(1<<(i+1))
 elif mode=='t':
  rows[0]^=rows[1]
  for j in range(4):
   if rows[j]>>1&1:rows[j]^=1
 return sum(r<<(4*i) for i,r in enumerate(rows))

def verify():
 invertible={a for a in range(65536) if rank(a)==4}
 assert len(invertible)==20160
 unseen=invertible.copy(); classes=[]
 while unseen:
  start=min(unseen);queue=[start];unseen.remove(start);n=0
  while queue:
   a=queue.pop();n+=1
   for mode,i in [('s',0),('s',1),('s',2),('t',0)]:
    b=swap_add(a,mode,i)
    if b in unseen:unseen.remove(b);queue.append(b)
  classes.append((start,n))
 assert len(classes)==10
 found={a:n for a,n in classes}
 assert set(found)==set(EXPECTED)
 assert sum(found.values())==20160
 for a,(size,np,nl,ns,sc,lc) in EXPECTED.items():
  assert found[a]==size
  assert invariant(a)==(np,nl,ns),(hex(a),invariant(a))
  o=next(x for aa,x in zip(reps,orders) if aa==a)
  actual,pts=spectrum(a,2*o)
  assert actual==sc,(a,actual,sc)
  assert lines(a,pts,2*o)==lc,(a,lines(a,pts,2*o),lc)
  assert sum(k*v for k,v in sc.items())==45
  assert sum(k*v for k,v in lc.items())==27
 print('TEN_BINARY_EXTREMAL_CUBIC_FROBENIUS_SPECTRA_VERIFIED')

if __name__=='__main__':verify()
