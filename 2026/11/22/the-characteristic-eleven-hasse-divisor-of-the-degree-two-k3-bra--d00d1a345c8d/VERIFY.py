#!/usr/bin/env python3
"""Exact finite-field verification of a genus-ten branch-sextic Hasse divisor.
Standard library only. All arithmetic is over F_11, with t formal.
"""
from math import factorial
P=11
BASIS=[(i,j,3-i-j) for i in range(4) for j in range(4-i)]
assert len(BASIS)==10

def add(F,G):
    H=F.copy()
    for n,c in G.items():H[n]=(H.get(n,0)+c)%P
    return {n:c for n,c in H.items() if c}
def scale(F,c,shift=0):
    return {n+shift:v*c%P for n,v in F.items() if v*c%P}
def mul(F,G):
    H={}
    for i,a in F.items():
        for j,b in G.items():
            H[i+j]=(H.get(i+j,0)+a*b)%P
    return {i:a for i,a in H.items() if a}
def power(F,n):
    ans={0:1}
    while n:
        if n&1:ans=mul(ans,F)
        F=mul(F,F);n//=2
    return ans

def coefficient_tables():
    # Homogeneous and dehomogenized multinomial expansions, assembled separately.
    hom={};aff={}
    for a in range(11):
        for c in range(11-a):
            for d in range(11-a-c):
                e=10-a-c-d
                m=factorial(10)//(factorial(a)*factorial(c)*factorial(d)*factorial(e))%P
                v=(6*a+2*e,6*c+2*e,6*d+2*e)
                h=hom.setdefault(v,{})
                h[e]=(h.get(e,0)+m)%P
                # In F(x,y,1)^10 the chosen constant term has exponent d.
                vv=(6*a+2*e,6*c+2*e)
                f=aff.setdefault(vv,{})
                f[e]=(f.get(e,0)+m)%P
    return hom,aff

def matrices():
    hom,aff=coefficient_tables()
    M=[];N=[]
    for i,j,k in BASIS:
        row=[];row2=[]
        for r,s,t in BASIS:
            key=(11*(i+1)-(r+1),11*(j+1)-(s+1),11*(k+1)-(t+1))
            key2=key[:2]
            row.append({m:v for m,v in hom.get(key,{}).items() if v%P})
            row2.append({m:v for m,v in aff.get(key2,{}).items() if v%P})
        M.append(row);N.append(row2)
    assert M==N
    return M

def polval(F,b):return sum(c*pow(b,i,P) for i,c in F.items())%P

def rank(A):
    A=[row[:] for row in A]; n=len(A);r=0
    for c in range(len(A[0])):
        piv=next((k for k in range(r,n) if A[k][c]%P),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,P)
        A[r]=[(z*inv)%P for z in A[r]]
        for k in range(n):
            if k!=r:
                f=A[k][c]
                if f:A[k]=[(x-f*y)%P for x,y in zip(A[k],A[r])]
        r+=1
        if r==n:break
    return r

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%P for j in range(n)] for i in range(n)]

def main():
    M=matrices()
    A={2:1,5:-1%P};B={1:2,4:4};C={1:3,4:2,7:5,10:1}
    support={0:(0,A),3:(3,A),9:(9,A),1:(8,B),8:(1,B),
             2:(7,B),7:(2,B),4:(6,B),6:(4,B),5:(5,C)}
    assert {(i,j) for i in range(10) for j in range(10) if M[i][j]} == {(i,j) for i,(j,x) in support.items()}
    for i,(j,f) in support.items():assert M[i][j]=={k:v%P for k,v in f.items()}
    # Determinant: permutation has three transpositions.
    D=scale(mul(mul(power(A,3),power(B,6)),C),-1)
    U={0:-1%P,3:1};V={0:1,3:2};W={0:2,3:1};Q={0:4,3:1}
    expected=scale(mul(mul(mul(mul({13:1},power(U,4)),power(V,6)),W),Q),9)
    assert D==expected
    counts={0:0,4:0,6:0,9:0,10:0};bad=[];details=[]
    for t in range(11):
        if pow(t,3,11)==6:
            bad.append(t);continue
        H=[[polval(M[i][j],t) for j in range(10)] for i in range(10)]
        r=rank(H)
        Hp=[[(i==j)*1 for j in range(10)] for i in range(10)]
        for _ in range(20):Hp=matmul(Hp,H)
        assert rank(Hp)==r # rational-field semilinear Frobenius twist is trivial
        u=pow(t,3,11)
        goal=0 if t==0 else 4 if u==5 else 6 if u==1 else 9 if u in (7,9) else 10
        assert r==goal,(t,r,goal)
        counts[r]+=1;details.append((t,r))
    assert counts=={0:1,4:1,6:1,9:2,10:5},counts
    assert bad==[8],bad
    assert [t for t in range(11) if pow(t,3,11)==1]==[1]
    assert [t for t in range(11) if pow(t,3,11)==5]==[3]
    assert [t for t in range(11) if pow(t,3,11)==7]==[6]
    assert [t for t in range(11) if pow(t,3,11)==9]==[4]
    assert [t for t in range(11) if pow(t,3,11)==6]==[8]
    assert len(set((0,1,5,7,9,6)))==6
    print('GENUS10_BRANCH_SEXTIC_HASSE_VERIFIED p=11 nonordinary_geometric=13 '
          'smooth_F11=10 ranks_F11=(0:1,4:1,6:1,9:2,10:5) '
          'singular_F11=8 determinant_degree=49')
    print('b,p_rank:',details)
if __name__=='__main__':main()
