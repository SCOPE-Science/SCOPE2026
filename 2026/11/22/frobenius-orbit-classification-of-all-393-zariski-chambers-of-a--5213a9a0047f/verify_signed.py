from itertools import combinations,permutations
from collections import Counter,defaultdict
from math import lcm
V=[x for x in range(32) if x.bit_count()%2==0]; ix={v:i for i,v in enumerate(V)}
# Geometric negative curves: 0=Q, weight2= L_ij, weight4=E_i.
E=[sum(1<<j for j in range(5) if j!=i) for i in range(5)]
L={(i,j):(1<<i)|(1<<j) for i in range(5) for j in range(i+1,5)}
# All distinct vertex masks satisfying no Hamming dist four.
supports=[mask for mask in range(1<<16) if all((V[i]^V[j]).bit_count()!=4 for i,j in combinations([i for i in range(16) if mask>>i&1],2))]
assert len(supports)==393
S=set(supports)
counts=Counter(m.bit_count() for m in supports)
def transform_bitset(x,eps,perm):
 y=eps
 for i in range(5):
  if x>>i&1:y^=1<<perm[i]
 return y

def support_perm(eps,perm):
 return tuple(ix[transform_bitset(v,eps,perm)] for v in V)

def mapped_support(s,p):
 t=0
 while s:
  low=s&-s; t|=1<<p[low.bit_length()-1];s^=low
 return t

def signature(eps,perm):
 seen=set(); a=[]
 for i in range(5):
  if i in seen:continue
  j=i;cyc=[]
  while j not in seen:
   seen.add(j);cyc.append(j);j=perm[j]
  neg=sum((eps>>j)&1 for j in cyc)%2
  a.append((len(cyc),neg))
 return tuple(sorted(a,reverse=True))

def cycle_profile(perm):
 seen=set();out=Counter();F=Counter()
 for s in supports:
  if s in seen:continue
  t=s;n=0
  while t not in seen:
   seen.add(t);n+=1;t=mapped_support(t,perm)
  assert t==s
  out[n]+=1
  if n==1:F[s.bit_count()]+=1
 return out,F

rep={}; sizes=Counter();checks={}
for prm in permutations(range(5)):
 for eps in range(32):
  if eps.bit_count()%2:continue
  sig=signature(eps,prm);sizes[sig]+=1
  p=support_perm(eps,prm)
  if sig not in rep: rep[sig]=(eps,prm,p)
  if sig not in checks:checks[sig]=cycle_profile(p)
  assert cycle_profile(p)==checks[sig],(sig,eps,prm)
assert len(rep)==18 and sum(sizes.values())==1920

def sig_label(sig):
 return ' '.join(str(n)+('-' if neg else '+') for n,neg in sig)
for sig in sorted(rep,reverse=True):
 prof,F=checks[sig]
 eps,prm,p=rep[sig]
 print(f'{sig_label(sig):18s} |class {sizes[sig]:4} |rational {sum(F.values()):3} |fixed support-size {dict(sorted(F.items()))} |orbit profile {dict(sorted(prof.items()))}')
print('geometric',dict(sorted(counts.items())),'classes',len(rep))
