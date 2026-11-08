#!/usr/bin/env python3
"""Exact finite-field checks for p-power image ranks of Picard groups of line pencils.
All computations use integer arithmetic in explicitly specified finite fields.
This is a finite verification of the interpolation lemmas, not an infinite-family proof.
"""
from itertools import product

class Field:
    def __init__(self,p,poly):
        self.p=p; self.mod=poly; self.d=len(poly)-1; self.q=p**self.d
        assert poly[-1] == 1
    def coeff(self,a):
        c=[]
        for _ in range(self.d): c.append(a%self.p); a//=self.p
        return c
    def encode(self,c):
        return sum((v%self.p)*self.p**i for i,v in enumerate(c))
    def add(self,a,b):
        return self.encode([(x+y)%self.p for x,y in zip(self.coeff(a),self.coeff(b))])
    def mul(self,a,b):
        A=self.coeff(a);B=self.coeff(b)
        tmp=[0]*(2*self.d-1)
        for i,x in enumerate(A):
            for j,y in enumerate(B):tmp[i+j]=(tmp[i+j]+x*y)%self.p
        for k in range(2*self.d-2,self.d-1,-1):
            lead=tmp[k]
            for j in range(self.d): tmp[k-self.d+j]=(tmp[k-self.d+j]-lead*self.mod[j])%self.p
        return self.encode(tmp[:self.d])
    def power(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            a=self.mul(a,a);n//=2
        return z
    def inverse(self,a):
        assert a!=0
        return self.power(a,self.q-2)
    def rank(self,A):
        A=[row[:] for row in A]; row=0;ncol=len(A[0]);nr=len(A)
        for col in range(ncol):
            pivot=next((i for i in range(row,nr) if A[i][col]!=0),None)
            if pivot is None:continue
            A[row],A[pivot]=A[pivot],A[row]
            inv=self.inverse(A[row][col]);A[row]=[self.mul(inv,z) for z in A[row]]
            for i in range(nr):
                if i==row:continue
                u=A[i][col]
                if not u:continue
                A[i]=[self.add(z,self.mul(self.p-1,self.mul(u,w))) for z,w in zip(A[i],A[row])]
            row+=1
            if row==nr:break
        return row

def vandermonde(F,m,j):
    return [[F.power(i,k) for k in range(j+1)] for i in range(m)]

def image_rank(F,m,r):
    s=F.p**r;L=(m-2)//s
    return sum(m-F.rank(vandermonde(F,m,s*j)) for j in range(1,L+1))

def expected_rank(m,p,r):
    s=p**r;L=(m-2)//s
    return L*(m-1)-s*L*(L+1)//2

def check_field(p,poly,maxm):
    F=Field(p,poly)
    for m in range(3,maxm+1):
        for j in range(m-1):
            assert F.rank(vandermonde(F,m,j))==j+1,(p,m,j)
        ranks=[]
        for r in range(5):
            actual=image_rank(F,m,r)
            expect=expected_rank(m,p,r)
            assert actual==expect,(p,m,r,actual,expect)
            ranks.append(actual)
        assert ranks[0]==(m-1)*(m-2)//2
        assert ranks[-1]==0
        if p**1 >= m-1: assert ranks[1]==0
        if p <= m-2: assert ranks[1]>0
        if m in (4,5,8,maxm):print('FIELD',F.q,'p',p,'m',m,'rho',ranks[:4])
    print('FIELD_CHECK_PASSED',F.q,'m3_to',maxm)

# All chosen modulus polynomials are irreducible over the specified prime fields.
check_field(2,[1,1,0,0,1],10) # F16, x^4+x+1
check_field(3,[1,0,1],9)     # F9, x^2+1
check_field(5,[2,0,1],10)    # F25, x^2+2
check_field(7,[0,1],7)      # F7
# The first non-vector group: four concurrent lines in characteristic 2.
F=Field(2,[1,1,1]);slopes=[0,1,2,3];m=4
V2=vandermonde(F,m,2)
assert F.rank(V2)==3
# Local class u=(1+t,1,1,1), so [2]u=(1+t^2,1,1,1).
e1=[1,0,0,0]
assert F.rank([row+[v] for row,v in zip(V2,e1)])==4
assert expected_rank(4,2,1)==1 and expected_rank(4,2,2)==0
# Directly enumerate the ring-unit subgroup and the square-image intersection.
V1=vandermonde(F,m,1)
A=set()
for coeff in product(range(F.q),repeat=5):
    a=[];b=[]
    for i in range(m):
        ai=F.add(F.mul(coeff[0],V1[i][0]),F.mul(coeff[1],V1[i][1]))
        bi=0
        for j in range(3):bi=F.add(bi,F.mul(coeff[2+j],V2[i][j]))
        a.append(ai);b.append(bi)
    A.add(tuple(a+b))
assert len(A)==F.q**5
square_image={tuple([0]*m+list(v)) for v in product(range(F.q),repeat=m)}
assert len(square_image)==F.q**m
assert len(A&square_image)==F.q**3
assert len(square_image)//len(A&square_image)==F.q
print('FOUR_LINES_CHAR2_EXACT_SQUARE_IMAGE_QUOTIENT',len(square_image)//len(A&square_image))
print('FOUR_LINES_CHAR2_ORDER4_WITNESS_PASSED')
print('ALL_CHECKS_PASSED')
