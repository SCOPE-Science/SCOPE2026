"""Exact finite-field checks for eight-branch Howe covers over F_7."""
from itertools import combinations, product
from collections import Counter

P = 7
NONSQUARE = 3

def pow7(a, e):
    result = 1
    while e:
        if e & 1:
            result = result * a % P
        a = a * a % P
        e >>= 1
    return result

def chi7(a):
    a %= P
    return 0 if a == 0 else (1 if pow7(a, 3) == 1 else -1)

def mul49(x, y):
    a,b = x
    c,d = y
    return ((a*c-b*d)%P, (a*d+b*c)%P)  # u^2=-1

def pow49(x, e):
    v = (1,0)
    while e:
        if e & 1:
            v = mul49(v, x)
        x = mul49(x,x)
        e >>= 1
    return v

def chi49(x):
    return 0 if x==(0,0) else (1 if pow49(x,24)==(1,0) else -1)

def polyval49(roots, x):
    z = (1,0)
    for r in roots:
        z = mul49(z, ((x[0]-r)%P,x[1]))
    return z

def polyval7(roots, x):
    z = 1
    for r in roots:
        z = z * (x-r) % P
    return z

F49=list(product(range(7),repeat=2))
assert len(F49)==49 and len({mul49(x,x) for x in F49})==25
# The genus-3 complementary double cover.
S=sum(chi49(((pow49(x,7)[0]-x[0])%7,(pow49(x,7)[1]-x[1])%7)) for x in F49)
assert S == 42

counts=Counter()
pairs=Counter()
for left in combinations(range(P),3):
    right=tuple(i for i in range(P) if i not in left)
    tr1=-sum(chi7(polyval7(left,x)) for x in range(7))
    tr2=-1-sum(chi7(polyval7(right,x)) for x in range(7))
    pairs[(tr1,tr2)]+=1
    assert abs(tr1)==abs(tr2) and abs(tr1) in {0,4}
    for c,d in product((1,NONSQUARE),repeat=2):
        t1=chi7(c)*tr1
        t2=chi7(d)*tr2
        expected_n1=8-t1-t2
        expected_n2=92-(t1*t1-14)-(t2*t2-14)
        n1=(1+chi7(d)) + sum((1+chi7(c*polyval7(left,x)))*(1+chi7(d*polyval7(right,x))) for x in range(7))
        n2=2+sum((1+chi49(mul49((c,0),polyval49(left,x))))*(1+chi49(mul49((d,0),polyval49(right,x)))) for x in F49)
        assert n1==expected_n1 and n2==expected_n2,(left,c,d,n1,n2,expected_n1,expected_n2)
        counts[(t1,t2,n1,n2)]+=1
assert len(counts)==5,counts
assert sum(counts.values())==140
assert sum(k[3]==120 and v or 0 for k,v in counts.items())==84
assert sum(k[3]==88 and v or 0 for k,v in counts.items())==56
assert pairs=={(0,0):21,(4,-4):7,(-4,-4):7},pairs
# Independent anharmonic-orbit count for each complement pair.
def cross_ratio(pts):
    a,b,c,d = pts
    if d == 7: return ((a-c) * pow(b-c,-1,P)) % P
    if c == 7: return ((b-d) * pow(a-d,-1,P)) % P
    if b == 7: return ((a-c) * pow(a-d,-1,P)) % P
    if a == 7: return ((b-d) * pow(b-c,-1,P)) % P
    return ((a-c)*(b-d)*pow((a-d)*(b-c),-1,P))%P
classes=Counter()
for left in combinations(range(7),3):
    a=tuple(left)+(7,)
    b=tuple(x for x in range(7) if x not in left)
    la,lb=cross_ratio(a),cross_ratio(b)
    ca='harmonic' if la in (2,4,6) else 'equianharmonic'
    cb='harmonic' if lb in (2,4,6) else 'equianharmonic'
    assert la in (2,3,4,5,6) and lb in (2,3,4,5,6) and ca==cb
    classes[ca]+=1
assert classes=={'harmonic':21,'equianharmonic':14},classes
print('EIGHT_BRANCH_HOWE_F7_VERIFIED 35 partitions 140 marked covers')
print('monic traces:',dict(sorted(pairs.items())))
print('twist spectra (trace pair; N1; N2; count):')
for key,value in sorted(counts.items()):
 print(key,value)
