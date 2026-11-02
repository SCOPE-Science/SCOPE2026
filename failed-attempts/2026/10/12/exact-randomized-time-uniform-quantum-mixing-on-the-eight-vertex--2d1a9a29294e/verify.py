#!/usr/bin/env python3
"""Exact verification of a phase-grid witness for randomized mixing on P8.
Pure Python standard library, no numerical extrapolation or external dependencies.
"""
from fractions import Fraction
from itertools import product

# W[a][b][c], where phase angles (a,b,c)*pi/2 are used.
W = [
 [[1,1,1,1],[5,21,1,9],[1,13,5,1],[1,1,1,1]],
 [[1,1,21,5],[1,1,1,1],[1,1,9,1],[1,1,1,1]],
 [[1,17,1,1],[1,17,1,1],[17,1,1,1],[1,1,1,1]],
 [[9,1,1,1],[1,1,21,13],[1,1,1,9],[17,1,1,1]],
]
# Entries displayed in row=a, column=b, slices c=0,1,2,3.
# Exact signs for cos/sin of integer multiples of pi/2.
C4=(1,0,-1,0);S4=(0,1,0,-1)

def rank_mod(rows,p):
    A=[[x%p for x in row] for row in rows]
    rank=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(rank,len(A)) if A[i][col]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank]
        inv=pow(A[rank][col],-1,p)
        A[rank]=[(x*inv)%p for x in A[rank]]
        for i in range(len(A)):
            if i!=rank and A[i][col]:
                fac=A[i][col]
                A[i]=[(x-fac*y)%p for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==len(A):break
    return rank

class Cyclo:
    # Rational polynomial modulo Phi_18(z)=z^6-z^3+1.
    def __init__(self,coeff=()):
        self.a=tuple(Fraction(coeff[i]) if i<len(coeff) else Fraction(0) for i in range(6))
    def __add__(self,b):
        if not isinstance(b,Cyclo): b=Cyclo((b,))
        return Cyclo([x+y for x,y in zip(self.a,b.a)])
    __radd__=__add__
    def __neg__(self):return Cyclo([-x for x in self.a])
    def __sub__(self,b):return self+-b if isinstance(b,Cyclo) else self+Cyclo((-b,))
    def __mul__(self,b):
        if not isinstance(b,Cyclo):return Cyclo([x*b for x in self.a])
        q=[Fraction(0)]*11
        for i,x in enumerate(self.a):
            for j,y in enumerate(b.a):q[i+j]+=x*y
        for k in range(10,5,-1):
            a=q[k];q[k]=0;q[k-3]+=a;q[k-6]-=a # z^6=z^3-1
        return Cyclo(q[:6])
    __rmul__=__mul__
    def __truediv__(self,b):return self*Fraction(1,b)
    def __eq__(self,b):return self.a == (b.a if isinstance(b,Cyclo) else Cyclo((b,)).a)
    def eval_mod(self,h,p):
        return sum((x.numerator*pow(x.denominator,-1,p)*pow(h,i,p))%p for i,x in enumerate(self.a))%p

Z=Cyclo((0,1)); powers=[Cyclo((1,))]
for _ in range(17):powers.append(powers[-1]*Z)
assert powers[18-1]*Z==1
assert Z*Z*Z*Z*Z*Z - Z*Z*Z + Cyclo((1,))==0

def cos9(k):return (powers[k%18]+powers[-k%18])/2

def vprod(i,j,k): # i,j in 1,...,8, k in 1,...,4
    return (cos9((i-j)*k)-cos9((i+j)*k))/9

def main():
    assert sum(W[a][b][c] for a,b,c in product(range(4),repeat=3))==256
    assert min(W[a][b][c] for a,b,c in product(range(4),repeat=3))>=1
    D=[[0]*4 for _ in range(4)]; S=[[0]*4 for _ in range(4)]
    P=[]
    for a,b,c in product(range(4),repeat=3):
        phi=((a+b)%4,a,c,b)
        x=tuple(C4[t] for t in phi);y=tuple(S4[t] for t in phi)
        w=W[a][b][c]
        P.append((x,y,w))
        for i in range(4):
            for j in range(4):D[i][j]+=w*x[i]*x[j];S[i][j]+=w*y[i]*y[j]
    signs=(1,-1,1,-1)
    for i in range(4):
        for j in range(4):
            assert D[i][j] == (128 if i==j else -16)
            assert S[i][j] == (128 if i==j else -16*signs[i]*signs[j])
    # Verify sine-projector identities in the exact cyclotomic field.
    V={(i,j):[vprod(i,j,k) for k in range(1,5)] for i in range(1,9) for j in range(1,9)}
    for (i,j),v in V.items():
        delta=int(i==j)+int(i+j==9)
        assert sum((u*u for u in v),Cyclo()) == Fraction(1,18)+Fraction(delta,36)
        z=sum((signs[k]*v[k] for k in range(4)),Cyclo()) if (i+j)%2 else sum(v,Cyclo())
        expected=Fraction(1,2) if (i==j or i+j==9) else Fraction(0)
        assert z==expected
        acc=sum((v[k]*v[l]*D[k][l] for k in range(4) for l in range(4)),Cyclo()) if (i+j)%2==0 else sum((v[k]*v[l]*S[k][l] for k in range(4) for l in range(4)),Cyclo())
        assert 4*acc/256==Fraction(1,8)
    # The grid samples span the entire affine space of the 16 phase-frequency modes.
    # Lower bound from a reduction of Q(zeta18) to F_109; upper bound: 16 modes.
    p=109
    roots=[h for h in range(1,p) if pow(h,18,p)==1 and pow(h,9,p)==p-1 and pow(h,6,p)!=1 and pow(h,3,p)!=1]
    assert roots
    h=roots[0]
    wmod={(i,j):[x.eval_mod(h,p) for x in V[(i,j)]] for i in range(1,9) for j in range(i,9)}
    grid=[]
    for x,y,_ in P:
        row=[]
        for i in range(1,9):
            for j in range(i,9):
                val=sum(wmod[(i,j)][k]*(x[k] if (i+j)%2==0 else y[k]) for k in range(4))
                row.append(4*val*val%p)
        grid.append(row)
    centered=[[ (x-y)%p for x,y in zip(row,grid[0])] for row in grid[1:]]
    dimension=rank_mod(centered,p)
    assert dimension==16,dimension
    print('VERIFY_OK pmf=64 exact_moments=32 exact_projector_entries=64 mod109_affine_rank=16')

if __name__=='__main__': main()
