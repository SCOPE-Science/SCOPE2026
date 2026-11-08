"""Exact self-contained checks for five-symbol binary permutation-burst spheres.
Python 3 standard library only. All computations use integer arithmetic.
"""
from itertools import product, combinations
from math import comb

STATES = tuple(product((0, 1), repeat=4))
TERMINAL16 = {
 '0000':(63,2), '0001':(68,2), '0010':(66,3), '0011':(70,1),
 '0100':(66,1), '0101':(68,1), '0110':(68,1), '0111':(68,1),
 '1000':(68,1), '1001':(68,1), '1010':(68,1), '1011':(66,1),
 '1100':(70,1), '1101':(66,3), '1110':(68,2), '1111':(63,2),
}
INITIAL_MAX_COUNTS = {
 5:(10,20), 6:(16,8), 7:(22,2), 8:(26,14),
 9:(32,4),10:(38,2),11:(42,10),12:(48,4),13:(54,2),
 14:(58,10),15:(64,4),16:(70,2),17:(74,10),18:(80,4),
}

def choose(n,r):
 return comb(n,r) if 0<=r<=n else 0

def contribution(v):
 """Outputs whose first and last *changed* sites are v's endpoints."""
 length=len(v)
 a=v[0]+v[-1]
 inside=sum(v[1:-1])
 return choose(length-2,inside+2*a-2)

def local_count(x):
 n=len(x)
 return 1+sum(contribution(x[i:i+length])
   for length in range(2,min(5,n)+1)
   for i in range(n-length+1))

def source_count(x):
 """Independent published first-changed-position formula, for n>=5."""
 n=len(x)
 return sum(choose(4,sum(x[i+1:i+5])+(1 if x[i] else -1))
            for i in range(n-4)) + choose(4,sum(x[n-4:]))

def brute_count(x):
 """Directly form distinct output words without using either counting formula."""
 n=len(x)
 outputs=set()
 for i in range(n-4):
  w=sum(x[i:i+5])
  for indices in combinations(range(5),w):
   block=[0]*5
   for j in indices:block[j]=1
   outputs.add(x[:i]+tuple(block)+x[i+5:])
 return len(outputs)

def evolve(V):
 next_v={s:(-10**12,0) for s in STATES}
 for s,(value,num) in V.items():
  for bit in (0,1):
   word=s+(bit,)
   dest=word[1:]
   extra=sum(contribution(word[-length:]) for length in range(2,6))
   candidate=value+extra
   score,count=next_v[dest]
   if candidate>score:
    next_v[dest]=(candidate,num)
   elif candidate==score:
    next_v[dest]=(score,count+num)
 return next_v

def maximum(V):
 score=max(v for v,c in V.values())
 return score,sum(c for v,c in V.values() if v==score)

def formula(n):
 assert n>=5
 m,r=divmod(n,3)
 return 16*m+(-16,-10,-6)[r]

def count_formula(n):
 if n==5:return 20
 if n==6:return 8
 if n==8:return 14
 return (4,2,10)[n%3]

def run():
 V={s:(local_count(s),1) for s in STATES}
 rows={4:V}
 for n in range(5,46):
  V=evolve(V)
  rows[n]=V
  assert maximum(V)[0]==formula(n),(n,maximum(V),formula(n))
  assert maximum(V)[1]==count_formula(n),(n,maximum(V),count_formula(n))
  if n in INITIAL_MAX_COUNTS:assert maximum(V)==INITIAL_MAX_COUNTS[n]
 assert {''.join(map(str,s)):p for s,p in rows[16].items()}==TERMINAL16
 assert all(rows[19][s]==(rows[16][s][0]+16,rows[16][s][1]) for s in STATES)
 assert all(rows[n+3][s]==(rows[n][s][0]+16,rows[n][s][1])
            for n in range(16,43) for s in STATES)
 print('Exact 16-state recurrence, 16->19 shift identity, and all 5..45 maxima/counts: PASS')
 tested=0
 for n in range(5,13):
  hist={}
  for x in product((0,1), repeat=n):
   a=brute_count(x)
   b=local_count(x)
   c=source_count(x)
   assert a==b==c,(n,x,a,b,c)
   hist[a]=hist.get(a,0)+1
   tested+=1
  peak=max(hist)
  assert (peak,hist[peak])==(formula(n),count_formula(n)),(n,peak,hist)
 print('Direct distinct-output enumeration + two independent formulas:',tested,'words, lengths 5..12: PASS')
 # An independent exhaustive check of the *entire state vector* at the critical
 # lengths, from the published first-changed-position formula rather than DP.
 for length in (16,19):
  weights={v:choose(4, ((v>>1)&15).bit_count()+ (1 if v&1 else -1))
           for v in range(32)}
  suffix={v:choose(4,v.bit_count()) for v in range(16)}
  direct={s:(-10**12,0) for s in STATES}
  for word in range(1<<length):
   score=sum(weights[(word>>i)&31] for i in range(length-4))
   score+=suffix[(word>>(length-4))&15]
   term=tuple((word>>(length-4+j))&1 for j in range(4))
   old,num=direct[term]
   if score>old:direct[term]=(score,1)
   elif score==old:direct[term]=(score,num+1)
  assert direct==rows[length],('independent statewise',length)
 print('Independent exhaustive per-state formula enumeration at lengths 16 and 19: PASS')
 print('ALL_CERTIFICATES_OK')

if __name__=='__main__':run()
