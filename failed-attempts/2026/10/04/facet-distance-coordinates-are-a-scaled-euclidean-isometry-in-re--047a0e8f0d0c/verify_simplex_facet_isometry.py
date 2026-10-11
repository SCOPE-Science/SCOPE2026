#!/usr/bin/env python3
import math, random

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return [x-y for x,y in zip(a,b)]
def norm2(a): return dot(a,a)
def add_scaled(dst,a,s):
    for j,x in enumerate(a): dst[j]+=s*x

def vertices(n):
    # Unit-circumradius regular n-simplex in the sum-zero hyperplane of R^(n+1).
    c=math.sqrt((n+1)/n)
    m=n+1
    out=[]
    for i in range(m):
        out.append([c*((1.0 if i==j else 0.0)-1.0/m) for j in range(m)])
    return out

def point_from_bary(V,lam):
    p=[0.0]*len(V[0])
    for a,v in zip(lam,V): add_scaled(p,v,a)
    return p

def sample_bary(m,rng):
    x=[rng.expovariate(1.0) for _ in range(m)]
    s=sum(x)
    return [z/s for z in x]

def check():
    rng=random.Random(210031)
    worst_metric=0.0
    worst_sum=0.0
    worst_radial=0.0
    worst_inverse=0.0
    worst_bary=0.0
    tests=0
    for n in range(2,13):
        V=vertices(n)
        r=1.0/n
        H=(n+1)*r
        # frame and vertex geometry
        for i,u in enumerate(V):
            assert abs(norm2(u)-1.0)<2e-14
            for j,v in enumerate(V):
                target=1.0 if i==j else -1.0/n
                assert abs(dot(u,v)-target)<3e-14
        for _ in range(1200):
            la=sample_bary(n+1,rng); lb=sample_bary(n+1,rng)
            p=point_from_bary(V,la); q=point_from_bary(V,lb)
            da=[H*x for x in la]; db=[H*x for x in lb]
            worst_sum=max(worst_sum,abs(sum(da)-H),abs(sum(db)-H))
            lhs=norm2(sub(p,q))
            rhs=n/(n+1)*sum((a-b)**2 for a,b in zip(da,db))
            worst_metric=max(worst_metric,abs(lhs-rhs))
            radial=sum((x-r)**2 for x in da)
            target=(n+1)/n*norm2(p)
            worst_radial=max(worst_radial,abs(radial-target))
            # d_i/H must recover the barycentric coordinate.
            worst_bary=max(worst_bary,max(abs(da[i]/H-la[i]) for i in range(n+1)))
            # p = n/(n+1) sum_i (d_i-r) u_i
            rec=[0.0]*(n+1)
            for di,u in zip(da,V): add_scaled(rec,u,n/(n+1)*(di-r))
            worst_inverse=max(worst_inverse,math.sqrt(norm2(sub(rec,p))))
            tests+=1
    print(f"tests={tests}")
    print(f"worst_metric_error={worst_metric:.3e}")
    print(f"worst_sum_error={worst_sum:.3e}")
    print(f"worst_radial_error={worst_radial:.3e}")
    print(f"worst_inverse_error={worst_inverse:.3e}")
    print(f"worst_bary_error={worst_bary:.3e}")
    assert worst_metric < 2e-12
    assert worst_sum < 2e-12
    assert worst_radial < 2e-12
    assert worst_inverse < 2e-12
    assert worst_bary < 2e-12
    print("VERIFY_OK")

if __name__=='__main__': check()
