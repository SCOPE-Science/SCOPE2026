#!/usr/bin/env python3
"""Separate direct polynomial-power check over F_{p^2}; exhaustive coefficient parameters."""

def add(a,b,p):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def mul(a,b,p,d):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def rank(M,p,d):
    # For 3x3 matrices only, derive rank by minors over the extension.
    z=(0,0)
    if any(x!=z for row in M for x in row): r=1
    else: return 0
    subidx=((0,1),(0,2),(1,2))
    for i,j in subidx:
        for u,v in subidx:
            s=mul(M[i][u],M[j][v],p,d)
            t=mul(M[i][v],M[j][u],p,d)
            if add(s,((-t[0])%p,(-t[1])%p),p)!=z:r=2
    def det3():
        terms=[]
        for a,b,c,sign in ((0,1,2,1),(1,2,0,1),(2,0,1,1),(2,1,0,-1),(1,0,2,-1),(0,2,1,-1)):
            val=mul(mul(M[0][a],M[1][b],p,d),M[2][c],p,d)
            terms.append((sign*val[0]%p,sign*val[1]%p))
        out=z
        for val in terms:out=add(out,val,p)
        return out
    if det3()!=z:return 3
    return r

def direct_M(c,p,d):
    one=(1,0);zero=(0,0);m=(p-1)//2
    poly=[one]
    f=[zero for _ in range(9)]
    f[0]=one;f[4]=c;f[8]=one
    for _ in range(m):
        nxt=[zero]*(len(poly)+8)
        for i,a in enumerate(poly):
            for j,b in ((0,one),(4,c),(8,one)):
                nxt[i+j]=add(nxt[i+j],mul(a,b,p,d),p)
        poly=nxt
    return [[poly[p*i-j] for j in range(1,4)] for i in range(1,4)]

for p,d in ((7,3),(11,2)):
    assert pow(d,(p-1)//2,p)==p-1
    z=(0,0);one=(1,0)
    totals={};nonord=0
    for x in range(p):
        for y in range(p):
            c=(x,y)
            c2=mul(c,c,p,d)
            if c2==(4,0):continue
            A=mul((3,0),c,p,d) if p==7 else add((5,0),((-c2[0])%p,(-c2[1])%p),p)
            if p==7:
                B=mul(c,add(c2,(-1%p,0),p),p,d)
            else:
                B=mul(mul(c,add(c2,(-3%p,0),p),p,d),add(c2,one,p),p,d)
            e_rank=(2 if A!=z else 0)+(1 if B!=z else 0)
            M=direct_M(c,p,d)
            assert M[0][2]==A and M[2][0]==A and M[1][1]==B,(p,c,M,A,B)
            assert rank(M,p,d)==e_rank,(p,c,M,e_rank)
            totals[e_rank]=totals.get(e_rank,0)+1
            if e_rank<3:nonord+=1
    expected={7:{0:1,2:2,3:44},11:{1:2,2:5,3:112}}[p]
    assert totals==expected,(p,totals,expected)
    print('EXTENSION_ENUMERATION_PASS',p,'rank_counts',totals,'nonordinary',nonord)
print('ALL_EXTENSION_CHECKS_PASS')
