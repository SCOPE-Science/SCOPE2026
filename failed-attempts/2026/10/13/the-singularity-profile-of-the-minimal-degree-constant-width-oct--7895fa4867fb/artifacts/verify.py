#!/usr/bin/env python3
from fractions import Fraction
from math import comb

# Integer polynomial coefficients in ascending powers.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return trim(c)
def scale(a,k): return trim([k*x for x in a])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def power(a,n):
    r=[1]; b=a
    while n:
        if n&1:r=mul(r,b)
        b=mul(b,b); n//=2
    return r
def deriv(a): return trim([i*a[i] for i in range(1,len(a))] or [0])
def shift(a,c):
    # p(c+e)
    out=[Fraction(0)]*len(a)
    for k,ak in enumerate(a):
        for j in range(k+1): out[j]+=Fraction(ak)*comb(k,j)*Fraction(c)**(k-j)
    return trim(out)
def series_div(n,d,N):
    q=[Fraction(0)]*N
    assert d[0]!=0
    for k in range(N):
        rhs=Fraction(n[k]) if k<len(n) else Fraction(0)
        for j in range(1,min(k+1,len(d))): rhs-=Fraction(d[j])*q[k-j]
        q[k]=rhs/Fraction(d[0])
    return q

def gcdq(a,b):
    a=[Fraction(x) for x in trim(a)]; b=[Fraction(x) for x in trim(b)]
    while b!=[0]:
        r=a[:]
        while len(r)>=len(b) and r!=[0]:
            k=len(r)-len(b); c=r[-1]/b[-1]
            for j in range(len(b)): r[j+k]-=c*b[j]
            r=trim(r)
        a,b=b,r
    if a==[0]: return a
    z=a[-1]; return [x/z for x in a]

# t-parametrization [X:Y:Z].
# X=-8(t-1)^3(t+1)(t^4+2t^3+6t^2+2t+1)
T=[0,1]; one=[1];
tm1=[-1,1]; tp1=[1,1]; R=[1,2,6,2,1]
X=scale(mul(mul(power(tm1,3),tp1),R),-8)
Y=scale([3,-16,-36,-48,50,-48,-36,-16,3],-1)
Z=power([1,0,1],4)
assert len(X)==9 and len(Y)==9 and len(Z)==9
assert gcdq(gcdq(X,Y),Z)==[Fraction(1)]

# Verify the degree-eight homogeneous equation via invariant q=x^2+y^2, w=y(y^2-3x^2).
Q=add(power(X,2),power(Y,2))
W=mul(Y,add(power(Y,2),scale(power(X,2),-3)))
terms=[]
def term(poly,k): terms.append(scale(poly,k))
term(power(Q,4),1)
term(mul(power(Q,3),power(Z,2)),-28)
term(mul(mul(power(Q,2),W),Z),16)
term(mul(power(Q,2),power(Z,4)),-32562)
term(mul(mul(Q,W),power(Z,3)),-4320)
term(mul(Q,power(Z,6)),4960116)
term(mul(power(W,2),power(Z,2)),64)
term(mul(W,power(Z,5)),151632)
term(power(Z,8),-182284263)
S=[0]
for a in terms:S=add(S,a)
assert S==[0]

# Exact tangent-slope identity: dy/dx=(t^2-1)/(2t).
Xp=deriv(X); Yp=deriv(Y); Zp=deriv(Z)
NX=add(mul(Xp,Z),scale(mul(X,Zp),-1))
NY=add(mul(Yp,Z),scale(mul(Y,Zp),-1))
lhs=scale(mul(mul(NY,[0,1]),[2]),1)
rhs=mul(NX,[-1,0,1])
assert add(lhs,scale(rhs,-1))==[0]
# A second generic preimage would therefore have u=-1/t; it is not an identity because y(t)-y(-1/t)=32t/(1+t^2).

# At t=1, affine expansions begin x=-12e^3+..., y-9=-9e^4+..., giving Puiseux pair (3,4).
xs=series_div(shift(X,1),shift(Z,1),7)
ys_num=add(Y,scale(Z,-9))
ys=series_div(shift(ys_num,1),shift(Z,1),7)
assert xs[:5]==[0,0,0,Fraction(-12),Fraction(18)]
assert ys[:5]==[0,0,0,0,Fraction(-9)]

# The nonreal nodes on x=0 arise from the reciprocal quartic R.
# Every root of R maps to y^2+18y+189=0.
Nnode=add(add(power(Y,2),scale(mul(Y,Z),18)),scale(power(Z,2),189))
# exact divisibility by R by long division
def divremq(a,b):
    a=[Fraction(x) for x in a]; b=[Fraction(x) for x in b]; q=[Fraction(0)]*max(1,len(a)-len(b)+1); r=trim(a)
    while r!=[0] and len(r)>=len(b):
        k=len(r)-len(b); c=r[-1]/b[-1]; q[k]=c
        for j in range(len(b)): r[j+k]-=c*b[j]
        r=trim(r)
    return trim(q),r
_,rem=divremq(Nnode,R); assert rem==[Fraction(0)]
assert sum(Fraction(c) for c in R)==12 and sum(Fraction(c)*((-1)**i) for i,c in enumerate(R))==4
# Since slope(t)-slope(1/t)=(t^2-1)/t, paired branches are transverse at all roots of R.

# Restriction to the symmetry axis x=0: F(0,y,1)=(y-9)^3(y+7)(y^2+18y+189)^2.
yminus9=[-9,1]; yplus7=[7,1]; quad=[189,18,1]
fac=mul(mul(power(yminus9,3),yplus7),power(quad,2))
# Direct invariant substitution with q=y^2,w=y^3.
y=[0,1]; qy=power(y,2); wy=power(y,3)
Fy=[0]
for p,k in [(power(qy,4),1),(power(qy,3),-28),(mul(power(qy,2),wy),16),(power(qy,2),-32562),(mul(qy,wy),-4320),(qy,4960116),(power(wy,2),64),(wy,151632),([1],-182284263)]: Fy=add(Fy,scale(p,k))
assert Fy==fac

# Gaussian-rational arithmetic and local series at t=i for the infinity branch.
def g(a=0,b=0): return (Fraction(a),Fraction(b))
def ga(x,y): return (x[0]+y[0],x[1]+y[1])
def gm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gi(x):
    d=x[0]*x[0]+x[1]*x[1]; return (x[0]/d,-x[1]/d)
def gd(x,y): return gm(x,gi(y))
def gp(x,n):
    r=g(1); b=x
    while n:
        if n&1:r=gm(r,b)
        b=gm(b,b); n//=2
    return r
def gshift(a,c):
    out=[g() for _ in a]
    for k,ak in enumerate(a):
        for j in range(k+1): out[j]=ga(out[j],gm(g(ak*comb(k,j)),gp(c,k-j)))
    return out
def gseries_div(n,d,N):
    q=[g() for _ in range(N)]
    for k in range(N):
        rhs=n[k] if k<len(n) else g()
        for j in range(1,min(k+1,len(d))): rhs=ga(rhs,gm(g(-1),gm(d[j],q[k-j])))
        q[k]=gd(rhs,d[0])
    return q
for sign in (1,-1):
    c=g(0,sign)
    qser=gseries_div(gshift(X,c),gshift(Y,c),9)
    rser=gseries_div(gshift(Z,c),gshift(Y,c),9)
    q0=qser[0]; U=qser[:]; U[0]=g()
    assert U[1]==g() and U[2]==g(0,-sign)
    # V = r - U^2/8 + sign*i*U^3/16 has order 7 (the sign convention matches t=sign*i).
    def conv(a,b,N):
        o=[g() for _ in range(N)]
        for i,aa in enumerate(a):
            for j,bb in enumerate(b):
                if i+j<N:o[i+j]=ga(o[i+j],gm(aa,bb))
        return o
    U2=conv(U,U,9); U3=conv(U2,U,9)
    V=[]
    for k in range(9):
        z=rser[k]
        z=ga(z,gm(g(Fraction(-1,8)),U2[k]))
        z=ga(z,gm(g(0,Fraction(sign,16)),U3[k]))
        V.append(z)
    assert all(V[k]==g() for k in range(7)) and V[7]==g(Fraction(1,4))

# Delta budget for a rational plane octic.
pa=(8-1)*(8-2)//2
assert pa==21
assert 3*3+6*1+2*3==pa
print('VERIFY_OK')
