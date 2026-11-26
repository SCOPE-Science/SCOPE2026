import itertools,json
p=3
M=[(i,j,4-i-j) for i in range(4,-1,-1) for j in range(4-i,-1,-1)]
assert len(M)==15
vs=[]
for v in itertools.product(range(3),repeat=3):
 if v!=(0,0,0):
  r=next(x for x in v if x)
  vi=tuple(x*pow(r,-1,3)%3 for x in v)
  if vi not in vs:vs.append(vi)
vs=sorted(vs)

def indep(u,v):return any((u[i]*v[j]-u[j]*v[i])%3 for i in range(3) for j in range(i+1,3))
def span2(u,v):return sorted({tuple((a*u[i]+b*v[i])%3 for i in range(3)) for a in range(3) for b in range(3)})
def poly_mul_linear(poly,lin):
 out={}
 for e,c in poly.items():
  for i,a in enumerate(lin):
   if a:
    v=tuple(e[j]+(i==j) for j in range(3))
    out[v]=(out.get(v,0)+c*a)%3
 return out

def coeffs_change(Q):
 # Q columns P,Q,R
 coords=[tuple(Q[k][j] for j in range(3)) for k in range(3)]
 out=[]
 for m in M:
  poly={(0,0,0):1}
  for i,k in enumerate(m):
   for _ in range(k):poly=poly_mul_linear(poly,coords[i])
  out.append(poly)
 return out

def primitive_plane(u,v):
 x=tuple((a*u[0]+b*v[0])%3 for a,b in [])

flags=[]
for P in vs:
 seen=set()
 for V in vs:
  if not indep(P,V):continue
  S=span2(P,V)
  if tuple(S) in seen:continue
  seen.add(tuple(S))
  R=next(r for r in vs if r not in S)
  C=coeffs_change([[P[i],V[i],R[i]] for i in range(3)])
  rows=[[d.get((4-k,k,0),0) for d in C] for k in range(4)]
  transverse=[d.get((3,0,1),0) for d in C]
  assert any(transverse)
  flags.append({'P':P,'Q':V,'R':R,'rows':rows,'transverse':transverse})
assert len(flags)==52,len(flags)
open('hyperflex_flags.json','w').write(json.dumps({'monomials':M,'flags':flags}))
print('flags',len(flags),'points',len(vs))
