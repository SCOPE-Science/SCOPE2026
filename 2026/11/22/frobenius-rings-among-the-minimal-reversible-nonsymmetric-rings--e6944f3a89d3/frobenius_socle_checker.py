#!/usr/bin/env python3
"""Exact F2 quotient linear-algebra checks of presentations and graded pairings.

Standalone Python 3, standard library only. Presentation strings encode sums
over F2 of noncommutative monomials. All words are truncated at radical
length D+1. These finite checks support the filtered proof; they are not
by themselves a proof of any independent completeness classification.
"""

from itertools import product
from collections import defaultdict

D2={
1:['xxyy','xx+yy','xx+xy+yx'],
2:['xxyy','xx+yy','xx+xy+yx+xxx'],
3:['xxyy','xx+yy','xx+xy+yx+xxx+xxy'],
4:['xxyy','xx+yy','xx+xy+yx+xxxy'],
5:['xxyy','xx+yy','xx+xy+yx+xxx+xxy+xxxy'],
6:['xxyy','xx+yy+xxx','xx+xy+yx+xxx+xxxy'],
7:['xx+yx+yy','xyx+xyy','xxy+xyx+yyx'],
}
D3={
8:['xx+yy','xz+zy','xy+xz+zx','xx+xz+yx','xy+yz','zz'],
9:['xx+yy+xxx','xz+zy','xy+xz+zx','xx+xz+yx','xy+yz','zz'],
10:['xx+yy','xz+zy','xy+xz+zx','xx+xz+yx','xy+yz','zz+xxx'],
11:['xx+yy+xxx','xz+zy','xy+xz+zx','xx+xz+yx','xy+yz','zz+xxx'],
12:['xx+zy','xx+xz+zz','xx+xy+xz+zx','xx+xz+yx','xz+yy','xx+xy+yz','xxx+yzy','xxx+zyy'],
13:['xx+zy+xxx','xx+xz+zz','xx+xy+xz+zx','xx+xz+yx','xz+yy','xx+xy+yz','xxx+yzy','xxx+zyy'],
14:['xx+yy','xy+zx','xz+zy','xx+xz+yx','xy+xz+yz','zz'],
15:['xx+yy+xxy','xy+zx','xz+zy','xx+xz+yx','xy+xz+yz','zz'],
16:['xx+yy','xy+zx','xz+zy','xx+xz+yx','xy+xz+yz','zz+xxy'],
17:['xx+yy+xxy','xy+zx+xxy','xz+zy','xx+xz+yx','xy+xz+yz','zz+xxy'],
18:['xx+zy','xx+xz+zz','xy+xz+zx','xx+xz+yx','xz+yy','xx+xy+xz+yz','yzy','zyy'],
19:['xx+zy+xxx','xx+xz+zz','xy+xz+zx','xx+xz+yx','xz+yy','xx+xy+xz+yz','yzy','zyy'],
}

def xor_basis(rows):
    B={}
    for v in rows:
        a=v
        while a:
            i=a.bit_length()-1
            if i in B: a^=B[i]
            else:
                B[i]=a;break
    return B

def reduce(v,B):
    while v:
        i=v.bit_length()-1
        if i not in B: break
        v^=B[i]
    return v

def rref_reduce(v,B):
    # B rows echelon, reduce including nonpivot coordinate
    for i in sorted(B,reverse=True):
        if v>>i&1:v^=B[i]
    return v

# rank of linear equations over F2

def nullity(mats,n):
    # input row integer masks, ambient columns n
    return n-len(xor_basis(mats))


def run(k,rels):
    if k in D2:alphabet='xy'; D=4 if k<=6 else 3
    else:alphabet='xyz'; D=3
    words=['']+[ ''.join(t) for d in range(1,D+1) for t in product(alphabet,repeat=d)]
    index={w:i for i,w in enumerate(words)}
    def bitpoly(terms):
        v=0
        for x in terms.split('+'):
            assert x in index,(k,x)
            v^=(1<<index[x])
        return v
    rel={bitpoly(x) for x in rels}
    ideal=[]
    for r in rel:
        terms=[words[i] for i in range(len(words)) if r>>i&1]
        low=min(map(len,terms))
        for l in range(D-low+1):
            for p in product(alphabet,repeat=l):
                for rr in range(D-low-l+1):
                    for t in product(alphabet,repeat=rr):
                        lword=''.join(p);rword=''.join(t)
                        v=0
                        for w in terms:
                            ww=lword+w+rword
                            if len(ww)<=D:v^=1<<index[ww]
                        ideal.append(v)
    B=xor_basis(ideal)
    piv=set(B)
    basis=[i for i in range(len(words)) if i not in piv]
    dim=len(basis)
    def red(v):return rref_reduce(v,B)
    assert dim==8,(k,dim)
    # quotient basis coordinates
    def coords(v):
        v=red(v)
        assert v&sum((1<<i for i in piv),0)==0
        return sum((1<<j) for j,i in enumerate(basis) if v>>i&1)
    def multiply_vec(a,b):
        v=0
        for i in range(len(words)):
            if a>>i&1:
                for j in range(len(words)):
                    if b>>j&1:
                        s=words[i]+words[j]
                        if len(s)<=D:v^=1<<index[s]
        return red(v)
    bm=[1<<i for i in basis]
    xword={x:1<<index[x] for x in alphabet}
    # socle elements annihilated by x,y,z from L/R. equations for 8 input basis coords => out 8 coords each
    rows_left=[];rows_right=[]
    for x in alphabet:
        left=[coords(multiply_vec(xword[x],b)) for b in bm]
        right=[coords(multiply_vec(b,xword[x])) for b in bm]
        for i in range(8):
            rows_left.append(sum((1<<j) for j in range(8) if left[j]>>i&1))
            rows_right.append(sum((1<<j) for j in range(8) if right[j]>>i&1))
    socL=nullity(rows_left,8);socR=nullity(rows_right,8)
    socBi=nullity(rows_left+rows_right,8)
    # quotient J^D dimension compare
    return k,socL,socR,socBi,basis,[words[i] for i in basis]


def check(alphabet,D,rels):
    words=['']+[''.join(t) for d in range(1,D+1) for t in product(alphabet,repeat=d)]
    index={w:i for i,w in enumerate(words)}
    ideal=[]
    for rel in rels:
        ts=rel.split('+')
        mn=min(len(w) for w in ts)
        for a in range(D-mn+1):
          for pre in product(alphabet,repeat=a):
           for b in range(D-mn-a+1):
            for post in product(alphabet,repeat=b):
                v=0
                for w in ts:
                    x=''.join(pre)+w+''.join(post)
                    if len(x)<=D:v^=1<<index[x]
                ideal.append(v)
    B=xor_basis(ideal)
    nonp=[w for i,w in enumerate(words) if i not in B]
    assert len(nonp)==8,(len(nonp),nonp)
    assert all(all(len(w)==len(words[p]) for p in B if v>>p&1) for v in B.values() for w in [] )
    graded=[[w for w in nonp if len(w)==i] for i in range(D+1)]
    def redword(w):return rref_reduce(1<<index[w],B)
    # target top basis length 1
    assert len(graded[D])==1,(graded[D],)
    top_index=index[graded[D][0]]
    def rank_binary(mat):
       rows=[sum((x<<j) for j,x in enumerate(row)) for row in mat]
       return len(xor_basis(rows))
    rank_data=[]
    for i in range(1,D):
       matrix=[]
       for u in graded[i]:
         matrix.append([int((redword(u+v)>>top_index)&1) for v in graded[D-i]])
       r=rank_binary(matrix)
       rank_data.append((i,len(graded[i]),len(graded[D-i]),r,matrix))
    return list(map(len,graded)),rank_data



# Homogeneous graded presentations from the classification, Appendix A.
G=['xx+yy','xx+xy+yx','xxyy']
A=['xz+yx','xx+xz+yy','xy+yz','xy+xz+zx','xx+xy+zy','xx+zz']
B=['xz+yx','xx+xy+xz+yy','xy+yz','xy+xz+zx','xx+xy+zy','xx+zz']
C=['xx+xy+xz+yx','xx+xy+yy','xx+yz','xx+xy+zx','xx+xz+zy','xy+zz','xxy','xxx+xxz']
D=['xy+xz+yx','xx+xy+yy','xx+yz','xx+xy+zx','xx+xy+xz+zy','xy+zz','xxx+xxy','xxz']

def main():
    # Independent full characteristic-two local-algebra socle calculations.
    dims = {}
    for n, relations in {**D2,**D3}.items():
        _,sl,sr,sboth,_,_ = run(n,relations)
        assert sl == sr == sboth
        assert sboth == (2 if n == 7 else 1), (n,sl,sr,sboth)
        dims[n] = sboth
    assert len(dims) == 19 and sorted(dims)==list(range(1,20))
    print('CHARACTERISTIC_TWO_SOCLES_OK: 18 simple, ring 7 has dimension 2')

    # Degreewise perfect pairing with nonzero top degree over F2.
    models={'G':('xy',4,G),'A':('xyz',3,A),'B':('xyz',3,B),
            'C':('xyz',3,C),'D':('xyz',3,D)}
    for n in range(8,20):
        rel=[]
        for s in D3[n]:
            terms=s.split('+'); minimum=min(map(len, terms))
            rel.append('+'.join(w for w in terms if len(w)==minimum))
        models['char2_'+str(n)]=('xyz',3,rel)
    assert len(models)==17
    for label,(alphabet,Degree,relations) in models.items():
        hilbert,rank_data=check(alphabet,Degree,relations)
        expected=[1,2,2,2,1] if label=='G' else [1,3,3,1]
        assert hilbert == expected, (label,hilbert)
        for degree,nrows,ncols,rank,matrix in rank_data:
            assert nrows == ncols == rank, (label,degree,matrix)
        print(label, 'Hilbert',hilbert, 'top_pairing_ranks',
              [r[3] for r in rank_data])
    print('REVERSIBLE_256_SOCLE_CERTIFICATE_OK')

if __name__ == '__main__':
    main()
