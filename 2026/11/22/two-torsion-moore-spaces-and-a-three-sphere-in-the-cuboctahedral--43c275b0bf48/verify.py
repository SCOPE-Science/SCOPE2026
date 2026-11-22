#!/usr/bin/env python3
"""Standalone exact verifier of a finite geometric orbit-cell computation.
Standard-library Python 3.10+. Run: python3 verify.py
"""
import itertools, collections, math

def quotient(faces,perms):
 faceidx={f:i for i,f in enumerate(faces)}
 mp=[]
 for p in perms:
  tab=[1<<j for j in p]
  def T(f):
   z=0
   while f:
    b=f&-f; f-=b;z|=tab[b.bit_length()-1]
   return faceidx[z]
  mp.append(tuple(T(f) for f in faces))
 flags_by_dim=[];flags=[(i,) for i in range(len(faces))]
 def proper(z):
  sub=(z-1)&z
  while sub:
   yield sub
   sub=(sub-1)&z
 for k in range(1,max(f.bit_count() for f in faces)+1):
  if k>1:
   flags=[(faceidx[sub],)+f for f in flags for sub in proper(faces[f[0]])]
  reps={}
  for flag in flags:
   if flag in reps:continue
   im={tuple(m[x] for x in flag) for m in mp}
   rep=min(im)
   for f in im:reps[f]=rep
  out=sorted(set(reps.values()))
  flags_by_dim.append((out,reps))
  print('dim',k-1,'raw',len(flags),'orbits',len(out),flush=True)
 cells=[x[0] for x in flags_by_dim];cellidx=[{f:i for i,f in enumerate(cc)} for cc in cells]
 incidence=[]
 for d in range(1,len(cells)):
  inc=[]
  for flag in cells[d]:
   ff=[]
   for i in range(len(flag)):
    face=flag[:i]+flag[i+1:]
    ff.append((cellidx[d-1][flags_by_dim[d-1][1][face]], (-1)**i))
   assert len(set(x[0] for x in ff))==len(ff)
   inc.append(ff)
  incidence.append(inc)
 alive=[set(range(len(x))) for x in cells];pairs=[]
 # inverted cofaces, real higher-dimensional cell free test
 while True:
  change=0
  for d in range(len(cells)-1,0,-1):
   supports=collections.defaultdict(set)
   for ci in alive[d]:
    for fi,sgn in incidence[d-1][ci]:
     if fi in alive[d-1]:supports[fi].add(ci)
   bad=set(f for idx in alive[d+1] for f,_ in incidence[d][idx]) if d<len(cells)-1 else set()
   for fi,s in sorted(supports.items()):
    if len(s)==1:
     ci=next(iter(s))
     if fi in alive[d-1] and ci in alive[d] and ci not in bad:
      alive[d-1].remove(fi);alive[d].remove(ci);pairs.append((d,fi,ci));change+=1
  if not change:break
 print('collapses',len(pairs),'remain',list(map(len,alive)),'Euler',sum((-1)**d*len(x) for d,x in enumerate(alive)),flush=True)
 return cells,incidence,pairs,alive


def construct():
 cube_edges=[(i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1]
 G_edges=[(i,j) for i in range(12) for j in range(i+1,12) if set(cube_edges[i])&set(cube_edges[j])]
 ged={e:i for i,e in enumerate(G_edges)};ced={e:i for i,e in enumerate(cube_edges)}
 perms=[]
 for perm in itertools.permutations(range(3)):
  for mask in range(8):
   def T(i):return sum((((i>>d)&1)^((mask>>d)&1))<<perm[d] for d in range(3))
   cp=[ced[tuple(sorted((T(a),T(b))))] for a,b in cube_edges]
   perms.append(tuple(ged[tuple(sorted((cp[a],cp[b])))] for a,b in G_edges))
 faces=[]
 def rec(f,used,k):
  if f:faces.append(f)
  for i in range(k,len(G_edges)):
   a,b=G_edges[i]
   if (used>>a)&1 or (used>>b)&1:continue
   rec(f|(1<<i), used|(1<<a)|(1<<b),i+1)
 rec(0,0,0)
 faces.sort(key=lambda x:(x.bit_count(),x))
 return G_edges,faces,perms

def modrank(vectors,p):
 basis={}
 for vv in vectors:
  v={i:z%p for i,z in vv.items() if z%p}
  while v:
   pivot=min(v)
   if pivot not in basis:
    inv=pow(v[pivot],-1,p)
    basis[pivot]={i:(x*inv)%p for i,x in v.items()}
    break
   t=v[pivot]
   for i,x in basis[pivot].items():
    z=(v.get(i,0)-t*x)%p
    if z:v[i]=z
    else:v.pop(i,None)
 return len(basis)

def reduced_complex(alive,inc):
 cc=[sorted(x) for x in alive];mp=[{v:i for i,v in enumerate(z)} for z in cc]
 matrices=[]
 for d in range(1,len(cc)):
  cols=[]
  for old in cc[d]:
   out={mp[d-1][r]:v for r,v in inc[d-1][old] if r in mp[d-1]}
   cols.append(out)
  matrices.append(cols)
 return cc,matrices

def unit_reduce(cols,nrow):
 rows={i:{} for i in range(nrow)}
 c={j:dict(C) for j,C in enumerate(cols)}
 for j,C in c.items():
  for i,v in C.items():rows[i][j]=v
 count=0
 while True:
  opts=[]
  for j,C in c.items():
   for i,v in C.items():
    if abs(v)==1:opts.append(((len(rows[i])-1)*(len(C)-1),len(C)+len(rows[i]),i,j,v))
  if not opts:break
  _,_,i,j,v=min(opts)
  C=c[j].copy();R=rows[i].copy()
  for i2,a in C.items():
   if i2==i:continue
   for j2,b in R.items():
    if j2==j:continue
    z=rows[i2].get(j2,0)-a*b//v
    if z:rows[i2][j2]=z;c[j2][i2]=z
    else:rows[i2].pop(j2,None);c[j2].pop(i2,None)
  for ii in C:rows[ii].pop(j,None)
  for jj in R:c[jj].pop(i,None)
  del rows[i],c[j];count+=1
 return rows,c,count

def original_pi1(faces,nvert):
 fs2=sorted((f for f in faces if f.bit_count()==2))
 fs3=[f for f in faces if f.bit_count()==3]
 par=list(range(nvert))
 def root(i):
  while par[i]!=i:par[i]=par[par[i]];i=par[i]
  return i
 edges={};gen=0
 for f in fs2:
  a,b=[i for i in range(nvert) if f>>i&1]
  if root(a)!=root(b):par[root(a)]=root(b);edges[(a,b)]=0
  else:gen+=1;edges[(a,b)]=gen
 assert gen==181
 def red(w):
  out=[]
  for x in w:
   if out and out[-1]==-x:out.pop()
   else:out.append(x)
  while len(out)>=2 and out[0]==-out[-1]:out=out[1:-1]
  return tuple(out)
 rel=[]
 for f in fs3:
  a,b,c=[i for i in range(nvert) if f>>i&1]
  rel.append(red(x for x in (edges[a,b],edges[b,c],-edges[a,c]) if x))
 steps=0
 while True:
  candidates=[]
  for idx,w in enumerate(rel):
   counts=collections.Counter(map(abs,w))
   for g,k in counts.items():
    if k==1:candidates.append((len(w),len(set(w)),g,idx))
  if not candidates:break
  _,_,g,ri=min(candidates);w=rel[ri]
  k=next(i for i,x in enumerate(w) if abs(x)==g)
  sg=1 if w[k]>0 else -1;rest=w[k+1:]+w[:k]
  sub=tuple(-x for x in reversed(rest)) if sg==1 else rest
  new=[]
  for j,rr in enumerate(rel):
   if j==ri:continue
   z=[]
   for x in rr:
    if x==g:z.extend(sub)
    elif x==-g:z.extend(-y for y in reversed(sub))
    else:z.append(x)
   new.append(red(z))
  rel=new;steps+=1
 assert steps==gen and not any(rel)
 return steps

def check():
 ed,faces,perms=construct()
 assert (len(ed),len(faces),len(perms))==(24,2648,48)
 assert [sum(f.bit_count()==k for f in faces) for k in range(1,7)]==[24,204,744,1116,528,32]
 # Five group generators all fix barycenters of nonempty simplices.
 for j in [1,2,4,8,16]:
  pp=perms[j]
  assert any(sum(1<<pp[i] for i in range(24) if f>>i&1)==f for f in faces)
 assert original_pi1(faces,24)==181
 cells,inc,pairs,alive=quotient(faces,perms)
 assert [len(a) for a in cells]==[73,843,2983,4253,2520,480]
 assert len(pairs)==5117
 cc,mat=reduced_complex(alive,inc)
 assert [len(a) for a in cc]==[38,229,421,230,0,0]
 # Signed chain-complex identities.
 for d in range(1,len(mat)):
  for col in mat[d]:
   acc=collections.defaultdict(int)
   for i,a in col.items():
    for j,b in mat[d-1][i].items():acc[j]+=a*b
   assert all(x==0 for x in acc.values())
 assert modrank(mat[0],101)==37 and modrank(mat[1],101)==192
 assert modrank(mat[2],101)==229
 rows,columns,units=unit_reduce(mat[2],len(cc[2]))
 assert units==227 and (len(rows),len(columns))==(194,3)
 labels=list(columns)
 A=[[rows[i].get(j,0) for j in labels] for i in rows]
 d1=0
 for a in A:
  for v in a:d1=math.gcd(d1,v)
 d2=0
 for a,b in itertools.combinations(A,2):
  for j,k in itertools.combinations(range(3),2):d2=math.gcd(d2,a[j]*b[k]-a[k]*b[j])
 assert (d1,d2)==(2,12)
 # Remaining matrix has rank 2: a pair of proportional columns.
 assert all(a[0]==-a[2] for a in A) or all(a[1]==-a[2] for a in A) or all(a[0]==-a[1] for a in A)
 # gcd of 3x3 minors consequently zero, completing Smith invariants 2,6,0.
 print('PASS_CUBOCTAHEDRAL_MATCHING_QUOTIENT_H2_Z2_PLUS_Z6_H3_Z_PI1_TRIVIAL')
if __name__=='__main__':check()
