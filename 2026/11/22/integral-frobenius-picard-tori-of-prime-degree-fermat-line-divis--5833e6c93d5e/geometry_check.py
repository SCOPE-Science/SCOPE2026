from itertools import combinations, product
from collections import Counter, defaultdict
p=11
r=next(a for a in range(2,p) if pow(a,5,p)==1 and a!=1)
roots=[(-pow(r,a,p))%p for a in range(5)]
pairs=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for label, pairing in enumerate(pairs):
 for i,j in product(range(5),repeat=2):
  u=[0]*4;v=[0]*4
  (a,b),(c,d)=pairing
  u[b]=1;u[a]=roots[i];v[d]=1;v[c]=roots[j]
  lines.append((label,i,j,u,v))
def rref(M):
 M=[list(row) for row in M]; rows=len(M);cols=len(M[0]); piv=[];k=0
 for c in range(cols):
  nxt=next((i for i in range(k,rows) if M[i][c]%p),None)
  if nxt is None:continue
  M[k],M[nxt]=M[nxt],M[k]
  z=pow(M[k][c],-1,p); M[k]=[z*x%p for x in M[k]]
  for i in range(rows):
   if i!=k and M[i][c]%p:
    z=M[i][c];M[i]=[(a-z*b)%p for a,b in zip(M[i],M[k])]
  piv.append(c);k+=1
  if k==rows:break
 return M,piv
def nullvec(M):
 R,pivs=rref(M);free=next((j for j in range(4) if j not in pivs),None)
 if free is None:return None
 v=[0]*4;v[free]=1
 for i,c in enumerate(pivs):v[c]=(-R[i][free])%p
 return v
pts=defaultdict(set)
edge_counts=Counter()
for i,j in combinations(range(75),2):
 li,lj=lines[i],lines[j]
 u,v=li[3:];x,y=lj[3:]
 M=[[u[k],v[k],-x[k],-y[k]] for k in range(4)]
 nv=nullvec(M)
 if nv is None:continue
 pt=tuple((nv[0]*u[k]+nv[1]*v[k])%p for k in range(4))
 first=next(k for k,a in enumerate(pt) if a)
 pt=tuple((a*pow(pt[first],-1,p))%p for a in pt)
 pts[pt].update((i,j));edge_counts[(li[0],lj[0])]+=1
print('p',p,'r',r,'roots',roots,'edges',sum(edge_counts.values()),'edge kinds',edge_counts)
print('number points',len(pts),'multiplicity',Counter(map(len,pts.values())))
print('triple?',[(k,v) for k,v in pts.items() if len(v) not in (2,5)][:3])
print('P5 count by pairing',Counter(next(iter({lines[z][0] for z in v})) for v in pts.values() if len(v)==5))

# Explicit certificate assertions (not simply a printed census).
assert len(lines)==75
assert len(pts)==405
assert Counter(map(len,pts.values()))==Counter({2:375,5:30})
assert sum(edge_counts.values())==675
assert sorted(edge_counts.values())==[100,100,100,125,125,125]
for t,s in ((0,1),(0,2),(1,2)):
    for a,b,c in product(range(5),repeat=3):
        e=((b+c-a) if (t,s)==(0,1) else (c-a-b) if (t,s)==(0,2) else (a+b-c))%5
        la=lines[25*t+5*a+b];lb=lines[25*s+5*c+e]
        M=[[la[3][j],la[4][j],-lb[3][j],-lb[4][j]] for j in range(4)]
        assert len(rref(M)[1])<4
print('FERMAT_GEOMETRY_VERIFIED')
