"""Direct finite-field matrix checks for involutions of a cyclic radical-square-zero algebra."""
from itertools import product
from collections import Counter
from math import comb, gcd


def rank_mod(mat, q):
    A=[list(r) for r in mat]
    m=len(A); d=len(A[0]); pos=0
    for j in range(d):
        pivot=next((i for i in range(pos,m) if A[i][j]%q), None)
        if pivot is None: continue
        A[pos],A[pivot]=A[pivot],A[pos]
        x=pow(A[pos][j]%q,-1,q)
        A[pos]=[(x*v)%q for v in A[pos]]
        for i in range(m):
            if i==pos: continue
            c=A[i][j]
            if c: A[i]=[(v-c*w)%q for v,w in zip(A[i], A[pos])]
        pos+=1
        if pos==m: break
    return pos


def morph_matrix(x, lam, k,q):
    n=len(x); M=[[0]*(2*n) for _ in range(2*n)]
    for j in range(n):
        a=(j+k)%n
        M[a][j]=1
        M[n+(a-1)%n][j]=x[(a-1)%n]%q
        M[n+a][j]=(-x[a])%q
        M[n+a][n+j]=lam[j]%q
    return M


def is_square_one(M,q):
    n=len(M)
    for i in range(n):
        for j in range(n):
            s=sum(M[i][k]*M[k][j] for k in range(n))%q
            if s!=int(i==j):return False
    return True


def multiply(g,h,q):
    x,lam,k=g;y,mu,t=h;n=len(x)
    z=list(x)
    for i in range(n):z[(i+k)%n]=(z[(i+k)%n]+lam[i]*y[i])%q
    new=tuple(mu[i]*lam[(i+t)%n]%q for i in range(n))
    return (tuple(z),new,(k+t)%n)


def inverse(g,q):
    x,lam,k=g;n=len(x)
    y=[0]*n
    for j in range(n):y[(j-k)%n]=(-x[j]*pow(lam[(j-k)%n],-1,q))%q
    return (tuple(y),tuple(pow(lam[(j-k)%n],-1,q) for j in range(n)),(-k)%n)


def audit(n,q):
    values=range(q); nonzero=range(1,q)
    idg=((0,)*n,(1,)*n,0)
    predicted=Counter({2*n-r:comb(n,r)*q**r for r in range(n+1)})
    if n%2==0:predicted[n]+=(q*(q-1))**(n//2)
    observed=Counter(); involutions=[]; rotation_counts=Counter()
    for k in range(n):
        for lam in product(nonzero,repeat=n):
            for x in product(values,repeat=n):
                M=morph_matrix(x,lam,k,q)
                if not is_square_one(M,q):continue
                d=2*n-rank_mod([[int(i==j)-M[i][j] for j in range(2*n)] for i in range(2*n)],q)
                observed[d]+=1;rotation_counts[k]+=1
                involutions.append((x,lam,k))
    assert observed==predicted,(observed,predicted)
    assert rotation_counts[0]==(q+1)**n
    for k in range(1,n):
        expect=(q*(q-1))**(n//2) if n%2==0 and k==n//2 else 0
        assert rotation_counts[k]==expect
    # Check semidirect multiplication directly on representatives with nonzero radical/shears.
    tests=involutions[:7]+involutions[-7:]+[idg]
    for g in tests:
        assert multiply(g,inverse(g,q),q)==idg
        for h in tests:
            gh=multiply(g,h,q)
            Mg=morph_matrix(*g,q);Mh=morph_matrix(*h,q);Mgh=morph_matrix(*gh,q)
            assert all((sum(Mg[i][z]*Mh[z][j] for z in range(2*n))-Mgh[i][j])%q==0
                       for i in range(2*n) for j in range(2*n))
    if n==4 and q==3:
        # BFS conjugacy under generators of radical translations, independent arrow scalings and rotation.
        generators=[]
        for j in range(n):
            y=[0]*n;y[j]=1;generators.append((tuple(y),(1,)*n,0))
            mu=[1]*n;mu[j]=2;generators.append(((0,)*n,tuple(mu),0))
        generators.append(((0,)*n,(1,)*n,1))
        invgen=[inverse(g,q) for g in generators]
        remain=set(involutions);orbits=[]
        while remain:
            z=next(iter(remain));todo=[z];orbit={z}
            while todo:
                g=todo.pop()
                for h,hi in zip(generators,invgen):
                    v=multiply(multiply(h,g,q),hi,q)
                    if v not in orbit: orbit.add(v);todo.append(v)
            assert orbit<=remain
            remain-=orbit;orbits.append(len(orbit))
        assert sorted(orbits)==[1,12,18,36,36,81,108],sorted(orbits)
        print('CONJUGACY_OK',n,q,sorted(orbits))
    print('COUNT_OK',n,q,'total',sum(observed.values()),'fixed_dimensions',dict(sorted(observed.items())))

if __name__=='__main__':
    for n,q in [(3,3),(4,3),(3,5)]:audit(n,q)
    print('VERIFY_OK')

# The proof's fixed-algebra multiplication is also independently checkable from
# the basis structure; this function is available for manual tests.
def product_in_algebra(a,b,q):
    n=len(a)//2
    return tuple((a[i]*b[i])%q for i in range(n))+tuple((a[i]*b[n+i]+a[n+i]*b[(i+1)%n])%q for i in range(n))
