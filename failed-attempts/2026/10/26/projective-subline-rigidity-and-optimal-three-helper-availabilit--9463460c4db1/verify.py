#!/usr/bin/env python3
"""Independent finite-field check of four-column dependencies and subline criteria.

Uses only integer polynomial arithmetic and exhaustive four-subset enumeration.
"""
from itertools import combinations
from math import comb

class GF:
    def __init__(self, p, poly):
        self.p = p
        self.f = poly
        self.m = len(poly)-1
        self.q = p**self.m
        assert poly[-1] == 1
        self.vec = [self.digits(a) for a in range(self.q)]
        self.add_table = [[self.encode([(a[i]+b[i])%p for i in range(self.m)]) for b in self.vec] for a in self.vec]
        self.neg_table = [self.encode([(-a[i])%p for i in range(self.m)]) for a in self.vec]
        self.mul_table = [[self.multiply_vec(a,b) for b in self.vec] for a in self.vec]
        self.inv_table = [0] + [next(j for j in range(1,self.q) if self.mul_table[i][j]==1) for i in range(1,self.q)]
    def digits(self, a):
        v=[]
        for _ in range(self.m):
            v.append(a%self.p); a//=self.p
        return v
    def encode(self,v):
        x=0
        for a in reversed(v): x=x*self.p+a
        return x
    def multiply_vec(self,a,b):
        t=[0]*(2*self.m-1)
        for i in range(self.m):
            for j in range(self.m):
                t[i+j]=(t[i+j]+a[i]*b[j])%self.p
        for d in range(2*self.m-2,self.m-1,-1):
            c=t[d]
            for j in range(self.m):
                t[d-self.m+j]=(t[d-self.m+j]-c*self.f[j])%self.p
        return self.encode(t[:self.m])
    def add(self,x,y):return self.add_table[x][y]
    def sub(self,x,y):return self.add_table[x][self.neg_table[y]]
    def mul(self,x,y):return self.mul_table[x][y]
    def div(self,x,y):return self.mul_table[x][self.inv_table[y]]
    def pow(self,x,n):
        t=1
        while n:
            if n&1:t=self.mul(t,x)
            x=self.mul(x,x); n>>=1
        return t
    def rank(self, rows):
        a=[list(row) for row in rows]
        r=0
        ncols=len(a[0]); nrows=len(a)
        for col in range(ncols):
            pivot=next((i for i in range(r,nrows) if a[i][col]),None)
            if pivot is None: continue
            a[r],a[pivot]=a[pivot],a[r]
            z=self.inv_table[a[r][col]]
            for k in range(col,ncols):a[r][k]=self.mul(a[r][k],z)
            for i in range(nrows):
                if i==r:continue
                z=a[i][col]
                if z:
                    for k in range(col,ncols):a[i][k]=self.sub(a[i][k],self.mul(z,a[r][k]))
            r+=1
            if r==nrows:break
        return r

def run(p,f,s):
    F=GF(p,f);q=F.q;R=p**s
    h=p**__import__('math').gcd(F.m,s)
    cols=[[1,x,F.pow(x,R),F.pow(x,R+1)] for x in range(q)]+[[0,0,0,1]]
    checked=0;dep=0;max_mismatch=0
    line_through_target={x:0 for x in range(q+1)}
    for Q in combinations(range(q+1),4):
        dep0=F.rank([[cols[x][j] for x in Q] for j in range(4)])<4
        target=Q[0]
        others=[]
        if target==q:
            others=list(Q[1:])
        else:
            for z in Q[1:]:
                if z==q: others.append(0)
                else: others.append(F.inv_table[F.sub(z,target)])
        a,b,c=others
        d1=F.sub(b,a);d2=F.sub(c,a)
        ratio=F.div(d1,d2)
        geom=(F.pow(ratio,R)==ratio)
        if dep0!=geom:raise AssertionError((p,F.m,s,Q,dep0,geom))
        checked+=1
        dep+=int(dep0)
        if dep0:
            for z in Q:line_through_target[z]+=1
    expected=comb(q+1,3)*(h-2)//4
    if dep!=expected:raise AssertionError(('support count',dep,expected))
    for i in range(q+1):
        if line_through_target[i]!=q*(q-1)*(h-2)//6:
            raise AssertionError(('coordinate support count',i,line_through_target[i]))
    directions=(q-1)//(h-1)
    per_direction=q//h
    repair_count=q*(q-1)*(h-2)//6
    print(f'OK p={p} m={F.m} s={s} q={q} h={h}: 4-subsets={checked}; dependent={dep}; repair_triples_per_coordinate={repair_count}; directional_parallel_classes={directions}; affine_lines_per_direction={per_direction}',flush=True)

for p,f,s in [(3,[1,0,1],1),(5,[2,0,1],1),(3,[2,2,0,1],1),(3,[2,2,0,1],2)]:
    run(p,f,s)
print('SUBLINE_REPAIR_CENSUS_OK')
