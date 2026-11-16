from itertools import product, permutations
from pathlib import Path
import subprocess, tempfile, re
from collections import Counter
# Exact computations take place in the integral basis (1, sqrt(5)).
P=101
S=(0,1); ONE=(1,0); ZERO=(0,0)
def add(u,v):return u[0]+v[0],u[1]+v[1]
def neg(u):return -u[0],-u[1]
def sub(u,v):return add(u,neg(v))
def mul(u,v):return u[0]*v[0]+5*u[1]*v[1],u[0]*v[1]+u[1]*v[0]
def dm(u):return u[0]+45*u[1]
verts=[]
for x,y,z in product((-2,2),repeat=3):verts.append(((x,0),(y,0),(z,0)))
for sy,sz in product((-1,1),repeat=2):verts.append((ZERO,(-sy,sy),(sz,sz)))
for sx,sy in product((-1,1),repeat=2):verts.append(((-sx,sx),(sy,sy),ZERO))
for sx,sz in product((-1,1),repeat=2):verts.append(((sx,sx),ZERO,(-sz,sz)))
assert len(verts)==20
rows=[]
for x,y,z in verts:
 rows.append([ONE,mul(x,y),mul(y,z),mul(z,x),sub(mul(x,x),mul(y,y)),sub(mul(y,y),mul(z,z))])
perm=list(permutations(range(5)))
sgn=[]
for per in perm:
 inv=sum(per[i]>per[j] for i in range(5) for j in range(i+1,5))
 sgn.append(-1 if inv%2 else 1)
def det5(M):
 out=ZERO
 for ps,sg in zip(perm,sgn):
  t=ONE
  for i,j in enumerate(ps):t=mul(t,M[i][j])
  out=add(out,t if sg==1 else neg(t))
 return out
with tempfile.TemporaryDirectory() as tmp:
 exe = str(Path(tmp) / "verify_mod101")
 subprocess.run(["g++", "-O2", "-std=c++17", str(Path(__file__).with_name("verify_mod101.cpp")), "-o", exe], check=True)
 out = subprocess.check_output([exe], text=True)
assert "rank8=123030 skipped=2940 closures=40991 max=12 top=25" in out
assert "size 12: 25 hyperplanes" in out
maxm = [int(x) for x in re.findall(r"^maxmask (\d+)", out, re.M)]
assert len(maxm) == 25

nulls={}
for mask in maxm:
 indices=[i for i in range(20) if mask>>i&1]
 assert len(indices)==12
 axes=[]
 for i in indices:
  if not any(all(x==neg(y) for x,y in zip(verts[i],verts[j])) for j in indices if j!=i):
   raise RuntimeError(('not antipodal',mask,i))
  if not any(all(x==neg(y) for x,y in zip(verts[i],verts[j])) for j in axes):axes.append(i)
 assert len(axes)==6
 found=False
 for omit in range(6):
  M=[rows[i] for j,i in enumerate(axes) if j!=omit]
  c=[]
  for j in range(6):
   v=det5([[row[k] for k in range(6) if k!=j] for row in M])
   c.append(v if j%2==0 else neg(v))
  if all(x==ZERO for x in c):continue
  zs=[i for i in range(20) if sum((mul(rows[i][j],c[j])[0] for j in range(6)))==0 and sum((mul(rows[i][j],c[j])[1] for j in range(6)))==0]
  assert set(zs)==set(indices),(mask,zs)
  found=True
  nulls[mask]=c
  break
 assert found,mask
assert len(nulls) == 25
print('DODECAHEDRAL_ERASURES_EXACT_CHECK_OK: 25 twelve-point singular sets, all thirteen-point sets full rank')
