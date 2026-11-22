#!/usr/bin/env python3
"""Exact independent Cartier-coefficient and Legendre checks over F_23 and F_529.

No third-party modules. The quadratic field is F_23[w]/(w^2+1).
"""
from collections import Counter

P = 23
ZERO = (0, 0)
ONE = (1, 0)


def add(a, b, p):
    return ((a[0]+b[0])%p, (a[1]+b[1])%p)


def mul(a, b, p):
    return ((a[0]*b[0]-a[1]*b[1])%p, (a[0]*b[1]+a[1]*b[0])%p)


def scale(a, v, p):
    return ((a[0]*v)%p, (a[1]*v)%p)


def legendre_values(t, p):
    """P_1(t),...,P_(p-2)(t) using the characteristic-p recurrence."""
    v = [ONE, t]
    for n in range(1, p-2):
        q = add(scale(mul(t,v[n],p),2*n+1,p),scale(v[n-1],-n,p),p)
        v.append(scale(q,pow(n+1,-1,p),p))
    assert len(v)==p-1
    return v[1:]


def cartier_diagonal(t, p):
    """Independently obtain [z^i](1+2*t*z+z^2)^((p-1)/2)."""
    out=[ONE]
    for _ in range((p-1)//2):
        nxt=[ZERO]*(len(out)+2)
        for i,c in enumerate(out):
            nxt[i]=add(nxt[i],c,p)
            nxt[i+1]=add(nxt[i+1],scale(mul(t,c,p),2,p),p)
            nxt[i+2]=add(nxt[i+2],c,p)
        out=nxt
    return out[1:p-1]


def p_rank(t,p,independent=True):
    L=legendre_values(t,p)
    if independent:
        D=cartier_diagonal(t,p)
        assert len(D)==p-2
        assert all(c==scale(v,(-1)**i,p) for i,(c,v) in enumerate(zip(D,L),1))
    return sum(v!=ZERO for v in L)


def poly_add(a,b,p):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]=(c[i]+v)%p
    for i,v in enumerate(b):c[i]=(c[i]+v)%p
    while len(c)>1 and c[-1]==0:c.pop()
    return c


def poly_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    while len(c)>1 and c[-1]==0:c.pop()
    return c


def poly_mod(a,b,p):
    a=a[:]
    while len(a)>=len(b):
        k=(a[-1]*pow(b[-1],-1,p))%p
        off=len(a)-len(b)
        for j,v in enumerate(b):a[off+j]=(a[off+j]-k*v)%p
        while len(a)>1 and a[-1]==0:a.pop()
        if a==[0]:break
    return a


def legendre_polys(p):
    x=[0,1];v=[[1],x]
    for n in range(1,p-2):
        w=poly_mul(v[n],x,p)
        w=[((2*n+1)*c*pow(n+1,-1,p))%p for c in w]
        z=[((-n)*c*pow(n+1,-1,p))%p for c in v[n-1]]
        v.append(poly_add(w,z,p))
    return v


def main():
    ranks={a:p_rank((a,0),P) for a in range(P) if a not in (1,P-1)}
    groups={r:sorted(a for a,v in ranks.items() if v==r) for r in sorted(set(ranks.values()))}
    assert groups=={
        10:[0],17:[9,14],19:[4,6,7,10,11,12,13,16,17,19],
        20:[2,3,5,8,15,18,20,21]
    }
    assert Counter(ranks.values())=={10:1,17:2,19:10,20:8}
    # An explicit algebraic certificate that every smooth prime-field parameter
    # has a vanishing Legendre value: Q(t) divides a product of five P_i(t).
    polys=legendre_polys(P)
    Q=[0]*22
    for j in range(1,22,2):Q[j]=1
    product=[1]
    for n in (2,5,7,9,11):product=poly_mul(product,polys[n],P)
    assert poly_mod(product,Q,P)==[0]
    # Distinct roots of Q are F_23\{+1,-1}; check Q(1),Q(-1) !=0.
    for t in range(P):
        val=sum(co*t**i for i,co in enumerate(Q))%P
        assert (val==0)==(t not in (1,P-1))
    # First-prime property (among primes >=5): explicit exhaustive witnesses.
    expected={5:[2,3],7:[2,5],11:[5,6],
       13:[2,4,5,6,7,8,9,11],17:[5,6,7,8,9,10,11,12],
       19:[2,4,6,7,8,11,12,13,15,17],23:[]}
    for p,wit in expected.items():
        obs=[a for a in range(p) if a not in (1,p-1) and p_rank((a,0),p)==p-2]
        assert obs==wit,(p,obs)
    # F_(23^2)=F_23[w]/(w^2+1), irreducible since 23 ==3 mod4.
    assert pow(-1%P,(P-1)//2,P)==P-1
    extension_hist=Counter()
    for a in range(P):
        for b in range(P):
            if (a,b) in ((1,0),(P-1,0)):continue
            extension_hist[p_rank((a,b),P)]+=1
    assert extension_hist=={10:1,17:2,19:24,20:10,21:490}
    h=ONE
    for v in legendre_values((0,3),P):h=mul(h,v,P)
    assert h==(0,1) # product P_i(3w) = w, an explicit ordinary witness.
    print('GENUS_21_QUOTIENT_F23',groups)
    print('GENUS_505_COVER_F23',dict(sorted((23*r+22,n) for r,n in Counter(ranks.values()).items())))
    print('GENUS_21_QUOTIENT_F529',dict(sorted(extension_hist.items())))
    print('F23_FIRST_PRIME_AT_LEAST_5_WITH_ZERO_ORDINARY',min(p for p,v in expected.items() if not v))
    print('F23_POLYNOMIAL_DIVISIBILITY_CERTIFICATE', 'Q divides P_2 P_5 P_7 P_9 P_11')
    print('GENUS_505_PGL2_23_ARITHMETIC_GAP_VERIFIED')

if __name__=='__main__':main()
