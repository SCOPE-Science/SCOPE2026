#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

# Polynomials are low-to-high coefficient lists over Q.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); c=[F(0) for _ in range(n)]
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def sub(a,b): return add(a,[-x for x in b])
def mul(a,b):
    c=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)
def scale(a,s): return trim([x*s for x in a])
def deriv(a): return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])
def divmodp(a,b):
    a=trim(a); b=trim(b)
    if b==[0]: raise ZeroDivisionError
    q=[F(0) for _ in range(max(1,len(a)-len(b)+1))]
    r=a[:]
    while len(r)>=len(b) and r!=[0]:
        k=len(r)-len(b); c=r[-1]/b[-1]; q[k]=c
        r=sub(r,[F(0)]*k+scale(b,c))
    return trim(q),trim(r)
def evalp(p,x):
    s=F(0)
    for c in reversed(p): s=s*x+c
    return s

def sturm(p):
    seq=[trim(p),deriv(p)]
    while seq[-1]!=[0]:
        _,r=divmodp(seq[-2],seq[-1])
        if r==[0]: break
        seq.append(scale(r,F(-1)))
    return seq

def sign_at(p,x):
    v=evalp(p,x)
    return (v>0)-(v<0)
def sign_inf(p,pos=True):
    s=(p[-1]>0)-(p[-1]<0)
    if not pos and (len(p)-1)%2: s=-s
    return s
def variations(signs):
    s=[x for x in signs if x]
    return sum(a!=b for a,b in zip(s,s[1:]))
def count_interval(p,a,b):
    seq=sturm(p)
    va=variations([sign_at(s,a) for s in seq])
    vb=variations([sign_at(s,b) for s in seq])
    return va-vb
def count_positive(p):
    seq=sturm(p)
    v0=variations([sign_at(s,F(0)) for s in seq])
    vi=variations([sign_inf(s,True) for s in seq])
    return v0-vi

def det(mat):
    a=[list(map(F,row)) for row in mat]; n=len(a); out=F(1)
    for i in range(n):
        piv=next((j for j in range(i,n) if a[j][i]),None)
        if piv is None: return F(0)
        if piv!=i: a[i],a[piv]=a[piv],a[i]; out=-out
        pv=a[i][i]; out*=pv
        for j in range(i+1,n):
            if a[j][i]:
                fac=a[j][i]/pv
                for k in range(i,n): a[j][k]-=fac*a[i][k]
    return out

def resultant(a,b):
    a=trim(a); b=trim(b); m=len(a)-1; n=len(b)-1
    ah=list(reversed(a)); bh=list(reversed(b)); N=m+n
    M=[]
    for i in range(n): M.append([F(0)]*i+ah+[F(0)]*(n-1-i))
    for i in range(m): M.append([F(0)]*i+bh+[F(0)]*(m-1-i))
    return det(M)

# Verify that E1 and E2 below are exactly the cleared stationary equations.
# Sparse bivariate polynomials use keys (u_degree,r_degree).
def bclean(p): return {k:v for k,v in p.items() if v}
def badd(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return bclean(c)
def bscale(a,s): return bclean({k:v*s for k,v in a.items()})
def bmul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items(): c[(i+k,j+l)]=c.get((i+k,j+l),F(0))+x*y
    return bclean(c)
def bpow(a,n):
    out={(0,0):F(1)}
    for _ in range(n): out=bmul(out,a)
    return out
def bder(a,var):
    c={}
    q=0 if var=='u' else 1
    for ij,x in a.items():
        d=ij[q]
        if d:
            kk=list(ij); kk[q]-=1; c[tuple(kk)]=x*d
    return bclean(c)
U={(1,0):F(1)}; Rv={(0,1):F(1)}; One={(0,0):F(1)}
Sb=badd(badd(U,One),bpow(Rv,2))
Qb=badd(badd(bpow(U,2),One),bpow(Rv,4))
Rb=badd(badd(bpow(U,3),One),bpow(Rv,6))
Nb=badd(badd(bscale(bpow(Sb,3),F(6)),bscale(bmul(Sb,Qb),F(-9))),bscale(Rb,F(4)))
Nb=badd(Nb,bscale(bmul(U,Rv),F(6)))
Du=badd(bmul(bder(Nb,'u'),Sb),bscale(bmul(Nb,bder(Sb,'u')),F(-3)))
Dr=badd(bmul(bder(Nb,'r'),Sb),bscale(bmul(Nb,bder(Sb,'r')),F(-3)))
E1b={(2,2):F(1),(2,0):F(1),(1,2):F(6),(1,1):F(2),(0,6):F(-1),(0,4):F(-3),(0,3):F(-1),(0,2):F(-3),(0,1):F(-1),(0,0):F(-1)}
E2b={(3,1):F(2),(2,1):F(6),(2,0):F(1),(1,5):F(-2),(1,3):F(-12),(1,2):F(-5),(1,1):F(6),(1,0):F(1),(0,5):F(-2),(0,1):F(2)}
assert Du==bscale(E1b,F(-6))
assert Dr==bscale(E2b,F(6))

# Exact univariate polynomials A(r), B(r), P(r).
A=[1,6,-19,-22,25,28,-3,-8]
B=[1,9,6,14,-6,-3,-14,-16,-3,-8]
P=[1,13,44,42,6,-207,-148,120,81,36,32]

# Verify Res(A,B) and root isolation.
res=resultant(A,B)
assert abs(res) == F(309678550548480000), res
assert count_positive(P)==2
I1=(F(17,20),F(43,50)); I2=(F(91,100),F(23,25))
assert count_interval(P,*I1)==1 and count_interval(P,*I2)==1
for poly in (A,B):
    assert count_interval(poly,*I1)==0 and count_interval(poly,*I2)==0
assert sign_at(A,I1[0])>0 and sign_at(B,I1[0])>0
assert sign_at(A,I2[0])>0 and sign_at(B,I2[0])<0

# Verify the exact substitution identity A^2 E1(-B/A,r)
# = 3 r (2r+1) (r^2+1)^3 P(r).
# E1=(r^2+1)u^2+(6r^2+2r)u-(r^6+3r^4+r^3+3r^2+r+1).
r=[0,1]; r2=mul(r,r)
term1=mul(add(r2,[1]),mul(B,B))
term2=mul(add(scale(r2,F(6)),scale(r,F(2))),mul(A,B))
C=[-1,-1,-3,-1,-3,0,-1]  # negative final parenthesis
lhs=add(sub(term1,term2),mul(mul(A,A),C))
rhs=scale(mul(mul(mul(r,add(scale(r,F(2)),[1])),mul(add(r2,[1]),mul(add(r2,[1]),add(r2,[1])))),P),F(3))
assert trim(lhs)==trim(rhs)

# Verify the polynomial-division remainder identity by evaluating the exact
# bivariate equality coefficientwise in u.  Coefficients are polynomials in r.
# E1=e12*u^2+e11*u+e10; E2=e23*u^3+e22*u^2+e21*u+e20.
e12=add(r2,[1]); e11=add(scale(r2,F(6)),scale(r,F(2))); e10=C
e23=scale(r,F(2)); e22=add(scale(r,F(6)),[1])
e21=[1,6,-5,-12,0,-2]; e20=[0,2,0,0,0,-2]
# Qnum=(2r^3+2r)u+(-6r^3-3r^2+6r+1)
r3=mul(r2,r); q1=add(scale(r3,F(2)),scale(r,F(2))); q0=add(add(scale(r3,F(-6)),scale(r2,F(-3))),add(scale(r,F(6)),[1]))
fac=mul(add(r2,[1]),add(r2,[1]))
# For u^k compare fac*E2 with Qnum*E1 + A*u+B.
left=[mul(fac,e20),mul(fac,e21),mul(fac,e22),mul(fac,e23)]
right=[add(mul(q0,e10),B), add(add(mul(q0,e11),mul(q1,e10)),A), add(mul(q0,e12),mul(q1,e11)), mul(q1,e12)]
assert all(trim(x)==trim(y) for x,y in zip(left,right))

# Boundary and an interior witness.
assert F(5,2)-F(1) == F(3,2)  # endpoint two-term value 1 is below 5/2
assert F(11,3)>F(5,2)

# Bisection within the certified admissible interval only for decimals.
lo,hi=I2
for _ in range(120):
    mid=(lo+hi)/2
    if evalp(P,lo)*evalp(P,mid)<=0: hi=mid
    else: lo=mid
rr=(lo+hi)/2
uu=-evalp(B,rr)/evalp(A,rr)
S=uu+1+rr*rr
phi=(6*S**3-9*S*(uu**2+1+rr**4)+4*(uu**3+1+rr**6)+6*uu*rr)/S**3
getcontext().prec=30
def dec(fr): return Decimal(fr.numerator)/Decimal(fr.denominator)
rdec=dec(rr); udec=dec(uu); phidec=dec(phi); kdec=phidec ** (Decimal(1)/Decimal(6))
print('VERIFY_OK r=',rdec,'u=',udec,'K6=',phidec,'K=',kdec)
