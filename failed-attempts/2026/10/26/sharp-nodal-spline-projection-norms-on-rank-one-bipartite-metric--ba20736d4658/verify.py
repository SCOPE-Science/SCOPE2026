from fractions import Fraction as F
from itertools import product

def inv(A):
 n=len(A)
 X=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
 for k in range(n):
  piv=next(j for j in range(k,n) if X[j][k]);X[k],X[piv]=X[piv],X[k]
  h=X[k][k];X[k]=[v/h for v in X[k]]
  for i in range(n):
   if i!=k:
    h=X[i][k];X[i]=[X[i][j]-h*X[k][j] for j in range(2*n)]
 return [x[n:] for x in X]

def intabs(u,v):
 if u*v>=0:return (abs(u)+abs(v))/2
 return (u*u+v*v)/(2*(abs(u)+abs(v)))

cnt=0
for a in range(2,6):
 for b in range(2,6):
  for uu in (tuple([1]*a),tuple(range(1,a+1)),tuple(range(a,0,-1))):
   for vv in (tuple([1]*b),tuple(range(1,b+1)),tuple(range(b,0,-1))):
    U=sum(uu);V=sum(vv);n=a+b
    E=[(i,a+j,F(uu[i]*vv[j])) for i in range(a) for j in range(b)]
    M=[[F() for _ in range(n)] for _ in range(n)]
    for i,j,l in E:
     M[i][i]+=l/3;M[j][j]+=l/3;M[i][j]+=l/6;M[j][i]+=l/6
    I=inv(M)
    norm=[sum((l*intabs(I[k][i],I[k][j]) for i,j,l in E),F()) for k in range(n)]
    expected=[F(7,3)-F(4,3)*F(uu[i],U)/(1+F(uu[i],U)) for i in range(a)] + [F(7,3)-F(4,3)*F(vv[j],V)/(1+F(vv[j],V)) for j in range(b)]
    assert norm==expected,(uu,vv,norm,expected)
    cnt+=1
print('exact weighted bipartite graph families checked:',cnt)
