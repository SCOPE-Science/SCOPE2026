"""Replay verifier: re-derives histogram from scratch, checks agreement + audits.
Run: python3 verify.py
Exits 0 iff all checks pass; prints certificate lines.
"""
import math, collections
P = 30030
PRIMES = [2,3,5,7,11,13]
EXPECTED = {2:1485,4:1485,6:1690,8:394,10:438,12:188,14:58,16:12,18:8,22:2}

def cop_gcd():
    return [n for n in range(1,P+1) if math.gcd(n,P)==1]

def cop_sieve():
    s = bytearray(b"\x01")*(P+1); s[0]=0
    for p in PRIMES:
        for m in range(p,P+1,p): s[m]=0
    return [n for n in range(1,P+1) if s[n]]

def gaps(cop):
    g=[cop[i+1]-cop[i] for i in range(len(cop)-1)]
    g.append((P+cop[0])-cop[-1])
    return g

a=cop_gcd(); b=cop_sieve()
assert a==b, "enumerations disagree"
assert len(a)==5760
assert len(a)==P*1//2*2//3*4//5*6//7*10//11*12//13  # phi(30030)=5760
g=gaps(a)
c=dict(collections.Counter(g))
assert c==EXPECTED, c
assert sum(c.values())==5760
assert sum(k*v for k,v in c.items())==P
assert max(g)==22
assert all(d%2==0 for d in c), "all gaps even"
assert c.get(20,0)==0
for d in [2,4,6,8,10,12,14,16,18,22]:
    assert c.get(d,0)>0, d
# 22-gap witnesses: endpoints coprime, interior clean, count exactly 2
pos=[i for i,x in enumerate(g) if x==22]
assert len(pos)==2
for i in pos:
    u=a[i]; v=u+22
    assert math.gcd(u,P)==1 and math.gcd(v,P)==1, (u,v)
    assert all(math.gcd(n,P)>1 for n in range(u+1,v)), u
starts=sorted(a[i] for i in pos)
assert starts==[9439,20569], starts
print("HIST", c)
print("SUM_N=5760 MOM=30030 MAX=22 N20=0")
print("GAP22_STARTS", starts)
print("VERIFY_OK")
