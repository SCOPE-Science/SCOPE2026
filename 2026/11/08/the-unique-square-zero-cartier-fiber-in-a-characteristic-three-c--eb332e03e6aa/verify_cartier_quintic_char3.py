#!/usr/bin/env python3
"""Exact characteristic-three Cartier calculations for cyclic quintic curves.

Uses only Python's standard library. The generic assertion is certified via
symbolic polynomial identities, not inferred from finite-field samples.
"""
from itertools import product

P = 3

def pmul(a, b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%P
    return z

def rank(M, ops):
    rows=[list(row) for row in M]
    lead=0
    for c in range(len(rows[0])):
        found=next((r for r in range(lead,len(rows)) if rows[r][c]!=0),None)
        if found is None: continue
        rows[lead],rows[found]=rows[found],rows[lead]
        inv=ops.pow(rows[lead][c],ops.order-2)
        rows[lead]=[ops.mul(x,inv) for x in rows[lead]]
        for r in range(len(rows)):
            if r!=lead and rows[r][c]:
                f=rows[r][c]
                rows[r]=[ops.sub(x,ops.mul(f,y)) for x,y in zip(rows[r],rows[lead])]
        lead+=1
        if lead==len(rows): break
    return lead

class Field:
    def __init__(self, modulus):
        self.mod=modulus;self.n=len(modulus)-1;self.order=3**self.n
    def add(self,a,b):
        aa=self.digs(a);bb=self.digs(b)
        return self.encode([(x+y)%3 for x,y in zip(aa,bb)])
    def sub(self,a,b):
        aa=self.digs(a);bb=self.digs(b)
        return self.encode([(x-y)%3 for x,y in zip(aa,bb)])
    def digs(self,a):
        t=[]
        for _ in range(self.n): t.append(a%3);a//=3
        return t
    def encode(self,a):
        return sum((x%3)*3**i for i,x in enumerate(a))
    def mul(self,a,b):
        q=pmul(self.digs(a),self.digs(b))
        for d in range(len(q)-1,self.n-1,-1):
            c=q[d]
            if c:
                for j in range(self.n):q[d-self.n+j]=(q[d-self.n+j]-c*self.mod[j])%3
        return self.encode(q[:self.n])
    def pow(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def root3(self,a):
        return self.pow(a,3**(self.n-1))

def mat_mul(A,B,F):
    return [[sum_in_field((F.mul(A[i][k],B[k][j]) for k in range(len(B))),F) for j in range(len(B[0]))] for i in range(len(A))]

def sum_in_field(it,F):
    z=0
    for x in it: z=F.add(z,x)
    return z

def twisted_compose(C,D,F):
    # C semilinear (inverse Frobenius): C o D has matrix C * (D^{1/3}).
    return mat_mul(C,[[F.root3(x) for x in row] for row in D],F)

def cartier_matrix(lam,F):
    u=F.add(1,lam)
    f=[0,lam,F.sub(0,u),1]
    f2=pmul(f,f) if F.n==1 else None
    # For arbitrary extension field, direct coefficient convolution in F.
    f2=[0]*7
    for i in range(4):
        for j in range(4):f2[i+j]=F.add(f2[i+j],F.mul(f[i],f[j]))
    xf=[0]+f
    # basis e1=dx/y^2, e2=dx/y^3, e3=dx/y^4,e4=x dx/y^4
    C=[[0]*4 for _ in range(4)]
    C[2][0]=F.root3(f2[2]);C[3][0]=F.root3(f2[5])
    C[1][2]=F.root3(f[2]);C[1][3]=F.root3(xf[2])
    return C

def generic_polynomial_check():
    # In F_3[t]: f=x^3-(1+t)x^2+t*x. Coefficient polynomials
    # f^2 at x^2=t^2, at x^5=(1+t); x f at x^2=t.
    t=[0,1];u=[1,1]
    assert pmul(t,t)==[0,0,1]
    assert pmul([2],u)==[2,2]
    # Ninth power of C^2 e1 is -(t^2)(1+t)^3 + (1+t)*t^3.
    u3=pmul(pmul(u,u),u)
    t2=pmul(t,t);t3=pmul(t2,t)
    alpha=pmul([2],pmul(t2,u3));beta=pmul(u,t3)
    alpha += [0]*(max(len(alpha),len(beta))-len(alpha))
    beta += [0]*(max(len(alpha),len(beta))-len(beta))
    discriminant=[(a+b)%3 for a,b in zip(alpha,beta)]
    # -(t^2)(1+t)(t-1)^2
    boundary=pmul([2],pmul(t2,pmul(u,pmul([2,1],[2,1]))))
    assert discriminant==boundary,(discriminant,boundary)
    # Factorization forces C²=0 exactly t=0,-1,1,
    # but smooth parameter excludes t=0,1.
    return discriminant

def main():
    poly=generic_polynomial_check()
    assert poly==[0,0,2,1,1,2],poly
    totals=[]
    for modulus in ([0,1],[1,0,1],[2,2,0,1]):
        F=Field(modulus)
        if F.n>1:
            # Verify polynomial is irreducible by checking field inverses.
            assert all(F.mul(a,F.pow(a,F.order-2))==1 for a in range(1,F.order))
        assert all(F.pow(F.root3(a),3)==a for a in range(F.order))
        found=0
        for lam in range(F.order):
            if lam in (0,1):continue
            C=cartier_matrix(lam,F)
            C2=twisted_compose(C,C,F)
            C3=twisted_compose(C,C2,F)
            r=[rank(Q,F) for Q in (C,C2,C3)]
            assert r==([2,0,0] if lam==2 else [2,1,0]),(F.order,lam,r)
            # independent computation: C^2(e1) written from coefficients
            u=F.add(1,lam)
            c2=F.add(F.mul(F.root3(F.root3(F.pow(lam,2))),F.root3(F.sub(0,u))),
                     F.mul(F.root3(F.root3(u)),F.root3(lam)))
            assert C2[1][0]==c2,(F.order,lam,C2[1][0],c2)
            assert F.pow(c2,9)==F.mul(F.sub(0,F.pow(lam,2)),F.mul(u,F.pow(F.sub(lam,1),2)))
            found+=1
        totals.append((F.order,found))
    print('CYCLIC_QUINTIC_CHAR3_CARTIER_PASS', 'symbolic_C2_ninth=',poly, 'tested=',totals)
if __name__=='__main__':main()
