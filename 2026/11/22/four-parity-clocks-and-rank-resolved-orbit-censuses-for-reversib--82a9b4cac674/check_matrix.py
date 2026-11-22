import itertools

def rank(rows,n):
 pivots={}
 for x in rows:
  while x:
   k=x.bit_length()-1
   if k in pivots:x^=pivots[k]
   else:pivots[k]=x;break
 return len(pivots)

def mul(a,b,n):
 return [__import__('functools').reduce(lambda z,j:z^b[j],(j for j in range(n) if row>>j & 1),0) for row in a]

def eye(n):return [1<<i for i in range(n)]
def build_A(B):
 v=len(B)
 return [sum(((b>>j)&1)<<(v+j) for j in range(v)) for b in B] + [sum(((B[i]>>j)&1)<<i for i in range(v)) for j in range(v)]
def build_T(A):
 n=len(A)
 return [A[i]^(1<<(i+n)) for i in range(n)] + [1<<i for i in range(n)]
def expected(v,k,l,rho,t):
 b1=min(2, t&-t);b2=min(4,t&-t); c= (2*min(2,t&-t) if t%3==0 else 0)
 if k%2==0 and l%2==0:return 2*rho*b2+(2*v-4*rho)*b1
 if k%2==1 and l%2==0:return v*c
 if k%2==0 and l%2==1:return 2*b1+(v-1)*c
 return c+2*(rho-1)*b2+(2*v+2-4*rho)*b1

def verify(name,B):
 v=len(B); k=B[0].bit_count(); l=(B[0]&B[1]).bit_count()
 assert 1<k<v
 assert all(x.bit_count()==k for x in B)
 assert all((x&y).bit_count()==l for i,x in enumerate(B) for j,y in enumerate(B) if i<j)
 assert all(sum((x>>j)&1 for x in B)==k for j in range(v))
 rho=rank(B,v)
 A=build_A(B);T=build_T(A);n=4*v
 P=eye(n)
 outcome=[]
 for t in range(1,13):
  P=mul(P,T,n)
  null=n-rank([P[i]^(1<<i) for i in range(n)],n)
  exp=expected(v,k,l,rho,t)
  assert null==exp,(name,t,null,exp)
  outcome.append((t,null))
 order=next(t for t,cnt in outcome if cnt==n)
 pred={(0,0):4,(1,0):6,(0,1):6,(1,1):12}[(k%2,l%2)]
 assert order==pred,(name,order,pred)
 print(name, 'v,k,l,rho',v,k,l,rho,'order',order,'dims',outcome)

B3=[sum((i!=j)<<j for j in range(3)) for i in range(3)]
B4=[sum((i!=j)<<j for j in range(4)) for i in range(4)]
Bf=[sum(((i&j).bit_count()%2==0)<<(j-1) for j in range(1,8)) for i in range(1,8)]
Bcomp=[x^((1<<7)-1) for x in Bf]
D={1,3,4,5,9}; B11=[sum((((i-j)%11 in D))<<j for j in range(11)) for i in range(11)]
B15=[sum(((i&j).bit_count()%2==0)<<(j-1) for j in range(1,16)) for i in range(1,16)]
for nm,B in [('3-2-1',B3),('4-3-2',B4),('Fano',Bf),('complement-Fano',Bcomp),('Paley-11',B11),('PG3,2',B15)]:verify(nm,B)
