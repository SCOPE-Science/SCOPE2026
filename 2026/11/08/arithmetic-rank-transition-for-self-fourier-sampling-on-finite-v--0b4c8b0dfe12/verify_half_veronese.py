#!/usr/bin/env python3
"""Independent direct Fourier-matrix and Gauss-period tests for the rank-one Veronese sampling theorem.
Requires Python 3 and NumPy. Run: python verify_half_veronese.py
"""
import cmath
import math
import numpy as np


def model(p, d=None):
    """F_p if d absent; otherwise F_{p^2}=F_p[T]/(T^2-d), d nonsquare."""
    q=p if d is None else p*p
    if d is not None: assert pow(d,(p-1)//2,p)==p-1
    def add(x,y):
        if d is None: return (x+y)%p
        return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
    def mul(x,y):
        if d is None: return x*y%p
        a,b=x%p,x//p; c,e=y%p,y//p
        return ((a*c+d*b*e)%p)+p*((a*e+b*c)%p)
    def neg(x): return (((-x)%p) if d is None else (-x%p)+p*(-(x//p)%p))
    def sub(x,y): return add(x,neg(y))
    def power(x,n):
        z=1
        while n:
            if n&1:z=mul(z,x)
            x=mul(x,x); n//=2
        return z
    def trace(x): return x if d is None else (2*(x%p))%p
    g=next(g for g in range(2,q) if len({power(g,j) for j in range(q-1)})==q-1)
    return q,add,mul,sub,trace,power,g


def verify(p,d=None,full_matrix=True):
    q,add,mul,sub,trace,power,g=model(p,d)
    h=(q-1)//2
    gen=mul(g,g)
    H=[power(gen,j) for j in range(h)]
    assert len(set(H))==h
    root=cmath.exp(2j*math.pi/p)
    periods=[sum(root**trace(H[j])*cmath.exp(2j*math.pi*k*j/h) for j in range(h)) for k in range(h)]
    expected=[abs(h+q*periods[0])]+[abs(h-periods[0])]*q
    for k in range(1,h): expected += [math.sqrt(q)*abs(periods[k])]*(q+1)
    N=(q+1)*h
    assert len(expected)==N
    if full_matrix:
        reps=[(1,u) for u in range(q)]+[(0,1)]
        points=[]
        for x,y in reps:
            for s in H: points.append((mul(s,mul(x,x)),mul(s,mul(x,y)),mul(s,mul(y,y))))
        assert len(set(points))==N
        mat=np.empty((N,N),dtype=np.complex128)
        for i,(a,b,c) in enumerate(points):
            for j,(A,B,C) in enumerate(points):
                t=sub(add(mul(a,C),mul(c,A)),add(mul(b,B),mul(b,B)))
                mat[i,j]=root**trace(t)
        vals=np.linalg.svd(mat,compute_uv=False)
        err=max(abs(x-y) for x,y in zip(sorted(expected),sorted(vals)))
        assert err<3e-9,(q,err)
        direct_zeros=sum(s<2e-8 for s in vals)
        expected_zeros=sum(s<2e-8 for s in expected)
        assert direct_zeros==expected_zeros,(q,direct_zeros,expected_zeros)
        print('q=',q,'size=',N,'formula_error=',f'{err:.3g}','kernel=',direct_zeros)
    else:
        print('q=',q,'size=',N,'period_spectrum_formula=structural','period_zeros=',sum(abs(x)<1e-8 for x in periods[1:]))
    if d is not None and p%4==1:
        # Trace-zero line excludes the square subgroup: an exact finite-field assertion.
        assert all(trace(t)!=0 for t in H)
        Q=(p+1)//2
        assert h==(p-1)*Q
        # Characters of H trivial on F_p^x are precisely k divisible by p-1;
        # all nontrivial such characters have period zero.
        for k in range(p-1,h,p-1):
            # Character sums are numerically zero, with exact proof by F_p-line decomposition.
            assert abs(periods[k])<1e-8,(q,k,periods[k])
        assert sum(abs(periods[k])<1e-8 for k in range(1,h))>=Q-1
        print('  exact_trace_fiber_kernel_lower_bound=',(Q-1)*(q+1))
    if d is None:
        assert all(abs(z)>1e-8 for z in periods)
        assert all(s>1e-8 for s in expected)


if __name__=='__main__':
    for p,d in ((3,None),(5,None),(7,None),(11,None),(3,2),(5,2)):
        verify(p,d)
    verify(13,2,full_matrix=False)
    print('VERONESE_ARITHMETIC_PHASE_TRANSITION_PASS')
