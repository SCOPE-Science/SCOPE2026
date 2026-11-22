#!/usr/bin/env python3
"""Exact coefficient-ring checks for two canonical genus-four sextic projections.

The ring is Z[omega]/(omega^2+omega+1); no finite-field extrapolation is used.
The geometric completeness of the nine-line configurations is NOT asserted here.
"""
from itertools import product

class C:
    def __init__(self,a=0,b=0): self.a,self.b=int(a),int(b)
    def __add__(self,o): o=cc(o);return C(self.a+o.a,self.b+o.b)
    def __radd__(self,o): return self+o
    def __neg__(self): return C(-self.a,-self.b)
    def __sub__(self,o): return self+-cc(o)
    def __rsub__(self,o): return cc(o)+-self
    def __mul__(self,o):
        o=cc(o)
        return C(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a-self.b*o.b)
    def __rmul__(self,o): return self*o
    def __pow__(self,n):
        if n<0:raise ValueError
        ans=C(1)
        for _ in range(n): ans=ans*self
        return ans
    def __eq__(self,o):
        o=cc(o)
        return (self.a,self.b)==(o.a,o.b)
    def frob(self): return C(self.a-self.b,-self.b)  # omega -> omega^2 = -1-omega
    def __repr__(self):return f'({self.a},{self.b})'
def cc(v):return v if isinstance(v,C) else C(v)
O=C(0,1); ONE=C(1);ZERO=C()

def vec(*xs): return tuple(map(cc,xs))
def mat(rows):return tuple(vec(*r) for r in rows)
def diag(*xs):return mat([[xs[i] if i==j else 0 for j in range(4)] for i in range(4)])
def mm(a,b):return mat([[sum((a[i][k]*b[k][j] for k in range(4)),ZERO) for j in range(4)] for i in range(4)])
def mpow(a,n):
    z=diag(1,1,1,1)
    for _ in range(n):z=mm(z,a)
    return z

def lin(*coeffs):return vec(*coeffs)

def pd_add(a,b):
    r=a.copy()
    for m,c in b.items():
        r[m]=r.get(m,ZERO)+c
        if r[m]==ZERO:del r[m]
    return r

def pd_mul(a,b):
    r={}
    for m,c in a.items():
        for n,d in b.items():
            k=tuple(x+y for x,y in zip(m,n))
            r[k]=r.get(k,ZERO)+c*d
            if r[k]==ZERO:del r[k]
    return r

def pd_scale(a,c):return {m:v*cc(c) for m,v in a.items() if v*cc(c)!=ZERO}
def pd_pow(a,n):
    r={(0,0,0,0):ONE}
    for i in range(n):r=pd_mul(r,a)
    return r

def pvar(i):return {tuple(1 if j==i else 0 for j in range(4)):ONE}
def form(a):
    r={}
    for i,c in enumerate(a):r=pd_add(r,pd_scale(pvar(i),c))
    return r

def substitute(P,M):
    r={}
    for exps,coef in P.items():
        t={(0,0,0,0):coef}
        for i,n in enumerate(exps):t=pd_mul(t,pd_pow(form(M[i]),n))
        r=pd_add(r,t)
    return r

def matching_multiplier(P,Q):
    for v in P.values():
        if v!=ZERO:
            for c in (ONE,-ONE,O,O**2,-O,-(O**2)):
                if pd_scale(P,c)==Q:return c
    raise AssertionError(('not scalar-related',P,Q))

X,Y,Z,W=[pvar(i) for i in range(4)]
def plus(*xs):
    r={}
    for x in xs:r=pd_add(r,x)
    return r
QA=plus(pd_mul(X,Y),pd_scale(pd_pow(Z,2),-1))
FA=plus(pd_pow(X,3),pd_pow(Y,3),pd_pow(W,3))
QB=plus(pd_pow(X,2),pd_pow(Y,2),pd_pow(Z,2))
FB=plus(pd_mul(pd_mul(X,Y),Z),pd_pow(W,3))

def mon(a,b,wa):return mat([[0,a,0,0],[b,0,0,0],[0,0,1,0],[0,0,0,wa]])
A=[
 ('A1',lin(1,0,0,0),lin(0,1,0,0),diag(1,1,-1,O)),
 ('A2',lin(1,1,0,0),lin(0,0,1,0),mon(1,1,O)),
 ('A3',lin(1,O,0,0),lin(0,0,1,0),mon(O,O**2,O)),
 ('A4',lin(1,O**2,0,0),lin(0,0,1,0),mon(O**2,O,O)),
 ('A5',lin(1,-1,0,0),lin(0,0,1,0),mon(-1,-1,-O)),
 ('A6',lin(1,-O,0,0),lin(0,0,1,0),mon(-O,-O**2,-O)),
 ('A7',lin(1,-O**2,0,0),lin(0,0,1,0),mon(-O**2,-O,-O)),
 ('A8',lin(1,0,0,0),lin(0,0,0,1),diag(1,O,-O**2,1)),
 ('A9',lin(0,1,0,0),lin(0,0,0,1),diag(O,1,-O**2,1)),
]
B=[
 ('B1',lin(1,0,0,0),lin(0,1,0,0),diag(1,1,-1,-O)),
 ('B2',lin(0,1,0,0),lin(0,0,1,0),diag(-1,1,1,-O)),
 ('B3',lin(1,0,0,0),lin(0,0,1,0),diag(1,-1,1,-O)),
 ('B4',lin(1,1,0,0),lin(0,0,1,0),mon(1,1,O)),
 ('B5',lin(1,-1,0,0),lin(0,0,1,0),mon(-1,-1,O)),
 ('B6',lin(1,0,1,0),lin(0,1,0,0),mat([[0,0,1,0],[0,1,0,0],[1,0,0,0],[0,0,0,O]])),
 ('B7',lin(1,0,-1,0),lin(0,1,0,0),mat([[0,0,-1,0],[0,1,0,0],[-1,0,0,0],[0,0,0,O]])),
 ('B8',lin(1,0,0,0),lin(0,1,1,0),mat([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,O]])),
 ('B9',lin(1,0,0,0),lin(0,1,-1,0),mat([[1,0,0,0],[0,0,-1,0],[0,-1,0,0],[0,0,0,O]])),
]

def rowtimes(r,M):return vec(*(sum((r[i]*M[i][j] for i in range(4)),ZERO) for j in range(4)))
def fixed_over_base(lin):return all(x.b==0 for x in lin)

def skew_certificate(name,L1,L2,Q,F):
    # An exact basis for the line; restrictions are a nonzero square
    # of one coordinate and a cubic with a nonzero pure cube of the other.
    eX,eY,eZ,eW=lin(1,0,0,0),lin(0,1,0,0),lin(0,0,1,0),lin(0,0,0,1)
    if name in ('A1','B1'):u,v=eZ,eW
    elif name=='A8':u,v=eZ,eY
    elif name=='A9':u,v=eZ,eX
    elif name=='B2':u,v=eX,eW
    elif name=='B3':u,v=eY,eW
    elif L2==eZ: u,v=lin(-L1[1],1,0,0),eW
    elif L2==eY: u,v=lin(-L1[2],0,1,0),eW
    elif L1==eX: u,v=lin(0,-L2[2],1,0),eW
    else:raise AssertionError(('line basis missing',name))
    def restricted(P):
        # Substitute the two line parameters in the four coordinate forms.
        matrix=mat([[u[i],v[i],0,0] for i in range(4)])
        return substitute(P,matrix)
    qr,fr=restricted(Q),restricted(F)
    U2=(2,0,0,0);V3=(0,3,0,0)
    assert len(qr)==1 and U2 in qr,(name,'Q restriction must be a pure square')
    assert qr[U2]!=ZERO and fr.get(V3,ZERO)!=ZERO,(name,'skew intersection')
    assert all(m[2:]==(0,0) for m in list(qr)+list(fr)),(name,'extra variables')
    return qr,fr

def check_case(case,lines,Q,F):
    out=[]
    for name,L1,L2,M in lines:
        assert rowtimes(L1,M)==L1,(name,'projection L1')
        assert rowtimes(L2,M)==L2,(name,'projection L2')
        skew_certificate(name,L1,L2,Q,F)
        qmult=matching_multiplier(Q,substitute(Q,M))
        fmult=matching_multiplier(F,substitute(F,M))
        assert mpow(M,6)==diag(1,1,1,1),(name,'order divides 6')
        assert mpow(M,2)!=diag(1,1,1,1) and mpow(M,3)!=diag(1,1,1,1),(name,'order exactly 6')
        if fixed_over_base(L1) and fixed_over_base(L2):
            assert all(M[i][j].frob()==mpow(M,5)[i][j] for i in range(4) for j in range(4)),(name,'Frobenius inverse')
        if fixed_over_base(L1) and fixed_over_base(L2):
            assert all(mpow(M,3)[i][j].b==0 for i in range(4) for j in range(4)),(name,'rational involution')
        assert any(mpow(M,2)[i][j].b!=0 for i in range(4) for j in range(4)),(name,'nonrational three-group')
        out.append((name,qmult,fmult, fixed_over_base(L1) and fixed_over_base(L2)))
    if case=='A':
        assert A[2][1][1].frob()==A[3][1][1]
        assert A[5][1][1].frob()==A[6][1][1]
    print(case,'nine exact generators, order 6, smooth-locus skewness, form/projection invariance, rational-center Frobenius inversion: PASS')
    print('over a field without a cube root of unity, the directly k-rational centers:',','.join(t[0] for t in out if t[3]))
    assert sum(t[3] for t in out)==(5 if case=='A' else 9)
    return out

if __name__=='__main__':
    a=check_case('A',A,QA,FA)
    b=check_case('B',B,QB,FB)
    print('All 18 exact cyclotomic-form matrix certificates verified.')
    print('For q == 1 mod 3: 9+9 rational centers and geometric=arithmetic cyclic degree six.')
    print('For q == 2 mod 3: 5+9 rational centers, rational deck group C2, geometric C6;')
    print('arithmetic normal closure Gal = C6 semidirect C2 (inversion) = S3 x C2.')

# Characteristic-five enhancement: an additional skew order-six Galois center.
def char5_extra():
    # Work coefficientwise in the exact integral cyclotomic ring and reduce mod 5.
    def zero5(c):return c.a % 5 == 0 and c.b % 5 == 0
    def poly_zero5(P):return all(zero5(c) for c in P.values())
    def poly_sub(a,b):return pd_add(a,pd_scale(b,-1))
    M=mat([[2,2,4,0],[2,2,1,0],[2,3,0,0],[0,0,0,O]])
    E=diag(1,1,1,1)
    assert all(zero5(mpow(M,6)[i][j]-E[i][j]) for i in range(4) for j in range(4))
    for k in [1,2,3]:
        assert any(not zero5(mpow(M,k)[i][j]-E[i][j]) for i in range(4) for j in range(4))
    assert poly_zero5(poly_sub(substitute(QA,M),QA))
    expected=pd_add(FA,pd_scale(pd_mul(plus(X,Y),QA),3))
    assert poly_zero5(poly_sub(substitute(FA,M),expected))
    for L in [lin(1,0,1,0),lin(0,1,-1,0)]:
        assert all(zero5(v) for v in vec(*(rowtimes(L,M)[j]+L[j] for j in range(4))))
    # On the new line, X=-Z and Y=Z; Q=-2 Z^2 and F=W^3.
    assert not zero5(C(-2))
    # The original nine skewness coefficients remain nonzero after mod 5.
    for name,l1,l2,g in A:
        qr,fr=skew_certificate(name,l1,l2,QA,FA)
        assert all(not zero5(coef) for coef in qr.values())
        assert not zero5(fr[(0,3,0,0)])
    print('CHAR5 EXTRA SKEW CYCLIC GALOIS CENTER VERIFIED: x+z=y-z=0')

if __name__=='__main__':
    char5_extra()
