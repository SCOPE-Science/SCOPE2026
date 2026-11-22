"""Checks the finite-field involution census for cubic truncated symmetric algebras.
No external dependencies; binary and quartic extension fields are supported.
"""
from itertools import product
from math import prod


def mul(a,b,q):
    if q==2: return a&b
    assert q==4
    out=0
    while b:
        if b&1: out ^= a
        b >>= 1
        a <<= 1
        if a&4: a ^= 7  # x^2+x+1
    return out

def linear_rank(mat,q):
    a=[list(r) for r in mat]
    rows=len(a); cols=len(a[0]) if rows else 0
    r=0
    for j in range(cols):
        k=next((k for k in range(r,rows) if a[k][j]),None)
        if k is None: continue
        a[k],a[r]=a[r],a[k]
        inv=next(v for v in range(1,q) if mul(v,a[r][j],q)==1)
        a[r]=[mul(inv,v,q) for v in a[r]]
        for i in range(rows):
            if i!=r and a[i][j]:
                f=a[i][j]
                a[i]=[v^mul(f,w,q) for v,w in zip(a[i],a[r])]
        r+=1
        if r==rows: break
    return r

def mm(A,B,q):
    return [[reduce_xor(mul(A[i][k],B[k][j],q) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def reduce_xor(values):
    x=0
    for v in values: x^=v
    return x

def quad_basis(d): return [(i,j) for i in range(d) for j in range(i,d)]

def sym2(A,q):
    d=len(A); basis=quad_basis(d); loc={ij:k for k,ij in enumerate(basis)}; D=len(basis)
    M=[[0]*D for _ in range(D)]
    # image of e_i e_j under linear substitution A(e_i) A(e_j)
    for col,(i,j) in enumerate(basis):
        for k in range(d):
            for l in range(d):
                M[loc[min(k,l),max(k,l)]][col] ^= mul(A[k][i],A[l][j],q)
    return M

def Qmap_constraint(A,q):
    d=len(A); W=sym2(A,q); D=len(W); out=[[0]*(d*D) for _ in range(d*D)]
    # each Q entry indexed (quadratic basis index, generator index)
    for a in range(D):
        for j in range(d):
            row=a*d+j
            for i in range(d):
                out[row][a*d+i]^=A[i][j]
            for b in range(D):
                out[row][b*d+j]^=W[a][b]
    return out

def class_count(d,r,q):
    s=d-2*r
    def gaussian(n,k):
        return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))
    gl=prod(q**r-q**i for i in range(r))
    return gaussian(d,r)*gaussian(d-r,r)*gl

def pred_dim(d,r):
    D=d*(d+1)//2; s=d-2*r; R=r*(d-r)
    return (d-r)*D-s*R

def matrices(d,q):
    for vec in product(range(q),repeat=d*d):
        A=[list(vec[i*d:(i+1)*d]) for i in range(d)]
        if linear_rank(A,q)==d: yield A

def invol_type(A,q):
    d=len(A); sq=mm(A,A,q)
    for i in range(d): sq[i][i]^=1
    if any(any(row) for row in sq): return None
    N=[row[:] for row in A]
    for i in range(d): N[i][i]^=1
    return linear_rank(N,q)

def exhaust(d,q):
    typ={}; errors=[]; total=0
    for A in matrices(d,q):
        r=invol_type(A,q)
        if r is None: continue
        dim=d*(d+1)//2*d-linear_rank(Qmap_constraint(A,q),q)
        if dim != pred_dim(d,r):errors.append((A,r,dim,pred_dim(d,r)))
        typ[r]=typ.get(r,0)+1
        total+=q**dim
    return typ,total,errors

def main():
    for d,q in [(1,2),(1,4),(2,2),(2,4),(3,2)]:
        observed,total,errors=exhaust(d,q)
        predicted={r:class_count(d,r,q) for r in range(d//2+1)}
        expected=sum(v*q**pred_dim(d,r) for r,v in predicted.items())
        assert not errors and observed==predicted and total==expected,(d,q,errors,observed,predicted,total,expected)
        print(f'EXHAUST all linear automorphisms q={q}, d={d}, strata={observed}, involutions={total}: PASS')
    # Independent polynomial substitution: no use of the linear constraint matrix.
    basis=[(1,0),(0,1),(2,0),(1,1),(0,2)]
    def polynomial_mul(p,w,q):
        out={}
        for (a,b),v in p.items():
            for (c,e),u in w.items():
                if a+b+c+e<3:
                    key=(a+c,b+e)
                    out[key]=out.get(key,0)^mul(v,u,q)
        return {k:v for k,v in out.items() if v}
    def polynomial_comp(p,f,q):
        out={}
        for (a,b),v in p.items():
            h={(0,0):v}
            for _ in range(a):h=polynomial_mul(h,f[0],q)
            for _ in range(b):h=polynomial_mul(h,f[1],q)
            for k,u in h.items():out[k]=out.get(k,0)^u
        return {k:u for k,u in out.items() if u}
    cnt=0
    for A in matrices(2,2):
        for v in product(range(2),repeat=6):
            polys=[]
            for j in range(2):
                coeffs=[A[0][j],A[1][j]]+[v[k*2+j] for k in range(3)]
                polys.append({mon:c for mon,c in zip(basis,coeffs) if c})
            ok=(polynomial_comp(polys[0],polys,2)=={(1,0):1} and
                polynomial_comp(polys[1],polys,2)=={(0,1):1})
            cnt+=int(ok)
    assert cnt==88,cnt
    print('DIRECT 384 polynomial substitutions q=2,d=2; exactly 88 involutions: PASS')
    # Sampling larger dimensions tests the asserted symmetric-square module formula.
    import random
    rng=random.Random(20121116)
    for d in (4,5,6):
        for r in range(d//2+1):
            # Standard Jordan form and 30 random conjugates through invertible row transformations.
            J=[[int(i==j) for j in range(d)] for i in range(d)]
            for i in range(r):J[i][r+i]^=1
            mats=[J]
            for _ in range(30):
                A=[row[:] for row in J]
                for _ in range(3*d):
                    i,j=rng.sample(range(d),2)
                    for col in range(d): A[i][col]^=A[j][col]
                    for row in range(d): A[row][j]^=A[row][i] # conjugate by transvection
                mats.append(A)
            for A in mats:
                # The row and column transvection sequence preserves square-1 type.
                assert invol_type(A,2)==r
                observed=d*(d+1)//2*d-linear_rank(Qmap_constraint(A,2),2)
                assert observed==pred_dim(d,r),(d,r,observed)
        print(f'SAMPLED Jordan classes d={d}, q=2, 31 matrices per rank: PASS')

if __name__=='__main__': main()
