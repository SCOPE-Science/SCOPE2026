#!/usr/bin/env python3
"""Independent finite-field basis-equation checks for CPA structures on an irreducible almost-abelian Lie algebra. Standard library only."""
from itertools import product

class Field:
    def __init__(self, p, modulus):
        self.p=p
        self.modulus=tuple(modulus)
        self.e=len(modulus)
        self.q=p**self.e
        self.digits=[self._digits(i) for i in range(self.q)]
        self.toint={x:i for i,x in enumerate(self.digits)}
        self.add=[[self.toint[tuple((a+b)%p for a,b in zip(self.digits[i],self.digits[j]))] for j in range(self.q)] for i in range(self.q)]
        self.neg=[self.toint[tuple((-a)%p for a in self.digits[i])] for i in range(self.q)]
        self.mul=[[self._mul(i,j) for j in range(self.q)] for i in range(self.q)]
        self.inv=[0]+[next(j for j in range(1,self.q) if self.mul[i][j]==1) for i in range(1,self.q)]
    def _digits(self,i):
        out=[]
        for _ in range(self.e): out.append(i%self.p);i//=self.p
        return tuple(out)
    def _mul(self,i,j):
        p=self.p;e=self.e
        a=self.digits[i];b=self.digits[j]
        coeff=[0]*(2*e-1)
        for x in range(e):
            for y in range(e):coeff[x+y]=(coeff[x+y]+a[x]*b[y])%p
        for t in range(2*e-2,e-1,-1):
            h=coeff[t]
            for y in range(e):coeff[t-e+y]=(coeff[t-e+y]-h*self.modulus[y])%p
        return self.toint[tuple(coeff[:e])]

def nullspace(rows,F,n):
    a=[r[:] for r in rows];pivot=[];row=0
    for col in range(n):
        idx=next((i for i in range(row,len(a)) if a[i][col]),None)
        if idx is None:continue
        a[row],a[idx]=a[idx],a[row]
        inv=F.inv[a[row][col]]
        a[row]=[F.mul[inv][x] for x in a[row]]
        for i in range(len(a)):
            if i==row or a[i][col]==0:continue
            c=a[i][col]
            a[i]=[F.add[u][F.neg[F.mul[c][v]]] for u,v in zip(a[i],a[row])]
        pivot.append(col);row+=1
        if row==len(a):break
    free=[j for j in range(n) if j not in pivot]
    basis=[]
    for f in free:
        vec=[0]*n;vec[f]=1
        for i,col in enumerate(pivot):vec[col]=F.neg[a[i][f]]
        basis.append(vec)
    return basis

def test(name,F,A,d,expected,expected_support=None):
    q=F.q;N=d+1
    # C[k][i][j] is the coefficient of basis vector k in [i,j].
    C=[[[0]*N for _ in range(N)] for __ in range(N)]
    for i in range(d):
        for j in range(d):
            C[i+1][0][j+1]=A[i][j]
            C[i+1][j+1][0]=F.neg[A[i][j]]
    pairs=[(i,j) for i in range(N) for j in range(i,N)]
    ix={p:i for i,p in enumerate(pairs)};nvar=N*len(pairs)
    def index(i,j,k):return k*len(pairs)+ix[(min(i,j),max(i,j))]
    eq=[]
    for i,j,z,k in product(range(N),repeat=4):
        row=[0]*nvar
        for l in range(N):
            ind=index(l,z,k)
            row[ind]=F.add[row[ind]][C[l][i][j]]
        for h in range(N):
            idx=index(j,z,h)
            row[idx]=F.add[row[idx]][F.neg[C[k][i][h]]]
            idx=index(i,z,h)
            row[idx]=F.add[row[idx]][F.neg[C[k][h][j]]]
        if any(row):eq.append(row)
    basis=nullspace(eq,F,nvar)
    assert len(basis)==3*d,(name,'symmetric biderivations',len(basis),3*d)
    def value(T,i,j):return [T[index(i,j,k)] for k in range(N)]
    def left(T,i,y):
        return [sum_field((F.mul[y[j]][T[index(i,j,k)]] for j in range(N))) for k in range(N)]
    def sum_field(items):
        a=0
        for b in items:a=F.add[a][b]
        return a
    def cpa(T):
        for i,j,k in product(range(N),repeat=3):
            iz=left(T,i,value(T,j,k));jz=left(T,j,value(T,i,k))
            for h in range(N):
                bracket=sum_field(F.mul[C[l][i][j]][T[index(l,k,h)]] for l in range(N))
                if F.add[bracket][F.neg[F.add[iz[h]][F.neg[jz[h]]]]]!=0:return False
        return True
    count=0;support={}
    for coeff in product(range(q),repeat=len(basis)):
        T=[sum_field(F.mul[coeff[j]][basis[j][k]] for j in range(len(basis))) for k in range(nvar)]
        if cpa(T):
            count+=1
            # Ordinary image rank from column span over F.
            vectors=[value(T,i,j) for i,j in pairs]
            r=nvar # use elimination on map image columns
            r=N-len(nullspace(vectors,F,N))
            support[r]=support.get(r,0)+1
            assert all(T[index(i,j,k)]==0 for i in range(1,N) for j in range(1,N) for k in range(N))
    assert count==expected,(name,count,expected)
    default={0:1,1:q**d-1,d:expected-q**d}
    assert support==(default if expected_support is None else expected_support),(name,support)
    print(f'{name}: symmetric_biderivation_dimension={len(basis)}, CPA_count={count}, image_rank_distribution={dict(sorted(support.items()))}, PASS')

if __name__=='__main__':
    F2=Field(2,[0]);F3=Field(3,[0]);F4=Field(2,[1,1])
    test('F2, degree 2',F2,[[0,1],[1,1]],2,8)
    test('F3, degree 2',F3,[[0,2],[1,0]],2,18)
    test('F2, degree 3',F2,[[0,0,1],[1,0,1],[0,1,0]],3,16)
    test('F4 scalar extension of F2, degree 2',F4,[[0,1],[1,1]],2,64,{0:1,1:23,2:40})
    print('CPA_IRREDUCIBLE_GALOIS_DESCENT_VERIFIED')
