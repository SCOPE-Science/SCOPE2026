from itertools import product
Q=1009
I=next(x for x in range(1,Q) if x*x%Q==Q-1)
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for j,x in enumerate(a):
  for k,y in enumerate(b):c[j+k]=(c[j+k]+x*y)%Q
 return c
def rank(A):
 A=[list(row) for row in A]
 if not A:return 0
 n=len(A);k=len(A[0]);v=0
 for j in range(k):
  i=next((i for i in range(v,n) if A[i][j]%Q),None)
  if i is None: continue
  A[v],A[i]=A[i],A[v]
  p=pow(A[v][j],-1,Q);A[v]=[(x*p)%Q for x in A[v]]
  for i in range(v+1,n):
   if A[i][j]:
    f=A[i][j]
    A[i]=[(x-f*y)%Q for x,y in zip(A[i],A[v])]
  v+=1
  if v==n: break
 return v

def polyrank(P,d):
 u=[0]*(len(P));v=[0]*len(P)
 for j,c in enumerate(P):u[j]=(I*c)%Q;v[j]=(-I*c)%Q
 u[1]=(u[1]+1)%Q;v[1]=(v[1]+1)%Q
 U=[[1]];V=[[1]]
 for j in range(d):U.append(mul(U[-1],u));V.append(mul(V[-1],v))
 n=2*(len(P)-1)*d+1
 cols=[]
 for j,k in product(range(d+1),repeat=2):
  w=mul(U[j],V[k]);cols.append(w+[0]*(n-len(w)))
 return rank(list(zip(*cols)))

for m in range(2,7):
 P=[(2*j+3)%13 for j in range(m)]+[1]
 for d in range(0,9):
  actual=polyrank(P,d);want=(d+1)**2-max(0,d-m+1)**2
  assert actual==want,(m,d,actual,want)
print('GRAPH_PROFILE_RANK_PASS 45')
for m,d in [(3,2),(3,3),(4,3),(5,4)]:
    P=[(2*j+3)%13 for j in range(m)]+[1]
    D=(d+1)**2-max(0,d-m+1)**2
    rows=[]
    for t in range(D):
        pp=sum(c*pow(t,j,Q) for j,c in enumerate(P))%Q
        u=(t+I*pp)%Q
        v=(t-I*pp)%Q
        rows.append([pow(u,j,Q)*pow(v,k,Q)%Q for j,k in product(range(d+1),repeat=2)])
    assert rank(rows)==D,(m,d)
print('GRAPH_FINITE_SAMPLING_PASS 4')
