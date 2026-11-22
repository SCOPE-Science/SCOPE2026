#!/usr/bin/env python3
"""Exact cycle-type census for affine maps of two finite length-two local rings.
No external libraries; compared to an independent closed formula.
"""
from collections import Counter
from math import gcd


def field_mul(x,y,p):
    # F_p for degree 1, F_9 = F_3[t]/(t^2+1) for degree 2.
    if p == 3 and x < 9 and y < 9:
        a,b = x%3,x//3
        c,d = y%3,y//3
        return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
    return (x*y)%p


def build_ring(p, f, mixed):
    q=p**f
    if f==1:
        if mixed:
            mod=p*p
            add=lambda x,y:(x+y)%mod
            mul=lambda x,y:(x*y)%mod
            in_rad=lambda x:x%p==0
        else:
            mod=p*p
            def add(x,y): return (x%p+y%p)%p +p*((x//p+y//p)%p)
            def mul(x,y):return (x%p*y%p)%p +p*(((x%p)*(y//p)+(x//p)*(y%p))%p)
            in_rad=lambda x:x%p==0
    elif p==3 and f==2:
        mod=81
        if mixed:
            # GR(9,2) = (Z/9)[t]/(t^2+1)
            def add(x,y):return ((x%9+y%9)%9)+9*((x//9+y//9)%9)
            def mul(x,y):
                a,b=x%9,x//9; c,d=y%9,y//9
                return ((a*c-b*d)%9)+9*((a*d+b*c)%9)
            in_rad=lambda x:x%3==0 and (x//9)%3==0
        else:
            # F_9[epsilon]/(epsilon^2): coefficients in F_9
            def fa(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
            def add(x,y):return fa(x%9,y%9)+9*fa(x//9,y//9)
            def mul(x,y):
                a,b=x%9,x//9;c,d=y%9,y//9
                ab=field_mul(a,c,3)
                cross=fa(field_mul(a,d,3),field_mul(b,c,3))
                return ab+9*cross
            in_rad=lambda x:x%9==0
    else: raise ValueError((p,f))
    one=1
    return mod,add,mul,in_rad,one


def trial(p,f,mixed):
    q=p**f
    mod, add,mul,in_rad,one=build_ring(p,f,mixed)
    unit=[u for u in range(mod) if not in_rad(u)]
    assert len(unit)==q*q-q
    z=0
    observed=Counter()
    fixed=Counter()
    for u in unit:
        ux=[mul(u,x) for x in range(mod)]
        for a in range(mod):
            perm=[add(v,a) for v in ux]
            assert len(set(perm))==mod
            seen=[False]*mod
            cc=Counter()
            for x in range(mod):
                if seen[x]:continue
                v=x;n=0
                while not seen[v]:
                    seen[v]=True
                    v=perm[v]
                    n+=1
                assert v==x
                cc[n]+=1
            observed[tuple(sorted(cc.items()))]+=1
            fixed[cc.get(1,0)]+=1
    # Mathematical formula not based on recorded permutations
    expected=Counter()
    def put(typ,count):expected[tuple(sorted(typ.items()))]+=count
    put({1:q*q},1)
    put({p:q*q//p},q**3-q*q+q-1 if not mixed else q-1)
    if mixed:put({p*p:q*q//(p*p)},q*q*(q-1))
    put({1:q,p:q*(q-1)//p},q*(q-1))
    for d in range(2,q):
        if (q-1)%d:continue
        phi=sum(gcd(i,d)==1 for i in range(1,d+1))
        put({1:1,d:(q*q-1)//d},phi*q*q)
        put({1:1,d:(q-1)//d,d*p:q*(q-1)//(d*p)},phi*(q-1)*q*q)
    assert observed==expected, ('cycle_type_mismatch',p,f,mixed,observed-expected,expected-observed)
    predicted_fixed=Counter({q*q:1,q:q*(q-1),1:q**3*(q-2),0:(q-1)*(q*q+1)})
    assert fixed==predicted_fixed, ('fixed_mismatch',p,f,mixed,fixed,predicted_fixed)
    assert sum(observed.values())==q**3*(q-1)
    print(f'PASS p={p} f={f} {"mixed" if mixed else "equal"}: group={sum(observed.values())} types={len(observed)} fixed={dict(sorted(fixed.items()))}')
    return observed

if __name__=='__main__':
    for p,f in [(3,1),(5,1),(3,2)]:
        e=trial(p,f,False)
        m=trial(p,f,True)
        assert e!=m
    print('LENGTH_TWO_AFFINE_CYCLE_CENSUS_VERIFIED')
