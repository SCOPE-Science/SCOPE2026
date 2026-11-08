"""Direct finite-field checks for idempotent Nijenhuis operators on almost-abelian Lie algebras.
Run: python check.py. Standard library only. The original torsion identity is evaluated on all basis pairs."""
from itertools import product
from collections import Counter


def span(gens, q, m):
    acc = {(0,) * m}
    for v in gens:
        acc = {tuple((a[i]+c*v[i]) % q for i in range(m)) for a in acc for c in range(q)}
    return frozenset(acc)


def subspaces(q, m):
    vectors = list(product(range(q), repeat=m))
    return set(span(gens, q, m) for gens in product(vectors, repeat=m))


def matvec(A, v, q):
    return tuple(sum(a*x for a,x in zip(row, v)) % q for row in A)


def space_rank(S, q):
    d=0
    s=len(S)
    while s>1:
        assert s%q == 0
        s//=q
        d+=1
    assert s==1
    return d


def formula_counts(q, A):
    m=len(A)
    spaces=subspaces(q,m)
    zero=(0,)*m
    by_dim=Counter()
    spaces_by_dim={i:[] for i in range(m+1)}
    for S in spaces:
        if all(matvec(A,v,q) in S for v in S):
            d=space_rank(S,q)
            by_dim[d]+=1
            spaces_by_dim[d].append(S)
    N={}
    for r in range(m+2):
        I1=by_dim[m-r] if 0<=m-r<=m else 0
        I2=by_dim[r-1] if 0<=r-1<=m else 0
        D=0
        if 1<=r<=m:
            for W in spaces_by_dim[r-1]:
                for K in spaces_by_dim[m-r]:
                    if W.intersection(K)=={zero}:
                        D+=1
        N[r]=q**(r*(m-r+1))*(I1+I2) if 0<=r<=m+1 else 0
        if 1<=r<=m:
            N[r]+=(q-1)*q**m*D
    return N


def rank(rows,q):
    rows=[list(row) for row in rows]
    R=0; cols=len(rows[0])
    for j in range(cols):
        pivot=next((i for i in range(R,len(rows)) if rows[i][j]),None)
        if pivot is None:continue
        rows[R],rows[pivot]=rows[pivot],rows[R]
        inv=pow(rows[R][j],-1,q)
        rows[R]=[(x*inv)%q for x in rows[R]]
        for i in range(len(rows)):
            if i!=R:
                f=rows[i][j]
                if f: rows[i]=[(u-f*v)%q for u,v in zip(rows[i],rows[R])]
        R+=1
        if R==len(rows):break
    return R


def direct_counts(q,A):
    m=len(A); n=m+1
    vectors=list(product(range(q),repeat=n))
    basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    def bracket(x,y):
        Ax=matvec(A,x[1:],q)
        Ay=matvec(A,y[1:],q)
        return (0,)+tuple((x[0]*Ay[i]-y[0]*Ax[i])%q for i in range(m))
    brackets={(i,j):bracket(basis[i],basis[j]) for i in range(n) for j in range(i+1,n)}
    C=Counter()
    for columns in product(vectors,repeat=n):
        def apply(v):
            return tuple(sum(v[j]*columns[j][i] for j in range(n))%q for i in range(n))
        if any(apply(columns[i]) != columns[i] for i in range(n)):
            continue
        for i,j in brackets:
            left=bracket(columns[i],columns[j])
            a=bracket(columns[i],basis[j]);b=bracket(basis[i],columns[j]);c=apply(brackets[i,j])
            inner=tuple((a[h]+b[h]-c[h])%q for h in range(n))
            if left!=apply(inner):break
        else:
            rows=[[columns[j][i] for j in range(n)] for i in range(n)]
            C[rank(rows,q)]+=1
    return dict(C)


def main():
    cases=[
        (2, ((1,0),(0,1)), 'scalar m2'),
        (2, ((1,1),(0,1)), 'Jordan m2'),
        (2, ((0,1),(1,1)), 'irreducible m2'),
        (3, ((1,0),(0,2)), 'split squarefree m2'),
        (2, ((1,0,0),(0,1,0),(0,0,1)), 'scalar m3'),
        (2, ((1,1,0),(0,1,1),(0,0,1)), 'Jordan m3'),
        (2, ((0,1,0),(0,0,1),(1,1,0)), 'irreducible m3'),
    ]
    for q,A,label in cases:
        predicted=formula_counts(q,A)
        observed=direct_counts(q,A)
        assert all(predicted[r]==observed.get(r,0) for r in predicted),(label,predicted,observed)
        print(f'{label} GF({q}): rank spectrum {dict(sorted(observed.items()))}; total {sum(observed.values())}; PASS')
    print('ALMOST_ABELIAN_NIJENHUIS_DIRECT_TORSION_OK')

if __name__=='__main__':main()
