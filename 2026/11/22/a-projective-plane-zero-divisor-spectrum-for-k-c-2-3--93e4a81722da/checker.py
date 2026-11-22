#!/usr/bin/env python3
"""Independent finite-field multiplication and projective-incidence checks.

Usage: python3 checker.py
No third-party packages needed for essential tests.
"""
from collections import Counter
import random
import math

MONOMS = (1,2,4,3,5,6,7)   # x,y,z,xy,xz,yz,xyz; support bitmasks

class Field:
    def __init__(self,degree,poly):
        self.e=degree; self.q=1<<degree; self.poly=poly
    def mul(self,a,b):
        r=0
        for _ in range(self.e):
            if b&1:r^=a
            b>>=1
            a<<=1
            if a&self.q:a^=self.poly
        return r
    def power(self,a,k):
        r=1
        while k:
            if k&1:r=self.mul(r,a)
            a=self.mul(a,a);k>>=1
        return r
    def div(self,a,b):
        assert b
        return self.mul(a,self.power(b,self.q-2))
    def dot(self,v,w):
        return self.mul(v[0],w[2]) ^ self.mul(v[1],w[1]) ^ self.mul(v[2],w[0])
    def normalized(self,v):
        j=next(i for i,x in enumerate(v) if x)
        a=v[j]
        return tuple(self.div(x,a) for x in v),a
    def mul_ring(self,a,b):
        r=[0]*7
        for i,mask in enumerate(MONOMS):
            if not a[i]:continue
            for j,mask2 in enumerate(MONOMS):
                if b[j] and not mask&mask2:
                    k=MONOMS.index(mask|mask2)
                    r[k]^=self.mul(a[i],b[j])
        return tuple(r)
    def index_tuple(self,num):
        r=[]
        for _ in range(7):r.append(num%self.q);num//=self.q
        return tuple(r)
    def classify(self,a):
        v=a[:3];w=a[3:6]
        if not any(v):
            if not any(w):return ('U',)
            line,_=self.normalized(w)
            return ('L',line)
        point,alpha=self.normalized(v)
        # s = <point,w>/alpha (characteristic 2)
        return ('P',point,self.div(self.dot(point,w),alpha))
    def linked(self,ca,cb):
        if ca[0]=='U' or cb[0]=='U':return True
        if ca[0]=='L' and cb[0]=='L':return True
        if ca[0]=='P' and cb[0]=='P':return ca==cb
        if ca[0]=='P':p=ca[1];line=cb[1]
        else:p=cb[1];line=ca[1]
        return self.dot(p,line)==0

def determinant3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
          - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
          + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def quotient(q):
    a=q-1;b=q*(q-1);c=q**3*(q-1);m=q*q+q+1
    return [[a-1,m*b,m*q*c], [a,m*b-1,(q+1)*q*c], [a,(q+1)*b,c-1]]

def run():
    rng=random.Random(20261115)
    for e,poly in ((1,0b11),(2,0b111),(3,0b1011)):
        f=Field(e,poly);q=f.q
        # Explicit check that chosen modulus gives field inverses
        for x in range(1,q):assert f.mul(x,f.div(1,x))==1
        m=q*q+q+1;b=q*(q-1);c=q**3*(q-1)
        points=sorted({f.normalized((x,y,z))[0]
                       for x in range(q) for y in range(q) for z in range(q)
                       if x or y or z})
        lines=points  # dual coordinates use the same canonical list
        assert len(points)==len(lines)==m
        incidence=[[int(f.dot(p,l)==0) for p in points] for l in lines]
        assert all(sum(row)==q+1 for row in incidence)
        assert all(sum(incidence[i][j]*incidence[k][j] for j in range(m)) == (q+1 if i==k else 1)
                   for i in range(m) for k in range(m))
        print('q=%s projective incidence identity NN^T=qI+J checked (%s lines)' % (q,m))
        if q<=4:
            count=Counter(f.classify(f.index_tuple(i)) for i in range(1,q**7))
            assert sum(count.values())==q**7-1
            assert sum(1 for a in count if a[0]=='P')==m*q
            assert sum(1 for a in count if a[0]=='L')==m
            assert count[('U',)]==q-1
            assert all(n==c for k,n in count.items() if k[0]=='P')
            assert all(n==b for k,n in count.items() if k[0]=='L')
            print('q=%s class sizes: %s point-parameter cliques of size %s; %s line blocks of size %s; %s universal vertices' % (q,m*q,c,m,b,q-1))
        if q==2:
            total=0
            for i in range(1,q**7):
                a=f.index_tuple(i);ca=f.classify(a)
                for j in range(i+1,q**7):
                    bvec=f.index_tuple(j);cb=f.classify(bvec)
                    assert (not any(f.mul_ring(a,bvec)))==f.linked(ca,cb),(i,j)
                    total+=1
            print('q=2 exhaustive unordered distinct pairs checked:',total)
        else:
            samples=25000 if q==4 else 10000
            for _ in range(samples):
                i=rng.randrange(1,q**7);j=rng.randrange(1,q**7)
                if i==j:continue
                a=f.index_tuple(i);bvec=f.index_tuple(j)
                assert (not any(f.mul_ring(a,bvec)))==f.linked(f.classify(a),f.classify(bvec)),(q,i,j)
            print('q=%s randomized independent pair products checked: %s' % (q,samples))
        T=quotient(q)
        D=determinant3(T)
        formula= -q**9*((q-1)**3-1)-2*(q**7-2*q**4+q**3+1)
        assert D==formula and D<0
        print('q=%s quotient 3x3 determinant: %s' % (q,D))
    try:
        import numpy as np
        f=Field(1,0b11);q=2;m=7;b=2;c=8;a=1
        R=[f.index_tuple(i) for i in range(1,128)]
        adj=np.array([[int(i!=j and not any(f.mul_ring(u,v)))
                       for j,v in enumerate(R)] for i,u in enumerate(R)],dtype=float)
        empirical=np.linalg.eigvalsh(adj)
        E=(a-1)+m*(b-1)+m*q*(c-1)
        disc=(2-c)**2 - 4*(1-c-b*q*q*c)
        qr=[(c-2-math.sqrt(disc))/2,(c-2+math.sqrt(disc))/2]
        predicted=[-1]*E+[c-1]*(m*(q-1))+[qr[0]]*(m-1)+[qr[1]]*(m-1)
        predicted+=list(np.linalg.eigvals(np.array(quotient(q),dtype=float)).real)
        assert len(predicted)==len(empirical)==127
        assert max(abs(x-y) for x,y in zip(sorted(predicted),empirical))<1e-8
        print('q=2 direct adjacency numerical spectrum: 127 eigenvalues agree with factorization')
    except ImportError:
        print('Optional numerical spectrum comparison not run: numpy not installed')
    print('ALL CHECKS PASSED')

if __name__=='__main__':run()
