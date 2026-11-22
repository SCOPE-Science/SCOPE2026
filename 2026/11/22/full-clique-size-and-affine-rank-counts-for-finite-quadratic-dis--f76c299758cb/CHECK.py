from itertools import product

def chi(a,q):
 a%=q
 return 0 if a==0 else (1 if pow(a,(q-1)//2,q)==1 else -1)
def og(n,delta,q):
 if n==0:return 1
 if n%2:
  s=n//2
  out=2*q**(s*s)
  for j in range(1,s+1):out*=q**(2*j)-1
  return out
 s=n//2
 sig=chi((-1)**s*delta,q)
 out=2*q**(s*(s-1))*(q**s-sig)
 for j in range(1,s):out*=q**(2*j)-1
 return out

def model(q,d,r,a):
 k=r-1
 if r%q!=0:
  if d<k:return (0,0)
  det=(pow(a*pow(2,-1,q),k,q)*r)%q
  m=d-k
  if m==0 and chi(det,q)!=1:return (0,0)
  e=og(d,1,q)//og(m,pow(det,-1,q),q)
  return (q**d*e,0)
 else:
  if d<k-1:return (0,0)
  h=k-1; det=(pow(a*pow(2,-1,q),h,q)*k)%q
  m=d-h
  if m==0 and chi(det,q)!=1:return (0,0)
  de=pow(det,-1,q)
  e=og(d,1,q)//og(m,de,q)
  if m==0:z=1
  elif m%2:z=q**(m-1)
  else:z=q**(m-1)+(q-1)*q**(m//2-1)*chi((-1)**(m//2)*de,q)
  return (q**d*e*z,q**d*e)

def brute(q,d,r,a):
 vec=list(product(range(q),repeat=d))
 qnorm=lambda v:sum(t*t for t in v)%q
 vs=[v for v in vec if qnorm(v)==a]
 diff=lambda v,w:sum((x-y)**2 for x,y in zip(v,w))%q
 paths=[tuple()]
 for _ in range(r-1):
  paths=[seq+(v,) for seq in paths for v in vs if all(diff(v,u)==a for u in seq)]
 def rank(l):
  a=[list(v) for v in l]; n=len(a); c=0; p=0
  while c<d and p<n:
   z=next((j for j in range(p,n) if a[j][c]%q),None)
   if z is None:c+=1;continue
   a[z],a[p]=a[p],a[z]; inv=pow(a[p][c],-1,q)
   a[p]=[(e*inv)%q for e in a[p]]
   for j in range(n):
    if j!=p:
     t=a[j][c];a[j]=[(e-t*f)%q for e,f in zip(a[j],a[p])]
   p+=1;c+=1
  return p
 dep=sum(rank(seq)<len(seq) for seq in paths)
 return (q**d*len(paths),q**d*dep)

if __name__=='__main__':
 c=0
 for q in (3,5,7):
  for d in range(1,5 if q==3 else 4):
   for r in range(2, min(6,d+3)):
    for a in range(1,q):
     if q**(d*(min(r-1,d)))>10000000:continue
     x=model(q,d,r,a);y=brute(q,d,r,a)
     if x!=y:
      print('FAIL',q,d,r,a,x,y);raise SystemExit(1)
     c+=1
 print('EQUILATERAL_COUNT_OK',c)

# Extension-field check: F_9=F_3[t]/(t^2+1). This block runs only under
# explicitly supplied command line flag and is otherwise unused.
def gf9_trials():
    def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
    def neg(x):return (-x%3)+3*((-(x//3))%3)
    def sub(x,y):return add(x,neg(y))
    def mul(x,y):
        a,b=x%3,x//3;c,d=y%3,y//3
        return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
    def pow9(a,n):
        v=1
        while n:
            if n&1:v=mul(v,a)
            a=mul(a,a);n//=2
        return v
    def chi9(x):return 1 if pow9(x,4)==1 else -1
    def qsum(v):
        t=0
        for x in v:t=add(t,mul(x,x))
        return t
    def diff(v,w):return qsum([sub(x,y) for x,y in zip(v,w)])
    cases=0
    for d in (2,3):
        vv=list(product(range(9),repeat=d))
        for a in range(1,9):
            v1=[v for v in vv if qsum(v)==a]
            cnt=0;dep=0
            for u in v1:
                for v in v1:
                    if diff(u,v)!=a:continue
                    cnt+=1
                    # In characteristic three the pair is dependent exactly
                    # when the second vector is minus the first.
                    if v==tuple(neg(x) for x in u):dep+=1
            if d==2:
                exp=8;dp=8
            else:
                split=chi9(mul(neg(1),a))==1
                # discriminant of orthogonal complement = 1/a.
                exp=(90*17 if split else 72)
                dp=90 if split else 72
            if (cnt,dep)!=(exp,dp):
                raise AssertionError((d,a,cnt,dep,exp,dp))
            cases+=1
    return cases
if __name__=='__main__':
    print('EXTENSION_FIELD_F9_OK',gf9_trials())
