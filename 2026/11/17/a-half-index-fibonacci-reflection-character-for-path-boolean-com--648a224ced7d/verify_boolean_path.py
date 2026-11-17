"""Reproduce signed diagram-reversal traces for path Boolean complexes.
For each cell choose a subset of vertices and an acyclic orientation of each
selected path edge. Boundaries are simplicial-position deletion maps.
"""
from collections import defaultdict
from itertools import product


def cells(n):
 out=defaultdict(list)
 for mask in range(1,1<<n):
  edges=[i for i in range(n-1) if (mask >> i)&3 == 3]
  for choices in product((0,1),repeat=len(edges)):
   bits=sum(b << i for i,b in zip(edges,choices))
   out[mask.bit_count()-1].append((mask,bits))
 return out

def boundary(n,c):
 mask,bits=c
 vertices=[i for i in range(n) if (mask>>i)&1]
 bd={}
 for j,i in enumerate(vertices):
  mm=mask&~(1<<i)
  bb=bits
  if i:bb &= ~(1<<(i-1))
  if i<n-1:bb &= ~(1<<i)
  bd[(mm,bb)] = (-1)**j
 return bd

def reflection(n,c):
 mask,bits=c
 mm=sum(1<<(n-1-i) for i in range(n) if (mask>>i)&1)
 bb=0
 for i in range(n-1):
  if (mask>>i)&3==3:
   if not ((bits>>i)&1):bb |= (1<<(n-2-i))
 sign=(-1)**(mask.bit_count()//2)
 return (mm,bb),sign

def rank_mod(columns,p=101):
 piv={}
 for col in columns:
  v={i:x%p for i,x in col.items() if x%p}
  while v:
   j=min(v)
   if j not in piv:
    t=pow(v[j],-1,p);piv[j]={k:(w*t)%p for k,w in v.items()};break
   scale=v[j]
   for k,w in piv[j].items():
    x=(v.get(k,0)-scale*w)%p
    if x:v[k]=x
    elif k in v:del v[k]
 return len(piv)

def fibonacci(k):
 a,b=0,1
 for _ in range(k):a,b=b,a+b
 return a

def expected_trace(n):
 if n%2:
  m=(n-1)//2
  return (-1)**m*fibonacci(m)
 m=n//2
 if m==1:return 1
 if m==2:return 0
 return (-1)**(m-1)*fibonacci(m-2)

def verify(n,full=True):
 C=cells(n)
 count={d:len(v) for d,v in sorted(C.items())}
 T=defaultdict(int)
 for d,cs in C.items():
  for c in cs:
   rc,s=reflection(n,c)
   assert reflection(n,rc)[0]==c
   if rc==c:T[d]+=s
   bd=boundary(n,c)
   for f,coef in bd.items():
    if f[0]:
     assert f in C[d-1] if n<=6 else True
   if full:
    refbd=boundary(n,rc)
    lhs={f:s*a for f,a in refbd.items()}
    rhs={}
    for f,a in bd.items():
     rf,z=reflection(n,f)
     rhs[rf]=rhs.get(rf,0)+a*z
    assert lhs==rhs,('NOT_CHAIN_MAP',n,c,lhs,rhs)
    if d>=2:
     dd={}
     for f,a in bd.items():
      for g,b in boundary(n,f).items():dd[g]=dd.get(g,0)+a*b
     assert all(x==0 for x in dd.values()),('D2',n,c,dd)
 reduced_lefschetz=-1+sum((-1)**d*t for d,t in T.items())
 trace=(-1)**(n-1)*reduced_lefschetz
 assert trace==expected_trace(n),(n,trace,expected_trace(n))
 assert (fibonacci(n-1)+trace)%2==0
 ranks=None;bettis=None
 if full:
  ranks={}
  for d in range(1,n):
   idx={c:i for i,c in enumerate(C[d-1])}
   col=[{idx[f]:a for f,a in boundary(n,c).items()} for c in C[d]]
   ranks[d]=rank_mod(col)
  bettis={d:len(C[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(n)}
  assert bettis=={d:(1 if d==0 else fibonacci(n-1) if d==n-1 else 0) for d in range(n)} if n>=3 else True
 print('n=%d cells=%s signed_fixed_traces=%s reduced_lefschetz=%d top_trace=%d beta=%d invariant=%d anti=%d %s' % (n, count,dict(sorted(T.items())),reduced_lefschetz,trace,fibonacci(n-1),(fibonacci(n-1)+trace)//2,(fibonacci(n-1)-trace)//2, 'homology='+str(bettis) if full else ''),flush=True)

if __name__=='__main__':
 for n in range(2,9):verify(n,full=True)
 for n in range(9,13):verify(n,full=False)
 print('VERIFY_OK')
