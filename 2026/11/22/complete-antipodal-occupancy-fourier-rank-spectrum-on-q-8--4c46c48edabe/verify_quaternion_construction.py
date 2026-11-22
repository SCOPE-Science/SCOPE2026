import itertools, json
import sympy as S
I=S.I; H=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
K={0:{0},1:{4},2:{2,4},3:{3,4},4:{1,2,3,4}}
def pattern_k(a,b):return set.union(*(K[j] for j in range(a,a+b+1)))
def classes(a,b):
    out=[]
    if a==0:
        for k in sorted(K[b]):out.append((k,0,k))
    if b>=2 or b==1 and a>0:
        for k in sorted(pattern_k(a,b)):out.append((k+2,1,k))
    if b==0:
        kvals={1:set(),2:{4},3:{3,4},4:{2,3,4}}.get(a,set())
        for k in sorted(kvals):out.append((k+2,1,k))
    for k in sorted(pattern_k(a,b)):
        if b==0 and a==1 and k!=4:continue
        out.append((k+4,2,k))
    return out

def s_special(a,k,r):
 if a==1:return [S.Integer(1)]
 if a==2:return [1,I] if r==1 else ([1,1] if k==2 else [1,2])
 if a==3:
  if r==1:
   if k==3:return [1,(-1+S.sqrt(-3))/2,(-1-S.sqrt(-3))/2]
   return [1,1,I*S.sqrt(2)]
  return [1,1,-2] if k==3 else [1,1,1]
 if a==4:
  if r==1:
   if k==2:return [1,1,I,I]
   lam=([3,4,5*I,0] if k==3 else [3,4,3*I,4*I]); return [sum(H[t][i]*lam[t] for t in range(4))/4 for i in range(4)]
  return {1:[1,1,1,1],2:[1,1,2,2],3:[1,2,3,4],4:[1,2,4,8]}[k]
 assert False

def choose_s(a,b,k,mode):
 if b==0:return list(map(S.sympify,s_special(a,k,mode))) + [S.Integer(0)]*(4-a)
 vals=[0,1,2,3,4,5,8]
 for z in itertools.product(vals,repeat=b):
  for y in itertools.product(vals[1:],repeat=a):
   s=list(map(S.Integer,y+z+(0,)*(4-a-b)))
   if mode==0 and any(x==0 for x in s[a:a+b]):continue
   if sum(sum(h*s[j] for j,h in enumerate(row))!=0 for row in H)!=k:continue
   # avoid pair violation as constructed; choose small enough singles
   return s
 raise ValueError((a,b,k,mode))

def choose_d(a,b,s,mode):
 if b==0:return s[:]
 if mode==0:return [S.Integer(0)]*4
 if mode==2:return list(s[:a])+[S.Integer(20)]*b+[S.Integer(0)]*(4-a-b)
 if mode==1:
  ds=list(s[:a])+[S.Integer(7)]*(b-1)
  ds.append(S.I*S.sqrt(S.expand(sum(t*t for t in ds))))
  ds.extend([S.Integer(0)]*(4-a-b))
  return ds
 raise ValueError(mode)

def zer(x):return S.simplify(x)==0

def verify(a,b,s,d,rank,r,k):
 assert all(not zer(s[j]) and zer(d[j]-s[j]) for j in range(a))
 assert all(not zer(s[j]+d[j]) and not zer(s[j]-d[j]) for j in range(a,a+b))
 assert all(zer(s[j]) and zer(d[j]) for j in range(a+b,4))
 ks=sum(not zer(sum(H[i][j]*s[j] for j in range(4))) for i in range(4))
 q=S.expand(sum(t*t for t in d))
 mr=0 if all(zer(v) for v in d) else (1 if zer(q) else 2)
 assert (ks,mr,ks+2*mr)==(k,r,rank),(a,b,k,r,rank,s,d,ks,mr,q)
 # direct independent 2x2 matrix verify, using Pauli representation
 M=S.Matrix([[d[0]+I*d[1],d[2]+I*d[3]],[-d[2]+I*d[3],d[0]-I*d[1]]])
 assert zer(S.expand(M.det()-q))
 if mr==0:assert all(zer(x) for x in M)
 if mr==1:assert zer(M.det()) and any(not zer(x) for x in M)
 if mr==2:assert not zer(M.det())

rows=[]
for b in range(5):
 for a in range(5-b):
  if a+b==0:continue
  classes_for={}
  for rank,r,k in classes(a,b):
   if rank in classes_for:continue
   s=choose_s(a,b,k,r); d=choose_d(a,b,s,r)
   verify(a,b,s,d,rank,r,k)
   classes_for[rank]={'k':k,'r':r,'s':list(map(str,s)),'d':list(map(str,d))}
  rows.append({'singles':a,'pairs':b,'size':a+2*b,'ranks':sorted(classes_for),'witnesses':classes_for})

from pathlib import Path
expected=json.loads(Path(__file__).with_name('quaternion_witnesses.json').read_text('utf-8'))
assert json.loads(json.dumps(rows))==expected
print('PASS: 14 occupancy types and 64 exact canonical witnesses match the stored certificate')
