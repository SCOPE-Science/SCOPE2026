"""Reproducibility checks for a sharp three-vertex fractional maximal stability theorem.

This program checks representative branch identities, strict interior witnesses,
and numerical inequalities. The analytic proof is in RESULT.md; finite checks
are not claimed to certify every real parameter or input.
"""
import itertools
import math
import random


def parameters(alpha):
    return 2.0 ** (alpha - 1.0), 3.0 ** (alpha - 1.0)


def critical():
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        a, h = parameters(mid)
        if a + h > 1.0: hi = mid
        else: lo = mid
    return (lo + hi) / 2.0


def value(u, alpha):
    a, h = parameters(alpha)
    x, y, z = u
    S = x + y + z
    return (max(x, h*S), max(y, a*(x+y), h*S),
            max(z, a*(x+z), h*S))


def branches(alpha):
    a, h = parameters(alpha)
    return (( (1.,0.,0.), (h,h,h) ),
            ( (0.,1.,0.), (a,a,0.), (h,h,h) ),
            ( (0.,0.,1.), (a,0.,a), (h,h,h) ))


def energy(y):
    return (y[1]-y[0])**2+(y[2]-y[0])**2


def dot(u, v):
    return sum(x*y for x, y in zip(u, v))


def sub(u, v):
    return tuple(x-y for x, y in zip(u, v))


def norm2(u):
    return dot(u,u)


def branch_rows(alpha, sel):
    r = branches(alpha)
    b = [r[j][k] for j,k in enumerate(sel)]
    return sub(b[1],b[0]), sub(b[2],b[0])


def lambda_two_rows(u,v):
    x,y,z = dot(u,u), dot(v,v), dot(u,v)
    return (x+y+math.sqrt((x-y)**2+4*z*z))/2


def formula(alpha):
    a,h = parameters(alpha)
    crit = critical()
    v = 2.0-4.0*h+6.0*h*h
    if alpha >= crit:
        return v
    return (3.0-2.0*h+3.0*h*h+math.sqrt((1.0+2.0*h-3.0*h*h)**2+4.0))/2.0


def selection(u, alpha):
    rr=branches(alpha)
    return tuple(max(range(len(candidates)), key=lambda k: dot(u,candidates[k]))
                 for candidates in rr)


def interior_witness(alpha):
    a,h=parameters(alpha)
    if alpha < critical():
        # Construct a strict (hub singleton, first leaf singleton, second leaf global) region.
        initial=(h, a*h/(1.0-a), 1.0-h/(1.0-a))
        # Increase first two coordinates along a positive direction at fixed mass.
        delta=1e-5 * min(1.0,initial[2])
        x=h+delta
        y=a*x/(1.0-a)+delta
        z=1.0-x-y
        u=(x,y,z)
        wanted=(0,0,2)
    else:
        upper=2*h/a-1.0
        x=(h+upper)/2
        u=(x,(1-x)/2,(1-x)/2)
        wanted=(0,2,2)
    rr=branches(alpha)
    assert min(u)>0, (alpha,u)
    for i,k in enumerate(wanted):
        for j,v in enumerate(rr[i]):
            if j != k:
                assert dot(u,rr[i][k])-dot(u,v)>1e-12, (alpha,i,j,u)
    assert selection(u,alpha)==wanted,(alpha,u,selection(u,alpha))
    return u,wanted


def witness_ratio(alpha):
    u,sel=interior_witness(alpha)
    r,s=branch_rows(alpha,sel)
    if sel==(0,0,2):
        la=lambda_two_rows(r,s)
        w=tuple(x+(la-2)*y for x,y in zip(r,s))
    else:
        w=s
    wnorm=math.sqrt(norm2(w))
    w=tuple(x/wnorm for x in w)
    margin=1e300
    for i,k in enumerate(sel):
        rr=branches(alpha)[i]
        for j,v in enumerate(rr):
            if j==k:continue
            gap=dot(u,sub(rr[k],v))
            speed=abs(dot(w,sub(rr[k],v)))
            if speed>0: margin=min(margin,gap/speed)
    eps=min(1e-4,margin/20, min(x/(20*abs(y)) for x,y in zip(u,w) if y!=0))
    v=tuple(x+eps*y for x,y in zip(u,w))
    assert selection(v,alpha)==sel
    q=math.sqrt(energy(sub(value(v,alpha),value(u,alpha)))/norm2(sub(v,u)))
    expected=math.sqrt(formula(alpha))
    assert abs(q-expected)<2e-6, (alpha,q,expected)
    return q


def main():
    root=critical()
    assert 0.21211<root<0.21212
    alphas=(0.005,0.02,0.1,0.2,root-1e-4,root+1e-4,0.25,0.4,0.5,0.8,0.99)
    rng=random.Random(17439)
    for alpha in alphas:
        a,h=parameters(alpha)
        goal=formula(alpha)
        assert 0.5<a<1 and 1/3<h<a
        assert 2*h/a-1>h
        assert goal>=0
        if alpha<root:
            assert a+h<1
            assert goal>=2
        else:
            assert a+h>1
        witness_ratio(alpha)
        # Compare the predicted sharp coefficient against all branches that
        # actually occur in 10000 random strictly positive input vectors.
        seen=set()
        for _ in range(10000):
            u=[math.exp(rng.uniform(-9,9)) for _ in range(3)]
            sel=selection(u,alpha)
            seen.add(sel)
            rr,ss=branch_rows(alpha,sel)
            assert lambda_two_rows(rr,ss)<=goal+1e-10,(alpha,sel)
            v=[math.exp(rng.uniform(-9,9)) for _ in range(3)]
            e=energy(sub(value(v,alpha),value(u,alpha)))
            assert e<=goal*norm2(sub(u,v))+1e-6,(alpha,u,v,e)
        print(f'alpha={alpha:.9f}, C={math.sqrt(goal):.12f}, observed_strata={len(seen)}')
    h=parameters(root)[1]
    left=(3-2*h+3*h*h+math.sqrt((1+2*h-3*h*h)**2+4))/2
    right=2-4*h+6*h*h
    assert left-right>1
    print(f'critical_alpha={root:.15f}; left={math.sqrt(left):.12f}; at_and_right={math.sqrt(right):.12f}')
    print('PASS: 11 witness constructions, 110000 random branch/difference checks, transition checks.')

if __name__=='__main__':
    main()
