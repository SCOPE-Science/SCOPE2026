"""Exact integral homology-lattice obstruction for a finite multiple chessboard complex.

Usage: python3 verify.py; requires only Python 3 standard library.
Each orientation and row/column labeling is fixed in RESULT.md.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, factorial
import json

N = 6
R = 4


def words_of_rooks():
    return [w for w in product(range(R), repeat=N)
            if max(Counter(w).values()) <= 2]


def integral_kernel(row_equations, num_columns, require_unit=True):
    """Exact rational row elimination with a certified integral kernel basis.

    If require_unit, each pivot must be +/-1. Otherwise test integrality
    of all free-coordinate basis vectors: then these form the whole Z-kernel.
    """
    pivots = {}
    nonzero_rows = 0
    for initial in row_equations:
        row = {k: Fraction(v) for k, v in initial.items() if v}
        while row:
            k = max(row)
            if k in pivots:
                q = row[k]
                for j, v in pivots[k].items():
                    t = row.get(j, 0) - q*v
                    if t:
                        row[j] = t
                    else:
                        row.pop(j, None)
            else:
                coefficient = row[k]
                if require_unit:
                    assert abs(coefficient) == 1, (k, coefficient)
                row = {j: v/coefficient for j, v in row.items()}
                pivots[k] = row
                nonzero_rows += 1
                break
    free = sorted(set(range(num_columns)) - set(pivots))
    basis = []
    for q in free:
        vector = {q: 1}
        for k in sorted(pivots):
            v = -sum(c*vector.get(j, 0) for j, c in pivots[k].items() if j != k)
            if v:
                vector[k] = v
        basis.append(vector)
    assert all(x.denominator==1 for v in basis for x in v.values())
    basis=[{j: int(x) for j,x in v.items()} for v in basis]
    assert all(sum(row.get(j, 0)*v.get(j, 0) for j in row) == 0
               for row in row_equations for v in basis)
    return pivots, free, basis


def matrix_automorphism(free, basis, object_list, index, permute, coefficient):
    M = [[0]*len(free) for _ in free]
    for column, vector in enumerate(basis):
        transformed = defaultdict(int)
        for old_id, value in vector.items():
            x = permute(object_list[old_id])
            transformed[index[x]] += coefficient*value
        for row, idx in enumerate(free):
            M[row][column] = transformed[idx]
    return M


def mmult(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]


def mtrace(A):
    return sum(A[i][i] for i in range(len(A)))


def mdiff(A, B):
    return [[a-b for a,b in zip(row1,row2)] for row1,row2 in zip(A,B)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def rational_nullspace(E, n):
    mat = [[Fraction(x) for x in row] for row in E]
    pivot_columns = []
    pivot_rows = []
    row = 0
    for col in range(n):
        first = next((i for i in range(row,len(mat)) if mat[i][col]), None)
        if first is None:
            continue
        mat[row],mat[first] = mat[first],mat[row]
        lead = mat[row][col]
        mat[row] = [x/lead for x in mat[row]]
        for i in range(len(mat)):
            if i==row or not mat[i][col]:
                continue
            factor = mat[i][col]
            mat[i] = [a-factor*b for a,b in zip(mat[i],mat[row])]
        pivot_columns.append(col)
        pivot_rows.append(row)
        row += 1
    free = sorted(set(range(n))-set(pivot_columns))
    basis = []
    for f in free:
        vector = [Fraction(0)]*n
        vector[f] = Fraction(1)
        for col,r in zip(pivot_columns,pivot_rows):
            vector[col] = -mat[r][f]
        basis.append(vector)
    assert all(sum(Fraction(e)*v for e,v in zip(eq,vec)) == 0
               for eq in E for vec in basis)
    return len(pivot_columns), basis


def det_int(A):
    n=len(A)
    if n==1: return A[0][0]
    if n==2: return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return sum((-1)**j*A[0][j]*det_int([row[:j]+row[j+1:] for row in A[1:]])
               for j in range(n))


def smith_from_minors(A):
    n=len(A)
    divisors=[1]
    for k in range(1,n+1):
        d=0
        for ii in combinations(range(n), k):
            for jj in combinations(range(n), k):
                d=gcd(d,det_int([[A[i][j] for j in jj] for i in ii]))
        assert d>0
        divisors.append(d)
    invariant=[divisors[i]//divisors[i-1] for i in range(1,n+1)]
    assert all(divisors[i]%divisors[i-1]==0 for i in range(1,n+1))
    assert all(invariant[i+1]%invariant[i]==0 for i in range(n-1))
    return invariant


def main():
    words=words_of_rooks()
    assert len(words)==1440
    iw={w:i for i,w in enumerate(words)}
    face_equations=defaultdict(dict)
    for k,word in enumerate(words):
        for column in range(N):
            face=word[:column]+(-1,)+word[column+1:]
            face_equations[face][k]=(-1)**column
    assert len(face_equations)==3600
    rows=list(face_equations.values())
    pivots, free, K=integral_kernel(rows,len(words))
    assert len(pivots)==1435 and free==[0,4,54,58,90]
    assert [len(b) for b in K]==[768,576,576,576,576]

    triples=list(combinations(range(N),3))
    pairs=list(combinations(range(N),2))
    it={x:i for i,x in enumerate(triples)}
    incidence=[{it[T]:1 for T in triples if set(P).issubset(T)} for P in pairs]
    w_piv,w_free,L=integral_kernel(incidence,len(triples),require_unit=False)
    assert len(w_piv)==15 and w_free==[0,1,2,4,5]

    S=[tuple(i+1 if j==i else i if j==i+1 else j for j in range(N))
       for i in range(N-1)]
    C=[matrix_automorphism(free,K,words,iw,lambda w,s=s: tuple(w[s[j]] for j in range(N)),-1)
       for s in S]
    D=[matrix_automorphism(w_free,L,triples,it,
                           lambda T,s=s: tuple(sorted(s[j] for j in T)),1)
       for s in S]
    id5=[[int(i==j) for j in range(5)] for i in range(5)]
    for seq in (C,D):
        assert all(mmult(M,M)==id5 for M in seq)
        assert all(mmult(seq[i],seq[j])==mmult(seq[j],seq[i])
                   for i in range(5) for j in range(5) if abs(i-j)>1)
        assert all(mmult(mmult(seq[i],seq[i+1]),seq[i]) ==
                   mmult(mmult(seq[i+1],seq[i]),seq[i+1]) for i in range(4))

    for a in range(R-1):
        rs={a:a+1,a+1:a}
        action=matrix_automorphism(free,K,words,iw,
                lambda w,rs=rs: tuple(rs.get(i,i) for i in w),1)
        assert action==id5

    eqs=[]
    for c,d in zip(C,D):
        for i in range(5):
            for j in range(5):
                eq=[0]*25
                for k in range(5):
                    eq[5*k+j]+=c[i][k]
                    eq[5*i+k]-=d[k][j]
                eqs.append(eq)
    rank,basis=rational_nullspace(eqs,25)
    assert rank==24 and len(basis)==1
    vec=basis[0]
    den=lcm(*(x.denominator for x in vec))
    integers=[int(x*den) for x in vec]
    g=gcd(*integers)
    q=[x//g for x in integers]
    # Sign is immaterial for the index; fix q's first entry positive.
    if q[0]<0:q=[-v for v in q]
    Q=[q[i*5:(i+1)*5] for i in range(5)]
    expectedQ=[[3,1,2,2,4],[-3,-2,-1,-4,-2],[-3,-2,-4,-1,-2],
               [3,4,2,2,1],[-3,-2,-1,-1,1]]
    assert Q==expectedQ
    assert all(mmult(c,Q)==mmult(Q,d) for c,d in zip(C,D))
    assert det_int(Q)==-162
    snf=smith_from_minors(Q)
    assert snf==[1,3,3,3,6]
    assert gcd(*q)==1
    assert [mtrace(c) for c in C]==[1]*5
    assert [mtrace(d) for d in D]==[1]*5
    result={
        'status':'PASS',
        'complex':'four rows, six columns, row capacities (2,2,2,2)',
        'facets':len(words),
        'facets_with_one_column_deleted':len(face_equations),
        'top_boundary_unit_pivots':len(pivots),
        'top_kernel_rank':len(K),
        'top_kernel_free_column_indices':free,
        'row_adjacent_transpositions_act_trivially':True,
        'column_adjacent_transposition_traces':[mtrace(x) for x in C],
        'column_generator_matrices':C,
        'incidence_kernel_rank':len(L),
        'incidence_free_column_indices':w_free,
        'incidence_generator_matrices':D,
        'equivariance_constraint_rank':rank,
        'primitive_intertwiner':Q,
        'intertwiner_determinant':det_int(Q),
        'intertwiner_smith_diagonal':snf,
        'minimal_nonzero_equivariant_index':abs(det_int(Q))
    }
    print(json.dumps(result,indent=2,separators=(',',': ')))

if __name__=='__main__':
    main()
