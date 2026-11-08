"""Independent finite-extension verification of the symmetrized matrix product."""
import itertools, random
q=9

def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def neg(a): return ((-a%3)%3)+3*((-(a//3))%3)
def mul(a,b):
  x,y=a%3,a//3; u,v=b%3,b//3
  return ((x*u+2*y*v)%3)+3*((x*v+y*u)%3)
def inv(a):
  assert a
  return next(b for b in range(1,9) if mul(a,b)==1)
def mm(A,B):
  a,b,c,d=A; e,f,g,h=B
  return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))
def prod(A,B): return tuple(add(x,y) for x,y in zip(mm(A,B),mm(B,A)))
def rank(mat):
  M=[row[:] for row in mat];r=0
  for j in range(len(M[0])):
    pick=next((t for t in range(r,len(M)) if M[t][j]),None)
    if pick is None:continue
    M[r],M[pick]=M[pick],M[r]
    t=inv(M[r][j]);M[r]=[mul(t,z) for z in M[r]]
    for k in range(len(M)):
      if k!=r and M[k][j]:
        v=M[k][j];M[k]=[add(x,neg(mul(v,y))) for x,y in zip(M[k],M[r])]
    r+=1
    if r==len(M):break
  return r

def expect(C):
  a,b,c,d=C
  scalar= b==0 and c==0 and a==d
  eig=zero=0
  lines=[(1,t) for t in range(q)]+[(0,1)]
  for x,y in lines:
    xx=add(mul(a,x),mul(b,y));yy=add(mul(c,x),mul(d,y))
    if add(mul(xx,y),neg(mul(x,yy)))==0:
      eig+=1
      if xx==0 and yy==0:zero+=1
  U=(q-1)*q*(q*q-q-1)
  H=q**3-1 if scalar else q-1
  return U+q*(q-1)*(q+1-eig+q*zero)+q*q*H+(q**4 if C==(0,0,0,0) else 0)

mats=list(itertools.product(range(q),repeat=4))
basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
rng=random.Random(436214)
targets=[(0,0,0,0),(1,0,0,1),(0,1,0,0),(1,0,0,0),(1,0,0,2),(1,1,0,1),(0,1,1,0)]
targets+=rng.sample(mats,15)
for C in targets:
  count=0
  for A in mats:
    cols=[prod(A,E) for E in basis]
    M=[[cols[j][i] for j in range(4)] for i in range(4)]
    r=rank(M)
    ext=[M[i]+[C[i]] for i in range(4)]
    if rank(ext)==r:count+=q**(4-r)
  assert count==expect(C),(C,count,expect(C))
print('q=9 verified_targets',len(targets),'all 6561 first factors per target','EXTENSION_FIELD_CHECK_PASS')
