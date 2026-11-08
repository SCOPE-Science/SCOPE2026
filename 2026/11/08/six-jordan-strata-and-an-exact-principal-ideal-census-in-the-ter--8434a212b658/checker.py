#!/usr/bin/env python3
"""Independent original-multiplication checks for k[x,y]/(x^3,y^3), char(k)=3.

Run with Python 3.10+ without third-party dependencies.  Exhaustive over
F_3 on all 3^8 radical elements; deterministic spot tests over F_9.
"""
from collections import Counter
from itertools import product
from random import Random

MONS = ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2),(2,2))
INDEX = {m:i for i,m in enumerate(MONS)}

class Field:
    def __init__(self,q):
        assert q in (3,9)
        self.q=q
        def ab(t): return t%3,t//3
        def add(a,b):
            x,y=ab(a); z,w=ab(b)
            return ((x+z)%3)+3*((y+w)%3)
        def mul(a,b):
            x,y=ab(a); z,w=ab(b)
            # F_9 = F_3[t]/(t^2+1), t^2=2.
            return ((x*z+2*y*w)%3)+3*((x*w+y*z)%3)
        if q==3:
            add=lambda a,b:(a+b)%3
            mul=lambda a,b:(a*b)%3
        self.add=[[add(a,b) for b in range(q)] for a in range(q)]
        self.mul=[[mul(a,b) for b in range(q)] for a in range(q)]
        self.neg=[next(b for b in range(q) if self.add[a][b]==0) for a in range(q)]
        self.inv=[0]+[next(b for b in range(1,q) if self.mul[a][b]==1) for a in range(1,q)]
    def sub(self,a,b):return self.add[a][self.neg[b]]

def multiplication_matrix(f,F):
    M=[[0]*9 for _ in range(9)]
    for j,(u,v) in enumerate(MONS):
        for k,(a,b) in enumerate(MONS):
            if u+a<3 and v+b<3:
                i=INDEX[(u+a,v+b)]
                M[i][j]=F.add[M[i][j]][f[k]]
    return M

def matrix_product(A,B,F):
    C=[[0]*9 for _ in range(9)]
    for i in range(9):
        for z in range(9):
            if A[i][z]:
                for j in range(9):
                    if B[z][j]:
                        C[i][j]=F.add[C[i][j]][F.mul[A[i][z]][B[z][j]]]
    return C

def rref(M,F):
    A=[row[:] for row in M]
    nr=len(A); nc=len(A[0]); p=0
    for j in range(nc):
        k=next((i for i in range(p,nr) if A[i][j]),None)
        if k is None: continue
        A[p],A[k]=A[k],A[p]
        inv=F.inv[A[p][j]]
        A[p]=[F.mul[inv][v] for v in A[p]]
        for i in range(nr):
            if i!=p and A[i][j]:
                coeff=A[i][j]
                A[i]=[F.sub(v,F.mul[coeff][w]) for v,w in zip(A[i],A[p])]
        p+=1
        if p==nr:break
    return tuple(tuple(row) for row in A[:p]),p

def predicted_rank_pair(f,F):
    if f[1] or f[2]:return 6,3
    a,b,c=f[3:6]
    if a or b or c:
        delta=F.sub(F.mul[b][b],F.mul[a][c])
        return (4,1) if delta else (3,0)
    if f[6] or f[7]:return 2,0
    if f[8]:return 1,0
    return 0,0

def theoretical_element_ranks(q):
    return {0:1,1:q-1,2:q*(q*q-1),3:q**3*(q*q-1),
            4:q**5*(q-1),6:q**6*(q*q-1)}

def theoretical_ideal_dimensions(q):
    return {0:1,1:1,2:q+1,3:q*(q+1),4:q*q,6:q*(q+1)}

def exhaustive_F3():
    F=Field(3); ranks=Counter(); jordan=Counter(); ideals={}
    for tail in product(range(3),repeat=8):
        f=(0,)+tail
        M=multiplication_matrix(f,F)
        actual_1=rref(M,F)[1]
        actual_2=rref(matrix_product(M,M,F),F)[1]
        predicted=predicted_rank_pair(f,F)
        assert (actual_1,actual_2)==predicted,(f,actual_1,actual_2,predicted)
        assert actual_2<=actual_1
        assert matrix_product(matrix_product(M,M,F),M,F)==[[0]*9 for _ in range(9)]
        ranks[actual_1]+=1
        jordan[(actual_1,actual_2)]+=1
        # Independent canonical basis of the image ideal (f).
        image_rows=[[M[i][j] for i in range(9)] for j in range(9)]
        key,rank_ideal=rref(image_rows,F)
        assert rank_ideal==actual_1
        ideals[key]=rank_ideal
    assert dict(ranks)==theoretical_element_ranks(3)
    sizes=Counter(ideals.values())
    assert dict(sizes)==theoretical_ideal_dimensions(3)
    assert len(ideals)==3*(3*3+3+1)==39
    assert sum(ranks.values())==3**8
    print('F3 exhaustive radical elements:',sum(ranks.values()))
    print('F3 ranks:',dict(sorted(ranks.items())))
    print('F3 principal ideals by dimension:',dict(sorted(sizes.items())))
    print('F3 Jordan (rank M_f, rank M_f^2):',dict(sorted(jordan.items())))

def sampled_F9():
    F=Field(9); rr=Random(170903); cases=[]
    # Test every prescribed leading behavior with systematic canonical examples.
    for c in range(1,9):
        f=[0]*9; f[1]=c; cases.append(tuple(f))
        f=[0]*9; f[3]=c; cases.append(tuple(f))
        f=[0]*9; f[4]=c; cases.append(tuple(f))
        f=[0]*9; f[6]=c; cases.append(tuple(f))
        f=[0]*9; f[8]=c; cases.append(tuple(f))
    cases.extend(tuple([0]+[rr.randrange(9) for _ in range(8)]) for _ in range(1024))
    for f in cases:
        M=multiplication_matrix(f,F)
        M2=matrix_product(M,M,F)
        observed=(rref(M,F)[1],rref(M2,F)[1])
        predicted=predicted_rank_pair(f,F)
        assert observed==predicted,(f,observed,predicted)
        assert matrix_product(M2,M,F)==[[0]*9 for _ in range(9)]
    print('F9 deterministic directly checked elements:',len(cases))
    print('F9 predicted rank distribution (symbolic, not enumerated):',theoretical_element_ranks(9))
    print('F9 predicted principal-ideal distribution (symbolic, not enumerated):',theoretical_ideal_dimensions(9))
    assert sum(theoretical_element_ranks(9).values())==9**8
    assert sum(theoretical_ideal_dimensions(9).values())==3*(9*9+9+1)

if __name__=='__main__':
    exhaustive_F3()
    sampled_F9()
    print('TERNARY_GROUP_ALGEBRA_JORDAN_AND_PRINCIPAL_IDEALS_CHECKS_OK')
