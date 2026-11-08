#!/usr/bin/env python3
"""Exact checks for Radau IIA graph-heat positivity on rectangular rook graphs.

Python 3, standard library only. A proof of the universal statements accompanies
this certificate; finite matrix tests are cross-checks, not a substitute.
"""
from fractions import Fraction as Q
from math import comb

# Sparse formal polynomials in (p,q,h) with integer coefficients.
def mon(i=0,j=0,k=0,c=1):
    return {(i,j,k):c} if c else {}
def add(*xs):
    out={}
    for x in xs:
        for k,v in x.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def mul(x,y):
    out={}
    for (i,j,k),v in x.items():
        for (a,b,c),w in y.items():
            t=(i+a,j+b,k+c);out[t]=out.get(t,0)+v*w
    return {k:v for k,v in out.items() if v}
def scale(x,c):return {k:v*c for k,v in x.items() if v*c}
def power(x,n):
    z=mon()
    for _ in range(n):z=mul(z,x)
    return z
one=mon();p=mon(i=1);q=mon(j=1);h=mon(k=1)
zp=mul(p,h);zq=mul(q,h);zs=add(zp,zq)
def d(z):return add(power(z,2),scale(z,4),scale(one,6))
def num(z):return add(scale(one,6),scale(z,-2))
Dp,Dq,Ds=map(d,(zp,zq,zs)); Np,Nq,Ns=map(num,(zp,zq,zs))
DD=mul(mul(Dp,Dq),Ds)
Ap=mul(mul(Np,Dq),Ds);Aq=mul(mul(Dp,Nq),Ds);As=mul(mul(Dp,Dq),Ns)
Pminus=add(p,scale(one,-1));Qminus=add(q,scale(one,-1))
Dnum=add(DD,mul(Pminus,Ap),mul(Qminus,Aq),mul(mul(Pminus,Qminus),As))
Epnum=add(DD,scale(Ap,-1),mul(Qminus,Aq),scale(mul(Qminus,As),-1))
Eqnum=add(DD,mul(Pminus,Ap),scale(Aq,-1),scale(mul(Pminus,As),-1))
Fnum=add(DD,scale(Ap,-1),scale(Aq,-1),As)
Fexpected=add(
    mul(mul(power(p,2),power(q,2)),mul(power(add(p,q),2),power(h,6))),
    scale(mul(mul(mul(p,q),add(p,q)),mul(add(scale(power(p,2),3),scale(mul(p,q),7),scale(power(q,2),3)),power(h,5))),2),
    scale(mul(mul(mul(p,q),add(scale(power(p,2),4),scale(mul(p,q),9),scale(power(q,2),4))),power(h,4)),12),
    scale(mul(mul(mul(p,q),add(p,q)),power(h,3)),180),
    scale(mul(mul(p,q),power(h,2)),216))
assert Fnum==Fexpected, 'universal distance-two numerator identity'
assert all(v>0 for v in Fnum.values()), 'distance-two coefficients'

# Exact polynomial operations for fixed integral (p,q).
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out
def padd(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]+=x
    return out
def pscale(a,c):return [v*c for v in a]
def denom(k):return [6,4*k,k*k]
def numer(k):return [6,-2*k]
def coeffs(p,q):
    aa,bb,cc=denom(p),denom(q),denom(p+q)
    u,v,w=numer(p),numer(q),numer(p+q)
    z=pmul(pmul(aa,bb),cc)
    x=pmul(pmul(u,bb),cc);y=pmul(pmul(aa,v),cc);zz=pmul(pmul(aa,bb),w)
    return [padd(padd(z,pscale(x,p-1)),padd(pscale(y,q-1),pscale(zz,(p-1)*(q-1)))),
            padd(padd(z,pscale(x,-1)),padd(pscale(y,q-1),pscale(zz,-(q-1)))),
            padd(padd(z,pscale(x,p-1)),padd(pscale(y,-1),pscale(zz,-(p-1)))),
            padd(padd(z,pscale(x,-1)),padd(pscale(y,-1),zz))]
def transform(a,start,step):
    z=[Q(0)]*len(a)
    for k,c in enumerate(a):
        for j in range(k+1):z[j]+=Q(c)*comb(k,j)*start**(k-j)*step**j
    return z
def bern(a,A,B):
    z=transform(a,Q(A),Q(B)-Q(A));n=len(z)-1
    return [sum((z[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)),Q(0)) for k in range(n+1)]

safe=[(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)]
count_bern=0
for p0,q0 in safe:
    D,E1,E2,F=coeffs(p0,q0)
    for E in (E1,E2,F):
        assert all(c>=0 for c in E[1:]) and any(c>0 for c in E[1:]) and E[0]==0,(p0,q0,E)
    for A,B in [(0,1),(1,Q(3,2)),(Q(3,2),2)]:
        b=bern(D,A,B)
        assert all(v>0 for v in b),(p0,q0,A,B,b)
        count_bern+=len(b)
    assert all(c>0 for c in transform(D,Q(2),Q(1))), (p0,q0,'shift')

# Explicit symmetric polynomial P(p,q) in the negative-diagonal witness
# at h=12/(p+q): pq*T_xx = -pq*P / (11*(p²+10pq+33q²)*(33p²+10pq+q²)).
P=add(
    scale(power(p,4),33),scale(mul(power(p,3),q),340),
    scale(power(p,3),-384),scale(mul(power(p,2),power(q,2)),1190),
    scale(mul(power(p,2),q),384),scale(power(p,2),-4368),
    scale(mul(p,power(q,3)),340),scale(mul(p,power(q,2)),384),
    scale(mul(p,q),-14496),scale(power(q,4),33),
    scale(power(q,3),-384),scale(power(q,2),-4368))

def substitute_shift(P,p0,q0):
    out={}
    for (i,j,k),v in P.items():
        assert k==0
        for a in range(i+1):
            for b in range(j+1):
                t=(a,b);out[t]=out.get(t,0)+v*comb(i,a)*comb(j,b)*p0**(i-a)*q0**(j-b)
    return {k:v for k,v in out.items() if v}
for base in [(2,7),(3,5),(4,4)]:
    c=substitute_shift(P,*base)
    assert len(c)==15 and all(v>0 for v in c.values()),(base,c)

# Universal polynomial identity for the rational witness (no sampling needed).
tot=add(p,q)
def substitute_witness_h(poly):
    out={}
    for (i,j,k),v in poly.items():
        assert k<=6
        term=scale(mul(mul(power(p,i),power(q,j)),power(tot,6-k)),v*12**k)
        out=add(out,term)
    return out
wD=substitute_witness_h(Dnum)
wden=substitute_witness_h(DD)
A=add(power(p,2),scale(mul(p,q),10),scale(power(q,2),33))
B=add(scale(power(p,2),33),scale(mul(p,q),10),power(q,2))
assert not add(scale(mul(mul(wD,A),B),11),mul(mul(mul(p,q),P),wden)), 'formal diagonal witness identity'

# Exact check of witness algebra at assorted parameter points.
def R(z):return (6-2*z)/(z*z+4*z+6)
def peval(P,p0,q0):return sum(v*p0**i*q0**j for (i,j,k),v in P.items())
for p0 in range(2,21):
    for q0 in range(2,21):
        hh=Q(12,p0+q0);uu,vv,ww=(R(k*hh) for k in (p0,q0,p0+q0))
        dval=1+(p0-1)*uu+(q0-1)*vv+(p0-1)*(q0-1)*ww
        vtest=-Q(p0*q0*peval(P,p0,q0),11*(p0*p0+10*p0*q0+33*q0*q0)*(33*p0*p0+10*p0*q0+q0*q0))
        assert dval==vtest,(p0,q0,dval,vtest)

# Square edge threshold, algebraic point z=15 and positivity at m=37.
# E_m(z)*d(z)*d(2z)=4z^4+(36-4m)z^3+(18m+36)z^2+36mz.
for m in (2,3,4,36,37,38,100):
    for z in (Q(1,2),Q(6),Q(15),Q(20)):
        left=(1+(m-2)*R(z)-(m-1)*R(2*z))*(z*z+4*z+6)*((2*z)**2+4*(2*z)+6)
        right=4*z**4+(36-4*m)*z**3+(18*m+36)*z*z+36*m*z
        assert left==right,(m,z)
assert -810*(11*38-410)<0
assert 99**2-4*4*666==-855

# Whole-matrix inversions independently of the four-entry spectral formula.
def inverse(A):
    n=len(A);B=[[Q(A[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if B[k][j]);B[k],B[j]=B[j],B[k]
        t=B[j][j];B[j]=[x/t for x in B[j]]
        for i in range(n):
            if i!=j:
                t=B[i][j]
                if t:B[i]=[a-t*b for a,b in zip(B[i],B[j])]
    return [r[n:] for r in B]
def matmul(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),Q(0)) for j in range(n)] for i in range(n)]
checks=0
for pp,qq,hh in [(2,2,Q(1,7)),(2,3,Q(5,9)),(2,6,Q(2,3)),(3,4,Q(3,2)),(2,7,Q(12,9))]:
    n=pp*qq
    L=[[Q(0) for _ in range(n)] for _ in range(n)]
    for a in range(n):
        i,j=divmod(a,qq)
        for b in range(n):
            k,l=divmod(b,qq)
            if a!=b and (i==k or j==l):L[a][b]=-1;L[a][a]+=1
    L2=matmul(L,L)
    A=[[Q(6*(i==j))-2*hh*L[i][j] for j in range(n)] for i in range(n)]
    B=[[Q(6*(i==j))+4*hh*L[i][j]+hh*hh*L2[i][j] for j in range(n)] for i in range(n)]
    T=matmul(A,inverse(B))
    u,v,w=(R(k*hh) for k in (pp,qq,pp+qq))
    D=Q(1+(pp-1)*u+(qq-1)*v+(pp-1)*(qq-1)*w,pp*qq)
    E1=Q(1-u+(qq-1)*(v-w),pp*qq)
    E2=Q(1-v+(pp-1)*(u-w),pp*qq)
    F=Q(1-u-v+w,pp*qq)
    for a in range(n):
        for b in range(n):
            i,j=divmod(a,qq);k,l=divmod(b,qq)
            expected=D if a==b else E1 if j==l else E2 if i==k else F
            assert T[a][b]==expected,(pp,qq,hh,a,b)
            checks+=1
    assert all(sum(row)==1 for row in T)
print(f'VERIFY_OK: formal distance-two identity; {count_bern} positive Bernstein coefficients; '
      f'3 positive quadrant expansions; 361 witness equalities; square-edge threshold; '
      f'{checks} exact full-matrix entry identities.')
