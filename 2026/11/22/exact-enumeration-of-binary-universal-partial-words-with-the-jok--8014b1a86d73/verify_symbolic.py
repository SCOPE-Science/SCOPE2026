"""Exact symbolic overlap/matrix-tree calculation for binary third-position upwords.

Requires Python 3 and sympy. All arithmetic is rational/integer.
The mathematical argument establishing the bulk-overlap period is in RESULT.md.
"""
from sympy import Matrix, Rational, Symbol, factor, simplify

TRIPLES = [(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0)]


def make_edges(n, abc):
    r = n - 1
    a,b,c = abc
    tail = tuple(abc[i % 3] for i in range(r))
    p = (a,b,None) + tail
    edges = []
    for i in range(3):
        for bit in (0,1):
            edges.append(int(''.join(str(bit if k is None else k)
                                     for k in p[i:i+n]), 2))
    assert len(set(edges)) == 6
    V = 1 << r
    start = int(''.join(map(str,tail)),2)
    root = int(''.join(map(str,(a,b,1-c)+tail[:r-3])),2)
    return [e >> 1 for e in edges], [e & (V-1) for e in edges], start, root


def overlap_h(a,b,r):
    return sum(1 << (length-1) for length in range(1,r+1)
               if (a & ((1<<length)-1)) == (b >> (r-length)))


def q_matrix(n,abc):
    r=n-1
    u,v,s,t=make_edges(n,abc)
    return Matrix(6,6,lambda i,j: (
        overlap_h(u[i],u[j],r)-overlap_h(v[i],u[j],r)
        -overlap_h(u[i],t,r)+overlap_h(v[i],t,r))) / (1<<r)


def expected_per_class(residue, kind, X):
    table = {
        0: [(1+2*X)*(1-4*X)/28, (1-4*X)/28,
            (1-2*X)*(1-4*X)/28],
        1: [(1-8*X*X)/28, (1+6*X)/28,
            (1-2*X+8*X*X)/28],
        2: [(1-2*X)*(1+4*X)/28, (1-2*X)/28,
            (1+8*X+8*X*X)/28]}
    return table[residue][kind]


def main():
    X=Symbol('X')
    for residue in range(3):
        n0=next(n for n in range(9,12) if n%3==residue)
        total=0
        for index,abc in enumerate(TRIPLES):
            q0=q_matrix(n0,abc)
            q1=q_matrix(n0+3,abc)
            x0=Rational(1,2**(n0-1));x1=Rational(1,2**(n0+2))
            B=(q0-q1)/(x0-x1)
            A=q0-B*x0
            # Extra sizes test the periodic-overlap consequence. The proof
            # of this consequence is separate from finite test evidence.
            for n in [n0+6,n0+9]:
                assert q_matrix(n,abc)==A+B*Rational(1,2**(n-1))
            expr=factor((Matrix.eye(6)-A-B*X).det(method='domain-ge'))
            kind=[0,1,2,2,1,0][index]
            assert simplify(expr-expected_per_class(residue,kind,X))==0
            total+=expr
        want={0:(3-12*X)/14,1:(3+4*X)/14,2:(3+8*X)/14}[residue]
        assert simplify(total-want)==0
        for n in range(6,9):
            if n%3==residue:
                x=Rational(1,2**(n-1))
                for index,abc in enumerate(TRIPLES):
                    expr=(Matrix.eye(6)-q_matrix(n,abc)).det(method='domain-ge')
                    kind=[0,1,2,2,1,0][index]
                    assert simplify(expr-expected_per_class(residue,kind,x))==0
        print(f'congruence class {residue}: six determinant identities verified')
    print('ALL exact symbolic determinant checks passed')

if __name__=='__main__': main()
