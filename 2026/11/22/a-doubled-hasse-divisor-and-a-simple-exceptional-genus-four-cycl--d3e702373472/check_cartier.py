#!/usr/bin/env python3
"""Exact characteristic-31 Cartier-coefficient certificate for a cyclic-quintic genus-four family."""
from math import comb
P=31
BASIS=((0,2),(0,3),(0,4),(1,4))

def clean(d):
    return {mon:c%P for mon,c in d.items() if c%P}

def add(f,g,scale=1):
    z=dict(f)
    for mon,v in g.items(): z[mon]=(z.get(mon,0)+scale*v)%P
    return clean(z)

def mul(f,g):
    z={}
    for (u,v),c in f.items():
        for (w,t),d in g.items():
            m=(u+w,v+t)
            z[m]=(z.get(m,0)+c*d)%P
    return clean(z)

def power(f,n):
    z={(0,0):1}
    for _ in range(n): z=mul(z,f)
    return z

def coefficient(r,e):
    z={}
    for n_x3 in range(r+1):
        n_ax=e-3*n_x3
        n_b=r-n_x3-n_ax
        if n_ax<0 or n_b<0: continue
        mon=(n_ax,n_b)
        z[mon]=(z.get(mon,0)+comb(r,n_x3)*comb(r-n_x3,n_ax))%P
    return clean(z)

def matrix():
    m=[[{} for _ in BASIS] for _ in BASIS]
    for src,(i,j) in enumerate(BASIS):
        assert (P*j-j)%5==0
        r=(P*j-j)//5
        for dst,(k,h) in enumerate(BASIS):
            if h!=j: continue
            e=(k+1)*P-1-i
            m[dst][src]=coefficient(r,e)
    return m

def value(f,a,b):
    return sum(c*pow(a,i,P)*pow(b,j,P) for (i,j),c in f.items())%P

def rank(rows):
    a=[row[:] for row in rows]
    n=len(a); k=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(k,n) if a[i][j]),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        q=pow(a[k][j],-1,P);a[k]=[q*v%P for v in a[k]]
        for i in range(n):
            if i==k:continue
            c=a[i][j];a[i]=[(x-c*y)%P for x,y in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k

def main():
    M=matrix()
    for i in range(4):
        for j in range(4):
            assert bool(M[i][j]) == (i==j or (i>=2 and j>=2))
    B=add(mul(M[2][2],M[3][3]),mul(M[2][3],M[3][2]),-1)
    det=mul(mul(M[0][0],M[1][1]),B)
    A={(0,2):1,(3,0):-7}
    G={(0,2):1,(3,0):-1}
    target={k:14*v%P for k,v in mul(power(A,2),power(G,12)).items()}
    assert det==clean(target), (det,target)
    assert M[0][0]=={(3,0):3,(0,2):4}
    assert B=={k:(-8*v)%P for k,v in power(G,9).items()},'bottom block determinant'
    assert M[1][1]==mul({(3,0):98,(0,2):-14},power(G,3)), "middle 1x1 factor"
    # At a=1,b^2=7 the top two diagonal entries vanish, bottom determinant = -8*6^9 nonzero.
    for a in range(P):
        for b in range(P):
            if (b*b-a*a*a)%P==0:continue
            numeric=[[value(M[i][j],a,b) for j in range(4)] for i in range(4)]
            expected=2 if (b*b-7*a*a*a)%P==0 else 4
            assert rank(numeric)==expected,(a,b,rank(numeric),expected)
    print('PASS: 4x4 Cartier coefficient matrix, symbolic determinant identity, exact bottom determinant, all 930 smooth F31 pairs')
    print('det H = 14 (b^2 - 7a^3)^2 (b^2 - a^3)^12 mod 31')
    print('matrix nonzero entries, (row,col, coefficient terms):')
    for i in range(4):
        for j in range(4):
            if M[i][j]: print(i,j,sorted(M[i][j].items()))
    print('Examples (a,b): (1,10) exceptional rank',rank([[value(M[i][j],1,10) for j in range(4)] for i in range(4)]),'; (1,0) generic rank',rank([[value(M[i][j],1,0) for j in range(4)] for i in range(4)]))
if __name__=='__main__':main()
