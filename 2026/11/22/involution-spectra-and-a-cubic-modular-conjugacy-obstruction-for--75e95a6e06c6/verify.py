"""Finite-field spot checks for involutive automorphisms of free cube-zero algebras.
Run: python3 verify.py. Standard library only. Counts are checked independently
through equations and through direct automorphism composition for small cases.
"""
from itertools import product


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b, q):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % q
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a,b,q):
    return [[(a[i][j]+b[i][j])%q for j in range(len(a[0]))] for i in range(len(a))]


def rank(mat,q):
    if not mat: return 0
    x=[row[:] for row in mat]
    h,w=len(x),len(x[0]); r=0
    for col in range(w):
        pivot=next((i for i in range(r,h) if x[i][col]%q),None)
        if pivot is None: continue
        x[r],x[pivot]=x[pivot],x[r]
        inv=pow(x[r][col],-1,q)
        x[r]=[(z*inv)%q for z in x[r]]
        for i in range(h):
            if i!=r and x[i][col]:
                m=x[i][col]
                x[i]=[(x[i][j]-m*x[r][j])%q for j in range(w)]
        r+=1
        if r==h: break
    return r


def det_invertible(g,q):
    return rank(g,q)==len(g)


def tensor(g,q):
    n=len(g)
    return [[g[i][u]*g[j][v]%q for u in range(n) for v in range(n)]
            for i in range(n) for j in range(n)]


def all_matrices(n,q):
    for a in product(range(q),repeat=n*n):
        yield [list(a[i*n:(i+1)*n]) for i in range(n)]


def equation(g,q):
    n=len(g); w=n*n; f=tensor(g,q)
    # Each h is a (w x n) matrix.  The linear equation is Fh + hg=0.
    m=[]
    for i in range(w):
        for j in range(n):
            row=[]
            for u in range(w):
                for v in range(n):
                    row.append((f[i][u]*(v==j)+(u==i)*g[v][j])%q)
            m.append(row)
    return m


def theory(g,q):
    n=len(g); r=rank(add(g,[[-x%q for x in row] for row in ident(n)],q),q)
    if q==2:
        s=n-2*r
        assert s>=0
        e=(n-r)*(s*s+2*n*r)
        return e,s**3
    # For odd prime fields: r = rank(g-I) = negative eigenspace dimension.
    b=r; a=n-b
    return 3*a*a*b+b**3,0


def direct_square(g,h,q):
    n=len(g); w=n*n
    f=tensor(g,q)
    full=[[0]*(n+w) for _ in range(n+w)]
    for i in range(n):
        for j in range(n): full[i][j]=g[i][j]
    for i in range(w):
        for j in range(n): full[n+i][j]=h[i][j]
        for j in range(w): full[n+i][n+j]=f[i][j]
    return matmul(full,full,q)==ident(n+w)


def check(q,n, exhaustive=False):
    total=0; by_type={}; automorphisms=0
    for g in all_matrices(n,q):
        if not det_invertible(g,q):continue
        automorphisms+=1
        if matmul(g,g,q)!=ident(n):continue
        e,orbdim=theory(g,q)
        null=n**3-rank(equation(g,q),q)
        assert null==e, (q,n,g,null,e)
        assert orbdim==2*e-n**3 if q==2 else orbdim==0
        total+=q**e
        k=rank(add(g,[[-x%q for x in row] for row in ident(n)],q),q)
        by_type[k]=by_type.get(k,0)+1
        if exhaustive:
            local=0
            for coefficients in product(range(q),repeat=n**3):
                h=[list(coefficients[i*n:(i+1)*n]) for i in range(n*n)]
                cond=not any(sum(equation(g,q)[j][t]*coefficients[t] for t in range(n**3))%q for j in range(n**3))
                actual=direct_square(g,h,q)
                assert cond==actual,(q,n,g,h)
                local+=int(actual)
            assert local==q**e,(q,n,local,e)
    return total,by_type,automorphisms


def orbit_action_check(q=2,n=2):
    """Independently enumerate shear-conjugation orbits on every actual solution."""
    assert (q,n)==(2,2)
    group_size=0
    for g in all_matrices(n,q):
        if not det_invertible(g,q) or matmul(g,g,q)!=ident(n):
            continue
        group_size+=1
        F=tensor(g,q)
        solution=set()
        for coeff in product(range(q),repeat=n**3):
            H=[list(coeff[i*n:(i+1)*n]) for i in range(n*n)]
            if add(matmul(F,H,q),matmul(H,g,q),q)==[[0]*n for _ in range(n*n)]:
                solution.add(coeff)
        translations=set()
        for coeff in product(range(q),repeat=n**3):
            K=[list(coeff[i*n:(i+1)*n]) for i in range(n*n)]
            T=add(matmul(K,g,q),matmul(F,K,q),q)
            translations.add(tuple(a for row in T for a in row))
        assert all(t in solution for t in translations)
        orbits=set()
        for h in solution:
            orbit=frozenset(tuple((a+b)%q for a,b in zip(h,t)) for t in translations)
            orbits.add(orbit)
        r=rank(add(g,[[-x%q for x in row] for row in ident(n)],q),q)
        s=n-2*r
        assert len(orbits)==q**(s**3),(g,len(orbits),s)
        assert all(len(o)==len(translations) for o in orbits)
    assert group_size==4
    print('CHAR2_SHEAR_ORBIT_DIRECT_ENUMERATION_OK')


def main():
    examples=[(2,1,True,2),(2,2,True,304),(2,3,False,134561792),
              (3,1,True,4),(3,2,False,7534),(5,2,False,1+5*6*5**4+5**8)]
    for q,n,exhaustive,expected in examples:
        total,types,aut=check(q,n,exhaustive)
        assert total==expected,(q,n,total,expected)
        print(f'prime_field={q} generators={n} invertible_linear={aut} involutions={total} types={types} direct={exhaustive}')
    orbit_action_check()
    print('FINITE_FIELD_INVOLUTION_AND_ORBIT_RANK_CHECKS_OK')

if __name__=='__main__':main()
