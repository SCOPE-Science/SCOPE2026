#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-three Schur quartic.
No non-standard dependencies. Operations use polynomial quotient fields.
"""
from itertools import product, combinations
from math import comb

class Field:
    def __init__(self, mod):
        self.mod=tuple(mod)
        self.d=len(mod)-1
        self.q=3**self.d
        self.zero=0;self.one=1
        self.dec=[tuple((n//(3**j))%3 for j in range(self.d)) for n in range(self.q)]
        self.enc={v:i for i,v in enumerate(self.dec)}
        self.add=[[self.enc[tuple((u[j]+v[j])%3 for j in range(self.d))] for v in self.dec] for u in self.dec]
        self.neg=[self.enc[tuple((-u[j])%3 for j in range(self.d))] for u in self.dec]
        self.mul=[]
        for u in self.dec:
            row=[]
            for v in self.dec:
                a=[0]*(2*self.d-1)
                for i in range(self.d):
                    for j in range(self.d):a[i+j]=(a[i+j]+u[i]*v[j])%3
                for h in range(2*self.d-2,self.d-1,-1):
                    c=a[h]
                    for j in range(self.d):a[h-self.d+j]=(a[h-self.d+j]-c*self.mod[j])%3
                row.append(self.enc[tuple(a[:self.d])])
            self.mul.append(row)
    def pow(self,a,n):
        b=1
        while n:
            if n&1:b=self.mul[b][a]
            a=self.mul[a][a];n//=2
        return b
    def sub(self,a,b):return self.add[a][self.neg[b]]

def Ppoints(f,n=4):
    for i in range(n):
        for tail in product(range(f.q),repeat=n-i-1):
            yield (0,)*i+(1,)+tail

def f4(f,v):
    x,y,z,w=v;M=f.mul
    return f.add[f.sub(f.sub(f.pow(x,4),M[x][f.pow(y,3)]),f.pow(z,4))][M[z][f.pow(w,3)]]

def line_rref(f):
    n=4
    for i,j in combinations(range(n),2):
        positions=[(r,c) for r,p in enumerate((i,j)) for c in range(p+1,n) if c not in (i,j)]
        for vals in product(range(f.q),repeat=len(positions)):
            a=[[0]*n for _ in range(2)]
            a[0][i]=a[1][j]=1
            for (r,c),v in zip(positions,vals):a[r][c]=v
            yield tuple(a[0]),tuple(a[1])

def line_inside(f,A,B):
    M=f.mul;plus=f.add
    def term(p,q):
        a,b=p;c,d=q
        c3=f.pow(c,3);d3=f.pow(d,3)
        return (M[a][c3],M[b][c3],M[a][d3],M[b][d3])
    def power(p):
        a,b=p
        return (f.pow(a,4),M[f.pow(a,3)][b],M[a][f.pow(b,3)],f.pow(b,4))
    X,Y,Z,W=[(A[i],B[i]) for i in range(4)]
    x4=power(X); xy3=term(X,Y); z4=power(Z); zw3=term(Z,W)
    return all(f.sub(f.sub(x4[i],xy3[i]),f.sub(z4[i],zw3[i]))==0 for i in range(4))

def expected_lines(f):
    # Our independent RREF enumerator should find the q+1 ruling lines plus directrices.
    # A ruling is spanned by (v^3,u^3,0,0) and (0,0,u,v)
    # in the coordinates (X,Z,U,V)=(x,z,x-y,z-w).
    q=f.q;M=f.mul
    pairs=[(1,t) for t in range(q)]+[(0,1)]
    def canonical(A,B):
        # convert vectors to original x,y,z,w where y=x-u and w=z-v
        def orig(V):X,Z,U,Vv=V;return (X,f.sub(X,U),Z,f.sub(Z,Vv))
        return tuple(orig(v) for v in (A,B))
    ls=[]
    for u,v in pairs:
        ls.append(canonical((f.pow(v,3),f.pow(u,3),0,0),(0,0,u,v)))
    ls.extend([canonical((1,0,0,0),(0,1,0,0)),canonical((0,0,1,0),(0,0,0,1))])
    return ls

def rref2(f,A,B):
    R=[list(A),list(B)];m=f.mul
    row=0
    for col in range(4):
        piv=next((r for r in range(row,2) if R[r][col]),None)
        if piv is None:continue
        R[row],R[piv]=R[piv],R[row]
        inv=f.pow(R[row][col],f.q-2)
        R[row]=[m[inv][a] for a in R[row]]
        for r in range(2):
            if r!=row:
                c=R[r][col]
                R[r]=[f.sub(R[r][k],m[c][R[row][k]]) for k in range(4)]
        row+=1
        if row==2:break
    assert row==2
    return tuple(tuple(a) for a in R)

def test(mod,check_lines=False):
    f=Field(mod);q=f.q
    pts=[P for P in Ppoints(f) if f4(f,P)==0]
    assert len(pts)==(q+1)**2,(q,len(pts))
    # singular geometric support over the rational field is x=y, z=w:
    singular=[P for P in pts if P[0]==P[1] and P[2]==P[3]]
    assert len(singular)==q+1
    print(f'GF({q}): S={len(pts)}, singular line={len(singular)}, expected={(q+1)**2}')
    if check_lines:
        found={rref2(f,A,B) for A,B in line_rref(f) if line_inside(f,A,B)}
        expected={rref2(f,A,B) for A,B in expected_lines(f)}
        assert found==expected,(q,len(found),len(expected),found^expected)
        print(f'GF({q}): all {len(found)} rational lines = {q+1} rulings + 2 directrices')

if __name__=='__main__':
    for mod,check in [((0,1),True),((1,0,1),True),((2,2,0,1),False)]:test(mod,check)
    # Formal polynomial coefficients: (x-y)^3 = x^3-y^3 mod 3.
    assert comb(3,1)%3==0 and comb(3,2)%3==0
    # Conductor calculation on Z=1: R=k[t^3,u,tu] inside k[t,u].
    def in_R(t_exp,u_exp):return t_exp%3<=u_exp
    for t_exp in range(12):
        assert in_R(t_exp,2) and in_R(t_exp+1,2) and in_R(t_exp+2,2)
    assert not in_R(2,1) and not in_R(1,0)
    # Complete-intersection Hilbert polynomial for (U^3,V^3).
    def C(n):return comb(n+3,3) if n>=0 else 0
    for m in range(4,15):
        assert C(m)-2*C(m-3)+C(m-6)==9*m-9
    print('FORMAL_IDENTITY_CONDUCTOR_HILBERT_OK')
    print('CHECK_OK')
