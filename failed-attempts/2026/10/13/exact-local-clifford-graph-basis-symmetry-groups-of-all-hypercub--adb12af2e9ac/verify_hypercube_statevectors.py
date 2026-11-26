"""Direct statevector check of graph-basis permutations for the full 2-, 4-, and 8-qubit hypercube basis."""
from math import sqrt
from itertools import product

I=((1+0j,0j),(0j,1+0j))
H=((1/sqrt(2),1/sqrt(2)),(1/sqrt(2),-1/sqrt(2)))
S=((1+0j,0j),(0j,1j))

def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def bm(A,B):return tuple(tuple((sum(A[i][k]*B[k][j] for k in range(2))%2) for j in range(2)) for i in range(2))
MI=((1,0),(0,1));MH=((0,1),(1,0));MS=((1,0),(1,1))
rep={MI:I};front=[MI]
for m in front:
 for mgen,ugen in ((MH,H),(MS,S)):
  t=bm(mgen,m)
  if t not in rep:rep[t]=mm(ugen,rep[m]);front.append(t)
assert len(rep)==6

def graphpsi(d):
 n=1<<d;lenstate=1<<n;out=[0]*lenstate
 for x in range(lenstate):
  k=0
  for i in range(n):
   for b in range(d):
    j=i^(1<<b)
    if i<j:k+=(x>>i&1)*(x>>j&1)
  out[x]=(-1 if k%2 else 1)/sqrt(lenstate)
 return out

def apply(U,vec,qubit):
 out=vec[:];sh=1<<qubit
 for i in range(0,len(vec),sh<<1):
  for j in range(i,i+sh):
   x=vec[j];y=vec[j+sh]
   out[j]=U[0][0]*x+U[0][1]*y
   out[j+sh]=U[1][0]*x+U[1][1]*y
 return out

def walsh(v):
 out=v[:];h=1
 while h<len(out):
  for b in range(0,len(out),2*h):
   for j in range(b,b+h):
    a=out[j];c=out[j+h]
    out[j]=a+c;out[j+h]=a-c
  h*=2
 return out

tests=0
for d in (1,2,3):
 n=1<<d;g=graphpsi(d)
 for ae,ao,be,bo in product((0,1),repeat=4):
  if ((ae*ao)^((d%2)*be*bo))!=1:continue
  even=((ae,be),((d%2)*bo,ao))
  odd=((ao,bo),((d%2)*be,ae))
  assert even in rep and odd in rep
  gates=[rep[even if i.bit_count()%2==0 else odd] for i in range(n)]
  for label in range(1<<n):
   vec=[g[x]*(-1 if (x&label).bit_count()%2 else 1) for x in range(1<<n)]
   for qubit,U in enumerate(gates): vec=apply(U,vec,qubit)
   spectrum=walsh([g[x].conjugate()*vec[x] for x in range(1<<n)])
   matches=[i for i,c in enumerate(spectrum) if abs(abs(c)-1)<1e-8]
   assert len(matches)==1 and all(abs(c)<1e-8 for i,c in enumerate(spectrum) if i!=matches[0]),(d,even,odd,label)
   tests+=1
 print('d',d,'graph basis dimension',1<<n,'tested every label')
print('STATEVECTOR_VERIFY_OK',tests,'individual basis permutations')
