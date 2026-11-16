#!/usr/bin/env python3
"""Independent exact checks for signed spanning-tree Walsh norms on K_{3,n}.
Standard library only. Finite checks corroborate, but do not prove, the limit theorem.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import sqrt


def signed_schur(columns):
    prod = 1
    w = [Fraction(0), Fraction(0), Fraction(0)]
    for a, b, c in columns:
        s = a + b + c
        assert s != 0
        prod *= s
        for j, pair in enumerate((a*b, a*c, b*c)):
            w[j] += Fraction(pair, s)
    value = prod * (w[0]*w[1] + w[0]*w[2] + w[1]*w[2])
    assert value.denominator == 1
    return int(value)


def signed_combinatorial(columns):
    n=len(columns)
    s=[sum(col) for col in columns]
    prod_omit=lambda om: product_int(s[k] for k in range(n) if k not in om)
    total=sum(a*b*c*prod_omit({i}) for i,(a,b,c) in enumerate(columns))
    for i in range(n):
        ai,bi,ci=columns[i]
        u=(ai*bi,ai*ci,bi*ci)
        for j in range(i+1,n):
            aj,bj,cj=columns[j]
            v=(aj*bj,aj*cj,bj*cj)
            total+=sum(u[r]*v[t] for r in range(3) for t in range(3) if r!=t)*prod_omit({i,j})
    return total


def product_int(xs):
    out=1
    for x in xs:out*=x
    return out


def is_spanning_tree(mask,n):
    parent=list(range(n+3))
    def root(x):
        while x!=parent[x]:
            x=parent[x]
        return x
    if mask.bit_count()!=n+2:
        return False
    for edge in range(3*n):
        if (mask>>edge)&1:
            u,v=edge//n,3+edge%n
            u,v=root(u),root(v)
            if u==v:return False
            parent[u]=v
    return True


def walsh(values):
    a=values.copy()
    h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a


def exact_dp_norms(N):
    # Weights |a+b+c| are integers adding to 12; Y=3(ab/s,ac/s,bc/s).
    steps=[]
    for a,b,c in product((1,-1), repeat=3):
        s=a+b+c
        steps.append(((3*a*b//s,3*a*c//s,3*b*c//s),abs(s)))
    assert sum(w for _,w in steps)==12
    # Check zero mean and covariance 5/9 (diagonal), -1/9 (off-diagonal).
    for i in range(3):
        assert sum(w*y[i] for y,w in steps)==0
        for j in range(3):
            cov=sum(w*y[i]*y[j] for y,w in steps)
            assert Fraction(cov,12*9)==(Fraction(5,9) if i==j else Fraction(-1,9))
    states={(0,0,0):1}
    results=[]
    for n in range(1,N+1):
        new=defaultdict(int)
        for (x,y,z),count in states.items():
            for (a,b,c),weight in steps:
                new[(x+a,y+b,z+c)]+=count*weight
        states=new
        assert sum(states.values())==12**n
        # E_uniform |W| = (3/2)^n E_tilt |Phi(sum_i X_i)|.
        numerator=sum(cnt*abs(x*y+x*z+y*z) for (x,y,z),cnt in states.items())
        norm=Fraction(3**n*numerator,2**n*9*12**n)
        results.append(norm)
    return results


def run():
    dps=exact_dp_norms(16)
    for n in range(1,6):
        m=3*n; tot=1<<m
        indicator=[int(is_spanning_tree(mask,n)) for mask in range(tot)]
        assert sum(indicator)==n*n*3**(n-1)
        transform=walsh(indicator)
        assert transform[0]==n*n*3**(n-1)
        for mask,val in enumerate(transform):
            columns=[tuple(-1 if mask>>(a*n+i)&1 else 1 for a in range(3)) for i in range(n)]
            assert val==signed_schur(columns)==signed_combinatorial(columns),(n,mask,val)
        direct=Fraction(sum(abs(x) for x in transform),tot)
        assert direct==dps[n-1],(n,direct,dps[n-1])
        print(f'n={n} |trees|={sum(indicator)} norm={direct} full_walsh_checked={tot}')
    # Exact iterative distribution through n=16; Gaussian limit is proven analytically.
    print('n=16 exact-normalized-ratio:',format(float(dps[15]/(16*Fraction(3,2)**16)),'.12f'))
    print('asymptotic-constant:',format((2*sqrt(2)-1)/3,'.12f'))
    print('K3N_SIGNED_TREE_FOURIER_AND_TILT_DP_PASS')

if __name__=='__main__':run()
