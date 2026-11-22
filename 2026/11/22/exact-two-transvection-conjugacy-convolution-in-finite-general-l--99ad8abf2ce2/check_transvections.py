"""Exhaustive, field-independent check of two-transvection spectral strata.
Run: python check_transvections.py
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self,p,d=1):
        self.p,self.d=p,d; self.q=p**d
        self.polys={(2,2):[1,1,1],(3,2):[1,0,1]}
        assert d==1 or (p,d) in self.polys
        self.A=[[0]*self.q for _ in range(self.q)]
        self.M=[[0]*self.q for _ in range(self.q)]
        for a in range(self.q):
            for b in range(self.q):
                ac=self.digits(a);bc=self.digits(b)
                self.A[a][b]=sum(((ac[i]+bc[i])%p)*p**i for i in range(d))
                c=[0]*(2*d-1)
                for i in range(d):
                    for j in range(d):c[i+j]=(c[i+j]+ac[i]*bc[j])%p
                if d>1:
                    poly=self.polys[p,d]
                    for k in range(2*d-2,d-1,-1):
                        t=c[k]
                        for j in range(d):c[k-d+j]=(c[k-d+j]-t*poly[j])%p
                self.M[a][b]=sum(c[i]*p**i for i in range(d))
        self.inv=[None]*self.q
        for a in range(1,self.q):
            self.inv[a]=next(b for b in range(1,self.q) if self.M[a][b]==1)
    def digits(self,x):
        r=[]
        for _ in range(self.d):r.append(x%self.p);x//=self.p
        return r
    def dot(self,u,v):
        t=0
        for x,y in zip(u,v):t=self.A[t][self.M[x][y]]
        return t
    def rank(self,m):
        a=[list(row) for row in m]; rows=len(a); cols=len(a[0]); r=0
        for j in range(cols):
            piv=next((i for i in range(r,rows) if a[i][j]!=0),None)
            if piv is None:continue
            a[r],a[piv]=a[piv],a[r]
            c=self.inv[a[r][j]]; a[r]=[self.M[c][x] for x in a[r]]
            for i in range(rows):
                if i==r:continue
                v=a[i][j]
                if v:
                    neg=self.p-1
                    a[i]=[self.A[a[i][k]][self.M[neg][self.M[v][a[r][k]]]] for k in range(cols)]
            r+=1
        return r

def exhaustive(p,d,n):
    F=Field(p,d);q=F.q
    # Fix A=I+e_1 e_2^* by transvection conjugacy.
    # Count every (v,psi) with v,psi nonzero and psi(v)=0;
    # each transvection is represented exactly q-1 times.
    ns=range(q);vs=[u for u in product(ns,repeat=n) if any(u)]
    C=Counter();u=tuple([1]+[0]*(n-1)); phi=tuple([0,1]+[0]*(n-2))
    aa=F.A;mm=F.M
    for v in vs:
      for psi in vs:
        if F.dot(v,psi):continue
        a=v[1];b=psi[0];t=mm[a][b]
        # K=AB-I=u*phi + v*psi + u*(phi(v))*psi
        k=[[0]*n for i in range(n)]
        for i in range(n):
          for j in range(n):
            k[i][j]=aa[mm[u[i]][phi[j]]][mm[v[i]][psi[j]]]
            k[i][j]=aa[k[i][j]][mm[mm[u[i]][a]][psi[j]]]
        r=F.rank(k)
        if t:
            assert r==2, (p,d,n,t,r)
            cat=f'trace_nonzero_{t}'
        elif r==0:
            cat='identity'
        elif r==1:
            cat='J2'
        elif r==2:
            k2=[[F.dot(k[i],[k[h][j] for h in range(n)]) for j in range(n)] for i in range(n)]
            cat='J22' if all(vv==0 for row in k2 for vv in row) else 'J3'
        else:raise AssertionError(('bad rank',p,d,n,r))
        C[cat]+=1
    assert all(x%(q-1)==0 for x in C.values())
    C={k:v//(q-1) for k,v in C.items()}
    T=(q**n-1)*(q**(n-1)-1)//(q-1)
    pred={'identity':1,'J2':2*q**(n-1)-q-2,'J3':2*(q**(n-1)-q)*q**(n-2),
          'J22':0 if n<=3 else (q**(n-1)-q)*(q**(n-2)-q)//(q-1)}
    for t in range(1,q):pred[f'trace_nonzero_{t}']=q**(2*n-3)
    assert sum(C.values())==T,(p,d,n,C,T)
    assert all(C.get(k,0)==v for k,v in pred.items()),(p,d,n,C,pred)
    return q,n,T,C

if __name__=='__main__':
    cases=[(2,1,2),(2,1,3),(2,1,4),(2,1,5),(3,1,2),(3,1,3),(3,1,4),
        (5,1,2),(5,1,3),(7,1,2),(2,2,2),(2,2,3),(2,2,4),
        (3,2,2),(3,2,3)]
    for p,d,n in cases:
        q,n,T,C=exhaustive(p,d,n)
        print(f'PASS q={q} n={n} transvections={T} identity={C.get("identity",0)} J2={C.get("J2",0)} J3={C.get("J3",0)} J22={C.get("J22",0)} other={sum(x for k,x in C.items() if k.startswith("trace_"))}')
    print('ALL PASS',len(cases),'cases')
