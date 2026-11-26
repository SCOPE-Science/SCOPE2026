#!/usr/bin/env python3
"""Direct verification of the characteristic-two truncated-derivation square-zero cone.
Finite tests corroborate the uniform symbolic proof; they are not its replacement.
"""
from itertools import product

def add(x,y):
    return x ^ y

def mul(x,y,q):
    if q == 2:
        return x & y
    if q == 4:
        a,b=x&1,(x>>1)&1
        c,d=y&1,(y>>1)&1
        return (a*c ^ b*d) | ((a*d ^ b*c ^ b*d)<<1)
    raise ValueError('Only explicitly implemented fields F2 and F4')

def apply_D(D,v,q):
    a,b,c,d,e,u,z,w=D
    t0,t1,t2,t3=v
    # D(1)=0, D(x)=a+bx+cy+dxy, D(y)=e+ux+zy+wxy
    # D(xy)=e*x + a*y + (b+z)*xy
    return (
        mul(t1,a,q)^mul(t2,e,q),
        mul(t1,b,q)^mul(t2,u,q)^mul(t3,e,q),
        mul(t1,c,q)^mul(t2,z,q)^mul(t3,a,q),
        mul(t1,d,q)^mul(t2,w,q)^mul(t3,b^z,q),
    )

def direct_square_zero(D,q):
    f=(D[0],D[1],D[2],D[3])
    g=(D[4],D[5],D[6],D[7])
    return not any(apply_D(D,f,q)) and not any(apply_D(D,g,q))

def equations(D,q):
    a,b,c,d,e,u,v,w=D
    m=lambda x,y:mul(x,y,q)
    return (
       m(a,b)^m(c,e),
       m(b,b)^m(c,u)^m(d,e),
       m(a,d)^m(b,c)^m(c,v),
       m(c,w)^m(d,v),
       m(a,u)^m(e,v),
       m(b,u)^m(e,w)^m(u,v),
       m(a,w)^m(c,u)^m(v,v),
       m(b,w)^m(d,u),
    )

def check(q):
    good=0
    boundary=0
    for D in product(range(q), repeat=8):
        equations_zero=not any(equations(D,q))
        direct_zero=direct_square_zero(D,q)
        assert equations_zero == direct_zero, ('equations disagree',q,D)
        if direct_zero:
            good += 1
            if D[0] == D[4] == 0:
                boundary += 1
    assert good == q**4+q**3-q, ('total',q,good)
    assert boundary == q**3+q**2-q, ('boundary',q,boundary)
    assert good-boundary == (q*q-1)*q*q
    print('FIELD',q,'TOTAL',good,'BOUNDARY',boundary,'OPEN',good-boundary)

if __name__ == '__main__':
    check(2)
    check(4)
    print('VERIFY_OK_WITT2_FROBENIUS_ZERO')
