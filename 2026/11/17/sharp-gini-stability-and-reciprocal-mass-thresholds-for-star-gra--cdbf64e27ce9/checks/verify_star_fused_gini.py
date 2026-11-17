#!/usr/bin/env python3
"""Exact-rational diagnostics for star-graph fusion and Gini stability.

Standard-library only. Finite tests support, but do not replace, the
unrestricted elementary algebraic argument in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def gini(x):
    return sum((abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1,len(x))),Q(0))


def clamp(v,l):
    return min(l,max(-l,v))


def star_prox(z,a,lam):
    """Exact weighted quadratic/absolute-edge proximal solution for a star."""
    penalties = [lam]*(len(z)-1) if not isinstance(lam,(list,tuple)) else list(lam)
    candidates=sorted(set([min(z),max(z)]+[v+s*l for v,l in zip(z[1:],penalties) for s in [-1,1] if min(z)<v+s*l<max(z)]))
    if len(candidates)==1: return list(z)
    for left,right in zip(candidates,candidates[1:]):
        mid=(left+right)/2
        active=sum(abs(mid-v)<l for v,l in zip(z[1:],penalties))
        F=lambda h:a*(h-z[0])+sum((clamp(h-v,l) for v,l in zip(z[1:],penalties)),Q(0))
        h=mid-F(mid)/(a+active)
        if left<=h<=right and F(h)==0:
            return [h]+[h+max(v-h-l,Q(0))-max(h-v-l,Q(0)) for v,l in zip(z[1:],penalties)]
    raise AssertionError('root not found')


def gini_block(k,r,a,c,A,d):
    p=r+1;t=k-r;n=k+1
    m=(a*c+A)/(a+r)
    s=c+A+d
    return Q(p)*(d*(1-m)+(t-d)*m)+d*(t-d),s*(n-s)


def local_norm(k,r,a):
    if r==0:return Q(1)
    if r==k:return Q(0)
    return max(Q(1),Q((r+1)*(k-r),(k-r+1))/(a+r), Q((r+1)*(k-r),k)*a/(a+r))


def global_norm(k,a):
    return max(local_norm(k,r,a) for r in range(k+1))


def proposed(k,a):
    small=Q(2*(k-1),k)/(a+1)
    big=max(Q((r+1)*(k-r),k)*a/(a+r) for r in range(1,k))
    return max(Q(1),small,big)


def witness(k,r,a,which):
    assert 1<=r<k
    t=k-r
    lam=[Q(1+i%4,2) for i in range(k)]
    base=[-sum(lam[r:],Q(0))/a]+[Q(0)]*r+[Q(4)*v for v in lam[r:]]
    # At base the fitted hub and fused leaves are zero; other leaves fit 3.
    raw=star_prox(base,a,lam)
    assert raw==[Q(0)]*(r+1)+[Q(3)*v for v in lam[r:]]
    direction=[Q(0)]*(k+1)
    if which=='hub':direction[0]=Q(1)
    elif which=='fused-leaves':
        for j in range(1,r+1): direction[j]=Q(1)
    elif which=='whole-block':
        for j in range(r+1):direction[j]=Q(1)
    else:raise ValueError(which)
    eps=Q(1,10000)
    shifted=[base[i]+eps*direction[i] for i in range(k+1)]
    out=star_prox(shifted,a,lam)
    diff=[(out[i]-raw[i])/eps for i in range(k+1)]
    expected=(a*direction[0]+sum(direction[1:r+1]))/(a+r)
    assert diff==[expected]*(r+1)+direction[r+1:]
    return gini(diff)/gini(direction)


if __name__=='__main__':
    count=0
    for k in range(2,15):
        for a in [Q(1,20),Q(1,3),Q(1,2),Q(4,5),Q(1),Q(6,5),Q(2),Q(3),Q(5),Q(20)]:
            assert proposed(k,a)==global_norm(k,a)
            for r in range(1,k):
                val=local_norm(k,r,a)
                for c in [0,1]:
                    for A in range(r+1):
                        for d in range(k-r+1):
                            v,den=gini_block(k,r,a,c,A,d)
                            if 0<den: assert v<=val*den, (k,r,a,c,A,d,v,den,val)
                            count+=1
    print('EXHAUSTIVE_BINARY_CUT_LOCAL_NORMS_PASSED',count)
    count=0
    for k in range(2,14):
        for a in [Q(1,7),Q(1,2),Q(1),Q(2),Q(7)]:
            for r in range(1,k):
                for name,target in [('hub',Q((r+1)*(k-r),k)*a/(a+r)),('fused-leaves',Q((r+1)*(k-r),k-r+1)/(a+r)),('whole-block',Q(1))]:
                    assert witness(k,r,a,name)==target,(k,a,r,name)
                    count+=1
    print('EXACT_ACTUAL_PROXIMAL_WITNESSES_PASSED',count)
    count=0; rng=Random(20261109)
    for k in range(2,10):
        for a in [Q(1,3),Q(1),Q(3),Q(11)]:
            for _ in range(180):
                x=[Q(rng.randrange(-50,51),5) for i in range(k+1)]
                y=[Q(rng.randrange(-50,51),5) for i in range(k+1)]
                penalties=[Q(1+j%5,3) for j in range(k)]
                outx=star_prox(x,a,penalties);outy=star_prox(y,a,penalties)
                assert gini([outx[i]-outy[i] for i in range(k+1)])<=global_norm(k,a)*gini([x[i]-y[i] for i in range(k+1)])
                count+=1
    print('EXACT_RANDOM_TWO_INPUT_INEQUALITIES_PASSED',count)
    for k in range(3,35):
        lo=Q(k-2,k); hi=Q(k,k-2)
        assert global_norm(k,lo)==1 and global_norm(k,hi)==1
        assert global_norm(k,lo*Q(99,100))>1 and global_norm(k,hi*Q(101,100))>1
        high_limit=max((r+1)*(k-r) for r in range(1,k))
        assert high_limit==((k+1)**2//4)
    print('SHARP_RECIPROCAL_MASS_THRESHOLDS_AND_ENVELOPE_PASSED')
    print('ALL_STAR_FUSION_GINI_DIAGNOSTICS_PASSED')
