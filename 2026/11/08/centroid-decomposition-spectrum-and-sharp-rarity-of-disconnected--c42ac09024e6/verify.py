"""Independent labeled finite-field census for the connected-support centroid formula."""
from itertools import product
from math import comb


def gl(n,q):
    z=1
    for i in range(n):z*=q**n-q**i
    return z

def predicted(n,q):
    g=[gl(i,q) for i in range(n+1)]
    c=[0]*(n+1)
    h=[[0]*(n+1) for _ in range(n+1)]
    h[0][0]=1
    for a in range(1,n+1):
        c[a]=g[a]-sum(comb(a-1,s-1)*c[s]*g[a-s] for s in range(1,a))
        for k in range(1,a+1):
            h[a][k]=sum(comb(a-1,s-1)*c[s]*h[a-s][k-1] for s in range(1,a+1))
        assert sum(h[a]) == g[a]
    return h[n]

def matrix_rank(rows,q):
    m=[list(row) for row in rows]; n=len(m); r=0
    for col in range(n):
        k=next((j for j in range(r,n) if m[j][col]),None)
        if k is None:continue
        m[r],m[k]=m[k],m[r]
        inv=pow(m[r][col],-1,q)
        m[r]=[z*inv%q for z in m[r]]
        for j in range(n):
            if j!=r and m[j][col]:
                w=m[j][col]
                m[j]=[(m[j][c]-w*m[r][c])%q for c in range(n)]
        r+=1
    return r

def components(rows):
    n=len(rows);parent=list(range(n))
    def rt(i):
        while parent[i]!=i:i=parent[i]
        return i
    for i in range(n):
        for j in range(n):
            if i!=j and (rows[i][j] or rows[j][i]):
                parent[rt(i)]=rt(j)
    return len({rt(i) for i in range(n)})

def direct(n,q):
    out=[0]*(n+1)
    for flat in product(range(q),repeat=n*n):
        rows=[flat[i*n:(i+1)*n] for i in range(n)]
        if matrix_rank(rows,q)==n:out[components(rows)]+=1
    return out

def centroid_dimension_independent(rows,q):
    """Solve all centroid linear identities, without using connectivity."""
    n=len(rows); eq=[]
    for i in range(n):
        for j in range(n):
            if i!=j:
                for k in range(n):
                    v=[0]*(n*n)
                    v[j*n+i]=(v[j*n+i]+rows[j][k])%q
                    v[i*n+j]=(v[i*n+j]-rows[i][k])%q
                    eq.append(v)
        for k in range(n):
            v=[0]*(n*n)
            for j in range(n):
                v[k*n+j]=(v[k*n+j]+rows[i][j])%q
            v[i*n+i]=(v[i*n+i]-rows[i][k])%q
            eq.append(v)
    rank=0
    for c in range(n*n):
        ix=next((rr for rr in range(rank,len(eq)) if eq[rr][c]%q),None)
        if ix is None:continue
        eq[rank],eq[ix]=eq[ix],eq[rank]
        pivot=pow(eq[rank][c],-1,q)
        eq[rank]=[v*pivot%q for v in eq[rank]]
        for rr in range(len(eq)):
            if rr!=rank and eq[rr][c]:
                v=eq[rr][c];eq[rr]=[(a-v*b)%q for a,b in zip(eq[rr],eq[rank])]
        rank+=1
    return n*n-rank

if __name__=='__main__':
    for n,q in [(1,2),(2,2),(3,2),(4,2),(2,3),(3,3),(2,5)]:
        seen=direct(n,q); expected=predicted(n,q)
        assert seen==expected,(n,q,seen,expected)
        print(f'(n={n},q={q}) centroid_dimensions_1..n={expected[1:]} GL={gl(n,q)}')
    # Test a separate centroid-equation solver against graph components.
    for n,q in [(2,2),(3,2),(3,3),(4,2)]:
        seen=0
        for flat in product(range(q),repeat=n*n):
            rows=[flat[i*n:(i+1)*n] for i in range(n)]
            if matrix_rank(rows,q)!=n:continue
            if seen%max(1,gl(n,q)//32)==0:
                assert centroid_dimension_independent(rows,q)==components(rows)
            seen+=1
    print('CENTROID_EQUATIONS_OK')
    # Check elementary bounds and exact telescoping identities over many parameters.
    from fractions import Fraction
    for q in [2,3,4,5,7]:
        for n in range(2,13):
            h=predicted(n,q);g=gl(n,q)
            p=Fraction(sum(h[2:]),g)
            a=Fraction(n*(q-1)*gl(n-1,q),g)
            e2=Fraction(comb(n,2)*(q-1)**2*gl(n-2,q),g)
            u=sum((Fraction(comb(n,s)*gl(s,q)*gl(n-s,q),g) for s in range(2,n//2+1)),Fraction())
            assert a-e2<=p<=a+u
    print('VERIFY_OK_CENTROID')
