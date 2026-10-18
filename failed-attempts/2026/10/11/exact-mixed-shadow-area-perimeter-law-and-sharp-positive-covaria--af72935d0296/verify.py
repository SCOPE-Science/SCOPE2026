#!/usr/bin/env python3
"""Independent finite Haar two-plane checks for mixed projected area/perimeter of a four-orthotope.
Only the analytic integration establishes the all-parameter theorem.
"""
import itertools,math,random
rng=random.Random(1647);N=180000
pairs=list(itertools.combinations(range(4),2))
sides=[(1.,1.,1.,1.),(1.,2.,3.,4.),(.7,1.3,2.0,4.5)]
def theory(a):
    spairs=sum(a[i]*a[j]*(a[i]+a[j]) for i,j in pairs)
    striple=sum(math.prod(a[k] for k in inds) for inds in itertools.combinations(range(4),3))
    return .5*spairs+3*math.pi/8*striple
sums=[0.]*len(sides);incident=0.;disjoint=0.
def unit4():
    q=[rng.gauss(0,1) for _ in range(4)]
    n=math.sqrt(sum(x*x for x in q))
    return [x/n for x in q]
for _ in range(N):
    u=unit4();v=unit4();d=sum(x*y for x,y in zip(u,v));v=[y-d*x for x,y in zip(u,v)];r=math.sqrt(sum(x*x for x in v));v=[x/r for x in v]
    r=[math.hypot(u[k],v[k]) for k in range(4)]
    p=[abs(u[i]*v[j]-u[j]*v[i]) for i,j in pairs]
    incident+=p[0]*r[0]
    disjoint+=p[5]*r[0]
    for k,ss in enumerate(sides):
        aa=sum(ss[i]*ss[j]*p[h] for h,(i,j) in enumerate(pairs))
        pp=2*sum(ss[i]*r[i] for i in range(4))
        sums[k]+=aa*pp
print('incidence',incident/N,'theory 1/4')
print('nonincidence',disjoint/N,'theory pi/16',math.pi/16)
assert abs(incident/N-.25)<.004
assert abs(disjoint/N-math.pi/16)<.004
for aa,ss in zip(sums,sides):
    th=theory(ss)
    print(ss,aa/N,th,'relative discrepancy',abs(aa/N/th-1))
    assert abs(aa/N-th)< .012*th
print('unit cube analytic EA=2, EP=16/3, EAP=',theory(sides[0]),'covariance=',theory(sides[0])-32/3)
assert abs(theory(sides[0])-(6+1.5*math.pi))<1e-12
print('VERIFY_OK',N,'independent 4D Haar Gram-Schmidt checks')
