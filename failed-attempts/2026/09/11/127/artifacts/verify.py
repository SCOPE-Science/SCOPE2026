"""Exhaustive census: no cyclic-symmetric Boolean 4-ary 3-edge operation.
Enumerates all 2**16 Boolean 4-ary ops (bit i = value on tuple i with
index = x1 + 2*x2 + 4*x3 + 8*x4). Cyclic invariance under
(x1,x2,x3,x4) -> (x2,x3,x4,x1). Tests three 3-edge identity systems:
  B (Berman-style): e(y,y,x,x)=x; e(y,x,y,x)=x; e(x,x,y,x)=x; e(x,x,x,y)=y
  A (all-x):        e(y,y,x,x)=x; e(y,x,y,x)=x; e(x,x,y,x)=x; e(x,x,x,y)=x
  C (alt):          e(y,y,x,x)=x; e(y,x,y,x)=x; e(y,x,x,y)=x; e(x,y,y,y)=y
Stdlib only. Prints VERIFY_OK on success."""
import itertools
T = list(itertools.product([0,1], repeat=4))
idx = {t:i for i,t in enumerate(T)}
def rot(t): return (t[1],t[2],t[3],t[0])
def get(tb,a,b,c,d): return tb[idx[(a,b,c,d)]]
def cyclic(tb): return all(tb[idx[t]]==tb[idx[rot(t)]] for t in T)
def B(tb):
    return all(get(tb,y,y,x,x)==x and get(tb,y,x,y,x)==x and get(tb,x,x,y,x)==x and get(tb,x,x,x,y)==y for x in (0,1) for y in (0,1))
def A(tb):
    return all(get(tb,y,y,x,x)==x and get(tb,y,x,y,x)==x and get(tb,x,x,y,x)==x and get(tb,x,x,x,y)==x for x in (0,1) for y in (0,1))
def C(tb):
    return all(get(tb,y,y,x,x)==x and get(tb,y,x,y,x)==x and get(tb,y,x,x,y)==x and get(tb,x,y,y,y)==y for x in (0,1) for y in (0,1))
n_cyc=nB=nA=nC=tB=tA=tC=0
for n in range(2**16):
    tb=[(n>>i)&1 for i in range(16)]
    b,a,c=B(tb),A(tb),C(tb)
    tB+=b; tA+=a; tC+=c
    if cyclic(tb):
        n_cyc+=1; nB+=b; nA+=a; nC+=c
print(f"cyclic={n_cyc} cycB={nB} cycA={nA} cycC={nC} totalB={tB} totalA={tA} totalC={tC}")
assert n_cyc==64, n_cyc
assert (nB,nA,nC)==(0,0,0), (nB,nA,nC)
assert (tB,tA,tC)==(64,64,64), (tB,tA,tC)
print("VERIFY_OK")
