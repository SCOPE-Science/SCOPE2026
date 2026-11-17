#!/usr/bin/env python3
"""Exact Cartier-rank checks for y^3=x^7+u*x+1 in characteristic 5.

The F25 check includes genuinely non-prime-field parameters, so inverse
Frobenius twists are used rather than ordinary matrix powers.
"""
from math import comb

P = 5
# F25 = F5[z]/(z^2+2); integers 0..24 encode a+5b*z, z^2=3.
def pair(a): return (a % 5, (a // 5) % 5)
def pack(a,b): return (a % 5) + 5*(b % 5)
def add(x,y):
    a,b=pair(x);c,d=pair(y);return pack(a+c,b+d)
def neg(x):
    a,b=pair(x);return pack(-a,-b)
def mult(x,y):
    a,b=pair(x);c,d=pair(y);return pack(a*c+3*b*d,a*d+b*c)
def powf(x,k):
    ans=1
    while k:
        if k&1:ans=mult(ans,x)
        x=mult(x,x);k//=2
    return ans

def rank(M):
    M=[row[:] for row in M]; n=len(M); r=0
    for j in range(n):
        piv=next((i for i in range(r,n) if M[i][j]),None)
        if piv is None:continue
        M[r],M[piv]=M[piv],M[r]
        inv=powf(M[r][j],23)
        M[r]=[mult(inv,x) for x in M[r]]
        for i in range(n):
            if i!=r and M[i][j]:
                a=M[i][j]
                M[i]=[add(z,neg(mult(a,w))) for z,w in zip(M[i],M[r])]
        r+=1
        if r==n:break
    return r

def mmul(A,B):
    n=len(A)
    return [[sum_f(mult(A[i][k],B[k][j]) for k in range(n)) for j in range(n)] for i in range(n)]
def sum_f(v):
    s=0
    for x in v:s=add(s,x)
    return s

def cartier_matrix(u):
    # Differential basis: dx/y, x dx/y; dx/y^2,...,x^3 dx/y^2.
    basis=[(1,1),(2,1),(1,2),(2,2),(3,2),(4,2)]
    A=[[0]*6 for _ in range(6)]
    for col,(a,j) in enumerate(basis):
        jj=next(z for z in (1,2) if (5*z-j)%3==0)
        c=(5*jj-j)//3
        f=[1,u,0,0,0,0,0,1]
        coeff=[1]
        for _ in range(c):
            new=[0]*(len(coeff)+7)
            for i,v in enumerate(coeff):
                for k,w in enumerate(f):
                    new[i+k]=add(new[i+k],mult(v,w))
            coeff=new
        for row,(b,j2) in enumerate(basis):
            if j2!=jj:continue
            exponent=5*b-a
            if 0<=exponent<len(coeff):
                # inverse Frobenius is z -> z^5 on F25
                A[row][col]=powf(coeff[exponent],5)
    return A

def profile(u):
    A=cartier_matrix(u); result=[6]; prod=[[int(i==j) for j in range(6)] for i in range(6)]
    # C(v)=A*v^{1/5}; C^r(basis)=A*A^{1/5}*...*A^{1/5^(r-1)}.
    twisted=[row[:] for row in A]
    for _ in range(6):
        prod=mmul(prod,twisted)
        result.append(rank(prod))
        twisted=[[powf(x,5) for x in row] for row in twisted]
    return tuple(result)

def symbolic_cartier_certificate():
    """Independent symbolic coefficient extraction in F5[u,x]."""
    # Monomial key (power_x,power_u), coefficient in F5.
    f={(0,0):1,(1,1):1,(7,0):1}
    def times(A,B):
        ans={}
        for (ax,au),a in A.items():
            for (bx,bu),b in B.items():
                key=(ax+bx,au+bu)
                ans[key]=(ans.get(key,0)+a*b)%5
        return {k:v for k,v in ans.items() if v}
    basis=[(1,1),(2,1),(1,2),(2,2),(3,2),(4,2)]
    H=[[{} for _ in range(6)] for _ in range(6)]
    for col,(a,j) in enumerate(basis):
        jp=2 if j==1 else 1
        c=(5*jp-j)//3
        poly={(0,0):1}
        for _ in range(c):poly=times(poly,f)
        for row,(b,j2) in enumerate(basis):
            if j2==jp:
                H[row][col]={u:co for (xp,u),co in poly.items() if xp==5*b-a}
    required={(0,5):{1:1},(1,4):{0:1},(2,1):{3:1},
              (3,0):{2:3},(3,1):{1:1},(4,0):{0:3}}
    for i in range(6):
        for j in range(6):
            assert H[i][j]==required.get((i,j),{}),(i,j,H[i][j])


def check():
    symbolic_cartier_certificate()
    generic=(6,4,3,2,1,0,0)
    exceptional=(6,2,1,0,0,0,0)
    bad=[]
    counts={'generic':0,'exceptional':0,'singular':0}
    for u in range(25):
        if powf(u,7)==2:
            counts['singular']+=1;bad.append(u);continue
        expected=exceptional if u==0 else generic
        computed=profile(u)
        assert computed==expected,(u,computed,expected)
        counts['exceptional' if u==0 else 'generic']+=1
    assert counts=={'generic':23,'exceptional':1,'singular':1},counts
    assert bad==[3],bad
    for u in [0,1,2,3,4,5,6,7,8,9,24]:
        # Every smooth parameter is p-rank zero in the complete finite-field test.
        if powf(u,7)!=2:assert profile(u)[-1]==0
    print('GENUS6_TRIGONAL_DEFORMATION_F25_CARTIER_PASS',counts,
          'generic_profile',generic,'special_profile',exceptional)

if __name__=='__main__':check()
