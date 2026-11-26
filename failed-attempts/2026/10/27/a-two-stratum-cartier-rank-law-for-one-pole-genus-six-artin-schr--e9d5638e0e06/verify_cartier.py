#!/usr/bin/env python3
"""Exact Cartier rank verification for characteristic-three one-pole genus-six curves.

A finite-field check of the universal formulas; it is not used as a substitute
for the proof of the rank statement over algebraically closed fields.
"""
from itertools import product


def add(u,v,q):
    return ((u%3+v%3)%3+3*((u//3+v//3)%3)) if q==9 else (u+v)%3


def neg(u,q):
    return ((-u%3)+3*(-(u//3)%3)) if q==9 else -u%3


def mul(u,v,q):
    if q==3:return u*v%3
    a,b=u%3,u//3
    c,d=v%3,v//3
    return ((a*c+2*b*d)%3)+3*((a*d+b*c)%3)


def cube(u,q):
    return mul(mul(u,u,q),u,q)


def inv(u,q):
    assert u
    for x in range(1,q):
        if mul(u,x,q)==1:return x
    raise AssertionError('inversion failed')


def field_rank(mat,q):
    z=[list(row) for row in mat]
    rank=0
    cols=len(z[0])
    for col in range(cols):
        pivot=next((i for i in range(rank,len(z)) if z[i][col]),None)
        if pivot is None:continue
        z[rank],z[pivot]=z[pivot],z[rank]
        fac=inv(z[rank][col],q)
        z[rank]=[mul(t,fac,q) for t in z[rank]]
        for i in range(len(z)):
            if i==rank or z[i][col]==0:continue
            fac=z[i][col]
            z[i]=[add(a,neg(mul(fac,b,q),q),q) for a,b in zip(z[i],z[rank])]
        rank+=1
        if rank==len(z):break
    return rank


def build_cartier(a,b,c,d,q):
    # The differential basis is dx, xdx, x²dx, x³dx, ydx, xydx.
    # Derive each column by expanding y=y³-f(x), using C(g³ w)=g C(w)
    # and C(x^n dx)=0 unless n=2 mod 3.
    f={7:1,5:a,4:b,2:c,1:d}
    images=[]
    for i,j in [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)]:
        out=[0]*6
        if j==0:
            if i%3==2:
                out[(i-2)//3]=1
        else:
            for e,coef in f.items():
                n=e+i
                if n%3==2:
                    k=(n-2)//3
                    assert k<=3
                    out[k]=add(out[k],neg(cube(coef,q),q),q)
        images.append(out)
    return [[images[j][i] for j in range(6)] for i in range(6)]


def matmul(A,B,q):
    out=[]
    for row in A:
        new=[]
        for j in range(len(B[0])):
            s=0
            for k,t in enumerate(row):s=add(s,mul(t,B[k][j],q),q)
            new.append(s)
        out.append(new)
    return out


def matcube(A,q):return [[cube(z,q) for z in row] for row in A]


def checks(q):
    count={3:0,4:0}
    for a,b,c,d in product(range(q),repeat=4):
        M=build_cartier(a,b,c,d,q)
        # Cartier is sigma-linear with sigma(x)=x^(1/3). For q=9
        # sigma(x)=x^3; for q=3 it is identity.
        M2=matmul(M,matcube(M,q),q)
        M3=matmul(M2,M,q) if q==3 else matmul(M2,M,q)
        # For GF9, sigma²=identity, so M3=M2*M.
        r=(field_rank(M,q),field_rank(M2,q),field_rank(M3,q))
        expected=(3 if a else 2,1,0)
        assert r==expected,(q,a,b,c,d,r,expected)
        count[6-r[0]]+=1
    assert count[3]==(q-1)*q**3 and count[4]==q**3,(q,count)
    return count

if __name__=='__main__':
    print('VERIFY_OK: characteristic 3 genus 6 Cartier ranks',checks(3),'F9',checks(9))
