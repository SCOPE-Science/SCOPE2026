"""Finite checks for an automorphism-group theorem on chain evolution algebras.
No third-party dependencies. Execute with Python 3.10+.
"""
from itertools import product
from math import gcd
from fractions import Fraction

class Field:
    def __init__(self, p, poly=None):
        self.p=p; self.poly=poly or [0,1]; self.f=len(self.poly)-1
        self.q=p**self.f
        self.X=list(range(self.q))
        self.ADD=[[self.add(a,b) for b in self.X] for a in self.X]
        self.MUL=[[self.mul(a,b) for b in self.X] for a in self.X]
    def digits(self,a):
        r=[]
        for _ in range(self.f):r.append(a%self.p);a//=self.p
        return r
    def pack(self,ds):return sum((c%self.p)*self.p**i for i,c in enumerate(ds))
    def add(self,a,b):return self.pack([(u+v)%self.p for u,v in zip(self.digits(a),self.digits(b))])
    def mul(self,a,b):
        A=self.digits(a);B=self.digits(b);C=[0]*(2*self.f-1)
        for i,u in enumerate(A):
            for j,v in enumerate(B):C[i+j]=(C[i+j]+u*v)%self.p
        for k in range(len(C)-1,self.f-1,-1):
            t=C[k]
            for j in range(self.f):C[k-self.f+j]=(C[k-self.f+j]-t*self.poly[j])%self.p
        return self.pack(C[:self.f])
    def pow(self,a,r):
        z=1
        for _ in range(r):z=self.MUL[z][a]
        return z

F2=Field(2);F3=Field(3);F4=Field(2,[1,1,1]);F8=Field(2,[1,1,0,1]);F16=Field(2,[1,1,0,0,1]);F27=Field(3,[1,2,0,1])

def normal_maps(field,n):
    for a in range(1,field.q):
        for b in range(field.q):
            cols=[]
            for j in range(n):
                col=[0]*n;col[j]=field.pow(a,2**j)
                if j==0:col[-1]=field.ADD[col[-1]][b] if n>1 else col[-1]
                cols.append(tuple(col))
            yield tuple(cols)

def product_in_algebra(F,x,y):
    z=[0]*len(x)
    for i in range(len(x)-1): z[i+1]=F.ADD[z[i+1]][F.MUL[x[i]][y[i]]]
    return tuple(z)

def hom(F,cols):
    n=len(cols)
    for i in range(n):
        if i<n-1:
            if product_in_algebra(F,cols[i],cols[i])!=cols[i+1]: return False
        elif any(product_in_algebra(F,cols[i],cols[i])):return False
        for j in range(i+1,n):
            if any(product_in_algebra(F,cols[i],cols[j])):return False
    return True

def invertible(F,cols):
    n=len(cols)
    A=[[cols[j][i] for j in range(n)] for i in range(n)]
    for col in range(n):
        k=next((r for r in range(col,n) if A[r][col]),None)
        if k is None:return False
        A[col],A[k]=A[k],A[col]
        piv=A[col][col]
        inv=next(t for t in range(1,F.q) if F.MUL[t][piv]==1)
        A[col]=[F.MUL[inv][v] for v in A[col]]
        for row in range(col+1,n):
            fac=A[row][col]
            A[row]=[F.ADD[u][(-F.MUL[fac][v])%F.p] if F.f==1 else F.ADD[u][F.pack([(-x)%F.p for x in F.digits(F.MUL[fac][v])])] for u,v in zip(A[row],A[col])]
    return True

def exhaustive_automorphisms(F,n):
    canonical=set(normal_maps(F,n)); hits=set()
    for entries in product(range(F.q),repeat=n*n):
        cols=tuple(tuple(entries[i*n:i*n+n]) for i in range(n))
        if not hom(F,cols):continue
        if invertible(F,cols):hits.add(cols)
    assert hits==canonical,(n,F.q,len(hits),len(canonical),next(iter(hits^canonical),None))
    print('FULL_AUTOMORPHISM_ENUM_OK',n,F.q,len(hits))

def group(F,n):
    m=F.q-1;L=2**(n-1)-1
    ch={a:F.pow(a,L) for a in range(1,F.q)}
    G=tuple((x,a) for a in range(1,F.q) for x in range(F.q))
    def mul(g,h):
        x,a=g;y,b=h
        return (F.ADD[x][F.MUL[ch[a]][y]],F.MUL[a][b])
    return G,m,ch,mul

def generated(mul,els,identity):
    seen={identity};boundary=[identity]
    while boundary:
        g=boundary.pop()
        for a in els:
            h=mul(g,a)
            if h not in seen:seen.add(h);boundary.append(h)
    return len(seen)

def count_conjugacy(F,n):
    G,m,ch,mul=group(F,n); d=gcd(2**(n-1)-1,m)
    pairs=0
    for g in G:
        for h in G:
            pairs+=(mul(g,h)==mul(h,g))
    assert pairs==len(G)*(m+d*d),(n,F.q,pairs,len(G)*(m+d*d))
    print('COMMUTING_PAIRS_OK',n,F.q,pairs,m+d*d)

def generating_pairs(F,n):
    G,m,ch,mul=group(F,n)
    num=sum(generated(mul,[g,h],(0,1))==len(G) for g in G for h in G)
    d=gcd(2**(n-1)-1,m);h=m//d
    prime_divs=[];v=m;ell=2
    while ell*ell<=v:
        if v%ell==0:
            prime_divs.append(ell)
            while v%ell==0:v//=ell
        ell+=1
    if v>1:prime_divs.append(v)
    cyc=Fraction(1)
    for ell in prime_divs:cyc*=1-Fraction(1,ell**2)
    if h==1:
        pr=cyc
        for i in range(F.f): pr*=1-Fraction(F.p**i,F.p**2)
    else:
        e=next(k for k in range(1,F.f+1) if pow(F.p,k,h)==1)
        r=F.f//e;pr=cyc
        for i in range(r):pr*=1-Fraction(F.p**(e*i),F.p**(e*(2-1)))
    assert Fraction(num,len(G)**2)==pr,(n,F.q,num,len(G)**2,pr)
    print('GENERATING_PAIRS_OK',n,F.q,num,len(G)**2,str(pr))

if __name__=='__main__':
    # Independent exhaustive enumeration of every endomorphism matrix in low dimensions,
    # retaining precisely invertible homomorphisms; not merely counting the prescribed normal forms.
    for F,n in ((F2,3),(F3,3),(F2,4)):
        exhaustive_automorphisms(F,n)
    for F,n in ((F2,2),(F3,3),(F4,2),(F4,3),(F8,3),(F8,4),(F16,3),(F27,13)):
        count_conjugacy(F,n)
    for F,n in ((F2,3),(F3,3),(F4,2),(F4,3),(F8,3),(F8,4)):
        generating_pairs(F,n)
    print('VERIFY_OK')
