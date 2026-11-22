"""Exact finite certificates for the no-adjacent-ones one-asymmetric-error channel.

Run with Python 3.9 or later: python z_channel_fib_verify.py.
No third-party dependencies; arithmetic is integer or Fraction.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations

MAX_CODE = {
 1:['0'],
 2:['00'],
 3:['000','101'],
 4:['0000','0101','1010'],
 5:['00100','01001','10010','10101'],
 6:['000000','001001','010010','010101','100100','101010'],
 7:['0000010','0010001','0100101','0101010','1000100','1001001','1010010','1010101'],
}
EARLY_DUAL = {
 1:['0'],
 2:['00'],
 3:['000','101'],
 4:['0000','0001','1010'],
 5:['00000','00101','01000','10000'],
 6:['000000','000001','000010','010100','100100','101000'],
}
FRACTIONAL_PRIMAL = {
 '0000000':1, '0001010':Fraction(1,2), '0010001':1,
 '0100010':Fraction(1,2), '0100101':1, '0101000':Fraction(1,2),
 '0101010':Fraction(1,2), '1000100':1, '1001001':1,
 '1010010':1, '1010101':1,
}
FRACTIONAL_DUAL = {
 '0000000':1,'0000101':1,'0001001':1,'0001010':1,
 '0010000':1,'0100000':1,'1000000':1,
 '1010000':Fraction(1,2),'1010001':Fraction(1,2),
 '1010010':Fraction(1,2),'1010100':Fraction(1,2),
}
CLIQUES_7 = [
 ['0000000','0100000','1000000','0000001','0001000','0010000','0000010','0000100'],
 ['0000100','0010100','0100100','1000100','0000101'],
 ['0001010','0100010','0101000','0101010'],
 ['0010000','1010000','0010001','0010010','0010100'],
 ['0010101','1000101','1010001','1010100','1010101'],
 ['0100101','0100001','0101001'],
 ['1000001','1001001','1001000','0001001'],
 ['1001010','1000010','1010010'],
]

def source_words(n):
 return [''.join(bits) for bits in __import__('itertools').product('01',repeat=n) if '11' not in ''.join(bits)]

def reads(x):
 return {x} | {x[:i]+'0'+x[i+1:] for i,b in enumerate(x) if b=='1'}

def verify():
 # Every source and read remains within the Fibonacci constraint.
 for n in range(1,8):
  words=source_words(n); W=set(words)
  assert all(reads(x)<=W for x in words)
  code=MAX_CODE[n]
  assert len(code)==len(set(code)) and set(code)<=W
  seen=set()
  for x in code:
   assert not seen.intersection(reads(x)),(n,x)
   seen.update(reads(x))
  if n<=6:
   support=set(EARLY_DUAL[n]); assert support<=W
   assert len(support)==len(code)
   for x in words: assert reads(x)&support,(n,x)
 # Exact fractional primal: one unit of available capacity per possible read.
 weights={x:Fraction(v) for x,v in FRACTIONAL_PRIMAL.items()}
 dual={y:Fraction(v) for y,v in FRACTIONAL_DUAL.items()}
 W=set(source_words(7))
 assert set(weights)<=W and set(dual)<=W
 assert sum(weights.values())==sum(dual.values())==9
 for y in W: assert sum((v for x,v in weights.items() if y in reads(x)),Fraction(0))<=1,(y,'primal')
 for x in W: assert sum((v for y,v in dual.items() if y in reads(x)),Fraction(0))>=1,(x,'dual')
 # Exact integral upper bound by 8 vertex-covering confusability cliques.
 assert len(CLIQUES_7)==8
 assert set().union(*(set(c) for c in CLIQUES_7))==W
 for C in CLIQUES_7:
  assert len(C)==len(set(C))
  for x,y in combinations(C,2):assert reads(x)&reads(y),(x,y)
 # An independent exact recurrence counts all maximum compatible codebooks.
 words=source_words(7)
 adj=[0]*len(words)
 for i,x in enumerate(words):
  for j,y in enumerate(words):
   if i!=j and reads(x)&reads(y):adj[i]|=1<<j
 @lru_cache(None)
 def independent_set_profile(mask):
  if not mask:return 0,1
  best=-1;which=-1
  mm=mask
  while mm:
   b=mm&-mm;i=b.bit_length()-1;mm-=b
   degree=(mask&adj[i]).bit_count()
   if degree>best:best=degree;which=i
  if best==0:return mask.bit_count(),1
  bit=1<<which
  a,ac=independent_set_profile(mask&~bit)
  b,bc=independent_set_profile(mask&~(bit|adj[which]));b+=1
  if a==b:return a,ac+bc
  return (a,ac) if a>b else (b,bc)
 assert independent_set_profile((1<<len(words))-1)==(8,10)
 return {'source_counts':[len(source_words(n)) for n in range(1,8)],
         'integral_code_optima':[len(MAX_CODE[n]) for n in range(1,8)],
         'LP_optima':[str(len(MAX_CODE[n])) for n in range(1,7)]+['9'],
         'maximum_codebook_count_n7':10,
         'number_of_finite_DFS_states':independent_set_profile.cache_info().currsize}

if __name__=='__main__':
 print('PASS',verify())
