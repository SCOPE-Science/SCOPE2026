from fractions import Fraction
MOD={2:0b111,4:0b10011,6:0b1000011}
def mul(a,b,n):
 m=MOD[n];r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&(1<<n):a^=m
 return r

def poww(a,k,n):
 b=1
 while k:
  if k&1:b=mul(b,a,n)
  a=mul(a,a,n);k>>=1
 return b

def count(f,n):
 q=1<<n;t=1
 for x in range(q):
  val=1
  for c in reversed(f):val=mul(val,x,n)^c # f monic: initial 1 then a6 ... a0
  if val==0:t+=1
  elif poww(val,(q-1)//3,n)==1:t+=3
 return t

def rank_points(f):
 s=[0]*7
 for n in range(1,7):
  t=count(f,n) if n%2==0 else (1<<n)+1
  s[n]=(1<<n)+1-t
 c=[1]
 for n in range(1,7):
  z=-sum(c[n-i]*s[i] for i in range(1,n+1))
  assert z%n==0,(n,z)
  c.append(z//n)
 return max((i for i,v in enumerate(c) if v%2),default=-1),c,s

for kind,f in [('rank0',(1,1,0,0,0,0,0)),('rank2',(0,1,0,0,0,0,1)),('rank4',(0,1,0,1,0,0,1))]:
 r,c,s=rank_points(f)
 print(kind,'p-rank via point counts:',r,'c0..6:',c,'power sums:',s)
 assert int(kind[-1])==r
print('POINTCOUNT_CHECKS_PASSED')
