"""Exhaustive factor-complete certificate for a Thue--Morse 2-Abelian antipower boundary."""
from collections import Counter
from fractions import Fraction

def morph(w): return ''.join('01' if a=='0' else '10' for a in w)
w='0'
for _ in range(9): w=morph(w)
assert len(w)==512

def signature(word):
 return (word[0],word[-1],sum(word[j:j+2]=='00' for j in range(len(word)-1)),sum(word[j:j+2]=='11' for j in range(len(word)-1)))

def rainbow(block,L,m):
 return len({signature(block[j*L:(j+1)*L]) for j in range(m)})==m

def factors(length):return {w[i:i+length] for i in range(len(w)-length+1)}
# Every length <= 64 factor occurs in this prefix, by the four input digrams
# in 01101001 and the length-64 substitution blocks.
assert {w[i:i+2] for i in range(7)}==set(('00','01','10','11'))
maximal={}
for L in range(1,6):
 scores={m:sum(map(lambda a:rainbow(a,L,m),factors(L*m))) for m in range(2,8)}
 top=max(m for m,n in scores.items() if n>0)
 maximal[L]=top
 print('ROOT',L,'max',top,'classes2..7',scores)
assert maximal=={1:2,2:4,3:4,4:4,5:6}
G=sorted(f for f in factors(30) if rainbow(f,5,6))
assert len(G)==12 and len(factors(30))==90
assert not any(rainbow(a,5,7) for a in factors(35))
print('RAINBOW_TEMPLATES',len(G));print('\n'.join(G))

# Uniform morphism frequency recursion: the count of a length-m factor is the
# half-sum of its even/odd phase preimage frequencies; m strictly decreases.
cache={2:{'00':Fraction(1,6),'01':Fraction(1,3),'10':Fraction(1,3),'11':Fraction(1,6)}}
def freq(m):
 if m in cache:return cache[m]
 assert m>=3
 result=Counter()
 for r in (0,1):
  length=(m+r+1)//2
  for u,f in freq(length).items():
   v=morph(u)[r:r+m]
   assert len(v)==m
   result[v]+=f/2
 assert sum(result.values())==1
 cache[m]=dict(result)
 return cache[m]
F=freq(30)
assert set(G).issubset(F)
rate=sum((F[x] for x in G),Fraction(0))
print('FREQ',[(x,str(F[x])) for x in G])
print('DENSITY',rate)
assert rate==Fraction(1,8) and len(F)==90
print('FIRST_WITNESS',3,w[3:33])
print('PASS')
