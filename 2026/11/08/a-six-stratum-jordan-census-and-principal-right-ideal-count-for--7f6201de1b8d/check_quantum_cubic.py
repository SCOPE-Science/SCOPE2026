#!/usr/bin/env python3
"""Direct quantum-cubic multiplication and Jordan census checks. Python 3 stdlib."""
from collections import Counter
from itertools import product
import random

class FiniteField:
    def __init__(self, order):
        self.n = order
        if order not in (4,7,13):
            raise ValueError('Only GF(4), GF(7), GF(13) are supported')
        self.qroot = {4:2,7:2,13:3}[order]
        self.add = [[(a^b if order==4 else (a+b)%order) for b in range(order)]for a in range(order)]
        self.mul = [[self._multiply(a,b) for b in range(order)]for a in range(order)]
        self.inv = [0] + [next(b for b in range(1,order) if self.mul[a][b]==1) for a in range(1,order)]
        assert self.mul[self.mul[self.qroot][self.qroot]][self.qroot] == 1
        assert self.qroot != 1 and self.mul[self.qroot][self.qroot]!=1
    def _multiply(self,a,b):
        if self.n !=4:return a*b%self.n
        p=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1):p ^= (1<<(i+j))
        if p & 8:p ^= 0b1100 # t^3=t^2+t when t^2=t+1
        if p & 4:p ^= 0b111  # t^2=t+1
        return p
    def pow(self,a,k):
        if k<0:return self.pow(self.inv[a],-k)
        x=1
        for _ in range(k):x=self.mul[x][a]
        return x

B=[(i,j) for i in range(3) for j in range(3)]
idx={z:i for i,z in enumerate(B)}


def mul(f,g,F):
    h=[0]*9
    for t,(a,b) in enumerate(B):
        if not f[t]:continue
        for s,(c,d) in enumerate(B):
            if not g[s] or a+c>=3 or b+d>=3:continue
            scale=F.pow(F.qroot,-b*c)
            h[idx[a+c,b+d]]=F.add[h[idx[a+c,b+d]]][F.mul[f[t]][F.mul[g[s]][scale]]]
    return h


def rank(A,F):
    M=[list(row) for row in A]
    rows=len(M);cols=len(M[0]);r=0
    for c in range(cols):
        k=next((i for i in range(r,rows) if M[i][c]),None)
        if k is None:continue
        M[r],M[k]=M[k],M[r]
        iv=F.inv[M[r][c]]
        M[r]=[F.mul[iv][x] for x in M[r]]
        for i in range(r+1,rows):
            v=M[i][c]
            if v:
                M[i]=[F.add[M[i][j]][F.mul[v][M[r][j]]] if F.n==4
                      else (M[i][j]-F.mul[v][M[r][j]])%F.n for j in range(cols)]
        r+=1
        if r==rows:break
    return r


def type_by_rank(f,F):
    # Matrix columns are the products f * x^i y^j, computed in the original algebra.
    A=[[0]*9 for i in range(9)]
    for j in range(9):
        e=[0]*9;e[j]=1
        prod=mul(f,e,F)
        for i in range(9):A[i][j]=prod[i]
    r=rank(A,F)
    ff=mul(f,f,F)
    if any(ff):
        assert not any(mul(ff,f,F)), 'A radical element has nonzero cube'
    r2=0
    if any(ff):
        B2=[[0]*9 for _ in range(9)]
        for j in range(9):
            e=[0]*9;e[j]=1
            prod=mul(ff,e,F)
            for i in range(9):B2[i][j]=prod[i]
        r2=rank(B2,F)
    return (r,r2)



def canonical_right_ideal(f,F):
    """Canonical RREF of the span of f times the standard basis."""
    rows=[]
    for j in range(9):
        e=[0]*9;e[j]=1
        rows.append(mul(f,e,F))
    r=0
    for c in range(9):
        k=next((i for i in range(r,9) if rows[i][c]),None)
        if k is None:continue
        rows[r],rows[k]=rows[k],rows[r]
        iv=F.inv[rows[r][c]]
        rows[r]=[F.mul[iv][z] for z in rows[r]]
        for i in range(9):
            if i==r:continue
            z=rows[i][c]
            if z:
                rows[i]=[F.add[rows[i][j]][F.mul[z][rows[r][j]]] if F.n==4
                        else (rows[i][j]-F.mul[z][rows[r][j]])%F.n for j in range(9)]
        r+=1
        if r==9:break
    return tuple(tuple(row) for row in rows[:r])

def main():
    F=FiniteField(4)
    counts=Counter();right_ideals=set()
    # Exhaustive direct matrix census of the full eight-dimensional radical.
    for coords in product(range(4),repeat=8):
        f=[0]+list(coords)
        counts[type_by_rank(f,F)]+=1
        right_ideals.add(canonical_right_ideal(f,F))
    q=4
    expected={(6,3):(q*q-1)*q**6,
              (4,1):q**5*(q-1),
              (3,0):(q*q-1)*q**3,
              (2,0):q*(q*q-1),
              (1,0):q-1,
              (0,0):1}
    assert dict(counts)==expected,(counts,expected)
    print('GF4 full radical direct Jordan census:',sorted(counts.items()))
    print('GF4 exhaustive tests:',sum(counts.values()))
    ideal_counts=Counter(len(basis) for basis in right_ideals)
    expected_ideals={0:1,1:1,2:q+1,3:q*(q+1),4:q*q,6:q*(q+1)}
    assert dict(ideal_counts)==expected_ideals,(ideal_counts,expected_ideals)
    print('GF4 distinct proper principal right ideals:',sorted(ideal_counts.items()))

    # Exhaustive direct matrix check of the six-dimensional second radical power.
    F=FiniteField(7);q=7
    allowed=[idx[i,j] for i,j in B if i+j>=2]
    counts=Counter()
    for coords in product(range(q),repeat=len(allowed)):
        f=[0]*9
        for j,v in zip(allowed,coords):f[j]=v
        counts[type_by_rank(f,F)]+=1
    expected={(4,1):q**5*(q-1),
              (3,0):(q*q-1)*q**3,
              (2,0):q*(q*q-1),
              (1,0):q-1,
              (0,0):1}
    assert dict(counts)==expected,(counts,expected)
    print('GF7 second radical power direct Jordan census:',sorted(counts.items()))
    print('GF7 exhaustive tests:',sum(counts.values()))

    rng=random.Random(42123)
    for q in (7,13):
        F=FiniteField(q)
        for _ in range(125):
            f=[0]+[rng.randrange(q) for _ in range(8)]
            if f[idx[(0,1)]]==0 and f[idx[(1,0)]]==0:
                f[idx[(1,0)]]=1
            assert type_by_rank(f,F)==(6,3)
        print('GF'+str(q)+' additional direct nonzero-linear-part tests: 125')
    print('QUANTUM_CUBIC_JORDAN_CENSUS_DIRECT_CHECK_OK')

if __name__=='__main__':main()
