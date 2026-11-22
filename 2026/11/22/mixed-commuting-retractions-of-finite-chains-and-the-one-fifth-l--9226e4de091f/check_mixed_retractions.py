from itertools import product

def compose(f,g):return tuple(f[g[i]] for i in range(len(f)))
def is_idem(f):return compose(f,f)==f

def monotone(f):return all(f[i]<=f[i+1] for i in range(len(f)-1))
def clamp(n,a,b):return tuple(min(max(i,a),b) for i in range(n))
def B(k):
 if k==0:return 0
 c=1 # B1
 for n in range(2,k+1):
  z=[1]
  for d in range(1,n):z.append(d)
  # use compositions
 from functools import lru_cache
 @lru_cache(None)
 def f(v): return 1 if v==0 else sum(d*f(v-d) for d in range(1,v+1))
 return f(k-1)
def E(k):return sum(B(i) for i in range(1,k+1))
def N(k):return sum((k-i+1)*B(i) for i in range(1,k+1)) if k>=1 else 0

def pred(n,a,b):
 L=b-a+1
 return B(L)*E(a)*E(n-b+1)+E(L-1)*(E(a)+E(n-b+1))+N(L-2)
for n in range(1,8):
 maps=[t for t in product(range(n), repeat=n) if monotone(t) and is_idem(t)]
 total=0
 for a in range(n):
  for b in range(a,n):
   c=clamp(n,a,b)
   actual=sum(compose(c,f)==compose(f,c) for f in maps)
   expected=pred(n,a+1,b+1)
   assert actual==expected,(n,a,b,actual,expected)
   total+=actual
 print('n',n,'monotone_idempotents',len(maps),'mixed_commuting_pairs',total)
print('MIXED_CLAMP_CHECK_PASSED')
