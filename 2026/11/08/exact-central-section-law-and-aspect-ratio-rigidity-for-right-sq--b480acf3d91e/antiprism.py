"""Exact Q[t]/(t^4-2) spherical-line arrangement for uniform square antiprism."""
import math,itertools,collections,json
from math import isqrt
D=4
zero=(0,)*D
one=(1,0,0,0)
t=(0,1,0,0)
t2=(0,0,1,0)
def aplus(x,y):return tuple(u+v for u,v in zip(x,y))
def aneg(x):return tuple(-u for u in x)
def aminus(x,y):return aplus(x,aneg(y))
def atimes(x,y):
 z=[0]*7
 for i,p in enumerate(x):
  for j,q in enumerate(y): z[i+j]+=p*q
 for k in (6,5,4):z[k-4]+=2*z[k]
 return tuple(z[:4])
def aval(x):return sum(c*2**(i/4) for i,c in enumerate(x))
def asgn(x):
 if x==zero:return 0
 for q in (10,20,30,50):
  scale=10**q
  low=isqrt(isqrt(2*scale**4))
  # isqrt(isqrt(...)) is floor root4
  assert low**4<=2*scale**4<(low+1)**4
  L=low;U=low+1
  # bounds with common denom scale^3
  den=scale**3
  lo=hi=0
  for k,c in enumerate(x):
   if c>=0:lo+=c*L**k*scale**(3-k);hi+=c*U**k*scale**(3-k)
   else:lo+=c*U**k*scale**(3-k);hi+=c*L**k*scale**(3-k)
  if lo>0:return 1
  if hi<0:return -1
 raise Exception('sign unknown '+str(x))
def vvadd(x,y):return tuple(aplus(p,q) for p,q in zip(x,y))
def vvneg(x):return tuple(aneg(p) for p in x)
def scale(s,x):return x if s>0 else vvneg(x)
def dp(x,y):
 r=zero
 for p,q in zip(x,y):r=aplus(r,atimes(p,q))
 return r
def cp(x,y):return tuple(aminus(atimes(x[(i+1)%3],y[(i+2)%3]),atimes(x[(i+2)%3],y[(i+1)%3])) for i in range(3))
def ez(x):return all(q==zero for q in x)
def nv(x):
 a=[aval(z) for z in x];p=math.sqrt(sum(z*z for z in a));return tuple(z/p for z in a)
# scale physical vertices by 2, z=+/- t where t=2^(1/4)
vertices=[( (2,0,0,0),zero,t),(zero,(2,0,0,0),t),((-2,0,0,0),zero,t),(zero,(-2,0,0,0),t)]
for i,j in itertools.product((-1,1),repeat=2):
 vertices.append((tuple(i*u for u in t2),tuple(j*u for u in t2),aneg(t)))
assert len(vertices)==8
norm=dp(vertices[0],vertices[0]);assert all(dp(v,v)==norm for v in vertices),norm
edges=set()
# top 4, bottom 4, each top to adjacent lower ring (same minimal horizontal separation)
for i,j in itertools.combinations(range(8),2):
 dis=dp(tuple(aminus(p,q) for p,q in zip(vertices[i],vertices[j])),tuple(aminus(p,q) for p,q in zip(vertices[i],vertices[j])))
 if dis==(8,0,0,0):edges.add((i,j))
assert len(edges)==16,(len(edges),edges)
print('VERTICES',vertices,'NORM',norm,'EDGES',sorted(edges),flush=True)

# sorted directions for all 8 great circles, none antipodal
m=len(vertices)
patterns=set()
for i,j in itertools.combinations(range(m),2):
 x0=cp(vertices[i],vertices[j]);assert not ez(x0)
 for h in (-1,1):
  x=scale(h,x0)
  for si,sj in itertools.product((-1,1),repeat=2):
   y=vvadd(scale(si,vertices[i]),scale(sj,vertices[j]))
   pat=[]
   for v in vertices:
    sg=asgn(dp(v,x)) or asgn(dp(v,y)) or asgn(dp(v,(one,tuple(3*c for c in one),tuple(7*c for c in one))))
    assert sg
    pat.append(sg)
   patterns.add(tuple(pat))
assert len(patterns)==58
print('PATTERNS',len(patterns),flush=True)

rays=[]
for i,j in itertools.combinations(range(m),2):
 x=cp(vertices[i],vertices[j])
 for h in (-1,1):
  q=scale(h,x)
  if not any(ez(cp(q,z)) and asgn(dp(q,z))>0 for z in rays):rays.append(q)
assert len(rays)==56
assert all(asgn(dp(vertices[i],cp(vertices[j],vertices[k])))!=0 for i,j,k in itertools.combinations(range(m),3))
print('DISTINCT RAYS',len(rays),flush=True)

def rcross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])

cells=[]
for pat in sorted(patterns):
 on=[x for x in rays if all(s*asgn(dp(v,x))>=0 for s,v in zip(pat,vertices))]
 assert len(on)>=3,(pat,len(on))
 xyz=[nv(x) for x in on]
 mid=[sum(q[i] for q in xyz) for i in range(3)]
 mid=[t/math.sqrt(sum(z*z for z in mid)) for t in mid]
 a=[xyz[0][i]-sum(x*y for x,y in zip(xyz[0],mid))*mid[i] for i in range(3)]
 a=[t/math.sqrt(sum(z*z for z in a)) for t in a]
 b=rcross(mid,a)
 order=sorted(range(len(on)),key=lambda i:math.atan2(sum(x*y for x,y in zip(xyz[i],b)),sum(x*y for x,y in zip(xyz[i],a))))
 on=[on[i] for i in order]
 line=[]
 for x,y in zip(on,on[1:]+on[:1]):
  inds=[i for i,v in enumerate(vertices) if dp(v,x)==zero and dp(v,y)==zero]
  assert len(inds)==1,(len(on),inds)
  line.append(inds[0])
 angles=[]
 for i in range(len(on)):
  a,b=line[i-1],line[i]
  assert a!=b
  cos= -pat[a]*pat[b]*aval(dp(vertices[a],vertices[b])) / aval(norm)
  angles.append(math.acos(max(-1,min(1,cos))))
 area=sum(angles)-(len(on)-2)*math.pi
 assert area>1e-10,(pat,area,len(on))
 count=sum(pat[i]*pat[j]<0 for i,j in edges)
 cells.append((pat,area,count,on,line))
print('TOTAL',sum(c[1] for c in cells), '4PI',4*math.pi)
counts=collections.Counter(c[2] for c in cells)
areas=collections.defaultdict(float)
for c in cells:areas[c[2]]+=c[1]
assert counts=={6:24,8:34},counts
print('SPECTRUM')
for k in sorted(counts):print(k,counts[k],areas[k]/(4*math.pi))
print('POLYGONS IN ARRANGEMENT',collections.Counter(len(c[3]) for c in cells))
# Exact symbolic expression: A_m= sum over cell vertices arccos(-sign sign dot/norm) - sum (vertices-2)pi
# coefficient grouped by each distinct arccos algebraic expression pair
res={}
for k in sorted(counts):
 terms=collections.Counter()
 for pat,area,count,on,line in cells:
  if count!=k:continue
  terms['pi']-=len(on)-2
  for i in range(len(on)):
   a,b=line[i-1],line[i]
   arg=tuple(-pat[a]*pat[b]*z for z in dp(vertices[a],vertices[b]))
   terms[arg]+=1
 res[k]={'regions':counts[k],'probability':areas[k]/(4*math.pi),'arc_terms':{str(t):c for t,c in terms.items() if c}}
 print('EXACT TERMS',k,terms)
# Validate exhaustive whole sphere via combinatorial region formula for great circles with multi-intersections:
# R=2+sum_over_undirected_lines (t_i?); sphere cell=2 + sum_at_v (multiplicity(v)-1) for all vertices
# Explanation: add each circle, number new regions equals number distinct crossings with previous circles (or 1 first).
# Euler V-E+F=2, E=sum at each vertex degree 2*m/2? great-circle total edges sum_{v} m(v), F=2+sum(m(v)-1).
incident=[]
for x in rays:
 k=sum(dp(x,v)==zero for v in vertices)
 incident.append(k)
assert 2+sum(k-1 for k in incident)==len(cells),(len(cells),2+sum(k-1 for k in incident))
print('EXACT_SECTION_CHECK_OK')
