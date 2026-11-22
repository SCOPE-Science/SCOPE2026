#!/usr/bin/env python3
"""Exact reconstruction and local Smith certificate for a cubic-surface incidence graph.

Python >=3.9, standard library only. The 27 rows are E_i, L_ij, Q_i,
with i=1..6 and i<j; each of 36 columns is a 12-line double-six.
"""
from itertools import combinations
from collections import Counter
from math import prod


def picard_data():
    names=[];curves=[]
    for i in range(6):
        names.append('E'+str(i+1))
        curves.append((0,)+tuple(int(j==i) for j in range(6)))
    for i,j in combinations(range(6),2):
        names.append('L'+str(i+1)+str(j+1))
        curves.append((1,)+tuple(-int(k in (i,j)) for k in range(6)))
    for i in range(6):
        names.append('Q'+str(i+1))
        curves.append((2,)+tuple(0 if j==i else -1 for j in range(6)))
    return names,curves

def pairing(x,y):
    return x[0]*y[0]-sum(a*b for a,b in zip(x[1:],y[1:]))

def sixers(curves):
    I=[[pairing(x,y) for y in curves] for x in curves]
    assert Counter(I[0])=={0:16,1:10,-1:1}
    S=[]
    for subset in combinations(range(27),6):
        if all(I[i][j]==0 for i,j in combinations(subset,2)):
            S.append(subset)
    assert len(S)==72
    double6=set()
    for A in S:
        B=tuple(i for i in range(27) if sum(I[i][j] for j in A)==5)
        assert len(B)==6 and all(I[i][j]==0 for i,j in combinations(B,2))
        assert set(B).isdisjoint(A)
        assert all(sum(I[i][j] for j in B)==5 for i in A)
        double6.add(tuple(sorted(A+B)))
    assert len(double6)==36
    return I, sorted(double6)

def root_double_sixes(curves):
    roots=[]
    for i,j in combinations(range(6),2):
        roots.append((0,)+tuple(int(k==i)-int(k==j) for k in range(6)))
    for t in combinations(range(6),3):
        roots.append((1,)+tuple(-int(k in t) for k in range(6)))
    roots.append((2,)+(-1,)*6)
    assert len(roots)==36 and all(pairing(r,r)==-2 for r in roots)
    out=set()
    for r in roots:
        plus=[i for i,v in enumerate(curves) if pairing(v,r)==1]
        minus=[i for i,v in enumerate(curves) if pairing(v,r)==-1]
        assert len(plus)==6 and len(minus)==6
        out.add(tuple(sorted(plus+minus)))
    assert len(out)==36
    return sorted(out)

def incidence(sets):
    B=[[int(i in s) for s in sets] for i in range(27)]
    assert all(sum(r)==16 for r in B)
    assert all(sum(B[i][j] for i in range(27))==12 for j in range(36))
    return B

def gram(B):
    return [[sum(B[i][k]*B[j][k] for k in range(36)) for j in range(27)] for i in range(27)]

def spectral_certificate(C):
    assert sum(C[i][i] for i in range(27))==432
    assert all(sum(row)==192 for row in C)
    # C*(C-12I)*(C-192I)=0; exact, not numeric eigenvalue sampling.
    C2=[[sum(C[i][k]*C[k][j] for k in range(27)) for j in range(27)] for i in range(27)]
    C3=[[sum(C2[i][k]*C[k][j] for k in range(27)) for j in range(27)] for i in range(27)]
    for i in range(27):
        for j in range(27):
            assert C3[i][j]-204*C2[i][j]+2304*C[i][j]==0
    # Since C has nonnegative entries and is positive semidefinite, its
    # only eigenvalues are 0,12,192, with multiplicities 6,20,1.
    # The full Laplacian consequently has spectrum 0,28,10^20,18^20,16^6,12^15.
    # Kirchhoff: product(nonzero eigenvalues)/63.
    tau=28*(10**20)*(18**20)*(16**6)*(12**15)//63
    assert 63*tau==28*(10**20)*(18**20)*(16**6)*(12**15)
    assert tau==(2**96)*(3**53)*(5**20)
    return tau

def laplacian(B):
    M=[[0]*63 for _ in range(63)]
    for i in range(27):M[i][i]=16
    for j in range(36):M[27+j][27+j]=12
    for i in range(27):
        for j in range(36):
            M[i][27+j]=M[27+j][i]=-B[i][j]
    assert all(sum(r)==0 for r in M)
    return M

def p_smith_valuations(A,p,precision=22):
    """Unimodular local elimination modulo p^precision, with exact valuation counts.

    If the remaining matrix has no unit, it is divided by p, reducing
    precision by one; a unit pivot permits elimination over Z/p^a.
    """
    modulus=p**precision
    M=[[a%modulus for a in row] for row in A]
    n=len(M); offset=0; valuations=[]
    for k in range(n):
        while True:
            pivot=next(((i,j) for i in range(k,n) for j in range(k,n)
                        if M[i][j]%p), None)
            if pivot is not None:break
            assert modulus>p and any(M[i][j] for i in range(k,n) for j in range(k,n)), 'precision exhausted'
            for i in range(k,n):
                for j in range(k,n):
                    assert M[i][j]%p==0
                    M[i][j]//=p
            modulus//=p;offset+=1
        i,j=pivot
        M[i],M[k]=M[k],M[i]
        for row in M:row[j],row[k]=row[k],row[j]
        inverse=pow(M[k][k],-1,modulus)
        for r in range(k+1,n):
            factor=(M[r][k]*inverse)%modulus
            if factor:
                for c in range(k+1,n):
                    M[r][c]=(M[r][c]-factor*M[k][c])%modulus
            M[r][k]=0
        valuations.append(offset)
    return valuations


def main():
    names,curves=picard_data()
    I,by_sixers=sixers(curves)
    by_roots=root_double_sixes(curves)
    assert by_roots==by_sixers
    B=incidence(by_sixers)
    C=gram(B)
    assert Counter((I[i][j],C[i][j]) for i in range(27) for j in range(i+1,27))=={(0,6):216,(1,8):135}
    tau=spectral_certificate(C)
    L=laplacian(B)
    targets={2:Counter({0:12,1:28,2:10,3:6,5:6}),
             3:Counter({0:42,1:1,2:5,3:14}),
             5:Counter({0:42,1:20})}
    vv={}
    for p,expected in targets.items():
        a=p_smith_valuations([r[:-1] for r in L[:-1]],p)
        b=p_smith_valuations([r[1:] for r in L[1:]],p)
        assert a==b and Counter(a)==expected
        vv[p]=a
    factors=[prod(p**vv[p][i] for p in vv) for i in range(62)]
    assert all(factors[i+1]%factors[i]==0 for i in range(61))
    assert Counter(factors)==Counter({1:12,2:28,4:2,60:1,180:5,540:2,1080:6,4320:6})
    assert prod(factors)==tau
    print('INCIDENCE_27_36_432_OK')
    print('GRAM_EIGENSPECTRUM_192_12_0_OK')
    print('TREE_ORDER_2^96_3^53_5^20_OK')
    print('TWO_ROOTED_LOCAL_SMITH_CHECKS_OK')
    print('INVARIANTS',sorted(Counter(factors).items()))
    print('DOUBLE_SIX_GRAPH_CRITICAL_GROUP_OK')

if __name__=='__main__': main()
