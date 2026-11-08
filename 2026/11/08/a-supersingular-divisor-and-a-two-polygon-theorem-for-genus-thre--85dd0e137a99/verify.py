#!/usr/bin/env python3
"""Exact checks for the Cartier strata of odd genus-three hyperelliptic models.

Requires Python 3 and SymPy. All finite-field arithmetic is implemented here.
"""
from itertools import product
from sympy import symbols, Matrix, factor, Poly

a,b,c = symbols('a b c')
H = Matrix([[0,c,0],[a,0,b],[0,1,0]])

def fr(M,e):
    return M.applyfunc(lambda z: z**e)

H2 = fr(H,3)*H
H3 = fr(H,9)*H2
t = a**3*c + b**3
assert H2 == Matrix([[a*c**3,0,b*c**3],[0,t,0],[a,0,b]])
assert all(Poly(z,a,b,c,modulus=3).is_zero for z in (H3 - Matrix([[0,c**9*t,0],[a*t**3,0,b*t**3],[0,t,0]])))
assert factor((b**3-a*a*b*b+a**3*c).subs(c,-(b/a)**3)) == -a*a*b*b
print('SYMBOLIC_IDENTITIES_OK; rank-jump polynomial = a^3*c+b^3')

class Field:
    def __init__(self, modulus):
        self.mod=tuple(x%3 for x in modulus)
        self.deg=len(modulus)-1
        assert self.mod[-1]==1
        self.q=3**self.deg
        self.one=1
        self.zero=0
    def coeff(self,n):
        return [(n//(3**i))%3 for i in range(self.deg)]
    def encode(self,ls):
        return sum(int(ls[i])%3*3**i for i in range(self.deg))
    def const(self,n):
        return n%3
    def add(self,x,y):
        return self.encode([(s+t)%3 for s,t in zip(self.coeff(x),self.coeff(y))])
    def neg(self,x):
        return self.encode([(-s)%3 for s in self.coeff(x)])
    def sub(self,x,y):
        return self.add(x,self.neg(y))
    def mul(self,x,y):
        u=self.coeff(x);v=self.coeff(y);n=self.deg
        t=[0]*(2*n-1)
        for i in range(n):
            for j in range(n): t[i+j]=(t[i+j]+u[i]*v[j])%3
        for k in range(2*n-2,n-1,-1):
            if t[k]:
                for j in range(n):
                    t[k-n+j]=(t[k-n+j]-t[k]*self.mod[j])%3
        return self.encode(t[:n])
    def pow(self,x,e):
        r=1
        while e:
            if e&1:r=self.mul(r,x)
            x=self.mul(x,x);e//=2
        return r
    def div(self,x,y):
        assert y
        return self.mul(x,self.pow(y,self.q-2))
    def frob(self,x,e):
        return self.pow(x,3**e)
    def matmul(self,A,B):
        return [[self.sum(self.mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    def sum(self,vals):
        r=0
        for x in vals:r=self.add(r,x)
        return r
    def rank(self,A):
        M=[r[:] for r in A];h=len(M);w=len(M[0]);pivot=0
        for j in range(w):
            k=next((k for k in range(pivot,h) if M[k][j]),None)
            if k is None: continue
            M[pivot],M[k]=M[k],M[pivot]
            z=M[pivot][j]
            M[pivot]=[self.div(x,z) for x in M[pivot]]
            for i in range(h):
                if i!=pivot and M[i][j]:
                    q=M[i][j]
                    M[i]=[self.sub(x,self.mul(q,y)) for x,y in zip(M[i],M[pivot])]
            pivot+=1
            if pivot==h:break
        return pivot

def check(F,a,b,c):
    m=F.mul
    # Cubic h(u)=u^3+a*u^2+b*u+c: squarefreeness iff c!=0 and h has simple roots.
    delta=F.add(F.sub(F.pow(b,3),m(m(a,a),m(b,b))),m(F.pow(a,3),c))
    smooth=bool(c and delta)
    # Validate smoothness independently using polynomial gcd Euclid.
    # Compute f=x^7+a*x^5+b*x^3+c*x and its formal derivative in characteristic three.
    f=[0,c,0,b,0,a,0,1]
    df=[c,0,0,0,m(2,a),0,1]
    def trim(v):
        while v and not v[-1]:v.pop()
        return v
    def rem(u,v):
        u=trim(u[:]);v=trim(v[:]);assert v
        while len(u)>=len(v):
            mult=F.div(u[-1],v[-1]);idx=len(u)-len(v)
            for j in range(len(v)):
                u[j+idx]=F.sub(u[j+idx],m(mult,v[j]))
            trim(u)
        return u
    def gcd(u,v):
        while v:
            u,v=v,rem(u,v)
        return u
    assert (len(gcd(f,df))==1)==smooth
    if not smooth: return False
    # Hasse-Witt Frobenius is the transpose of the coefficient matrix H=(c_{3i-j}).
    H=[[0,c,0],[a,0,b],[0,1,0]]
    T=[list(row) for row in zip(*H)]
    I=[[1 if i==j else 0 for j in range(3)] for i in range(3)]
    ranks=[];R=I
    for power in range(1,5):
        Tk=[[F.frob(v,power-1) for v in row] for row in T]
        R=F.matmul(R,Tk)
        ranks.append(F.rank(R))
    z=F.add(F.pow(b,3),m(F.pow(a,3),c))==0
    assert ranks==([2,1,0,0] if z else [2,2,2,2]), (F.q,a,b,c,ranks,z)
    return True

for label,mod in [('F3',[0,1]),('F9',[1,0,1]),('F27',[2,2,0,1])]:
    F=Field(mod); smooth_count=0;jump_count=0
    if F.q<=9:
        values=product(range(F.q),repeat=3)
    else:
        # Include the entire explicit one-parameter special fiber and a finite sample.
        samples=[(1,B,F.neg(F.pow(B,3))) for B in range(1,F.q)]
        samples += list(product(range(4),range(5),range(6)))
        values=samples
    for av,bv,cv in values:
        if check(F,av,bv,cv):
            smooth_count+=1
            if F.add(F.pow(bv,3),F.mul(F.pow(av,3),cv))==0:jump_count+=1
    assert smooth_count and jump_count
    print(f'{label}_OK smooth_tested={smooth_count} jump={jump_count}')
print('ALL_CHECKS_PASSED')
