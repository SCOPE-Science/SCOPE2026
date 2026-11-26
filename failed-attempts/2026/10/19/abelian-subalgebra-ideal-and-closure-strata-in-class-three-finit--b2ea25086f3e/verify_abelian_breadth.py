"""Direct finite-field RREF enumeration of abelian Lie subalgebras.

Checks the concrete Lie brackets and compares the resulting distribution with
an independently implemented Gaussian-binomial formula. No external packages.
"""
from itertools import combinations, product
from math import prod
from random import Random


def gaussian_safe(n, k, q):
    if not 0 <= k <= n: return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den


def rref_subspaces(n, q):
    yield ()
    for k in range(1,n+1):
        for pivots in combinations(range(n), k):
            pivset=set(pivots)
            free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivset]
            for vals in product(range(q), repeat=len(free)):
                rows=[[0]*n for _ in range(k)]
                for i,p in enumerate(pivots): rows[i][p]=1
                for (i,j),v in zip(free, vals): rows[i][j]=v
                yield tuple(tuple(row) for row in rows)


def bracket(v,w,q):
    a,b,c,_,_=v
    x,y,z,_,_=w
    t=(a*y-b*x)%q
    return (t,(t+2*c*x-2*a*z)%q,(t+2*b*z-2*c*y)%q)


def expected(m,q):
    Q=q**m; L=Q*Q+Q+1
    d=[0]*(3*m+1)
    for s in range(2*m+1):
        d[s]+=gaussian_safe(2*m,s,q)
        for r in range(1,m+1):
            d[s+r]+=L*gaussian_safe(m,r,q)*gaussian_safe(2*m,s,q)*q**(r*(2*m-s))
    return d


def linear_rank(rows,q):
    mat=[list(v) for v in rows if any(v)]
    r=0
    if not mat:return 0
    n=len(mat[0])
    for col in range(n):
        k=next((i for i in range(r,len(mat)) if mat[i][col]%q),None)
        if k is None:continue
        mat[r],mat[k]=mat[k],mat[r]
        iv=pow(mat[r][col],-1,q)
        mat[r]=[(x*iv)%q for x in mat[r]]
        for j in range(len(mat)):
            if j!=r and mat[j][col]%q:
                scale=mat[j][col]
                mat[j]=[(x-scale*y)%q for x,y in zip(mat[j],mat[r])]
        r+=1
        if r==len(mat):break
    return r


def ideal_closure_dimension(sub,q,coordinate_basis):
    generators=list(sub)
    for _ in range(6):
        oldrank=linear_rank(generators,q)
        for v in list(generators):
            for w in coordinate_basis:
                generators.append((0,0,*bracket(v,w,q)))
        if linear_rank(generators,q)==oldrank:
            return oldrank
    raise AssertionError('ideal closure iteration did not stabilize')


def exact(q):
    n=5; obs=[0]*(n+1); ideals=[0]*(n+1); closures=[0]*(n+1); total=0
    coordinate_basis=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    for sub in rref_subspaces(n,q):
        total+=1
        if all(bracket(u,v,q)==(0,0,0) for u,v in combinations(sub,2)):
            obs[len(sub)]+=1
            cldim=ideal_closure_dimension(sub,q,coordinate_basis)
            onlycentral=all(u[:3]==(0,0,0) for u in sub)
            onlyderived=all(u[:2]==(0,0) for u in sub)
            expectcl=len(sub) if onlycentral else 3 if onlyderived else 4
            assert cldim==expectcl,(q,sub,cldim,expectcl)
            closures[cldim]+=1
            # An ideal must contain its brackets with all five basis vectors.
            span=set()
            for coeff in product(range(q),repeat=len(sub)):
                span.add(tuple(sum(coeff[i]*sub[i][j] for i in range(len(sub)))%q for j in range(n)))
            if all((0,0,*bracket(u,v,q)) in span for u in sub for v in coordinate_basis):
                ideals[len(sub)]+=1
    exp=expected(1,q)
    assert obs[:4]==exp and obs[4:]==[0,0],(q,obs,exp)
    assert obs[3]==q*q+q+1
    expected_ideals=[gaussian_safe(2,s,q) for s in range(3)]+[1,0,0]
    assert ideals==expected_ideals,(q,ideals,expected_ideals)
    perline=q*q+q*(q+1)+1
    expected_closures=[1,q+1,1,perline,(q*q+q)*perline,0]
    assert closures==expected_closures,(q,closures,expected_closures)
    print('EXHAUSTIVE',q, 'all_linear_subspaces',total,'abelian_by_dimension',obs,
          'abelian_ideals_by_dimension',ideals,'ideal_closure_dimensions',closures)


def mod9mul(a,b):
    # F_9=F_3[T]/(T^2+1), encoded as 0..8 with a=a0+3a1.
    a0,a1=a%3,a//3
    b0,b1=b%3,b//3
    return ((a0*b0+2*a1*b1)%3)+3*((a0*b1+a1*b0)%3)

def mod9add(a,b):
    return ((a%3+b%3)%3)+3*((a//3+b//3)%3)

def mod9neg(a):
    return ((-a%3)%3)+3*((-(a//3))%3)

def mod9sub(a,b): return mod9add(a,mod9neg(b))

def F9bracket(v,w):
    a,b,c,_,_=v; x,y,z,_,_=w
    t=mod9sub(mod9mul(a,y),mod9mul(b,x))
    d=mod9add(t,mod9sub(mod9mul(2,mod9mul(c,x)),mod9mul(2,mod9mul(a,z))))
    e=mod9add(t,mod9sub(mod9mul(2,mod9mul(b,z)),mod9mul(2,mod9mul(c,y))))
    return (t,d,e)


def F9linecheck():
    # Each of the 91 projective lines yields an F_3-space of dimension 2.
    directions={}
    for a,b,c in product(range(9),repeat=3):
        if (a,b,c)==(0,0,0):continue
        pts=frozenset((mod9mul(t,a),mod9mul(t,b),mod9mul(t,c)) for t in range(9))
        directions[pts]=(a,b,c)
    assert len(directions)==91
    for pts in directions:
        for (a,b,c),(x,y,z) in combinations(pts,2):
            assert F9bracket((a,b,c,0,0),(x,y,z,0,0))==(0,0,0)
    # The centre-augmented spaces are 6-dimensional over F_3 and pairwise distinct.
    # Test the strict normalizer/ideal exception across all projective lines.
    ideals=0
    for pts in directions:
        if all(F9bracket((a,b,c,0,0),(x,y,z,0,0))[0]==0
               for a,b,c in pts for x,y,z in [(1,0,0),(0,1,0),(0,0,1)]):
            ideals+=1
    assert ideals==1
    # Count normalizers on the projected 3-space directly: Q^3 for the
    # derived line, Q^2 for each other line. The central lifts are free.
    buckets={81:0,729:0}
    for pts in directions:
        a,b,c=next(v for v in pts if v != (0,0,0))
        count=sum(F9bracket((a,b,c,0,0),(x,y,z,0,0))[0]==0
                  for x,y,z in product(range(9),repeat=3))
        buckets[count]+=1
    assert buckets=={81:90,729:1},buckets
    # Pairwise commutativity is tested independently of line enumeration.
    rng=Random(314159265)
    for _ in range(12000):
        p=tuple(rng.randrange(9) for _ in range(3))
        t=tuple(rng.randrange(9) for _ in range(3))
        commuting=F9bracket((*p,0,0),(*t,0,0))==(0,0,0)
        proportional=any(t==tuple(mod9mul(a,z) for z in p) for a in range(9)) if p!=(0,0,0) else True
        assert commuting==proportional,(p,t,commuting,proportional)
    print('NORMALIZER_DISTRIBUTION',buckets,'RANDOM_PAIR_TESTS',12000)
    print('F9_PROJECTIVE_LINES',len(directions),'UNIQUE_MAXIMAL_ABELIAN_IDEAL',ideals,
          'DIMENSION_COUNTS',expected(2,3))

if __name__=='__main__':
    for q in (3,5):exact(q)
    F9linecheck()
    print('ALL_FINITE_CHECKS_PASSED')
