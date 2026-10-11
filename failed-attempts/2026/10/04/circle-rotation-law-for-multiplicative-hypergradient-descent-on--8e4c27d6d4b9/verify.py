import math

def T(q,beta):
    if abs(q-1.0) < 1e-14:
        return None
    return (1.0+beta)*q if q < 1.0 else (1.0-beta)*q

def enter_band(q,beta,limit=10000):
    lo,hi=1.0-beta,1.0+beta
    for n in range(limit):
        if lo-1e-14 <= q <= hi+1e-14:
            return q,n
        q=T(q,beta)
        assert q is not None
    raise AssertionError("band entry failed")

for beta in (0.1,0.25,0.5,0.8,0.95):
    for q0 in (1e-12,1e-6,0.01,0.2,0.7,1.3,3.0,1e2,1e8):
        q,n=enter_band(q0,beta)
        assert 1.0-beta-1e-12 <= q <= 1.0+beta+1e-12

for beta in (0.2,0.5,0.7):
    A=math.log(1.0+beta)
    C=-math.log(1.0-beta)
    L=A+C
    candidates=(1.0-beta,0.8,0.93,1.07,1.2,1.0+beta)
    for q in candidates:
        if not (1.0-beta <= q <= 1.0+beta) or abs(q-1.0)<1e-12:
            continue
        qn=T(q,beta)
        z=(math.log(q)+C)%L
        zn=(math.log(qn)+C)%L
        expected=(z+A)%L
        err=min(abs(zn-expected),abs(zn-expected+L),abs(zn-expected-L))
        assert err < 2e-12

beta=(math.sqrt(5.0)-1.0)/2.0
q0=0.8
q=q0
vals=[]
for _ in range(3):
    vals.append(q)
    q=T(q,beta)
assert abs(q-q0) < 3e-14
assert all(abs(v-1.0)>1e-10 for v in vals)
assert min(abs(vals[i]-vals[j]) for i in range(3) for j in range(i)) > 1e-6

beta=0.5
L=math.log(3.0)
q=0.8
B=250
bins=set()
for _ in range(20000):
    z=(math.log(q)-math.log(0.5))%L
    bins.add(min(B-1,int(B*z/L)))
    q=T(q,beta)
    assert q is not None
assert len(bins)==B

for beta in (0.2,0.5,0.8):
    q,_=enter_band(1e-5,beta)
    x=1.0
    for _ in range(100):
        if abs(q-1.0)<1e-14:
            break
        xn=(1.0-q)*x
        assert abs(xn) <= beta*abs(x) + 1e-14
        q=T(q,beta)
        x=xn

print("verification passed")
