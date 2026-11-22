# Independent quotient-field construction and reverse (last-element) dynamic program.
from itertools import product
from collections import Counter,defaultdict
from math import comb

def gf4_mul(a,b):
    # polynomial x^2+x+1, independent of the bit-by-bit reduction used by C++
    table=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
    return table[a][b]

vectors=list(product(range(4),repeat=3))
normalized=[]
for u in vectors[1:]:
    nonzero=next(x for x in u if x)
    inv={1:1,2:3,3:2}[nonzero]
    normalized.append(tuple(gf4_mul(x,inv) for x in u))
pts=sorted(set(normalized));n=len(pts)
assert n==21
lines=[]
for a in pts:
    mask=0
    for j,b in enumerate(pts):
        x=0
        for c,d in zip(a,b):x ^= gf4_mul(c,d)
        if x==0:mask|=1<<j
    lines.append(mask)
assert all(x.bit_count()==5 for x in lines)
assert len(set(lines))==21
assert all((lines[i]&lines[j]).bit_count()==1 for i in range(21) for j in range(i+1,21))
M=1<<n
# Here line-hitting bitsets have a different indexing convention: bit j is a line.
incidence=[sum(1<<j for j,line in enumerate(lines) if line>>i&1) for i in range(n)]
coverage=[0]*M
for s in range(1,M):
    b=s&-s;coverage[s]=coverage[s^b]|incidence[b.bit_length()-1]
ways=[0]*M
ways[0]=1
for s in range(1,M):
    b=s
    c=coverage[s]
    acc=0
    while b:
        bit=b&-b
        pred=s^bit
        if coverage[pred]!=c: acc+=ways[pred]
        b-=bit
    ways[s]=acc
maxlen=max(s.bit_count() for s in range(M) if ways[s])
maxsets=[s for s in range(M) if s.bit_count()==maxlen and ways[s]]
assert all(coverage[s]==M-1 for s in maxsets)
signatures=Counter()
sequences=0
for s in maxsets:
    hist=[0]*6
    for lm in lines: hist[(s&lm).bit_count()]+=1
    signatures[tuple(hist)]+=1
    sequences+=ways[s]
print('n',n,'reachable',sum(bool(x) for x in ways),'max',maxlen,'supports',len(maxsets),'ordered',sequences)
for sig,num in sorted(signatures.items()):print('signature',sig,'number',num)
print('total_supports',len(maxsets)**2,'total_sequences',sequences**2*comb(maxlen*2,maxlen))

expected={
(0,3,11,4,2,1):30240,
(0,4,8,7,1,1):20160,
(0,4,9,4,4,0):20160,
(0,5,5,10,0,1):6048,
(0,5,6,7,3,0):60480,
(0,6,3,10,2,0):3360}
assert maxlen==10 and len(maxsets)==140448
assert sum(bool(x) for x in ways)==738840
assert sequences==36288000000 and dict(signatures)==expected
assert len(maxsets)**2==19725640704
assert sequences**2*comb(20,10)==243290200817664000000000000
print('PASS: independent reverse recurrence')
