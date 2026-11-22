from itertools import combinations
from functools import lru_cache
from collections import Counter
from math import factorial, comb

def partitions(n,k=None):
 if n==0:yield ();return
 if k is None:k=n
 for a in range(min(n,k),0,-1):
  for b in partitions(n-a,a):yield(a,)+b

def perm(parts):
 out=[];s=0
 for r in parts:
  out+=list(range(s+1,s+r))+[s];s+=r
 return out

def chi9(parts):
 c=[1]+[0]*6
 for r in parts:
  z=(-1)**(r+1)
  for j in range(6,r-1,-1):c[j]+=z*c[j-r]
 return c[6]

def make_orbits(parts):
 p=perm(parts);T=[tuple(x) for x in combinations(range(7),3)]
 ix={a:i for i,a in enumerate(T)};nxt=[ix[tuple(sorted(p[v] for v in a))] for a in T]
 vis=set();arr=[]
 for i in range(len(T)):
  if i in vis:continue
  orbit=[];j=i
  while j not in vis:vis.add(j);orbit.append(j);j=nxt[j]
  if all(set(T[a]) & set(T[b]) for a,b in combinations(orbit,2)):
   arr.append(orbit)
 return T,arr

def calc(parts):
 T,orbs=make_orbits(parts)
 k=len(orbs);N=[0]*k
 for i in range(k):
  for j in range(i+1,k):
   if any(set(T[a]).isdisjoint(T[b]) for a in orbs[i] for b in orbs[j]):
    N[i]|=1<<j;N[j]|=1<<i
 @lru_cache(None)
 def I(mask):
  if mask==0:return 1
  # choose vertex of maximum conflict degree for better split
  u=max((i for i in range(k) if mask>>i&1), key=lambda i:(N[i]&mask).bit_count())
  v=1<<u
  return I(mask^v)-I(mask &~(N[u]|v))
 ip=I((1<<k)-1)
 return {'parts':parts,'eligible_orbits':k,'is_poly_at_neg1':ip,'Ltilde':-ip,'H9':chi9(parts),'H6':chi9(parts)-ip,'cache_states':I.cache_info().currsize}

def contains(part,other):return len(other)<=len(part) and all(x<=y for x,y in zip(other,part))

def cells(part):return {(i,j) for i,row in enumerate(part) for j in range(row)}
@lru_cache(None)
def chi(part,mu):
 if not mu:return int(not part)
 r=mu[0];total=0
 for q in partitions(sum(part)-r) if sum(part)>=r else []:
  if not contains(part,q):continue
  skew=cells(part)-cells(q)
  if len(skew)!=r:continue
  # connected
  seen={next(iter(skew))};front=list(seen)
  while front:
   i,j=front.pop()
   for o in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
    if o in skew and o not in seen:seen.add(o);front.append(o)
  if len(seen)<len(skew):continue
  if any((i+1,j) in skew and (i,j+1) in skew and (i+1,j+1) in skew for i,j in skew):continue
  total+=(-1)**(len({i for i,j in skew})-1)*chi(q,mu[1:])
 return total

def z(part):
 cc=Counter(part);out=1
 for r,m in cc.items():out*=r**m*factorial(m)
 return out
# Further independent check: enumerate all compatible orbit subfamilies directly,
# rather than use the independence-polynomial deletion recurrence above.
def direct_signed_sum(parts):
    triples,orbits=make_orbits(parts)
    k=len(orbits)
    compatible=[]
    for i,oi in enumerate(orbits):
        allowed=0
        for j,oj in enumerate(orbits):
            if i!=j and all(set(triples[a]) & set(triples[b]) for a in oi for b in oj):
                allowed|=1<<j
        compatible.append(allowed)
    def visit(rest,sgn):
        total=sgn
        while rest:
            bit=rest & -rest;rest^=bit
            j=bit.bit_length()-1
            total+=visit(rest & compatible[j], -sgn)
        return total
    return visit((1<<k)-1,1)

def full_check():
    parts=list(partitions(7))
    rows=[calc(p) for p in parts]
    for row in rows:
        p=row['parts']
        assert row['is_poly_at_neg1']==direct_signed_sum(p),(p,'recurrence-versus-enumeration')
        assert row['H6']==1+chi((4,3),p)+chi((2,2,2,1),p),p
        assert row['H6']==chi9(p)-row['is_poly_at_neg1'],p
        assert chi((4,3),p)==(-1)**(7-len(p))*chi((2,2,2,1),p),p
    assert rows[-1]['H6']==29 and rows[-1]['H9']==7
    assert chi((4,3),(1,)*7)==14 and chi((2,2,2,1),(1,)*7)==14
    # Orthogonality against ALL 15 irreducible rational characters of S_7.
    mult={p:sum(row['H6']*chi(p,row['parts'])*factorial(7)//z(row['parts'])
                 for row in rows)//factorial(7) for p in parts}
    assert mult=={p:(1 if p in [(7,),(4,3),(2,2,2,1)] else 0) for p in parts}
    print('cycle type | eligible triple-orbits | signed orbit sum | trace H9 | trace H6')
    for row in rows: print('%s | %s | %s | %s | %s'%(
        ','.join(map(str,row['parts'])),row['eligible_orbits'],
        row['is_poly_at_neg1'],row['H9'],row['H6']))
    print('H6=Specht(7)+Specht(4,3)+Specht(2,2,2,1)')
    print('checks: 15 class representatives, independent orbit enumeration, 15 character inner products, all PASS')

if __name__=='__main__':
    full_check()
