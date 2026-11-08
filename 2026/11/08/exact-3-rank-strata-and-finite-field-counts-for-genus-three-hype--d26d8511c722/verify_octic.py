#!/usr/bin/env python3
"""Standalone finite-field checks for smooth even octics in characteristic three.
No external dependencies; all assertions are exact finite-field arithmetic.
"""
from itertools import product

class Field:
    def __init__(self, modulus):
        self.mod = [v % 3 for v in modulus]
        self.n = len(modulus)-1
        self.q = 3**self.n
        self.vals = list(range(self.q))
        self.vecs = [self._to_vec(i) for i in self.vals]
        self.add_table = [[self._from_vec([(x+y)%3 for x,y in zip(self.vecs[a],self.vecs[b])]) for b in self.vals] for a in self.vals]
        self.neg_table = [self._from_vec([(-x)%3 for x in self.vecs[a]]) for a in self.vals]
        self.mul_table = [[self._mul_slow(a,b) for b in self.vals] for a in self.vals]
        self.pow_table = [[self.pow(a,e) for e in (0,1,2,3,9,13)] for a in self.vals]
        self.inv_table = [0]+[self.pow(a,self.q-2) for a in self.vals[1:]]
        for a in self.vals[1:]:
            assert self.mul(a,self.inv(a)) == 1
    def _to_vec(self, a):
        return [(a//3**i)%3 for i in range(self.n)]
    def _from_vec(self, c):
        return sum(v*3**i for i,v in enumerate(c))
    def _mul_slow(self,a,b):
        u,v=self.vecs[a],self.vecs[b]
        w=[0]*(2*self.n-1)
        for i in range(self.n):
            for j in range(self.n):w[i+j]=(w[i+j]+u[i]*v[j])%3
        for k in range(len(w)-1,self.n-1,-1):
            z=w[k]
            for j in range(self.n): w[k-self.n+j]=(w[k-self.n+j]-z*self.mod[j])%3
        return self._from_vec(w[:self.n])
    def add(self,a,b): return self.add_table[a][b]
    def neg(self,a): return self.neg_table[a]
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):return self.mul_table[a][b]
    def inv(self,a):return self.inv_table[a]
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul(z,a) if hasattr(self,'mul_table') else self._mul_slow(z,a)
            a=self.mul(a,a) if hasattr(self,'mul_table') else self._mul_slow(a,a)
            n//=2
        return z

def trim(v):
    while v and v[-1]==0:v.pop()
    return v

def rem(f,g,K):
    f=trim(f[:]);g=trim(g[:]);inv=K.inv(g[-1])
    while len(f)>=len(g):
        z=K.mul(f[-1],inv);shift=len(f)-len(g)
        for j in range(len(g)):f[shift+j]=K.sub(f[shift+j],K.mul(z,g[j]))
        trim(f)
    return f

def smooth(a,b,c,K):
    f=[1,c,b,a,1]
    d=[c,K.neg(b),0,1]
    while d:
        f,d=d,rem(f,d,K)
    return len(f)==1

def rank(mat,K):
    M=[r[:] for r in mat]
    n=len(M);rk=0
    for col in range(n):
        piv=next((i for i in range(rk,n) if M[i][col]!=0),None)
        if piv is None:continue
        M[piv],M[rk]=M[rk],M[piv]
        fac=K.inv(M[rk][col]);M[rk]=[K.mul(fac,x) for x in M[rk]]
        for i in range(n):
            if i !=rk and M[i][col]:
                fac=M[i][col]
                M[i]=[K.sub(x,K.mul(fac,y)) for x,y in zip(M[i],M[rk])]
        rk+=1
    return rk

def matmul(X,Y,K):
    return [[sum_finite([K.mul(X[i][k],Y[k][j]) for k in range(3)],K) for j in range(3)] for i in range(3)]

def sum_finite(v,K):
    s=0
    for a in v:s=K.add(s,a)
    return s

def predicted(a,b,c,K):
    det=K.sub(K.mul(a,c),1)
    if det:return 2+int(b!=0)
    s=K.add(K.pow(c,3),a)
    return int(s!=0)+int(b!=0)

def main():
    for mod in ([0,1],[1,0,1],[1,2,0,1]):
        K=Field(mod); q=K.q
        counts=[0]*4; checked=0; r=sum(K.pow(a,4)==K.neg(1) for a in K.vals[1:])
        for a,b,c in product(K.vals,repeat=3):
            if not smooth(a,b,c,K): continue
            checked+=1
            H=[[c,0,1],[0,b,0],[1,0,a]]
            HH=matmul(matmul(H,[[K.pow(v,3) for v in row] for row in H],K),[[K.pow(v,9) for v in row] for row in H],K)
            p_rank=rank(HH,K)
            assert p_rank==predicted(a,b,c,K),('p-rank',q,a,b,c,p_rank,predicted(a,b,c,K))
            arank=3-rank(H,K)
            assert arank in (0,1),('a-number',q,a,b,c,arank)
            assert arank==int(p_rank!=3),('a-number versus ordinary',q,a,b,c,arank,p_rank)
            counts[p_rank]+=1
        expect=[0,r*(q-1),2*q*q-4*q+3-r*(q-2),q**3-3*q*q+5*q-5-r]
        assert counts==expect,(q,counts,expect)
        assert checked==q**3-q*q+q-2,(q,checked)
        print(f'GF({q}): smooth={checked}; roots={r}; rank counts={counts}; PASS')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
