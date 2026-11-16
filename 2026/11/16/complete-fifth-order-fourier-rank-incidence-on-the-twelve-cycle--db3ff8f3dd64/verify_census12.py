#!/usr/bin/env python3
"""Exact rank census of five-row, five-column restrictions of DFT_12.
Uses cyclotomic integers in Z[z]/(z**4-z**2+1), where z is primitive 12th root.
No floating-point rank decisions; exhaustive modulo-translation orbit census.
"""
import itertools, collections, json, hashlib
N=12; K=5
ALL=list(itertools.combinations(range(N),K))
assert len(ALL)==792

def shift(t,h): return tuple(sorted((v+h)%N for v in t))

def normal(t): return min(shift(t,h) for h in range(N))
REP=sorted({normal(t) for t in ALL})
assert len(REP)==66
assert all(len({shift(t,h) for h in range(N)})==N for t in REP)
# Coefficients for powers 0..11 of primitive z under z^4=z^2-1.
def mul_z(v):
 a,b,c,d=v
 return (-d,a,b+d,c)
POW=[(1,0,0,0)]
for i in range(1,N): POW.append(mul_z(POW[-1]))
assert mul_z(POW[-1])==POW[0]
PERM={}
for k in range(1,K+1):
 perms=[]
 for p in itertools.permutations(range(k)):
  sign=(-1)**sum(p[i]>p[j] for i in range(k) for j in range(i+1,k))
  perms.append((p,sign))
 PERM[k]=perms

def det0(rows,cols):
 k=len(rows); v=[0]*4
 for p,s in PERM[k]:
  exponent=sum(rows[i]*cols[p[i]] for i in range(k))%N
  d=POW[exponent]
  for j in range(4): v[j]+=s*d[j]
 return not any(v)

def rank(rows,cols):
 if not det0(rows,cols):return K
 for k in (4,3,2,1):
  for rr in itertools.combinations(rows,k):
   for cc in itertools.combinations(cols,k):
    if not det0(rr,cc):return k
 return 0

counts=collections.Counter(); incid={}; table=[]
for i,r in enumerate(REP):
 one=[]
 for j,c in enumerate(REP):
  v=rank(r,c)
  counts[v]+=1
  one.append(v)
 table.append(one)
 incid[str(i)]=dict(collections.Counter(one))
assert sum(counts.values())==4356
assert counts==collections.Counter({3:27,4:757,5:3572})
assert all(table[i][j]==table[j][i] for i in range(66) for j in range(66))

# Validate all-rank counts against direct finite-field gaussian elimination for each pair
# at a primitive 12th root modulo prime 1009. This can only underestimate char-zero rank.
p=1009
primitive=next(x for x in range(2,p) if len({pow(x,k,p) for k in range(1,p)})==p-1)
w=pow(primitive,(p-1)//12,p)
assert pow(w,12,p)==1 and all(pow(w,k,p)!=1 for k in (1,2,3,4,6))
def rank_mod(r,c):
 a=[[pow(w,(x*y)%N,p) for y in c] for x in r];rank=0
 for j in range(K):
  pivot=next((i for i in range(rank,K) if a[i][j]),None)
  if pivot is None:continue
  a[pivot],a[rank]=a[rank],a[pivot]
  iv=pow(a[rank][j],-1,p)
  for ii in range(rank+1,K):
   f=a[ii][j]*iv%p
   if f:
    for jj in range(j,K):a[ii][jj]=(a[ii][jj]-f*a[rank][jj])%p
  rank+=1
 return rank

mismatch=[]
for i,r in enumerate(REP):
 for j,c in enumerate(REP):
  mod_rank=rank_mod(r,c)
  if mod_rank != table[i][j]:mismatch.append((i,j,table[i][j],mod_rank))
print('all polynomial powers',POW)
print('representatives',len(REP),'representative pairs',len(REP)**2)
print('count per representative pair',sorted(counts.items()))
print('complete raw counts',sorted((k,v*144) for k,v in counts.items()))
assert not mismatch
print('rank_mod1009 disagreements',len(mismatch),mismatch[:6])
print('row 5-spark:',sum(all(v==5 for v in row) for row in table),'row max singular: ',max(sum(v<5 for v in row) for row in table))
print('row rank extrema', {k:sorted((sum(v==k for v in row),i) for i,row in enumerate(table))[-4:] for k in range(1,6)})
print('rank sample',[(k,[(REP[i],REP[j]) for i,row in enumerate(table) for j,v in enumerate(row) if v==k][:3]) for k in range(1,6)])
result={"modulus":12,"minor_size":5,"representatives":REP,"rank_matrix":table,"rank_orbit_counts":dict(counts),"rank_raw_counts":{str(k):v*144 for k,v in counts.items()},"modular_crosscheck_disagreements":mismatch,"modular_crosscheck_prime":p,"modular_crosscheck_root":w}
fn='census12.json'
with open(fn,'w',encoding='utf-8') as out:json.dump(result,out,sort_keys=True,separators=(',',':'))
print('saved',fn,hashlib.sha256(open(fn,'rb').read()).hexdigest())
