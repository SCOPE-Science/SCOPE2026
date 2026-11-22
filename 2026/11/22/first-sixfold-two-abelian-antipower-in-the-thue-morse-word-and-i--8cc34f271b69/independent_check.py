"""Independent two-block exhaustive and direct factor-frequency certificate."""
from collections import Counter
from fractions import Fraction

blocks={'0':'0','1':'1'}
for _ in range(6):
 blocks={k:''.join('01' if b=='0' else '10' for b in value) for k,value in blocks.items()}
B=64
assert all(len(s)==B for s in blocks.values())
weights={'00':Fraction(1,6),'01':Fraction(1,3),'10':Fraction(1,3),'11':Fraction(1,6)}


def all_factors(m):
 return set().union(*(
   { (blocks[p[0]]+blocks[p[1]])[i:i+m] for i in range(B)}
   for p in weights
 ))


def profile(v):
 pairs=Counter(v[i:i+2] for i in range(len(v)-1))
 return (v[0],v[-1],pairs['00'],pairs['01'],pairs['10'],pairs['11'])


def qualifying(word,n,k):
 classes=[profile(word[i*n:(i+1)*n]) for i in range(k)]
 return len(set(classes))==k

expected=[2,4,4,4,6]
for n in range(1,6):
 maxima=[k for k in range(2,8) if any(qualifying(s,n,k) for s in all_factors(n*k))]
 assert max(maxima)==expected[n-1], (n,maxima)
 assert not any(qualifying(s,n,expected[n-1]+1) for s in all_factors(n*(expected[n-1]+1)))
print('ROOT_MAXIMA_OK',expected)

f30=all_factors(30)
good=sorted(x for x in f30 if qualifying(x,5,6))
assert len(f30)==90 and len(good)==12
assert len({profile(x[i:i+5]) for i in range(6) for x in good})==6
assert not any(qualifying(x,5,7) for x in all_factors(35))

# Direct two-superblock weighted occurrence counts, without using a
# recursive factor-frequency algorithm.
freqs={}
for x in good:
 f=Fraction(0)
 for pair,weight in weights.items():
  s=blocks[pair[0]]+blocks[pair[1]]
  count=sum(s[i:i+30]==x for i in range(B))
  f+=weight*Fraction(count,B)
 freqs[x]=f
assert set(freqs.values())=={Fraction(1,96)}
assert sum(freqs.values(),Fraction(0))==Fraction(1,8)
assert all(len(x)==30 for x in good)
print('ALL_TWELVE_TEMPLATES_FREQUENCY_1_96_OK')
print('DENSITY_1_8_OK')
print('PASS')
