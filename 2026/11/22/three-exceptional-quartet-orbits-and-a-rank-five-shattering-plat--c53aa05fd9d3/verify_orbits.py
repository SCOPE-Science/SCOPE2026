"""Exact orbit classification of shattered 4-supports in Paley(81).
Run: python3 verify_orbits.py
Uses only the Python standard library, with an independent arithmetic implementation.
"""
from itertools import combinations
Q=81
DIG=[tuple((n//3**i)%3 for i in range(4)) for n in range(Q)]
def enc(v): return sum((a%3)*3**i for i,a in enumerate(v))
def add(x,y): return enc([(a+b)%3 for a,b in zip(DIG[x],DIG[y])])
def neg(x):return enc([(-a)%3 for a in DIG[x]])
def mul(x,y):
    a,b=DIG[x],DIG[y]
    p=[0]*7
    for i in range(4):
        for j in range(4):p[i+j]=(p[i+j]+a[i]*b[j])%3
    for i in range(6,3,-1):
        c=p[i];p[i]=0
        p[i-4]=(p[i-4]+c)%3
        p[i-3]=(p[i-3]+2*c)%3
    return enc(p)
def power(x,k):
    y=1
    for _ in range(k):y=mul(y,x)
    return y
SQ={mul(x,x) for x in range(1,Q)}
assert len(SQ)==40 and 0 not in SQ
ALL=(1<<Q)-1
MASK=[sum(1<<v for v in range(Q) if add(y,neg(v)) in SQ) for y in range(Q)]
assert all(m.bit_count()==40 for m in MASK)
def shattered(S):
    states=[ALL]
    for x in S:
        a=MASK[x];b=ALL^a
        states=[t&a for t in states]+[t&b for t in states]
        if any(t==0 for t in states):return False
    return True
# Squares and Frobenius preserve square-difference adjacency; translations do also.
FROB=[[power(x,3**j) for x in range(Q)] for j in range(4)]
assert all(mul(FROB[j][x],FROB[j][y])==FROB[j][mul(x,y)] for j in range(4) for x in range(Q) for y in range(Q))
def orbit(S):
    out=set()
    for a in SQ:
        for j in range(4):
            pts=[mul(a,FROB[j][x]) for x in S]
            for b in pts:
                out.add(tuple(sorted(add(x,neg(b)) for x in pts)))
    return out
all4={(0,)+s for s in combinations(range(1,Q),3)}
assert len(all4)==82160
remaining=all4.copy(); bad_orbits=[]; maximal_orbits=[]; hit4=0
while remaining:
    s=min(remaining)
    o=orbit(s)
    assert o<=remaining, (s,len(o),len(o&remaining))
    remaining-=o
    good=shattered(s)
    assert all(shattered(t)==good for t in o)
    if good:
        hit4+=len(o)
        has_extension=any(shattered(s+(x,)) for x in range(1,Q) if x not in s)
        if not has_extension:maximal_orbits.append((s,len(o)))
    else:bad_orbits.append((s,len(o)))
assert hit4==81920
assert bad_orbits==[((0,1,42,43),40),((0,3,6,46),160),((0,3,46,52),40)],bad_orbits
assert maximal_orbits==[((0,1,2,42),160),((0,1,42,44),80)],maximal_orbits
print('bad normalized four-orbits:',bad_orbits)
print('maximal shattered normalized four-orbits:',maximal_orbits)
print('bad ordinary four-faces:',sum(n*81//4 for _,n in bad_orbits))
print('maximal ordinary four-faces:',sum(n*81//4 for _,n in maximal_orbits))
print('ORBIT_OK')
