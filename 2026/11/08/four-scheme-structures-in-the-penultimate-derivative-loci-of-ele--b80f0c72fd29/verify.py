#!/usr/bin/env python3
"""Exact finite-field checks for quadratic derivative-ideal normal forms.
All calculations use Python integers and modular elimination. Finite checks
corroborate but do not replace the characteristic-independent written proof.
"""
from itertools import combinations, product
from math import comb


def rref_rank(rows, p):
    rows = [[z % p for z in row] for row in rows]
    if not rows:
        return 0
    ncol = len(rows[0]); i = 0
    for j in range(ncol):
        k = next((k for k in range(i, len(rows)) if rows[k][j]), None)
        if k is None: continue
        rows[i], rows[k] = rows[k], rows[i]
        a = pow(rows[i][j], -1, p)
        rows[i] = [(z*a) % p for z in rows[i]]
        for k in range(len(rows)):
            if k != i and rows[k][j]:
                b = rows[k][j]
                rows[k] = [(u-b*v)%p for u,v in zip(rows[k], rows[i])]
        i += 1
        if i == len(rows): break
    return i


def rank_and_containment(A, B, p):
    return rref_rank(A,p)==rref_rank(B,p)==rref_rank(A+B,p)


def expected_case(L, p):
    c = comb(L+1, 2) % p
    if L % p:
        return 'axes' if c else 'axes_diagonal'
    return 'quadratic_double' if c else 'star_planes'


def quad_vectors(n, r, p):
    m=n-1; vars_ = list(range(n)) # y_0,...,y_(m-1), t at index m
    monoms = list(combinations(range(n), 2)) + [(i,i) for i in range(n)]
    # canonicalize unordered quadratic monomial indices
    monoms = sorted(monoms)
    mid = {pair:i for i,pair in enumerate(monoms)}
    def monomial(u,v):
        z=[0]*len(monoms)
        z[mid[tuple(sorted((u,v)))]] = 1
        return z
    def make(terms):
        z=[0]*len(monoms)
        for a,b,w in terms:
            z[mid[tuple(sorted((a,b)))]]+=w
        return [t%p for t in z]
    # x_i=y_i+t for i<n, x_(n-1)=t
    def x_pair(i,j):
        if i==m: return make([(j,m,1),(m,m,1)])
        if j==m: return make([(i,m,1),(m,m,1)])
        return make([(i,j,1),(i,m,1),(j,m,1),(m,m,1)])
    xs={(i,j):x_pair(i,j) for i,j in combinations(range(n),2)}
    rows=[]
    for U in combinations(range(n),r):
        row=[0]*len(monoms)
        for i,j in combinations(U,2):
            row=[(a+b)%p for a,b in zip(row,xs[i,j])]
        rows.append(row)
    case=expected_case(r-1,p)
    pairs=list(combinations(range(m),2))
    if case=='axes': expected=list(xs.values())
    elif case=='axes_diagonal':
        base=next(iter(xs.values()))
        expected=[[(a-b)%p for a,b in zip(v,base)] for v in xs.values()]
    else:
        base=monomial(*pairs[0]);expected=[[(a-b)%p for a,b in zip(monomial(*ij),base)] for ij in pairs]
        if case=='quadratic_double':expected.append(make([(m,m,1),(*pairs[0],1)]))
    return case,rows,expected


def test_support(n,L,p,case):
    r=L+1; axes=lambda a:sum(a_i!=0 for a_i in a)<=1
    diag=lambda a:len(set(a))==1
    def star(a): return any(len(set(a[:i]+a[i+1:]))==1 for i in range(n))
    for a in product(range(p),repeat=n):
        equations=all(sum(a[i]*a[j] for i,j in combinations(U,2))%p==0 for U in combinations(range(n),r))
        predicted=(axes(a) if case in ('axes','quadratic_double') else
                   axes(a) or diag(a) if case=='axes_diagonal' else star(a))
        assert equations==predicted,(n,L,p,case,a,equations,predicted)


def main():
    count=0;profiles={}; support=0
    for n in range(4,11):
      for r in range(2,n-1):
        L=r-1
        for p in (2,3,5,7):
          case,rows,expected=quad_vectors(n,r,p)
          assert rank_and_containment(rows,expected,p),(n,r,p,case)
          count+=1; profiles[case]=profiles.get(case,0)+1
          if n<=7 and p<=3:
              test_support(n,L,p,case);support+=1
    assert set(profiles)=={'axes','axes_diagonal','quadratic_double','star_planes'}
    print('QUADRATIC_IDEAL_SPAN_EQUALITIES_OK',count)
    print('FINITE_FIELD_SUPPORT_CHECKS_OK',support)
    print('ALL_FOUR_CASES_COVERED', sorted(profiles.items()))
    print('CERTIFICATE_OK')

if __name__=='__main__':main()
