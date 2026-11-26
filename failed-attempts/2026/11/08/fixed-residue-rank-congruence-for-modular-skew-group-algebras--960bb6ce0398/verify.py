"""Independent finite algebra checks for modular fixed-point and translation examples.
The theorem uses a projective-module rank argument, not exhaustive testing.
"""
from itertools import product
from math import comb


def laurent_mul(u,v,p):
    out={}
    for (a,i),x in u.items():
        for (b,j),y in v.items():
            # use normal form t^i s^a, s t^j = t^-j s
            k=(a+b)%2
            degree=i+(-j if a else j)
            key=(k,degree)
            out[key]=(out.get(key,0)+x*y)%p
    return {k:v for k,v in out.items() if v%p}


def test_infinite_dihedral(p,d):
    keys=[(a,i) for a in (0,1) for i in range(-d,d+1)]
    num=0
    for coefficients in product(range(p),repeat=len(keys)):
        x={k:c for k,c in zip(keys,coefficients) if c}
        if laurent_mul(x,x,p)==x:
            num+=1
            assert x=={} or x=={(0,0):1}
    return num


def add(A,B,p):
    C=dict(A)
    for i,b in B.items():C[i]=(C.get(i,0)+b)%p
    return {i:v for i,v in C.items() if v}


def mul(A,B,p):
    C={}
    for i,a in A.items():
        for j,b in B.items():C[i+j]=(C.get(i+j,0)+a*b)%p
    return {i:v for i,v in C.items() if v}


def shift(A,n,p):
    out={}
    for d,a in A.items():
        for j in range(d+1):
            out[j]=(out.get(j,0)+a*comb(d,j)*(n**(d-j)))%p
    return {i:v for i,v in out.items() if v}


def crossed_mul(U,V,p):
    W=[{} for _ in range(p)]
    for i,ui in enumerate(U):
        for j,vj in enumerate(V):
            W[(i+j)%p]=add(W[(i+j)%p],mul(ui,shift(vj,i,p),p),p)
    return W


def test_translation(p):
    a={p-1:p-1}  # -x^(p-1)
    E=[dict(a) for _ in range(p)]
    Q=crossed_mul(E,E,p)
    assert Q==E,(p,Q,E)
    S={}
    for j in range(p):S=add(S,shift(a,j,p),p)
    assert S=={0:1},(p,S)
    assert E != [{} for _ in range(p)]
    assert E != [{0:1}]+[{} for _ in range(p-1)]
    return len(E)

if __name__=='__main__':
    for d in range(3):
        n=test_infinite_dihedral(2,d)
        print(f'F2[D_infty] support exponents -{d}..{d}: {n} idempotents (only zero and one)')
        assert n==2
    for p in [2,3,5,7]:
        test_translation(p)
        print(f'Characteristic {p} Artin-Schreier shift: nontrivial idempotent e=-x^(p-1)sum s^i checked')
    print('VERIFY_OK')
