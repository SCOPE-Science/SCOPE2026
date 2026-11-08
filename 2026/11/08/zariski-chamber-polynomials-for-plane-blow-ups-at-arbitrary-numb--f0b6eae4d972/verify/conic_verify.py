#!/usr/bin/env python3
"""Exact finite checks for the chamber-support formula on conic-point blowups.

Uses only the Python standard library. Infinite-family assertions require the
symbolic Bézout/genus and combinatorial proof given separately.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def line_families(m):
    """Generate all subsets of edges of K_m with pairwise common endpoints.

    This backtracking uses edge compatibility, not the star/triangle formula.
    """
    edges = tuple(combinations(range(m), 2))
    result = []
    def visit(start, chosen):
        result.append(tuple(chosen))
        for i in range(start, len(edges)):
            e = edges[i]
            if all((e[0] in f or e[1] in f) for f in chosen):
                chosen.append(e)
                visit(i + 1, chosen)
                chosen.pop()
    visit(0, [])
    return result


def edge_formula(m):
    if m == 0:
        return [1]
    counts = [0] * (m + 1)
    counts[0] = 1
    for j in range(1, m):
        counts[j] = m * comb(m - 1, j)
    if m >= 2:
        counts[1] -= comb(m, 2)
    if m >= 3:
        counts[3] += comb(m, 3)
    return counts


def polynomial(n):
    no_c = Counter()
    yes_c = Counter()
    for m in range(n + 1):
        for j, number in enumerate(edge_formula(m)):
            no_c[n - m + j] += comb(n, m) * number
            if m >= 5:
                yes_c[n - m + j + 1] += comb(n, m) * number
    return no_c, yes_c


def minors_negative(matrix):
    """Exact negative definiteness via positive leading principal minors of -M."""
    size = len(matrix)
    # LDL^T without pivoting on -M, checking every pivot positive.
    L = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    diag = []
    for i in range(size):
        for j in range(i):
            rhs = Fraction(-matrix[i][j])
            rhs -= sum(L[i][k]*L[j][k]*diag[k] for k in range(j))
            L[i][j] = rhs / diag[j]
        pivot = Fraction(-matrix[i][i])
        pivot -= sum(L[i][k]**2*diag[k] for k in range(i))
        if pivot <= 0:
            return False
        diag.append(pivot)
        L[i][i] = 1
    return True


def geometry_matrix_support(n, selected_e, line_family, selected_c):
    curves = [('E',i) for i in selected_e]
    curves += [('L',e) for e in line_family]
    if selected_c:
        curves += [('C',None)]
    mat=[]
    for typ,x in curves:
        row=[]
        for typ2,y in curves:
            if typ == 'E' and typ2 == 'E': row.append(-int(x==y))
            elif typ == 'E' and typ2 == 'L': row.append(int(x in y))
            elif typ == 'L' and typ2 == 'E': row.append(int(y in x))
            elif typ == 'L' and typ2 == 'L': row.append(-1 if x == y else 1-len(set(x)&set(y)))
            elif typ == 'C' and typ2 == 'C': row.append(4-n)
            elif typ == 'C' and typ2 == 'E': row.append(1)
            elif typ == 'E' and typ2 == 'C': row.append(1)
            else:row.append(0)
        mat.append(row)
    return mat


def count_by_geometry(n, check_matrices=False):
    finite=Counter()
    infinite=Counter()
    allsets=set(range(n))
    for t in range(n+1):
        for points in combinations(range(n),t):
            remaining = tuple(sorted(allsets.difference(points)))
            for family in line_families(len(remaining)):
                actual_family = tuple((remaining[i],remaining[j]) for i,j in family)
                finite[t+len(family)] +=1
                if check_matrices:
                    assert minors_negative(geometry_matrix_support(n,points,actual_family,False))
                if t < n-4:
                    infinite[t+len(family)+1] +=1
                    if check_matrices:
                        assert minors_negative(geometry_matrix_support(n,points,actual_family,True))
                elif check_matrices and len(family)==0:
                    assert not minors_negative(geometry_matrix_support(n,points,actual_family,True))
    return finite,infinite


def abbreviated(C):
    return tuple(C[j] for j in range(max(C,default=0)+1))


def main():
    for m in range(0,12):
        actual=Counter(map(len,line_families(m)))
        assert dict(actual)=={j:c for j,c in enumerate(edge_formula(m)) if c}
    print('EDGE_FAMILIES_DIRECT_OK m=0..11')
    for n in range(7,11):
        expected = polynomial(n)
        actual = count_by_geometry(n, check_matrices=(n==7))
        assert actual == expected, (n,actual,expected)
        print('GEOMETRY_COUNTS_OK',n,sum(actual[0].values()),sum(actual[1].values()),
              abbreviated(actual[0]),abbreviated(actual[1]))
    for n in range(7,20):
        a,b=polynomial(n)
        total=sum(a.values())+sum(b.values())
        total_via_closed=(
          2*(2**n+n*3**(n-1)-n*2**(n-1)-comb(n,2)*2**(n-2)+comb(n,3)*2**(n-3))
          -sum(comb(n,m)*sum(edge_formula(m)) for m in range(5))
        )
        assert total==total_via_closed
    print('CLOSED_FORM_OK n=7..19')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':main()
