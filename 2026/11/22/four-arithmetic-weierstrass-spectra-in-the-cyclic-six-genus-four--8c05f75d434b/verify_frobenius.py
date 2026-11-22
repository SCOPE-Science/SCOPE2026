from collections import Counter

def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def add(a,b,p):
 return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])
def sub(a,b,p):
 return trim([((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p for i in range(max(len(a),len(b)))])
def mul(a,b,p):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
 return trim(c)
def rem(a,b,p):
 a=trim(a[:]); b=trim(b[:]);inv=pow(b[-1],-1,p)
 while len(a)>=len(b) and a!=[0]:
  k=len(a)-len(b);u=a[-1]*inv%p
  for i,z in enumerate(b):a[k+i]=(a[k+i]-u*z)%p
  trim(a)
 return a
def gcd(a,b,p):
 while b!=[0]:a,b=b,rem(a,b,p)
 return [(v*pow(a[-1],-1,p))%p for v in a]
def powmod(a,e,f,p):
 r=[1]
 while e:
  if e&1:r=rem(mul(r,a,p),f,p)
  a=rem(mul(a,a,p),f,p);e>>=1
 return r
def branches_spectrum(p,a,b):
 # x^10 + x^7 + a*x^4 + b*x
 f=[0]*(11);f[10]=1;f[7]=1;f[4]=a;f[1]=b
 df=[(i*f[i])%p for i in range(1,len(f))]
 if len(gcd(f,trim(df),p))>1:return None
 fix={0:0};xp=[0,1]
 for i in range(1,11):
  xp=powmod(xp,p,f,p)
  fix[i]=len(gcd(f,sub(xp,[0,1],p),p))-1
 cycles={}
 for i in range(1,11):
  n=fix[i]-sum(d*cycles[d] for d in cycles if i%d==0)
  assert n%i==0,(p,a,b,i,n)
  if n: cycles[i]=n//i
 assert sum(d*c for d,c in cycles.items())==10
 return tuple(sorted(cycles.items()))

def expected(p):
 return {((1,4),(2,3)):(p*p-6*p+11)//6,
 ((1,2),(2,4)):(p*p-4*p+7)//6,
 ((1,2),(2,1),(6,1)):(p-2)*(p+1)//3,
 ((1,1),(3,1),(6,1)):(p*p-1)//3}
for p in [5,11,17,23,29,41]:
 ct=Counter()
 for a in range(p):
  for b in range(p):
   s=branches_spectrum(p,a,b)
   if s:ct[s]+=1
 print(p,'actual',dict(ct),'expected',expected(p), 'PASS' if dict(ct)==expected(p) else 'FAIL')
 assert dict(ct)==expected(p)
print('CUBIC_BRANCH_SPECTRA_VERIFIED')
