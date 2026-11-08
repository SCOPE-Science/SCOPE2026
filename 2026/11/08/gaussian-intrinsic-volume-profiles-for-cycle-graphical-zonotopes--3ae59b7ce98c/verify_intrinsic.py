"""Exact-structural and numerical tests for cyclic graphic-zonotope intrinsic volumes.

Only the Python standard library is needed. These finite checks accompany,
but do not replace, the analytic proof for arbitrary cycle length.
"""
from itertools import combinations
from math import sqrt, isclose, erf


def determinant_integer(A):
    n=len(A)
    if not n:
        return 1
    B=[list(row) for row in A]
    sign=1
    prev=1
    for k in range(n-1):
        if B[k][k]==0:
            j=next((j for j in range(k+1,n) if B[j][k]),None)
            if j is None:
                return 0
            B[k],B[j]=B[j],B[k]
            sign=-sign
        pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=B[i][j]*pivot-B[i][k]*B[k][j]
                assert num%prev==0
                B[i][j]=num//prev
        for i in range(k+1,n):
            B[i][k]=0
        prev=pivot
    return sign*B[n-1][n-1]


def gram(n, edge_indices):
    vectors=[]
    for i in edge_indices:
        vec=[0]*n
        vec[i]=1
        vec[(i+1)%n]=-1
        vectors.append(vec)
    return [[sum(x*y for x,y in zip(u,v)) for v in vectors] for u in vectors]


def component_sizes(n, edge_indices):
    par=list(range(n))
    def root(a):
        while par[a]!=a:
            a=par[a]
        return a
    for i in edge_indices:
        x,y=root(i),root((i+1)%n)
        if x!=y:
            par[y]=x
    sizes={}
    for i in range(n):
        x=root(i)
        sizes[x]=sizes.get(x,0)+1
    return list(sizes.values())


def exact_forest_sums(n):
    sums=[0.] * n
    checks=0
    for k in range(n):
        for E in combinations(range(n), k):
            det=determinant_integer(gram(n,E))
            prod=1
            for j in component_sizes(n,E):
                prod*=j
            assert det==prod, (n,k,E,det,prod)
            sums[k]+=sqrt(det)
            checks+=1
    return sums, checks


def all_power_coeffs(n):
    a=[[0.]*(n+1) for _ in range(n+1)]
    a[0][0]=1.
    for m in range(1,n+1):
        for j in range(m,n+1):
            a[m][j]=sum(sqrt(l)*a[m-1][j-l] for l in range(1,j-m+2))
    return a


def spectrum(n):
    a=all_power_coeffs(n)
    return [n/(n-k)*a[n-k][n] for k in range(n)]


def f(z):
    return sum(sqrt(l)*z**l for l in range(1,1000))


def critical_point():
    lo,hi=0.,.8
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)<1:lo=mid
        else: hi=mid
    z=(lo+hi)/2
    p=[sqrt(l)*z**l for l in range(1,500)]
    mu=sum((j+1)*q for j,q in enumerate(p))
    second=sum((j+1)**2*q for j,q in enumerate(p))
    sig2=second-mu**2
    return z,1-1/mu,sig2/mu**3


def distribution_check(n,z,alpha,var):
    v=spectrum(n)
    mass=sum(v)
    mu=sum(k*value for k,value in enumerate(v))/mass
    variance=sum((k-mu)**2*value for k,value in enumerate(v))/mass
    # Compare finite-parameter standardized CDF with a normal law.
    cumulative=0.
    max_difference=0.
    for k,val in enumerate(v):
        cumulative+=val/mass
        normal=.5*(1+erf((k+.5-n*alpha)/sqrt(2*n*var)))
        max_difference=max(max_difference,abs(cumulative-normal))
    return {'n':n,'mass_ratio':mass*z**n,'mean_per_n':mu/n,
            'variance_per_n':variance/n,'normal_cdf_error':max_difference}


def main():
    count=0
    for n in range(3,12):
        direct,checked=exact_forest_sums(n)
        via=spectrum(n)
        for k,(a,b) in enumerate(zip(direct,via)):
            assert isclose(a,b,rel_tol=1e-12,abs_tol=1e-11),(n,k,a,b)
            count+=1
        assert isclose(direct[0],1.,rel_tol=1e-12)
        assert isclose(direct[-1],n*sqrt(n),rel_tol=1e-12)
        count+=checked+2
    z,alpha,var=critical_point()
    assert .4385<z<.4387 and .5293<alpha<.5295 and .2112<var<.2115
    print(f'Critical root={z:.15f}; alpha={alpha:.15f}; variance slope={var:.15f}')
    for n in (15,30,50,75,100,150):
        r=distribution_check(n,z,alpha,var)
        print('n={n:3d}: W_n*z^n={mass_ratio:.10f}; '
              'E[K]/n={mean_per_n:.10f}; Var[K]/n={variance_per_n:.10f}; '
              'CDF error={normal_cdf_error:.6f}'.format(**r))
        assert abs(r['mass_ratio']-1) < .2
        if n>=75:
            assert abs(r['mean_per_n']-alpha)<.005
            assert abs(r['variance_per_n']-var)<.008
            assert r['normal_cdf_error']<.04
    print(f'CHECKS_PASS: {count} finite determinant/component checks and numerical coefficient comparisons, plus asymptotic approximations')

if __name__=='__main__':
    main()
