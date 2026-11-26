#!/usr/bin/env python3
from fractions import Fraction as F

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(c)

def neg(a):
    return [-x for x in a]

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return trim(c)

def scale(a,c):
    return trim([F(c)*x for x in a])

def power(a,n):
    out=[F(1)]
    for _ in range(n):
        out=mul(out,a)
    return out

def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    q=[F(0)]*max(1,(len(a)-len(b)+1))
    while len(a)>=len(b) and a != [F(0)]:
        d=len(a)-len(b)
        c=a[-1]/b[-1]
        q[d]+=c
        a=sub(a,[F(0)]*d+scale(b,c))
    return trim(q),trim(a)

def rem(a,b):
    return divmod_poly(a,b)[1]

x=[F(0),F(1)]
one=[F(1)]
two=[F(2)]
eight=[F(8)]
q11=[F(4),F(2),F(3)]   # 3*x^2 + 2*x + 4
q8 =[F(2),F(4),F(3)]   # 3*x^2 + 4*x + 2

lhs=sub(
    scale(mul(power(x,3), add(add(power(x,2),x),one)),9),
    power(add(x,two),3),
)
rhs=mul(sub(x,one),mul(q11,q8))
assert trim(lhs)==trim(rhs)

# j = 27*x^3*(x^3+8)^3/(x^3-1)^3
x3=power(x,3)
num=scale(mul(x3,power(add(x3,eight),3)),27)
den=power(sub(x3,one),3)

for q,target in [(q11,-32768),(q8,8000)]:
    rn=rem(num,q)
    rd=rem(den,q)
    assert rd != [F(0)]
    assert trim(rn)==trim(scale(rd,target))

# The two quadratic factors have negative discriminants; hence they are
# irreducible over Q. Since neither divides x^3-1 (verified above by the
# nonzero denominator remainder), none of their roots is a cubic root of unity.
disc11=F(2)**2-4*F(3)*F(4)
disc8 =F(4)**2-4*F(3)*F(2)
assert disc11 == -44 and disc8 == -8
assert rem(den,q11) != [F(0)] and rem(den,q8) != [F(0)]

print("VERIFY_OK fixed_parameters=4 j_values=8000,-32768")
