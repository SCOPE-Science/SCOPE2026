"""Reproduce the complete rational tritangent-plane census of smooth cubic surfaces over F_2.
Requires Python 3.9+ and SymPy (for four-chart Groebner smoothness certificates).
Run with: python verify.py. The companion orbits.csv is a finite integer certificate,
fully rechecked against all 2^20-1 nonzero cubic equations.
"""
import itertools, json, collections
from pathlib import Path
import sympy as s

# Enumerate the cubic monomials in a fixed lexicographic exponent order.
mon4=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):
   mon4.append((a,b,c,3-a-b-c))
assert len(mon4)==20
X=s.symbols('x0:4')

def action_images():
 """Three elementary substitutions generating GL_4(F_2)."""
 substitutions=[]
 for kind in range(3):
  images=[]
  for ex in mon4:
   poly=s.Integer(1)
   for j,e in enumerate(ex):
    if kind==0: v=X[1-j] if j<2 else X[j]
    elif kind==1: v=X[(j+1)%4]
    else: v=X[0]+X[1] if j==0 else X[j]
    poly*=v**e
   q=s.Poly(s.expand(poly),*X,modulus=2)
   images.append(sum(1<<mon4.index(exp) for exp,c in q.terms() if c%2))
  substitutions.append(images)
 return substitutions

def apply_form(mask,images):
 res=0
 while mask:
  lsb=mask&-mask
  res ^=images[lsb.bit_length()-1];mask-=lsb
 return res

def check_generators_full():
 """Verify generators span all 20,160 invertible linear substitutions."""
 gs=[(2,1,4,8),(2,4,8,1),(3,2,4,8)]
 def mul(a,b):
  return tuple(__import__('functools').reduce(int.__xor__,(a[i] for i in range(4) if (v>>i)&1),0) for v in b)
 seen={(1,2,4,8)}
 queue=[(1,2,4,8)]
 for x in queue:
  for g in gs:
   y=mul(x,g)
   if y not in seen:
    seen.add(y);queue.append(y)
 assert len(queue)==20160

def verify_orbits():
 reps=[tuple(map(int,ln.split(','))) for ln in (Path(__file__).parent/'orbits.csv').read_text().strip().splitlines()]
 assert len(reps)==141
 trans=action_images();seen=bytearray(1<<20)
 total=0
 for rep,weight in reps:
  assert 1<=rep<(1<<20) and not seen[rep]
  seen[rep]=1;queue=[rep]
  for x in queue:
   for tr in trans:
    y=apply_form(x,tr)
    if not seen[y]:
     seen[y]=1;queue.append(y)
  assert len(queue)==weight,(rep,weight,len(queue))
  total+=len(queue)
 assert total==(1<<20)-1 and sum(seen)==total
 return reps

def smooth(mask):
 f=sum((s.prod(X[j]**e for j,e in enumerate(mon4[i])) for i in range(20) if (mask>>i)&1),s.Integer(0))
 deriv=[s.diff(f,x) for x in X]
 for pt in itertools.product((0,1),repeat=4):
  if any(pt) and all(int(z.subs(dict(zip(X,pt))))%2==0 for z in deriv):
   return False
 for j in range(4):
  eq=[z.subs({X[j]:1}) for z in deriv]
  vars=[X[i] for i in range(4) if i!=j]
  G=s.groebner(eq,*vars,order='grevlex',modulus=2)
  if not (len(G.polys)==1 and G.polys[0].is_ground and int(G.polys[0].LC())%2==1):
   return False
 return True

# Enumerate all ternary cubic plane sections that split into three distinct
# geometric lines. Frobenius orbit partitions are (1,1,1), (1,2), (3).
mon3=[]
for a in range(4):
 for b in range(4-a):
  mon3.append((a,b,3-a-b))
index3={a:i for i,a in enumerate(mon3)}
mon2=[(a,3-a) for a in range(4)]
index2={a:i for i,a in enumerate(mon2)}
def mulfield(a,b,degree,poly):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&(1<<degree):a^=poly
 return r

def field_lines(degree):
 n=1<<degree
 return [tuple(v) for v in itertools.product(range(n),repeat=3) if any(v) and next(z for z in v if z)==1]

def prod_linear(lines,d,poly):
 p={(0,0,0):1}
 for line in lines:
  q={}
  for e,a in p.items():
   for j,b in enumerate(line):
    if b:
     ee=list(e);ee[j]+=1;ee=tuple(ee)
     q[ee]=q.get(ee,0)^mulfield(a,b,d,poly)
  p=q
 assert sum(next(iter(p.keys())))==len(lines)
 return p

triset=set();patterns=collections.Counter()
L2=field_lines(1);L4=field_lines(2);L8=field_lines(3)
for a,b,c in itertools.combinations(L2,3):
 p=prod_linear((a,b,c),1,3);assert all(x in (0,1) for x in p.values())
 triset.add(sum(v<<index3[e] for e,v in p.items()))
patterns['111']=len(triset)
seen=set()
for a in L4:
 conj=tuple(mulfield(z,z,2,0b111) for z in a)
 if a==conj:continue
 if a in seen:continue
 seen.add(a);seen.add(conj)
 for b in L2:
  p=prod_linear((a,conj,b),2,0b111)
  assert all(x in (0,1) for x in p.values())
  triset.add(sum(v<<index3[e] for e,v in p.items()))
patterns['12']=len(triset)-patterns['111']
seen=set()
for a in L8:
 orbit=[a]
 while True:
  b=tuple(mulfield(z,z,3,0b1011) for z in orbit[-1]);
  if b==a:break
  orbit.append(b)
 if len(orbit)==1:continue
 assert len(orbit)==3
 if a in seen:continue
 seen.update(orbit)
 p=prod_linear(orbit,3,0b1011)
 assert all(x in (0,1) for x in p.values())
 triset.add(sum(v<<index3[e] for e,v in p.items()))
patterns['3']=len(triset)-sum(patterns.values())
assert len(triset)==106,(len(triset),patterns)
assert patterns=={'111':35,'12':49,'3':22}

def vector_xor_basis(normal):
 vectors=[i for i in range(16) if (i&normal).bit_count()%2==0]
 bas=[];span={0}
 for v in vectors[1:]:
  if v not in span:
   bas.append(v)
   span.update({u^v for u in list(span)})
 assert len(bas)==3
 return bas

def polyprod(A,B):
 out={}
 for a,x in A.items():
  for b,y in B.items():
   e=tuple(aa+bb for aa,bb in zip(a,b))
   out[e]=out.get(e,0) ^(x*y)
 return {k:v for k,v in out.items() if v}

def substitutions(basis):
 k=len(basis);fac=[]
 for xi in range(4):
  fac.append({tuple(int(j==h) for j in range(k)):1 for h in range(k) if (basis[h]>>xi)&1})
 return fac

def section_image(basis):
 k=len(basis);facs=substitutions(basis)
 out=[]
 for ex in mon4:
  p={(0,)*k:1}
  for j,e in enumerate(ex):
   for _ in range(e):p=polyprod(p,facs[j])
  if k==3:
   out.append(sum(1<<index3[e] for e in p))
  else:
   out.append(sum(1<<index2[e] for e in p))
 return out

planeimg=[section_image(vector_xor_basis(normal)) for normal in range(1,16)]
# enumerate F2 lines uniquely by the three nonzero vectors of their 2-dim linear space
lines={frozenset((a,b,a^b)) for a in range(1,16) for b in range(a+1,16)}
assert len(lines)==35
lineimg=[section_image(sorted(line)[:2]) for line in lines]


def main():
 check_generators_full()
 reps=verify_orbits()
 smoothreps=[(mask,weight) for mask,weight in reps if smooth(mask)]
 assert len(smoothreps)==36 and sum(w for _,w in smoothreps)==322560
 hist=collections.Counter()
 orbitcounts=collections.Counter()
 detail=[]
 for mask,weight in smoothreps:
  tcount=sum(apply_form(mask,ims) in triset for ims in planeimg)
  lcount=sum(apply_form(mask,ims)==0 for ims in lineimg)
  hist[(lcount,tcount)]+=weight
  orbitcounts[(lcount,tcount)]+=1
  detail.append((mask,weight,lcount,tcount))
 expected={
  (0,0):64512,(0,1):59640,(0,3):11200,(0,9):840,
  (1,0):23520,(1,1):75600,(1,2):15120,(1,3):420,
  (2,0):40320,(3,0):1120,(3,4):16800,(3,7):420,
  (5,3):11340,(9,6):1680,(15,15):28}
 assert dict(hist)==expected and sum(hist.values())==322560
 assert len(hist)==15 and len(orbitcounts)==15
 assert sum(1 for x in detail if x[2:]==(15,15))==1
 assert sum(1 for x in detail if x[2:]==(0,9))==1
 # Trace two independent extreme witnesses and their degrees.
 assert (66880,28,15,15) in detail and (67195,840,0,9) in detail
 print('BINARY_CUBIC_TRITANGENT_CENSUS_VERIFIED',
       'all_forms=1048575','all_orbits=141','smooth_orbits=36',
       'smooth_forms=322560','joint_profiles=15',
       'tritangent_section_forms=106',
       'sum_hist='+str(sum(hist.values())))
 print('weighted_joint_profile',sorted(hist.items()))
 print('orbit_counts',sorted(orbitcounts.items()))

if __name__=='__main__':main()
