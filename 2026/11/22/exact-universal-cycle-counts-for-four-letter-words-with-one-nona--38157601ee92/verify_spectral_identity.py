# Independent modular evaluations of the complete Laplacian determinant identity.
from itertools import product

def detmod(A,p):
 B=[[v%p for v in row] for row in A];n=len(B);out=1
 for i in range(n):
  k=next((j for j in range(i,n) if B[j][i]),None)
  if k is None:return 0
  if k!=i:B[i],B[k]=B[k],B[i];out=-out
  d=B[i][i];out=out*d%p;inv=pow(d,-1,p)
  for j in range(i+1,n):
   if B[j][i]:
    c=B[j][i]*inv%p
    for k in range(i+1,n):B[j][k]=(B[j][k]-c*B[i][k])%p
 return out%p

def graph(q):
 E=[w for w in product(range(q),repeat=4) if len(set(w))==3 and (w[0]==w[2] or w[1]==w[3] or w[0]==w[3])]
 V=sorted(set(w[:3] for w in E)|set(w[1:] for w in E)); pos={v:i for i,v in enumerate(V)}
 L=[[0]*len(V) for i in V]
 for w in E:
  a,b=pos[w[:3]],pos[w[1:]];L[a][a]+=1;L[a][b]-=1
 return L
for q in (4,5):
 L=graph(q);m=q*(q-1);n=q*(q-1)*(q-2)
 ds=q*(q-3)//2;da=(q-1)*(q-2)//2
 for t in (1,2,3):
  s=t+2;D=s**3-1; beta=q-2;alpha=(t+beta)*D+s*s+s
  C=(t+beta)*D-beta*(s*s+s+1)
  Delta=(alpha-s*s*(q-1))*(alpha-s*(q-1))-(s*s-beta)*(s-beta)
  for p in (1000000007,998244353):
   l=detmod([[L[i][j]+(t if i==j else 0) for j in range(len(L))] for i in range(len(L))],p)
   r=pow(D,n//3-m,p)*C*pow(alpha-beta,ds,p)*pow(alpha+beta,da,p)*pow(Delta,q-1,p)%p
   assert l==r,(q,t,p,l,r)
 print('spectral modular checks q=', q, 'OK')

print("SPECTRAL_IDENTITY_VERIFY_OK")
