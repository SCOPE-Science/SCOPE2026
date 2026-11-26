from pathlib import Path
DATA_PATH=Path(__file__).with_name("octchars.json")
import itertools,collections,math,json
# 6 vertices 2*axis + sign 0/1, opposite pair (0,1),(2,3),(4,5)
V=list(range(6)); E=tuple((a,b) for a in V for b in V if a<b and a//2!=b//2)

def cycles(perm):
 seen=set(); cs=[]
 for a in range(len(perm)):
  if a in seen:continue
  cyc=[];b=a
  while b not in seen:seen.add(b);cyc.append(b);b=perm[b]
  cs.append(cyc)
 return cs

def evperm(vper):
 edges_index={e:i for i,e in enumerate(E)}
 return [edges_index[tuple(sorted((vper[a],vper[b])))] for a,b in E]

def determinant(perm,b):
 inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3)); return (-1)**(inv+sum(b))

def signed_type(axes,bits):
 cs=cycles(axes)
 return tuple(sorted((len(c),(-1)**sum(bits[i] for i in c)) for c in cs))

def character(vper,det):
 ep=evperm(vper)
 poly=[1,0,0,0]
 for cyc in cycles(vper):
  v=cyc[0]; ll=len(cyc); fl=0
  for edge in E:
   if v not in edge:continue
   eid=E.index(edge); en=eid
   for _ in range(ll):en=ep[en]
   if en==eid:fl+=1
  factor=[1,0,0,0];
  if ll<=3:factor[ll]=1-fl
  poly=[sum(poly[j]*factor[i-j] for j in range(i+1)) for i in range(4)]
 for cyc in cycles(ep):
  ll=len(cyc)
  p2=[0,0,0,0]
  for i in range(4):
   for a in range(4):
    if i+a*ll<=3:p2[i+a*ll]+=poly[i]
  poly=p2
 ec=poly[3]
 # above sign check: for fixed undirected edge, if mapped endpoints orientation reversed negative
 efix=0
 for i,(a,b) in enumerate(E):
  if ep[i]==i:efix+=(1 if vper[a]<vper[b] else -1)
 vfix=sum(vper[i]==i for i in V)
 h1=efix-vfix+1+det
 h2=ec-1+h1
 return ec,efix,vfix,h1,h2
out={}; autom=[]
for p in itertools.permutations(range(3)):
 for b in itertools.product(range(2),repeat=3):
  vp=[2*p[a//2]+((a%2)^b[a//2]) for a in V]
  dt=determinant(p,b)
  key=signed_type(p,b)
  val=character(vp,dt)
  autom.append((vp,key,dt,val))
  if key in out:assert out[key][0]==val
  else:out[key]=(val,0,dt)
  x=out[key];out[key]=(x[0],x[1]+1,dt)
print('classes',len(out),'autos',len(autom))
for k,(v,n,d) in sorted(out.items()):print(k,'size',n,'det',d,'[chi,edge,vert,H1,H2]',v)
print('h2 invariants',sum(n*val[-1] for val,n,d in out.values())/48)
print('h1 invariants',sum(n*val[-2] for val,n,d in out.values())/48)
with open(DATA_PATH,'w') as f:json.dump({'classes':[{'signed_cycles':list(key),'size':n,'det':d,'chi_euler':v[0],'trace_edges':v[1],'trace_vertices':v[2],'chi_H1':v[3],'chi_H2':v[4]} for key,(v,n,d) in sorted(out.items())]},f,indent=2)
# represent four unoriented long diagonals of cube as sign triples with first coordinate +
D=[(1,s,t) for s in (-1,1) for t in (-1,1)]
did={x:i for i,x in enumerate(D)}
chars={
 'S4_trivial':{(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},
 'S4_sign':{(1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1},
 'S4_standard_31':{(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},
 'S4_standard_sign_211':{(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1},
 'S4_22':{(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0},
}
def diagonal_type(g):
 p=[]
 for vec in D:
  im=[None]*3
  for a in range(3):
   v=g[2*a if vec[a]==1 else 2*a+1]
   im[v//2]=1 if v%2==0 else -1
  if im[0]==-1:im=[-c for c in im]
  p.append(did[tuple(im)])
 return tuple(sorted((len(c) for c in cycles(p)),reverse=True))
inner={name:{sgn:0 for sgn in [-1,1]} for name in chars}
for g,k,d,values in autom:
 typ=diagonal_type(g)
 for name,c in chars.items():
  for sgn in [-1,1]: inner[name][sgn]+=values[-1]*c[typ]*(sgn if d==-1 else 1)
print('H2 decomposition',{name:{str(par):v//48 for par,v in zz.items()} for name,zz in inner.items()})
assert all(v%48==0 and v>=0 for zz in inner.values() for v in zz.values())
print('dimension check',sum((chars[n][(1,1,1,1)]*v//48) for n,zz in inner.items() for p,v in zz.items()))
with open(DATA_PATH) as f:r=json.load(f)
r['decomposition']={name:{str(par):v//48 for par,v in zz.items()} for name,zz in inner.items()}
with open(DATA_PATH,'w') as f:json.dump(r,f,indent=2)
h1={name:{sgn:0 for sgn in [-1,1]} for name in chars}
for g,k,d,values in autom:
 typ=diagonal_type(g)
 for name,c in chars.items():
  for sgn in [-1,1]:h1[name][sgn]+=values[-2]*c[typ]*(sgn if d==-1 else 1)
assert all(v%48==0 and v>=0 for zz in h1.values() for v in zz.values())
print('H1 decomposition',{name:{str(par):v//48 for par,v in zz.items()} for name,zz in h1.items()})
with open(DATA_PATH) as f:r=json.load(f)
r['h1_decomposition']={name:{str(par):v//48 for par,v in zz.items()} for name,zz in h1.items()}
with open(DATA_PATH,'w') as f:json.dump(r,f,indent=2)
