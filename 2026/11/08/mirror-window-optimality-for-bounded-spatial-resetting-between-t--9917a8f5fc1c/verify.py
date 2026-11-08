#!/usr/bin/env python3
"""Deterministic verification of the two-exit bounded spatial-resetting theorem.
Run: python3 verify.py (Python standard library only).
Numerical tests are cross-checks; the universal proof is in RESULT.md.
"""
import math


def formula(x, L, D, rate, a):
    if a > L/2:
        return formula(L-x, L, D, rate, L-a)
    if a == L/2:
        return x*(L-x)/(2*D)
    k = math.sqrt(rate/D)
    delta = L/2-a
    s = math.tanh(k*delta)/math.sqrt(D*rate)
    va = a*a/(2*D)+a*s
    if x <= a:
        return x*(2*a-x)/(2*D)+s*x
    if x <= L-a:
        # Cosh ratio is well behaved in the tested range.
        return va + (1-math.cosh(k*(x-L/2))/math.cosh(k*delta))/rate
    z = L-x
    return z*(2*a-z)/(2*D)+s*z


def tri_solve(diag, off, rhs):
    n=len(diag)
    b=list(diag)
    d=list(rhs)
    for i in range(1,n):
        mult=off/b[i-1]
        b[i]-=mult*off
        d[i]-=mult*d[i-1]
    out=[0.]*n
    out[-1]=d[-1]/b[-1]
    for i in range(n-2,-1,-1):
        out[i]=(d[i]-off*out[i+1])/b[i]
    return out


def evaluate_policy(N,D,L,a_index, rates):
    step=L/N
    d=D/(step*step)
    diag=[2*d+q for q in rates]
    rhs=[1.]*(N-1)
    y=tri_solve(diag,-d,rhs)
    z=tri_solve(diag,-d,rates)
    j=a_index-1
    v_at_a=y[j]/(1-z[j])
    return [0.]+[y[i]+z[i]*v_at_a for i in range(N-1)]+[0.]


def optimize_lattice(N,D,L,R,a_index):
    rates=[0.]*(N-1)
    for sweep in range(30):
        v=evaluate_policy(N,D,L,a_index,rates)
        new_rates=[R if v[j]>v[a_index]+1.e-11 else 0. for j in range(1,N)]
        if rates==new_rates:
            return v, rates, sweep
        rates=new_rates
    raise AssertionError('lattice policy iteration did not terminate')


def run():
    comparisons=0
    for N in (80,160,320):
        for a_index in (N//8,N//4,3*N//8,N//2,5*N//8):
            a=a_index/N
            for R in (0.3, 1.0, 7.0, 30.0):
                values,rates,sweeps=optimize_lattice(N,1.,1.,R,a_index)
                lo=min(a_index,N-a_index)
                hi=max(a_index,N-a_index)
                expected=[R if lo<j<hi else 0. for j in range(1,N)]
                assert rates==expected,(N,a,R,sweeps)
                # The piecewise analytic value is second-order consistent with a lattice model.
                errors=[abs(values[j]-formula(j/N,1.,1.,R,a)) for j in range(N+1)]
                assert max(errors)<8./N**2,(N,a,R,max(errors))
                comparisons+=N+1
                if a!=.5:
                    target=formula(a,1.,1.,R,a)
                    noreset=a*(1.-a)/2
                    assert 0<target<noreset
                else:
                    assert abs(formula(a,1.,1.,R,a)-.125)<1.e-12
    # Independent differential/smooth-fit identities at interfaces.
    for L,D,R,a in ((1.,.3,2.,.14),(5.,3.,7.,1.1),(2.,.7,11.,.73)):
        k=math.sqrt(R/D);delta=L/2-a
        s=math.tanh(k*delta)/math.sqrt(D*R)
        left_der=s
        inside_der=k/R*math.tanh(k*delta)
        assert abs(left_der-inside_der)<1.e-13
        assert abs((-1/D)-(-k*k/R))<1.e-12
        v_left=formula(a-1.e-8,L,D,R,a)
        v_right=formula(a+1.e-8,L,D,R,a)
        assert abs(v_right-v_left)<1.e-6
        for x in (a/2, (a+L/2)/2,L/2,L-a/2):
            dx=1.e-4*min(a,L/2-a)
            d2=(formula(x+dx,L,D,R,a)-2*formula(x,L,D,R,a)+formula(x-dx,L,D,R,a))/dx**2
            v=formula(x,L,D,R,a)
            va=formula(a,L,D,R,a)
            residual=1+D*d2+min(0.,R*(va-v))
            assert abs(residual)<2.e-5, residual
    print('PASS: independent tridiagonal lattice policy iteration and analytic HJB checks')
    print('Lattice values compared:', comparisons)
    print('Global policies tested:', 3*5*4)


if __name__=='__main__':
    run()
