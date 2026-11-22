"""Independent finite checks for the balanced associahedron eight-colouring theorem.
Run: python3 verify.py
"""
from functools import lru_cache
from collections import Counter

LEAF='*'
PATTERNS={
 (0,0):'(*(*(*(**))))',
 (0,1):'((**)((**)*))',
 (1,0):'(*(*((**)*)))',
 (1,1):'(*((**)(**)))',
}
PAIR=('((((**)*)*)*)','((*(**))(**))')


def parse(word):
 def go(pos):
  if word[pos]=='*':return None,pos+1
  assert word[pos]=='('
  x,p=go(pos+1)
  y,p=go(p)
  assert word[p]==')'
  return (x,y),p+1
 t,end=go(0)
 assert end==len(word)
 return t


def encode(t):
 return '*' if t is None else '('+encode(t[0])+encode(t[1])+')'


def q(a,b):
 return (a[0]^a[1]^b[0],a[1]^b[0]^b[1]^1)


def label(t):
 return (0,0) if t is None else q(label(t[0]),label(t[1]))


def recursive(t):
 """Obtain label, parity with an incoming preferred-path depth of 0 or 1."""
 if t is None:return (0,0),(0,0)
 a,da=recursive(t[0]);b,db=recursive(t[1])
 preferred_left=(a[1]^b[0])==0
 return q(a,b), ((1^da[1]^db[0],da[0]^db[0]) if preferred_left
                     else (da[0]^db[1],da[0]^db[0]))


def direct_parity(t):
 """Walk the preferred-path forest explicitly, without using the parity recursion."""
 def visit(node,depth):
  if node is None:return 0
  a=label(node[0]);b=label(node[1]);left=(a[1]^b[0])==0
  if left:return (1 if depth%2==0 else 0)^visit(node[0],depth+1)^visit(node[1],0)
  return visit(node[0],0)^visit(node[1],depth+1)
 return (visit(t,0),visit(t,1))


@lru_cache(None)
def trees(n):
 if n==1:return (None,)
 return tuple((a,b) for i in range(1,n) for a in trees(i) for b in trees(n-i))


def has_pattern(t,pats):
 if t is None:return False
 return encode(t) in pats or has_pattern(t[0],pats) or has_pattern(t[1],pats)


def rotations(t):
 if t is None:return set()
 out=set()
 a,b=t
 if a is not None:out.add((a[0],(a[1],b)))
 if b is not None:out.add(((a,b[0]),b[1]))
 for c in rotations(a):out.add((c,b))
 for c in rotations(b):out.add((a,c))
 return out


def forbidden_counts(m,nmax):
 # a(1)=1; a(n) = convolution a(i)a(n-i) - m*[n==5]
 d=[0]*(nmax+1);d[1]=1
 for n in range(2,nmax+1):
  d[n]=sum(d[i]*d[n-i] for i in range(1,n))-(m if n==5 else 0)
 return d


def graft(tree, address, replacement):
 if not address:return replacement
 if address[0]==0:return (graft(tree[0],address[1:],replacement),tree[1])
 return (tree[0],graft(tree[1],address[1:],replacement))

def leaf_addresses(t,address=()):
 if t is None:return [address]
 return leaf_addresses(t[0],address+(0,))+leaf_addresses(t[1],address+(1,))

def main():
 P={k:parse(v) for k,v in PATTERNS.items()}
 assert len(set(P.values()))==4
 for k,t in P.items():
  assert encode(t).count('*')==5
  assert label(t)==k
 s,t=tuple(parse(z) for z in PAIR)
 assert s!=t and encode(s).count('*')==encode(t).count('*')==5
 assert recursive(s)==((0,0),(0,0)),recursive(t)==((0,0),(1,1))
 assert direct_parity(s)==(0,0) and direct_parity(t)==(1,1)
 print('FOUR_LABEL_WITNESSES_AND_TWO_PARITY_WITNESSES_PASS')
 for n in range(1,8):
  for context in trees(n):
   for address in leaf_addresses(context):
    variants=[graft(context,address,P[k]) for k in sorted(P)]
    assert {label(v) for v in variants}==set(P)
    u=graft(context,address,s);v=graft(context,address,t)
    assert label(u)==label(v)
    assert direct_parity(u)[0]^direct_parity(v)[0]==1
 print('ALL_SMALL_GRAFT_CONTEXTS_LABEL_BIJECTION_AND_PARITY_FLIP_PASS')
 for n in range(1,11):
  all_t=trees(n)
  for t in all_t:
   assert label(t)==recursive(t)[0]
   assert direct_parity(t)==recursive(t)[1]
  if n>=3 and n<=8:
   universe=set(all_t)
   for t in all_t:
    for u in rotations(t):
     assert u in universe
     assert (label(t),direct_parity(t)[0])!=(label(u),direct_parity(u)[0])
  total=len(all_t)
  seen4=Counter(label(t) for t in all_t if has_pattern(t,set(PATTERNS.values())))
  assert len(set(seen4.values()))<=1
  two=set(PAIR)
  signed=Counter()
  for t in all_t:
   if has_pattern(t,two):
    k,p=recursive(t)
    signed[k]+=1 if p[0]==0 else -1
  assert all(v==0 for v in signed.values())
  avoid2=sum(not has_pattern(t,two) for t in all_t)
  avoid4=sum(not has_pattern(t,set(PATTERNS.values())) for t in all_t)
  assert avoid2==forbidden_counts(2,n)[n]
  assert avoid4==forbidden_counts(4,n)[n]
  counts=Counter((label(t),direct_parity(t)[0]) for t in all_t)
  assert all(abs(8*counts[k,b]-total)<=7*avoid2 for k in P for b in (0,1))
  print(f'EXHAUSTIVE n={n} Catalan={total} forbidden2={avoid2} forbidden4={avoid4} eight_counts={[counts[k,b] for k in sorted(P) for b in (0,1)]}')
 print('INDEPENDENT_PATH_DEPTH_RECURSION_AND_ROTATION_CHECK_PASS')
 print('FIRST_FRINGE_PATTERN_BALANCE_AND_FORBIDDEN_RECURRENCE_PASS')
 print('VERIFY_OK')

if __name__=='__main__':main()
