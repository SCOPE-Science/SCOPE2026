"""Independent finite checks of the canonical stack-sorting simplex metric.
Only Python standard library required. Finite checks corroborate the analytic proof.
"""
from fractions import Fraction
from math import asin, sqrt, log, pi, isclose

def stack_sort(word):
    st=[]; output=[]
    for value in word:
        while st and value>st[-1]:
            output.append(st.pop())
        st.append(value)
    output.extend(reversed(st))
    return tuple(output)

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def check_exact(n):
    identity=tuple(range(1,n+1)); word=tuple(range(2,n+1))+(1,)
    orbit=[word]
    while orbit[-1]!=identity:
        new=stack_sort(orbit[-1])
        assert new!=orbit[-1] and new not in orbit
        orbit.append(new)
    assert len(orbit)==n
    d={k:tuple((1 if j<k else 1-k if j==k else 0) for j in range(1,n+1)) for k in range(2,n+1)}
    assert set(orbit)=={identity}|{tuple(identity[j]+v[j] for j in range(n)) for v in d.values()}
    for k,v in d.items():
        assert dot(v,v)==k*(k-1)
        for j,w in d.items():
            if j!=k:assert dot(v,w)==0
    # Compute all dual facet normals directly in ambient integer/rational coordinates.
    base=tuple(sum(Fraction(d[k][j],k*(k-1)) for k in d) for j in range(n))
    normals={0:base}
    normals.update({k:tuple(-Fraction(v,k*(k-1)) for v in d[k]) for k in d})
    assert dot(base,base)==Fraction(n-1,n)
    for k in d:
        assert dot(base,d[k])==1
        assert dot(normals[k],d[k])==-1
        for j in d:
            if j!=k:assert dot(normals[k],d[j])==0
    for i in normals:
        for j in normals:
            if i>=j:continue
            inner=dot(normals[i],normals[j])
            if i and j:assert inner==0
            else:
                k=max(i,j)
                assert inner==-Fraction(1,k*(k-1))
    return len(orbit),len(normals)*(len(normals)-1)//2

if __name__=='__main__':
    count=0; facets=0
    for n in range(3,61):
        a,b=check_exact(n);count+=a;facets+=b
    for n in [100,1000,10000]:
        angles=[asin(sqrt(n/((n-1)*k*(k-1)))) for k in range(2,n+1)]
        mean=2*sum(angles)/(n*(n-1))
        second=2*sum(t*t for t in angles)/(n*(n-1))
        assert 0<mean and 0<second-mean*mean
        # Check scaling of the conditional empirical rare-angle CDF for x=2,3.
        for x in [2.,3.,5.]:
            cdf=sum(n*t<=x for t in angles)/(n-1)
            assert abs(cdf-(1-1/x))<.03 if n>=1000 else True
        assert .95<sum(angles)/log(n)<1.7
    print('STACK_SORT_RARE_ANGLES_PASS n=3..60 orbit_vertices=%d facet_pairs=%d asymptotics=100,1000,10000' %(count,facets))
