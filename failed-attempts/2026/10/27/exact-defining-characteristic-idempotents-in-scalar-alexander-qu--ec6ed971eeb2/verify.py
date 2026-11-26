#!/usr/bin/env python3
"""Direct finite census for idempotents of scalar Alexander quandle algebras.
Only finite-field arithmetic and definitions are used in the exhaustive test.
"""
from itertools import product


def field(q):
    if q == 4:
        # F_2[t]/(t^2+t+1), encoding c0 + c1*t as c0+2*c1.
        add=lambda a,b:a^b
        def mul(a,b):
            c=((a&1)*(b&1))
            d=((a&1)*(b>>1)^((a>>1)*(b&1)))
            e=(a>>1)*(b>>1)
            return ((c^e)&1)|(((d^e)&1)<<1)
        return add,mul,0,1
    if q in (3,5,7):
        return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q,0,1
    raise ValueError(q)


def mulpow(x,n,mul,one):
    y=one
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x)
        n//=2
    return y


def predicted(q,a,add,mul):
    one=1
    neg1=next(x for x in range(q) if add(one,x)==0)
    b=add(one,mul(neg1,a))
    assert a!=0 and b!=0
    resonant=[j for j in range(q-1) if add(mulpow(a,j,mul,one),mulpow(b,j,mul,one))==one]
    return b,resonant,q**len(resonant)+1


def brute(q,a):
    add,mul,zero,one=field(q)
    b,js,expect=predicted(q,a,add,mul)
    quandle=[[add(mul(a,i),mul(b,j)) for j in range(q)] for i in range(q)]
    # Direct quandle-algebra multiplication; no convolution shortcut.
    count=0;bad_aug=0
    for u in product(range(q),repeat=q):
        aug=0
        for x in u:aug=add(aug,x)
        # compare coefficients of u*u with u
        v=[zero]*q
        for i,ci in enumerate(u):
            if ci==zero:continue
            for j,cj in enumerate(u):
                if cj==zero:continue
                k=quandle[i][j]
                v[k]=add(v[k],mul(ci,cj))
        if tuple(v)==u:
            count+=1
            if aug==zero and any(x!=zero for x in u):bad_aug+=1
    assert count==expect,(q,a,expect,count)
    assert bad_aug==0,(q,a,bad_aug)
    return (q,a,b,js,count,bad_aug)


if __name__=='__main__':
    # Exhaustive coefficient-vector censuses in the original quandle product.
    for q,aa in [(3,[2]),(4,[2,3]),(5,[2,3,4]),(7,[2,4])]:
        for a in aa:
            print('EXHAUSTIVE_OK',brute(q,a),flush=True)
    # Arithmetic resonance consistency for a wider prime-field list.
    for p in (11,13,17,19):
        add=lambda a,b:(a+b)%p
        mul=lambda a,b:(a*b)%p
        for a in range(2,p):
            b,js,total=predicted(p,a,add,mul)
            assert 1 in js and 0 not in js and total>=p+1
        print('RESONANCE_OK',p,flush=True)
    print('VERIFY_OK',flush=True)
