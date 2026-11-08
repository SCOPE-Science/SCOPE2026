"""Independent small-dimensional exact simplex integration for complete-multipartite stable-set polytopes.
Requires scipy and sympy. Run python geometry_stable_set_moment_checker.py.
"""
import itertools
import math
from fractions import Fraction as F
import sympy as sp
import numpy as np
from scipy.spatial import ConvexHull

def vertices(parts):
    n=sum(parts); out={tuple([0]*n)}; offset=0
    for m in parts:
        for bits in itertools.product((0,1),repeat=m):
            x=[0]*n;x[offset:offset+m]=bits;out.add(tuple(x))
        offset+=m
    return sorted(out)

def expected(parts):
    n=sum(parts); q=(n+1)*(n+2)
    labels=[i for i,m in enumerate(parts) for _ in range(m)]
    mean=[F(parts[i]+1,2*(n+1)) for i in labels]
    moment=sp.zeros(n)
    for p in range(n):
        for k in range(n):
            a=parts[labels[p]]+1;b=parts[labels[k]]+1
            if p==k:moment[p,k]=sp.Rational(a*(a+1),3*q)
            elif labels[p]==labels[k]:moment[p,k]=sp.Rational(a*(a+1),4*q)
            else:moment[p,k]=sp.Rational(a*b,4*q)
    volume=F(math.prod(math.factorial(m) for m in parts),math.factorial(n))
    return sp.Rational(volume.numerator,volume.denominator),sp.Matrix(mean),moment

def integrate_polytope(parts):
    vv=vertices(parts);n=sum(parts)
    arr=np.array(vv,dtype=float)
    hull=ConvexHull(arr)
    # Average of all distinct 0-1 polytope vertices is a strict interior point.
    c=sp.Matrix([sp.Rational(sum(v[j] for v in vv),len(vv)) for j in range(n)])
    total=sp.S.Zero; first=sp.zeros(n,1); second=sp.zeros(n)
    for fac in hull.simplices:
        pts=[c]+[sp.Matrix(vv[i]) for i in fac]
        det=sp.det(sp.Matrix.hstack(*[v-c for v in pts[1:]]))
        if not det: continue # Qhull may return zero-volume simplices on nonsimplicial supporting faces
        vol=abs(det)/sp.factorial(n)
        v_sum=sum(pts,sp.zeros(n,1))
        second_s=v_sum*v_sum.T+sum((v*v.T for v in pts),sp.zeros(n))
        total+=vol
        first+=vol*v_sum/(n+1)
        second+=vol*second_s/((n+1)*(n+2))
    return total,first/total,second/total,len(hull.simplices)

def compositions(n):
    if n==0:yield ()
    for m in range(1,n+1):
        for r in compositions(n-m): yield (m,)+r

def inertia(parts):
    n=sum(parts);den=12*(n+1)**2*(n+2)
    return sp.Rational(sum((n-2)*m**3+6*n*m*m+(5*n+2)*m for m in parts),den)

def main():
    cases=0; simplices=0
    for n in range(2,6):
        seen=set()
        for p in compositions(n):
            if tuple(sorted(p)) in seen: continue
            seen.add(tuple(sorted(p)))
            v0,m0,s0=expected(p)
            v,m,s,ns=integrate_polytope(p)
            assert v==v0,(p,'volume',v,v0)
            assert m==m0,(p,'means',m,m0)
            assert s==s0,(p,'moments',s,s0)
            assert sp.trace(s-m*m.T)==inertia(p),(p,'trace')
            if len(p)>1:
                for i in range(n):
                    for j in range(i+1,n):
                        grp=[k for k,m in enumerate(p) for _ in range(m)]
                        assert (s-m*m.T)[i,j]!=0
                        assert ((s-m*m.T)[i,j]<0)==(grp[i]!=grp[j])
            cases+=1; simplices+=ns
    print('MULTIPARTITE_STAB_EXACT_SIMPLEX_MOMENTS_PASSED',cases,simplices)

if __name__=='__main__': main()

def moment_formula(parts, power):
    n=sum(parts)
    assert len(power)==n
    offset=0
    product=sp.S.One
    for m in parts:
        a=sum(power[offset:offset+m]); offset+=m
        product*=sp.rf(m+1,a)
    for exponent in power:
        product/=exponent+1
    return sp.factor(product/sp.rf(n+1,sum(power)))

def simplices_for(parts):
    vv=vertices(parts);n=sum(parts)
    hull=ConvexHull(np.array(vv,dtype=float))
    c=sp.Matrix([sp.Rational(sum(v[j] for v in vv),len(vv)) for j in range(n)])
    out=[]
    for f in hull.simplices:
        pts=[c]+[sp.Matrix(vv[i]) for i in f]
        det=sp.det(sp.Matrix.hstack(*[v-c for v in pts[1:]]))
        if det: out.append((pts,abs(det)/sp.factorial(n)))
    return out

def monomial_on_simplex(pts,power):
    n=len(power); degree=sum(power); nv=n+1
    zero=(0,)*nv
    coeff={zero:sp.S.One}
    for j,k in enumerate(power):
        for unused in range(k):
            new={}
            for exp, val in coeff.items():
                for v in range(nv):
                    if pts[v][j]==0: continue
                    new_exp=exp[:v]+(exp[v]+1,)+exp[v+1:]
                    new[new_exp]=new.get(new_exp,sp.S.Zero)+val*pts[v][j]
            coeff=new
    fac=sp.factorial(n)/sp.factorial(n+degree)
    return sp.factor(fac*sum((val*sp.prod(sp.factorial(e) for e in exps)
                              for exps,val in coeff.items()),sp.S.Zero))

def test_higher_moments():
    checked=0
    for n in range(2,5):
        seen=set()
        for parts in compositions(n):
            key=tuple(sorted(parts))
            if key in seen:continue
            seen.add(key)
            simplices=simplices_for(parts)
            total=sum((v for _,v in simplices),sp.S.Zero)
            for total_degree in (3,4):
                for power in itertools.product(range(total_degree+1),repeat=n):
                    if sum(power)!=total_degree: continue
                    exact=sum((vol*monomial_on_simplex(pts,power)
                               for pts,vol in simplices),sp.S.Zero)/total
                    predicted=moment_formula(parts,power)
                    assert exact==predicted,(parts,power,exact,predicted)
                    checked+=1
    print('MULTIPARTITE_STAB_ALL_MOMENTS_CUBIC_QUARTIC_CHECKS_PASSED',checked)

if __name__=='__main__': test_higher_moments()
