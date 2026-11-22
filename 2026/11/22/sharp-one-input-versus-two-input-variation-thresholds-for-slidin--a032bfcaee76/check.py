"""Self-contained exact and numerical checks for sliding four-point central spacings."""
from fractions import Fraction
from itertools import product, permutations
from random import Random

P = {
    '0000':0,'0001':2,'0010':0,'0011':1,
    '0100':0,'0101':1,'0110':1,'0111':0,
    '1000':0,'1001':1,'1010':1,'1011':0,
    '1100':1,'1101':0,'1110':2,'1111':0,
}
def var(y):
    return sum(abs(b-a) for a,b in zip(y,y[1:]))
def gap4(x):
    return [sorted(x[i:i+4])[2]-sorted(x[i:i+4])[1] for i in range(len(x)-3)]
def dstep(x,j):
    out=[]
    for i in range(len(x)-3):
        indices=sorted(range(i,i+4),key=lambda k:x[k])
        out.append((indices[2]>j)-(indices[1]>j))
    return out

def binary_g4(s):return int(s.count('1')==2)
# The 16-state, 32-edge exact Bellman potential certificate applies at every input length.
assert len(P)==16
for s,p in P.items():
    assert p>=0 and p<=2*sum(a!=b for a,b in zip(s,s[1:])), s
    for t in '01':
        dest=s[1:]+t
        reward=abs(binary_g4(s)-binary_g4(dest))-2*int(s[-1]!=t)
        assert p>=reward+P[dest],(s,t,p,reward,P[dest])
print('EXACT_16_STATE_BINARY_COAREA_CERTIFICATE_PASS 16 32')

# Exact derivative columns for strict rank-order chambers, exhaustive through length eight.
K={4:0,5:2,6:4,7:5,8:6}
for n in range(4,9):
    upper=0
    for x in permutations(range(n)):
        for j in range(n-1):upper=max(upper,var(dstep(x,j)))
        if upper>K[n]: raise AssertionError((n,upper,x))
    assert upper==K[n],(n,upper)
print('ALL_STRICT_RANK_CHAMBERS_PASS n=4..8')

# Finite exact attaining pairs, and persistent n>=8 embedding.
base={
    5: ((0,2,1,3,4), 1),
    6: ((0,1,3,2,4,5), 2),
    7: ((0,1,3,2,4,5,6), 2),
    8: ((0,1,2,4,3,5,6,7), 3),
}
for n in range(5,31):
    x0,j=base.get(n,base[8]);x=list(map(Fraction,x0))
    if n>8:x.extend(map(Fraction,range(8,n)))
    h=[Fraction(k>j) for k in range(n)];eps=Fraction(1,4)
    y=[a+eps*b for a,b in zip(x,h)]
    u=gap4(x);v=gap4(y)
    achieved=var([b-a for a,b in zip(u,v)])/var([b-a for a,b in zip(x,y)])
    assert achieved==K.get(n,6),(n,achieved)
print('EXACT_TWO_INPUT_ATTAINING_PAIRS_PASS n=5..30')

# One-input endpoints via binary step, and n=5 single replacement.
for n in range(5,31):
    if n==5:
        x=[0,0,0,1,1];tar=1
    else:
        x=[0,0,0]+[1]*(n-3);tar=2
    assert var(gap4(x))==tar*var(x),(n,gap4(x))
print('EXACT_ONE_INPUT_SHARPNESS_PASS n=5..30')

rng=Random(20261117)
for n in (4,5,6,7,8,12,30):
  for k in range(500):
    x=[Fraction(rng.randrange(-30,31),rng.randrange(1,11)) for _ in range(n)]
    y=[Fraction(rng.randrange(-30,31),rng.randrange(1,11)) for _ in range(n)]
    h=[a-b for a,b in zip(x,y)]
    if var(h): assert var([a-b for a,b in zip(gap4(x),gap4(y))])<=K.get(n,6)*var(h)
    assert var(gap4(x)) <= (0 if n==4 else 1 if n==5 else 2)*var(x)
print('RANDOM_RATIONAL_PAIR_AND_ONE_INPUT_STRESS_PASS 3500')
print('FOUR_POINT_CENTRAL_SPACING_ALL_CHECKS_PASS')
