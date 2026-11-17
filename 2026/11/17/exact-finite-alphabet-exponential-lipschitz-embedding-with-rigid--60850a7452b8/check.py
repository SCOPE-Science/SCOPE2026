#!/usr/bin/env python3
"""Independent finite-grid and phase diagnostics for sharp Lipschitz exponential embedding."""
from itertools import product
from math import exp, log, ceil, isclose

def phi(vals, lam):
    m=sum(vals)/len(vals)
    return sum(exp(lam*(v-m)) for v in vals)/len(vals)

def M(m,lam):
    return max(exp(-lam*k/m)*(1+k*(exp(lam)-1)/m) for k in range(1,m))

def brute(dims,lam):
    # Every vertex of {f(0)=0, |f(x)-f(y)|<=1 for adjacent x,y}
    # is integer-valued by total unimodularity of directed incidence.
    points=list(product(*(range(m) for m in dims)))
    neighbors=[]
    for i,p in enumerate(points):
        for j in range(i):
            q=points[j]
            if sum(a!=b for a,b in zip(p,q))==1: neighbors.append((i,j))
    D=len(dims)
    count=0; maxval=-1
    for vs in product(range(-D,D+1),repeat=len(points)-1):
        arr=(0,)+vs
        if any(abs(arr[i]-arr[j])>1 for i,j in neighbors):continue
        count+=1
        v=phi(arr,lam)
        if v>maxval: maxval=v
    expected=1
    for m in dims:expected*=M(m,lam)
    assert isclose(maxval,expected,rel_tol=1e-10,abs_tol=1e-10), (dims,lam,maxval,expected)
    return count

def main():
    tests=[((2,2),.3),((2,2),1),((2,3),.25),((2,3),1),((2,3),3),((3,3),1)]
    total=0
    for dims,lam in tests:
        count=brute(dims,lam)
        total+=count
        print('INTEGER_POLYTOPE_COMPARISON_PASSED',dims,lam,count)
    for m in range(2,30):
        for lam in [.1,.4,1.2,3.,8.]:
            B=1/(exp(lam/m)-1)-m/(exp(lam)-1)
            k=ceil(B)
            assert 1<=k<m
            assert isclose(M(m,lam),exp(-lam*k/m)*(1+k*(exp(lam)-1)/m),rel_tol=1e-9)
    print('ALL_CARDINALITY_STAIRCASE_TESTS_PASSED',28*5)
    lam=1.; p=1/lam-1/(exp(lam)-1)
    for m in range(50,401):
        a=log((exp(lam)-1)/lam)-1+lam/(exp(lam)-1)
        b=log(M(m,lam))
        approx=(lam**2)/(2*m**2)*min((m*p-round(m*p))**2,(m*p-(round(m*p)+1))**2)
        assert abs(a-b-approx)<2/m**3, (m,a-b,approx)
    print('SECOND_ORDER_ALPHABET_ENVELOPE_PASSED',351)
    print('ALL_LIPSCHITZ_EXPONENTIAL_DIAGNOSTICS_PASSED',total)
if __name__=='__main__':main()
