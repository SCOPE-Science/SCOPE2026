#!/usr/bin/env python3
"""Stand-alone finite-field checks for a class-four two-generator Lie algebra.
Run: python3 verify_lie.py. No external packages required.
"""
from itertools import product

N=8
EDGES=[(0,1,2),(2,0,3),(2,1,4),(3,0,5),(3,1,6),(4,0,6),(4,1,7)]

class Field:
    def __init__(self,q):
        self.q=q
        assert q in (2,3,4)
    def add(self,a,b): return a^b if self.q==4 else (a+b)%self.q
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        p=0
        while b:
            if b&1:p^=a
            a<<=1
            if a&4:a^=7
            b>>=1
        return p
    def neg(self,a):return a if self.q in (2,4) else (-a)%3
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def sub(self,a,b):return self.add(a,self.neg(b))

def addv(f,a,b):return tuple(f.add(x,y) for x,y in zip(a,b))
def scal(f,c,a):return tuple(f.mul(c,x) for x in a)
def zero():return (0,)*N
def unit(i):return tuple(int(j==i) for j in range(N))

def bracket(f,a,b):
    z=[0]*N
    for i,j,k in EDGES:
        v=f.sub(f.mul(a[i],b[j]),f.mul(a[j],b[i]))
        z[k]=f.add(z[k],v)
    return tuple(z)

def row_basis(f,rows):
    piv={}
    for row in rows:
        r=list(row)
        for j in sorted(piv):
            if r[j]:
                x=r[j]
                r=[f.sub(y,f.mul(x,z)) for y,z in zip(r,piv[j])]
        if not any(r):continue
        j=next(j for j,x in enumerate(r) if x)
        s=f.inv(r[j]);r=[f.mul(s,x) for x in r]
        piv[j]=r
    return piv

def isin(f,row,piv):
    r=list(row)
    for j in sorted(piv):
        if r[j]:
            x=r[j]
            r=[f.sub(y,f.mul(x,z)) for y,z in zip(r,piv[j])]
    return not any(r)

def cder(f,p,q,r,s):
    # central derivation determined by x->p*a+q*b, y->r*b+s*c
    u=[0]*N;v=[0]*N
    u[5:7]=[p,q];v[6:8]=[r,s]
    return tuple(u),tuple(v)

def image(f,dx,dy,z):
    return addv(f,scal(f,z[0],dx),scal(f,z[1],dy))

def verifier():
    for sz in (2,3,4):
        f=Field(sz);zeros=zero();basis=[unit(i) for i in range(N)]
        # Jacobi and alternation, including small characteristic.
        assert all(bracket(f,e,e)==zeros for e in basis)
        for a,b,c in product(basis,repeat=3):
            x=addv(f,bracket(f,a,bracket(f,b,c)),bracket(f,b,bracket(f,c,a)))
            assert addv(f,x,bracket(f,c,bracket(f,a,b)))==zeros
        # For central maps, checking all generator tuples suffices for derivation.
        for v in product(range(sz),repeat=4):
            dx,dy=cder(f,*v)
            for a,b in product(basis,repeat=2):
                assert image(f,dx,dy,bracket(f,a,b))==addv(f,bracket(f,image(f,dx,dy,a),b),bracket(f,a,image(f,dx,dy,b)))
        aid=[];inners=[]
        for pars in product(range(sz),repeat=4):
            dx,dy=cder(f,*pars)
            # this range test computes span of [L,alpha*x+beta*y] directly,
            # without using the determinant or theoretical normal forms.
            good=True
            for aa,bb in product(range(sz),repeat=2):
                element=addv(f,scal(f,aa,basis[0]),scal(f,bb,basis[1]))
                commutator=row_basis(f,[bracket(f,e,element) for e in basis])
                if not isin(f,image(f,dx,dy,element),commutator):
                    good=False;break
            if good:aid.append(pars)
            if pars[0]==pars[2] and pars[1]==pars[3]: inners.append(pars)
        predicted=sz**3 if sz==2 else sz**2
        assert len(aid)==predicted,(sz,len(aid),predicted)
        assert len(inners)==sz**2
        print('central q=',sz,' AID=',len(aid),' inner=',len(inners))
        if sz==2:
            special=(1,0,0,1)
            assert special in aid and special not in inners
            # Full vector test, 2^8 inputs, not just coset representatives.
            dx,dy=cder(f,*special)
            for t in product(range(2),repeat=N):
                commutator=row_basis(f,[bracket(f,e,t) for e in basis])
                assert isin(f,image(f,dx,dy,t),commutator)
            # All central derivations, all 256 possible inputs.
            for pars in product(range(2),repeat=4):
                dx,dy=cder(f,*pars)
                is_all=all(isin(f,image(f,dx,dy,t),row_basis(f,[bracket(f,e,t) for e in basis])) for t in product(range(2),repeat=N))
                assert is_all==(pars in aid)
            # Adjoint maps have 2^5 distinct values (center span a,b,c).
            inn_maps=set()
            for vec in product(range(2),repeat=N):
                inn_maps.add(tuple(bracket(f,vec,e) for e in basis))
            assert len(inn_maps)==32
            print('full F2 vector tests passed, inner maps=32; AID total 64 follows from quotient reduction')
    print('VERIFY_OK')

if __name__=='__main__':verifier()
