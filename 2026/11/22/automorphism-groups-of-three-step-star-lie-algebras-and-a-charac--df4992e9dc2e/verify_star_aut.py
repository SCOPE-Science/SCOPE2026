"""Finite-field checks of automorphisms of three-step star Lie algebras."""
import itertools,random,math

def rank(M,p):
 A=[list(map(lambda x:x%p,row)) for row in M]
 r=0
 for j in range(len(A[0])):
  piv=next((i for i in range(r,len(A)) if A[i][j]),None)
  if piv is None:continue
  A[r],A[piv]=A[piv],A[r]
  t=pow(A[r][j],-1,p);A[r]=[(v*t)%p for v in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:
    z=A[i][j];A[i]=[(a-z*b)%p for a,b in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r

def m_conditions(M,p):
 m=len(M)
 return all(2*M[i][k]*M[j][k]%p==0 for i in range(m) for j in range(i+1,m) for k in range(m))

def c_kernel_dimension(m,p):
 pairs=list(itertools.combinations(range(m),2))
 rows=[]
 for i,j in pairs:
  for a,b in pairs:
   row=[0]*(m*m)
   # [u_i + sum_k c_ki a_k, u_j + sum_k c_kj a_k]
   # coefficient: c_{a,j} if i=b; c_{b,j} if i=a; -c_{a,i} if j=b; -c_{b,i} if j=a.
   if i==a: row[b*m+j]+=1
   if i==b: row[a*m+j]+=1
   if j==a: row[b*m+i]-=1
   if j==b: row[a*m+i]-=1
   rows.append(row)
 return m*m-rank(rows,p)

def make_bracket(m,p):
 w=list(itertools.combinations(range(m),2)); n=1+2*m+len(w)
 def bracket(x,y):
  ans=[0]*n
  for i in range(m):
   ans[1+m+i]=(ans[1+m+i]+x[0]*y[1+i]-y[0]*x[1+i])%p
  for k,(i,j) in enumerate(w):
   ans[1+2*m+k]=(x[1+i]*y[1+m+j]+x[1+j]*y[1+m+i]-y[1+i]*x[1+m+j]-y[1+j]*x[1+m+i])%p
  return ans
 return bracket,n

def test_lift(m,p,M,lam,t,ch,cs,Z):
 bracket,n=make_bracket(m,p)
 basis=[[int(i==j) for i in range(n)] for j in range(n)]
 w=n-1-2*m
 # define generator h,u_i, derive a_i and w_ij
 H=[0]*n;H[0]=lam
 for i in range(m):H[1+i]=t[i];H[1+m+i]=ch[i]
 for k in range(w):H[1+2*m+k]=Z[0][k]
 U=[]
 for i in range(m):
  z=[0]*n
  for j in range(m):z[1+j]=M[j][i];z[1+m+j]=cs[j][i]
  for k in range(w):z[1+2*m+k]=Z[1+i][k]
  U.append(z)
 A=[bracket(H,u) for u in U]
 W=[bracket(U[i],A[j]) for i,j in itertools.combinations(range(m),2)]
 images=[H]+U+A+W
 assert rank(list(map(list,zip(*images))),p)==n
 for i in range(n):
  for j in range(n):
   lhs=bracket(images[i],images[j]); rhs=[0]*n
   for k,v in enumerate(bracket(basis[i],basis[j])):
    if v:
     rhs=[(a+v*b)%p for a,b in zip(rhs,images[k])]
   assert lhs==rhs,(m,p,i,j,lhs,rhs)

rng=random.Random(12347)
for p in (2,3,5):
 for m in (3,4):
  if m==4 and p==5:continue
  kdim=c_kernel_dimension(m,p)
  assert kdim==1,(p,m,kdim)
  for _ in range(30):
   if p==2:
    while True:
     M=[[rng.randrange(p) for j in range(m)] for i in range(m)]
     if rank(M,p)==m:break
   else:
    perm=list(range(m));rng.shuffle(perm)
    M=[[0]*m for i in range(m)]
    for j in range(m):M[perm[j]][j]=rng.randrange(1,p)
   c=rng.randrange(p);Cs=[[c*M[i][j] for j in range(m)] for i in range(m)]
   w=m*(m-1)//2
   test_lift(m,p,M,rng.randrange(1,p),[0 for _ in range(m)],
             [0 for _ in range(m)],Cs,[[rng.randrange(p) for _ in range(w)] for _ in range(m+1)])
  print('test_lift_ok',p,m,'kernel_C_dimension',kdim)
for p in (2,3):
 m=3; invertible=0;admissible=0
 for vals in itertools.product(range(p),repeat=m*m):
  M=[vals[i*m:(i+1)*m] for i in range(m)]
  if rank(M,p)==m:
   invertible+=1
   admissible+=int(m_conditions(M,p))
 expected=math.factorial(m)*(p-1)**m if p%2 else math.prod(p**m-p**i for i in range(m))
 assert admissible==expected,(p,invertible,admissible,expected)
 print('GL_and_admissible',p,invertible,admissible)
print('STAR_AUTOMORPHISM_GROUP_OK')
