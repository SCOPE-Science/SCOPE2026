import contextlib,io,itertools,collections,sys,json,time
with contextlib.redirect_stdout(io.StringIO()):
 import oct
from oct import V,E,incident,idx,bases,BC,rank_gf
p=32003
start=time.monotonic()

def modclean(d):return {i:v%p for i,v in d.items() if v%p}
def reduce(d,piv,track=None):
 d=modclean(d)
 for row in sorted(piv):
  if row not in d:continue
  v=d[row]
  for i,w in piv[row].items():
   u=(d.get(i,0)-v*w)%p
   if u:d[i]=u
   elif i in d:del d[i]
  if track is not None:track[row]=(track.get(row,0)+v)%p
 return d

def scalar(d,x):return modclean({i:v*x for i,v in d.items()})
def combine(a,b,x):
 z=a.copy()
 for i,v in b.items():z[i]=(z.get(i,0)+x*v)%p
 return modclean(z)

_,B=rank_gf(BC[2],p)
P={};K=[]
for j,col in enumerate(BC[1]):
 d=modclean(col); z={j:1}
 while d:
  row=min(d)
  if row not in P:
   inv=pow(d[row],-1,p)
   P[row]=(scalar(d,inv),scalar(z,inv));break
  factor=d[row]
  d=combine(d,P[row][0],-factor)
  z=combine(z,P[row][1],-factor)
 else:K.append(z)
assert len(K)==1041 and len(P)==363
H={};Hcycles={}
for z in K:
 d=reduce(z,B)
 track={}
 d=reduce(d,H,track)
 if d:
  for row,factor in track.items():z=combine(z,Hcycles[row],-factor)
  row=min(d);inv=pow(d[row],-1,p)
  H[row]=scalar(d,inv)
  Hcycles[row]=scalar(z,inv)
print("H calculated",len(H),"pivot count",len(B),"ker",len(K),flush=True)
assert len(H)==8
Hrows=sorted(H)
print('H basis',Hrows,'C1cycles lengths',[len(Hcycles[r]) for r in Hrows], 'seconds',round(time.monotonic()-start,2),flush=True)

edxi={e:i for i,e in enumerate(E)}

def v_to_e(vp):return [edxi[tuple(sorted((vp[a],vp[b])))] for a,b in E]

def apply_one(g,ep,vec):
 out=collections.defaultdict(int)
 for j,c in vec.items():
  ((v,h),),m=bases[1][j]
  gv=g[v];gref=ep[incident[v][0]];gh=ep[h]
  gm=tuple(sorted(ep[ee] for ee in m))
  for ee,s in [(gh,1),(gref,-1)]:
   if ee!=incident[gv][0]:
    jj=idx[1][(((gv,ee),),gm)]
    out[jj]+=c*s
 return modclean(out)

def coeffs(vec):
 d=reduce(vec,B)
 co={}
 while d:
  row=min(d)
  assert row in H,(row,len(d))
  v=d[row]
  co[row]=v
  d=combine(d,H[row],-v)
 return co

def allg():
 for perm in itertools.permutations(range(3)):
  for bs in itertools.product(range(2),repeat=3):
   vp=[2*perm[v//2]+((v%2)^bs[v//2]) for v in range(6)]
   yield vp

import characters
observed=[]
for g in allg():
 ep=v_to_e(g)
 diagtrace=0
 for i,row in enumerate(Hrows):
  cy=Hcycles[row]
  im=apply_one(g,ep,cy)
  # assert this is a cycle over GF(p)
  bd=collections.defaultdict(int)
  for jj,c in im.items():
   for r,v in BC[1][jj].items():bd[r]+=c*v
  assert all(z%p==0 for z in bd.values())
  diagtrace+=coeffs(im).get(row,0)
 tr=diagtrace%p
 if tr>p//2:tr-=p
 # find predicted
 pred=next(val[3] for gg,key,det,val in characters.autom if gg==g)
 assert tr==pred,(g,tr,pred)
 observed.append(tr)
print('all 48 H1 traces verified against geometric sign formula; histogram',dict(collections.Counter(observed)), 'seconds',round(time.monotonic()-start,2),flush=True)
print('EQUIV_OK')
