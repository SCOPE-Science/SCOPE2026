from itertools import product
from math import comb

def rank_vectors(vectors):
 B={}
 for x in vectors:
  while x:
   i=x.bit_length()-1
   if i not in B: B[i]=x; break
   x^=B[i]
 return list(B.values())

def mul_d8(g,h):
 a,b=g; c,d=h
 return ((a+(-1)**b*c)%4,(b+d)%2)
def mul(g,h):return tuple(mul_d8(a,b) for a,b in zip(g,h))
def direct(r):
 els=list(product(list(product(range(4),range(2))),repeat=r))
 m={v:i for i,v in enumerate(els)}
 tb=[[m[mul(a,b)] for b in els] for a in els]
 N=len(els)
 basis=[1<<i for i in range(N)]
 cur=basis
 dims=[N]
 for n in range(2,r+3):
  vec=[]
  for a in cur:
   # expand for basis a
   choices=[];bits=a
   while bits:
    x=bits&-bits;choices.append(x.bit_length()-1);bits-=x
   for j in range(N):
    v=0
    for i in choices:
     v^=1<<tb[i][j]
     v^=1<<tb[j][i]
    vec.append(v)
  cur=rank_vectors(vec)
  dims.append(len(cur))
 return dims

def formula(r,n):
 if n==1:return 8**r
 return sum(comb(r,k)*(4**r-4**(r-k)) for k in range(n-1,r+1))
for r in [1,2]:
 actual=direct(r)
 expected=[formula(r,n) for n in range(1,r+3)]
 print('r',r,'actual',actual,'expected',expected)
 assert actual==expected
print('JORDAN_DIRECT_CHECK_OK')

def mul_polys(a,b,r):
 # polynomials in t_i with t_i^2=0, bit index = subset
 out=0
 for i in range(1<<r):
  if a>>i & 1:
   for j in range(1<<r):
    if b>>j & 1 and i&j==0:out ^= 1<<(i|j)
 return out

def supp(v,r):
 return sum(1<<i for i in range(r) if v>>(2*i)&3)

def comm(u,w,r):
 c=0
 for i in range(r):
  a=(u>>(2*i))&3; b=(w>>(2*i))&3
  if ((a&1)*((b>>1)&1)^((a>>1)&1)*(b&1))&1: c|=1<<i
 return c

def exact_ideal_recurrence(r):
 V=1<<(2*r); D=1<<r
 # basis of A in t subset notation, each element is 1<<subset
 cur=[[1<<i for i in range(D)] for v in range(V)]
 dims=[V*D]
 for n in range(2,r+3):
  nxt=[]
  for v in range(V):
   generators=[]
   for u in range(V):
    c=comm(u,v^u,r)
    if not c:continue
    f=0
    for t in range(1,1<<r):
     if t &~ c==0:f|=1<<t
    for a in cur[u]:generators.append(mul_polys(a,f,r))
   nxt.append(rank_vectors(generators))
  cur=nxt
  dims.append(sum(len(a) for a in cur))
  # compare each coordinate ideal with formula
  for v,poly_basis in enumerate(cur):
   s=supp(v,r)
   expected=sum(1 for t in range(D) if t.bit_count()>=n-1 and t&s!=0)
   if len(poly_basis)!=expected:raise ValueError(f'coordinate failure r={r} n={n} v={v} got {len(poly_basis)} expected {expected}')
 return dims

for r in [1,2,3]:
 actual=exact_ideal_recurrence(r)
 expected=[formula(r,n) for n in range(1,r+3)]
 print('r',r,'recurrence',actual,'expected',expected)
 assert actual==expected
print('JORDAN_IDEAL_RECURSION_OK')
# Independent multiplication table for H_i = D8 or Q8 encoded in (a,b,c) over F2.
def mul_dq(g,h,kind):
 a,b,c=g; d,e,f=h
 return (a^d,b^e,c^f^(a&d)^(b&d)^((b&e) if kind=='Q8' else 0))

def mixed_direct(kinds):
 r=len(kinds); single=list(product(range(2),repeat=3))
 els=list(product(single,repeat=r)); N=len(els); inds={g:i for i,g in enumerate(els)}
 def gm(g,h):return tuple(mul_dq(g[i],h[i],kinds[i]) for i in range(r))
 tb=[[inds[gm(g,h)] for h in els] for g in els]
 cur=[1<<i for i in range(N)]; dims=[N]
 for n in range(2,r+3):
  out=[]
  for b in cur:
   iset=[]
   while b:
    x=b&-b;iset.append(x.bit_length()-1);b-=x
   for j in range(N):
    v=0
    for i in iset:v^=1<<tb[i][j];v^=1<<tb[j][i]
    out.append(v)
  cur=rank_vectors(out);dims.append(len(cur))
 return dims

for kinds in [('Q8',),('D8','Q8'),('Q8','Q8')]:
 r=len(kinds);d=mixed_direct(kinds);want=[formula(r,n) for n in range(1,r+3)]
 print(kinds,d,want);assert d==want
print('JORDAN_MIXED_GROUPS_OK')
