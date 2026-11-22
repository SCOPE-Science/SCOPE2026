"""Independent direct binary enumeration and explicit primitive constructions.
Uses only Python standard library. Run: python verify_direct.py
"""
from itertools import product
from math import gcd

def allowed(bits):
    n=len(bits)
    for k in range(n):
        b=''.join(bits[(k+j)%n] for j in range(6))
        if b[:2]==b[2:4] or b[1:3]==b[3:5] or b[:3]==b[3:6]:
            return False
    return True

def least_period(s):
    n=len(s)
    return next(d for d in range(1,n+1) if n%d==0 and all(s[i]==s[(i+d)%n] for i in range(n)))
counts=[]; primitive=[]
for n in range(1,17):
    cnt=pr=0
    for bits in product('01',repeat=n):
        if allowed(bits):
            cnt+=1
            if least_period(bits)==n:pr+=1
    counts.append(cnt);primitive.append(pr)
assert counts==[0,0,0,12,10,6,0,12,36,50,22,18,78,196,190,124]
assert [i+1 for i,c in enumerate(primitive) if c==0]==[1,2,3,7,8,12]
# Each excursion is a simple directed 5-gram cycle, with no intermediate
# return to the common vertex 10001; index zero defines its rooted label.
root='10001'
excursions={
 4:['10001','00010','00100','01000','10001'],
 5:['10001','00011','00110','01100','11000','10001'],
 6:['10001','00011','00111','01110','11100','11000','10001']
}
def legal6(s):return s[:2]!=s[2:4] and s[1:3]!=s[3:5] and s[:3]!=s[3:6]
for length,states in excursions.items():
    assert len(states)==length+1 and states[0]==states[-1]==root
    assert len(set(states[:-1]))==length
    for u,v in zip(states,states[1:]):
        assert u[1:]==v[:-1] and legal6(u+v[-1])

def build(spec):
    states=[root]
    for k in spec:
        cycle=excursions[k]
        states.extend(cycle[1:])
    return ''.join(s[0] for s in states[:-1])
for n in range(13,151):
    if n%2:
        m=n-5
        pairs=[(a,b) for a in range(m//4+1) for b in range(m//6+1) if 4*a+6*b==m]
        assert pairs
        a,b=pairs[0]; spec=[5]+[4]*a+[6]*b
    elif n%4==2:
        spec=[6]+[4]*((n-6)//4)
    else:
        spec=[6,6]+[4]*((n-12)//4)
    assert sum(spec)==n and len(set(spec))>1
    s=build(spec)
    assert len(s)==n and allowed(s) and least_period(s)==n,(n,s)
print('PASS: direct cyclic enumeration through length 16 and explicit')
print('least-period witnesses for every circumference 13 through 150.')
