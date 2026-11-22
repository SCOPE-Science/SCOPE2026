"""Independent small-dimensional checks of near-critical hypersimplex vertex-copy gaps."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial, sqrt
import random


def vertices(n,k):
    for I in combinations(range(n),k):
        yield tuple(1 if i in I else 0 for i in range(n))


def in_copy(x,v,l):
    return all((l if bit else F(0)) <= z <= (F(1) if bit else F(1)-l) for z,bit in zip(x,v))


def analytic_uncovered(x,n,k,l):
    R=max(k,n-k)
    if l<=F(1,R+1):
        return False
    nlow=sum(z<l for z in x)
    nhigh=sum(z>1-l for z in x)
    return nlow>=n-k+1 or nhigh>=k+1


def compositions_bounded(total,n,bound):
    if n==1:
        if 0<=total<=bound:yield (total,)
        return
    for j in range(min(total,bound)+1):
        for tail in compositions_bounded(total-j,n-1,bound):
            yield (j,)+tail


def projection_box_sum(x,v,l):
    """Orthogonal projection to copy via monotone 1D water filling."""
    lo=[float(l)*b for b in v]
    hi=[1-(float(l) if b==0 else 0) for b in v]
    target=sum(v)
    low,high=-2.,2.
    for _ in range(90):
        mid=(low+high)/2
        s=sum(max(lo[i],min(hi[i],x[i]+mid)) for i in range(len(x)))
        if s<target:low=mid
        else:high=mid
    a=(low+high)/2
    return [max(lo[i],min(hi[i],x[i]+a)) for i in range(len(x))]


def full_distance(x,n,k,l):
    return min(sqrt(sum((a-b)**2 for a,b in zip(x,projection_box_sum(x,v,l)))) for v in vertices(n,k))


def eulerian(n,j):
    return sum((-1)**r*comb(n+1,r)*(j+1-r)**n for r in range(j+2))


def run():
    exact=0; metric=0; gram=0; means=0
    # Independent membership: checking all candidate homothetic vertex copies.
    for n in range(4,8):
        for k in range(2,n-1):
            R=max(k,n-k)
            l=(F(1,R+1)+F(1,R))/2
            vs=list(vertices(n,k))
            for den in (3,4,5):
                for xs in compositions_bounded(k*den,n,den):
                    x=tuple(F(u,den) for u in xs)
                    iscovered=any(in_copy(x,v,l) for v in vs)
                    assert iscovered != analytic_uncovered(x,n,k,l),(n,k,l,x)
                    exact+=1
    # Independent Euclidean minimization over all homothetic copies.
    random.seed(0xC0FEE)
    for n in range(4,9):
        for k in range(2,n-1):
            R=max(k,n-k); m=R+1
            l=(F(1,R+1)+F(1,R))/2
            t=float(m*l-1)
            for _ in range(15):
                H=set(random.sample(range(n),min(k,n-k)-1))
                parts=[random.expovariate(1.) for i in range(n)]
                parts=[z/sum(parts) for z in parts]
                # rank asymmetry orientation; for balanced sample both types
                y=[(1 if i in H else float(l))-t*parts[i] for i in range(n)]
                if k>n/2 or (n==2*k and random.choice((False,True))):
                    x=[1-z for z in y]
                else:x=y
                d_pred=sqrt(n/(n-1))*t*min(parts[i] for i in range(n) if i not in H)
                d_actual=full_distance(x,n,k,l)
                assert abs(d_actual-d_pred)<1e-8,(n,k,d_actual,d_pred)
                metric+=1
    # Independently compute squared determinant of regular simplex edge Gram.
    for n in range(4,11):
        # Vertices t*e_i for i=0,...,n-1, in sum=t hyperplane.
        G=[[2 if i==j else 1 for j in range(n-1)] for i in range(n-1)]
        # Sylvester determinant by integer Bareiss elimination.
        A=[row[:] for row in G];prev=1
        for p in range(n-2):
            pivot=A[p][p]
            for i in range(p+1,n-1):
                for j in range(p+1,n-1):
                    z=A[i][j]*pivot-A[i][p]*A[p][j]
                    assert z%prev==0
                    A[i][j]=z//prev
            for i in range(p+1,n-1):A[i][p]=0
            prev=pivot
        assert A[-1][-1]==n
        gram+=1
    # Dirichlet min law: empirical E[D/Dmax]=1/n for every n.
    for n in (4,5,6,8):
        m=n-2 # choose any subset of m of n barycentric coordinates
        values=[]
        for _ in range(8000):
            a=[random.expovariate(1.) for i in range(n)]
            a=[z/sum(a) for z in a]
            values.append(m*min(a[:m]))
        assert abs(sum(values)/len(values)-1/n)<0.011
        means+=1
    # Eulerian body volume agrees with inclusion-exclusion for all integer middle layers.
    for n in range(4,13):
        for k in range(1,n):
            coeff=sum((-1)**r*comb(n,r)*(k-r)**(n-1) for r in range(k+1))
            assert coeff==eulerian(n-1,k-1)
            assert coeff>0
    print('HYPERSIMPLEX_FIRST_VOID_PASS exact_coverage',exact,'independent_metric_projections',metric,'gram',gram,'dirichlet',means)

if __name__=='__main__':run()
