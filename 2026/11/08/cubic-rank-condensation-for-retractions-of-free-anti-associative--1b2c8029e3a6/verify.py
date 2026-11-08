"""Standalone finite-field checks for retractions of free anti-associative algebras.

Run: python verify.py . All fields checked are prime fields of odd characteristic.
"""
import itertools
from fractions import Fraction


def gaussian(n, r, q):
    value = Fraction(1)
    for j in range(r):
        value *= Fraction(q ** (n-j)-1, q ** (r-j)-1)
    return int(value)


def predicted(n, q):
    return [gaussian(n, r, q) * q ** (
        r*(n-r) + r*(n*n-r*r+n**3-r**3) + (n-r)*(r*r+r**3)
    ) for r in range(n+1)]


def multiply(x, y, n, q):
    D=n+n*n+n**3
    z=[0]*D
    for i in range(n):
        for j in range(n):
            z[n+i*n+j] += x[i]*y[j]
            for k in range(n):
                z[n+n*n+i*n*n+j*n+k] += x[i]*y[n+j*n+k]
                z[n+n*n+i*n*n+j*n+k] -= x[n+i*n+j]*y[k]
    return tuple(v%q for v in z)


def hom_map(gens, n, q):
    D=n+n*n+n**3
    base=[tuple(int(i==j) for j in range(D)) for i in range(n)]
    images=list(gens)
    images += [multiply(gens[i],gens[j],n,q) for i in range(n) for j in range(n)]
    images += [multiply(gens[i],multiply(gens[j],gens[k],n,q),n,q)
               for i in range(n) for j in range(n) for k in range(n)]
    assert len(images)==D
    def f(x):
        return tuple(sum(x[i]*images[i][j] for i in range(D))%q for j in range(D))
    return f


def rank(m,q):
    rows=[list(row) for row in m]
    if not rows: return 0
    n=len(rows);k=len(rows[0]);r=0
    for j in range(k):
        pivot=next((i for i in range(r,n) if rows[i][j]%q),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][j],-1,q)
        rows[r]=[u*inv%q for u in rows[r]]
        for i in range(n):
            if i!=r:
                c=rows[i][j]
                if c:rows[i]=[(u-c*v)%q for u,v in zip(rows[i],rows[r])]
        r+=1
        if r==n:break
    return r


def exhaustive_one_generator(q):
    n=1;D=3;obs={0:0,1:0}
    for v in itertools.product(range(q),repeat=D):
        f=hom_map([v],n,q)
        if f(v)==v:
            rr=0 if not any(v) else 1
            obs[rr]+=1
    assert [obs[0],obs[1]]==predicted(n,q), (q,obs)
    print('EXHAUSTIVE_ONE_GENERATOR_OK',q,obs)


def linear_system_solutions(mat, rhs, q):
    rows=[list(row)+[b] for row,b in zip(mat,rhs)]
    piv=rank([row[:-1] for row in rows],q)
    aug=rank(rows,q)
    if piv!=aug:return 0
    return q**(len(mat[0])-piv)


def canonical_two_generator(q):
    n=2;D=n+n*n+n**3;P=((1,0),(0,0))
    S_count=0;T_sum=0
    zeros=[0]*D
    for sflat in itertools.product(range(q),repeat=n**3): # n * n^2 coefficients
        gens=[]
        for i in range(n):
            v=zeros.copy()
            for j in range(n): v[j]=P[i][j]
            for t in range(n*n):v[n+t]=sflat[i*n*n+t]
            gens.append(tuple(v))
        f=hom_map(gens,n,q)
        if any(f(gens[i])[n:n+n*n]!=gens[i][n:n+n*n] for i in range(n)):
            continue
        S_count+=1
        # Unknown cubic coefficients on each generator: derive their linear system
        Q=[f(gens[i])[n+n*n:] for i in range(n)]
        rows=[];rhs=[]
        for i in range(n):
            for triple in range(n**3):
                row=[]
                for j in range(n):
                    for u in range(n**3):
                        basis=zeros.copy();basis[n+n*n+u]=1
                        # coefficient of T_i - T(P e_i) - P^{tensor3}(T_i)
                        unit=1 if (i==j and triple==u) else 0
                        unit-=P[i][j]*(triple==u)
                        a,b,c=(u//(n*n),(u//n)%n,u%n)
                        x,y,z=(triple//(n*n),(triple//n)%n,triple%n)
                        unit-=(i==j)*P[a][x]*P[b][y]*P[c][z]
                        row.append(int(unit)%q)
                rows.append(row);rhs.append(Q[i][triple])
        choices=linear_system_solutions(rows,rhs,q)
        assert choices==q**8,(sflat,choices)
        T_sum+=choices
    assert S_count==q**4,(q,S_count)
    assert T_sum==q**12,(q,T_sum)
    assert gaussian(2,1,q)*q*T_sum==predicted(2,q)[1]
    print('CANONICAL_RANK_ONE_AFFINE_FIBER_OK',q,'S',S_count,'lifts',T_sum)


def conjugacy_samples(n,q):
    import random
    rng=random.Random(230108)
    D=n+n*n+n**3
    for r in range(n+1):
        for trial in range(12):
            U=[]
            for i in range(n):
                vec=[0]*D;vec[i]=1
                for j in range(n,D):vec[j]=rng.randrange(q)
                U.append(tuple(vec))
            g=hom_map(U,n,q)
            # inverse unipotent automorphism through finite-step iteration; g=I+N, N^3=0
            def inv(x):
                gx=g(x)
                nx=tuple((gx[i]-x[i])%q for i in range(D))
                nnx=tuple((g(nx)[i]-nx[i])%q for i in range(D))
                return tuple((x[i]-nx[i]+nnx[i])%q for i in range(D))
            def p(x):
                y=list(x)
                for i in range(n):
                    if i>=r:y[i]=0
                for d in (2,3):
                    offset=n if d==2 else n+n*n
                    for t in range(n**d):
                        word=[]; z=t
                        for _ in range(d):word.insert(0,z%n);z//=n
                        if any(a>=r for a in word):y[offset+t]=0
                return tuple(y)
            def f(x):return g(p(inv(x)))
            for j in range(n):
                basis=tuple(int(t==j) for t in range(D))
                assert f(f(basis))==f(basis)
            RR=rank([f(tuple(int(t==j) for t in range(D))) for j in range(D)],q)
            assert RR==r+r*r+r**3,(n,q,r,RR)
    print('RANDOM_UNIPOTENT_CONJUGACY_OK',n,q)

if __name__=='__main__':
    exhaustive_one_generator(3)
    exhaustive_one_generator(5)
    canonical_two_generator(3)
    conjugacy_samples(2,3)
    conjugacy_samples(3,3)
    print('VERIFY_OK')
