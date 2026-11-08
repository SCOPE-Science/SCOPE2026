"""Exact-rational independent tests for bipartite two-distance Lipschitz variance.

Run: python bipartite_variance_checker.py
Requires Python 3 standard library only. Small finite tests complement, but do
not replace, the all-parameter mathematical proof.
"""
from fractions import Fraction as F
from itertools import combinations


def predicted_scalar(m, n, t):
    N = m+n
    def side(a,b):
        C=a*t+b*(2-t)
        return max((m*n*(t-1)**2 + z*(C-z)) for k in range(a+1)
                   for l in range(b+1) for z in [t*k+(2-t)*l]) / N**2
    return max(side(m,n),side(n,m))


def predicted_hilbert(m,n,t):
    m,n=max(m,n),min(m,n)
    N=m+n
    a=min(F(1),t*t*F(m-1,2*m))
    b=min(1-a,t*t*F(n-1,2*n))
    c=1-a-b
    return (m*a+n*b)/N + F(m*n,N*N)*c


def independent_polytope_vertices(m,n,t):
    """Enumerate all sets of d active signed distance constraints."""
    N=m+n; d=N-1
    pairs=[(i,j,t if (i<m)==(j<m) else F(1))
           for i in range(N) for j in range(i+1,N)]
    rows=[]
    for i,j,b in pairs:
        vector=tuple((1 if q==i else 0)-(1 if q==j else 0)
                     for q in range(1,N))
        rows.extend((vector,b*sign) for sign in (-1,1))
    def solve(sys):
        mat=[[F(v) for v in row]+[bound] for row,bound in sys]
        for q in range(d):
            p=next((r for r in range(q,d) if mat[r][q]), None)
            if p is None:return None
            mat[q],mat[p]=mat[p],mat[q]
            k=mat[q][q]
            for c in range(q,d+1):mat[q][c]/=k
            for r in range(q+1,d):
                k=mat[r][q]
                if k:
                    for c in range(q,d+1):mat[r][c]-=k*mat[q][c]
        x=[F(0)]*d
        for q in range(d-1,-1,-1):
            x[q]=mat[q][d]-sum(mat[q][c]*x[c] for c in range(q+1,d))
        return (F(0),*x)
    vertices=set()
    for active in combinations(rows,d):
        x=solve(active)
        if x is not None and all(abs(x[i]-x[j])<=b for i,j,b in pairs):
            vertices.add(x)
    values=[sum((v[i]-v[j])**2 for i in range(N) for j in range(i+1,N))/N**2
            for v in vertices]
    return vertices,max(values)


def independent_hilbert_lp(m,n,t):
    N=m+n
    A=t*t*F(m-1,2*m);B=t*t*F(n-1,2*n)
    lines=[(F(1),F(0),F(0)),(F(1),F(0),A),
           (F(0),F(1),F(0)),(F(0),F(1),B),
           (F(1),F(1),F(1))]
    candidates=[]
    for (a,b,e),(c,d,f) in combinations(lines,2):
        det=a*d-b*c
        if not det:continue
        x=(e*d-b*f)/det; y=(a*f-e*c)/det
        if 0<=x<=A and 0<=y<=B and x+y<=1:
            candidates.append((m*x+n*y)/N + F(m*n,N*N)*(1-x-y))
    return max(candidates)


def run():
    checked=0;vertices_total=0; lp=0
    for m,n in [(2,2),(3,2)]:
        for t in [F(1),F(3,2),F(2)]:
            V,opt=independent_polytope_vertices(m,n,t)
            assert opt==predicted_scalar(m,n,t),(m,n,t,opt,predicted_scalar(m,n,t))
            checked+=1;vertices_total+=len(V)
    print('INDEPENDENT_FULL_SIGNED_CONSTRAINT_VERTEX_MAXIMA_PASSED',checked)
    print('DISTINCT_EXACT_VERTICES_RECONSTRUCTED',vertices_total)
    for m in range(2,12):
        for n in range(2,10):
            for t in [F(1),F(11,10),F(6,5),F(4,3),F(3,2),F(7,4),F(2)]:
                H=independent_hilbert_lp(m,n,t)
                assert H==predicted_hilbert(m,n,t),(m,n,t,H,predicted_hilbert(m,n,t))
                assert predicted_scalar(m,n,t)<=H
                if t<2:assert predicted_scalar(m,n,t)<H
                lp+=1
    print('INDEPENDENT_HILBERT_LINEAR_PROGRAM_VERTEX_CHECKS_PASSED',lp)
    for m in range(2,14):
        for n in range(2,14):
            t=F(2);big=max(m,n);N=m+n
            assert predicted_hilbert(m,n,t)==F(big,N)
            assert predicted_hilbert(m,n,t)-predicted_scalar(m,n,t)==F(big%2,N*N)
    print('GRAPH_ENDPOINT_PARITY_IDENTITIES_PASSED',12*12)
    for r in range(2,22,2):
        for t in [F(1),F(7,6),F(3,2),F(2)]:
            assert predicted_scalar(r,r,t)==(1+(t-1)**2)/4
    print('BALANCED_EVEN_PART_SCALAR_CURVES_PASSED',40)
    print('ALL_BIPARTITE_VARIANCE_DIAGNOSTICS_PASSED')

if __name__=='__main__':run()
