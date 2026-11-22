"""Finite-field checks for the 3-by-3 upper-triangular zero Jordan-product count.

Run: python checks/verify.py
No third-party dependencies. Odd q: prime test fields 3,5,7;
even q: binary extensions of degrees 1,2,3.
"""
from itertools import product
from collections import Counter

class Field:
    def __init__(self, q):
        self.q=q
        if q in (2,4,8):
            self.polynomial={2:0b11,4:0b111,8:0b1011}[q]
            self.degree={2:1,4:2,8:3}[q]
        elif q in (3,5,7):
            self.polynomial=None
        else:
            raise ValueError('test field not implemented')
        self.elements=range(q)
        self.add=[[self._add(x,y) for y in self.elements] for x in self.elements]
        self.mul=[[self._mul(x,y) for y in self.elements] for x in self.elements]
        self.neg=[next(y for y in self.elements if self.add[x][y]==0) for x in self.elements]
        self.inv={x: next(y for y in self.elements if self.mul[x][y]==1) for x in self.elements if x != 0} if q > 1 else {}
    def _add(self,a,b):
        return (a^b) if self.polynomial is not None else (a+b)%self.q
    def _mul(self,a,b):
        if self.polynomial is None:return a*b%self.q
        v=0
        while b:
            if b&1:v^=a
            b>>=1
            a<<=1
            if a&self.q:a^=self.polynomial
        return v

def matrix_rank(rows, F):
    rows=[row[:] for row in rows]
    rank=0
    for j in range(len(rows[0])):
        piv=next((i for i in range(rank,len(rows)) if rows[i][j]!=0),None)
        if piv is None:continue
        rows[rank],rows[piv]=rows[piv],rows[rank]
        rec=F.inv[rows[rank][j]]
        rows[rank]=[F.mul[v][rec] for v in rows[rank]]
        for i in range(rank+1,len(rows)):
            if rows[i][j]:
                z=F.neg[rows[i][j]]
                rows[i]=[F.add[rows[i][k]][F.mul[z][rows[rank][k]]] for k in range(len(rows[0]))]
        rank+=1
    return rank

def theoretical(q):
    if q%2:
        return q**3*(2*q-1)*(11*q*q-15*q+5)
    return q**5*(q**4+3*q**3-2*q*q-2*q+1)

def linear_antimultiplication_count(q):
    F=Field(q);add=F.add
    ranks=Counter()
    # A=(a,b,c,x,y,z), in order (11,22,33,12,23,13).
    for a,b,c,x,y,z in product(F.elements,repeat=6):
        # Columns of the Jordan-product linear map in B coordinates:
        # B=(d,e,f,u,v,w).
        L=[[0]*6 for _ in range(6)]
        L[0][0]=add[a][a]
        L[1][1]=add[b][b]
        L[2][2]=add[c][c]
        L[3][0]=x;L[3][1]=x;L[3][3]=add[a][b]
        L[4][1]=y;L[4][2]=y;L[4][4]=add[b][c]
        L[5][0]=z;L[5][2]=z;L[5][3]=y;L[5][4]=x;L[5][5]=add[a][c]
        ranks[matrix_rank(L,F)]+=1
    assert sum(ranks.values())==q**6
    return sum(count*q**(6-r) for r,count in ranks.items()), sorted(ranks.items())

def as_matrix(entries):
    a,b,c,x,y,z=entries
    return ((a,x,z),(0,b,y),(0,0,c))

def zero_jordan_literal(A,B,F):
    for i in range(3):
        for j in range(3):
            xy=0;yx=0
            for k in range(3):
                xy=F.add[xy][F.mul[A[i][k]][B[k][j]]]
                yx=F.add[yx][F.mul[B[i][k]][A[k][j]]]
            if F.add[xy][yx]:return False
    return True

def literal_pair_count(q):
    F=Field(q)
    mats=[as_matrix(v) for v in product(F.elements,repeat=6)]
    return sum(zero_jordan_literal(A,B,F) for A in mats for B in mats)

def main():
    for q in (2,3,4,5,7,8):
        actual,hist=linear_antimultiplication_count(q)
        expected=theoretical(q)
        print(f'q={q} linear count={actual} expected={expected} match={actual==expected}; rank_hist={hist}')
        assert actual==expected
    for q in (2,3):
        literal=literal_pair_count(q)
        print(f'q={q} literal 3x3 multiplication count={literal} expected={theoretical(q)} match={literal==theoretical(q)}')
        assert literal==theoretical(q)
    print('ALL_TRIANGULAR_ANTICOMMUTING_CHECKS_PASS')
if __name__=='__main__':main()
