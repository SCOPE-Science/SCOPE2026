"""Independent finite-field smoothness census for the normalized quintic pencil.
Pure Python standard library; run: python verify_finite_fields.py.
F49=F7[i]/(i^2+1), where -1 is nonsquare in F7.
"""
from collections import Counter

ZERO = (0,0); ONE = (1,0)
def Z(n):return (n%7,0)
def add(x,y):return ((x[0]+y[0])%7,(x[1]+y[1])%7)
def sub(x,y):return ((x[0]-y[0])%7,(x[1]-y[1])%7)
def mul(x,y):
    return ((x[0]*y[0]-x[1]*y[1])%7,
            (x[0]*y[1]+x[1]*y[0])%7)
def power(x,n):
    out=ONE
    while n:
        if n&1:out=mul(out,x)
        x=mul(x,x);n//=2
    return out
def inv(x):
    assert x != ZERO
    # The multiplicative group of F49 has order 48.
    return power(x,47)

def trim(f):
    while len(f)>1 and f[-1]==ZERO:f.pop()
    return f

def rem(f,g):
    f=trim(f[:]);g=trim(g[:]); assert g != [ZERO]
    while f != [ZERO] and len(f)>=len(g):
        t=mul(f[-1],inv(g[-1]));d=len(f)-len(g)
        for j,v in enumerate(g): f[j+d]=sub(f[j+d],mul(t,v))
        trim(f)
    return f

def gcd(f,g):
    while g != [ZERO]:f,g=g,rem(f,g)
    return f

def is_smooth(a,b):
    f=[ONE,b,a,ZERO,ZERO,ONE]  # x^5+a*x^2+b*x+1
    df=[b,mul(Z(2),a),ZERO,ZERO,Z(5)]
    return len(gcd(f,df))==1

def predicted_type(a,b):
    if b != ZERO:return 'ordinary'
    if a == ZERO:return 'rank0_a2'
    if power(a,5)==ONE:return 'rank1_a2'
    return 'rank2_a2'

for name,vals,expected in [
    ('F7',[Z(x) for x in range(7)],
     {'ordinary':38,'rank0_a2':1,'rank1_a2':1,'rank2_a2':4}),
    ('F49',[(u,v) for u in range(7) for v in range(7)],
     {'ordinary':2306,'rank0_a2':1,'rank1_a2':1,'rank2_a2':46}),
]:
    counts=Counter()
    for a in vals:
        for b in vals:
            if is_smooth(a,b):counts[predicted_type(a,b)]+=1
            else:counts['singular']+=1
    assert dict((k,counts[k]) for k in expected)==expected,(name,counts)
    assert counts['singular']==(5 if name=='F7' else 47)
    print(name,dict(counts))
print('FINITE_FIELD_CENSUS_OK')
