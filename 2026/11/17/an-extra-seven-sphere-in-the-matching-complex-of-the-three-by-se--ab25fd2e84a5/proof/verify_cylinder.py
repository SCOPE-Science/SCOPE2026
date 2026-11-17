#!/usr/bin/env python3
"""Exact integral discrete-Morse verification for M(P_3 square C_7).

Pure Python 3.10+; no nonstandard dependencies.  All arithmetic is integral.
Run from the enclosing research directory with:
    python3 proof/verify_cylinder.py
"""
import collections
import csv
from collections import deque
from pathlib import Path

N = 7
ORDER_A = [34, 22, 17, 32, 7, 28, 33, 19, 1, 14, 29, 12, 25, 20, 9, 27,
           3, 13, 6, 26, 8, 30, 10, 11, 23, 24, 15, 18, 21, 4, 0, 2, 16, 31, 5]
ORDER_B = [18, 34, 0, 1, 16, 11, 13, 27, 26, 31, 32, 22, 4, 19, 5, 10, 7,
           29, 3, 20, 12, 25, 24, 28, 14, 21, 2, 30, 9, 8, 23, 17, 15, 33, 6]
EXPECTED_F_VECTOR = (1,35,511,4060,19222,55867,99085,103231,58310,15267,1274)
EXPECTED_COVERS = 2303210


def graph_edges():
    vertex = lambda r,c: r*N+c
    edges=set()
    for col in range(N):
        for row in range(2):
            edges.add(tuple(sorted((vertex(row,col),vertex(row+1,col)))))
        for row in range(3):
            edges.add(tuple(sorted((vertex(row,col),vertex(row,(col+1)%N)))))
    out=sorted(edges)
    assert len(out)==35 and len(set(out))==35
    return out


def enumerate_faces(edges):
    vertex_sets=[(1<<u)|(1<<v) for u,v in edges]
    faces=[(0,0)]
    for index, occupied_by_edge in enumerate(vertex_sets):
        selected=1<<index
        extension=[(f|selected,used|occupied_by_edge)
                   for f,used in faces if not (used & occupied_by_edge)]
        faces.extend(extension)
    F={f for f,_ in faces}
    assert len(F)==len(faces)
    counter=collections.Counter(s.bit_count() for s in F)
    fvector=tuple(counter.get(k,0) for k in range(11))
    assert fvector==EXPECTED_F_VECTOR
    return F,fvector


def lex_morse_matching(F,order):
    unmatched=set(F)
    low_to_high={}
    for pivot in order:
        bit=1<<pivot
        chosen=[]
        for low in unmatched:
            if not low & bit and (low|bit) in unmatched:
                high=low|bit
                low_to_high[low]=high
                chosen.extend((low,high))
        unmatched.difference_update(chosen)
    assert 2*len(low_to_high)+len(unmatched)==len(F)
    return low_to_high, unmatched


def verify_gradient_acyclic(F,pair,edge_count):
    """Check every cover in augmented Hasse graph: matched up, others down."""
    indeg={s:0 for s in F}
    covers=0
    for s in F:
        bits=s
        while bits:
            b=bits&-bits
            low=s^b
            covers+=1
            if pair.get(low)==s:
                indeg[s]+=1
            else:
                indeg[low]+=1
            bits-=b
    assert covers==EXPECTED_COVERS
    pending=deque(s for s,d in indeg.items() if d==0)
    visited=0
    while pending:
        s=pending.popleft()
        visited+=1
        bits=s
        while bits:
            b=bits&-bits
            low=s^b
            if pair.get(low)!=s:
                indeg[low]-=1
                if indeg[low]==0:pending.append(low)
            bits-=b
        if s in pair:
            high=pair[s]
            indeg[high]-=1
            if indeg[high]==0:pending.append(high)
    assert visited==len(F)
    return covers


def incidence(high,bit):
    """Coefficient of the deleted-bit face in the oriented simplicial boundary."""
    return -1 if ((high & (bit-1)).bit_count()&1) else 1


def morse_boundary(pair,crit,edge_count):
    """Compute the exact critical degree-7 -> degree-6 boundary by gradient recursion."""
    upper=set(pair.values())
    degree6=sorted(s for s in crit if s.bit_count()==7)
    degree7=sorted(s for s in crit if s.bit_count()==8)
    assert all(s.bit_count() in (7,8) for s in crit)
    index={s:i for i,s in enumerate(degree6)}
    cache={}
    active=set()

    def project(a):
        if a in cache:return cache[a]
        if a in active:raise AssertionError('Gradient cycle in projection')
        if a in index:
            out={index[a]:1}
        elif a in upper:
            # This six-cell is the UPPER member of a lower-dimensional pair.
            out={}
        else:
            assert a in pair and pair[a].bit_count()==8
            high=pair[a]
            bit=high^a
            eps=incidence(high,bit)
            active.add(a)
            accum=collections.defaultdict(int)
            others=high^bit
            while others:
                other_bit=others&-others
                other_face=high^other_bit
                coeff=-eps*incidence(high,other_bit)
                for k,weight in project(other_face).items():
                    accum[k]+=coeff*weight
                others-=other_bit
            active.remove(a)
            out={k:v for k,v in accum.items() if v}
        cache[a]=out
        return out

    matrix=[]
    for top in degree7:
        row=[0]*len(degree6)
        bits=top
        while bits:
            bit=bits&-bits
            sign=incidence(top,bit)
            for i,v in project(top^bit).items():row[i]+=sign*v
            bits-=bit
        matrix.append(row)
    return degree6,degree7,matrix,len(cache)


def unit_pivot_reduction(M):
    """Integral unimodular row/column elimination using *only* unit pivots."""
    A=[row[:] for row in M]
    rows=len(A);cols=len(A[0])
    pivots=0
    for k in range(min(rows,cols)):
        found=next(((i,j) for i in range(k,rows) for j in range(k,cols)
                    if abs(A[i][j])==1),None)
        if found is None:break
        i,j=found
        A[i],A[k]=A[k],A[i]
        for row in A:row[k],row[j]=row[j],row[k]
        sign=A[k][k]
        assert sign in (-1,1)
        for i in range(k+1,rows):
            weight=A[i][k]
            if weight:
                for j in range(k,cols):A[i][j]-=weight*sign*A[k][j]
        for j in range(k+1,cols):
            weight=A[k][j]
            if weight:
                for i in range(k,rows):A[i][j]-=weight*sign*A[i][k]
        assert all(A[i][k]==0 for i in range(k+1,rows))
        assert all(A[k][j]==0 for j in range(k+1,cols))
        pivots+=1
    remaining=[A[i][j] for i in range(pivots,rows) for j in range(pivots,cols)]
    assert all(v==0 for v in remaining)
    assert pivots in (40,41)
    return pivots


def main():
    edges=graph_edges()
    F,fvector=enumerate_faces(edges)
    print('graph_vertices=21 graph_edges=35')
    print(f'augmented_face_count={len(F)} f_vector={",".join(map(str,fvector))}')
    print('reduced_euler=',-sum((-1)**k*x for k,x in enumerate(fvector)))
    assert sum((-1)**k*x for k,x in enumerate(fvector))==-57
    for name,order,expected_crit in [
        ('A',ORDER_A,(99,42)),('B',ORDER_B,(98,41))]:
        pair,crit=lex_morse_matching(F,order)
        covers=verify_gradient_acyclic(F,pair,len(edges))
        # Critical augmented faces only in cardinalities 7 and 8.
        C6,C7,B,expanded=morse_boundary(pair,crit,len(edges))
        assert (len(C6),len(C7))==expected_crit
        pivots=unit_pivot_reduction(B)
        assert len(C6)-pivots==58 and len(C7)-pivots==1
        assert not (0 in crit)
        # Unpair the empty face and its vertex to get one ordinary critical 0-cell.
        assert 0 in pair and pair[0].bit_count()==1
        if name=='A':
            f=Path(__file__).parent/'morse_boundary_A_42x99.csv'
            with f.open(newline='',encoding='utf-8') as inp:
                stored=[[int(v) for v in row] for row in csv.reader(inp)]
            assert stored==B,'The packaged signed Morse matrix differs'
        print(f'matching_{name}: pairs={len(pair)} critical_degree6={len(C6)} '
              f'critical_degree7={len(C7)} covers={covers} topological_sort={len(F)} '
              f'integral_unit_pivots={pivots} zeros={len(C7)-pivots} '
              f'projected_degree6_faces={expanded}')
    print('verified_integral_homotopy=wedge(58,S^6) vee S^7')

if __name__=='__main__':main()
