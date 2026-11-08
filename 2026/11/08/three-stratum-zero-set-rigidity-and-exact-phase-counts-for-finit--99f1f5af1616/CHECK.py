"""Exact finite checks for the finite-parabola power-of-two phase classification.
Only integer operations; the theorem for arbitrary primes and supports is proved separately.
"""
from itertools import combinations, product
from math import comb, factorial


def cyclotomic_vectors(p, q):
    # phi_(p*2^s)(X)=sum_{j=0}^{p-1}(-1)^j X^(j*q/2).
    d = (p-1)*(q//2)
    f=[0]*(d+1)
    for j in range(p): f[j*q//2]=(-1)**j
    assert f[-1]==1
    v=[0]*d;v[0]=1; powers=[]
    for _ in range(p*q):
        powers.append(tuple(v))
        z=v[-1]
        v=[0]+v[:-1]
        for i in range(d):v[i]-=z*f[i]
    assert all(v[i]==(i==0) for i in range(d))
    return powers


def predicted(p,q,R,phases):
    terms=[(R[j],phases[j]) for j in range(len(R))]
    q2=q//2
    counts=[0]*q
    for e in phases:counts[e]+=1
    origin=all(counts[t]==counts[t+q2] for t in range(q2))
    if not origin:return set()
    linecenter=None
    if len(R)%2==0:
        for c in range(p):
            if all(((2*c-x)%p in R and phases[R.index((2*c-x)%p)] == (phases[R.index(x)]+q2)%q) for x in R):
                linecenter=c;break
    return {(0,0)} if linecenter is None else {(a,(-2*a*linecenter)%p) for a in range(p)}


def arithmetic_A(q,r):
    m=q//2
    total=0
    for ts in product(range(r+1),repeat=m):
        if sum(ts)==r:
            den=1
            for t in ts:den*=factorial(t)**2
            total+=factorial(2*r)//den
    return total


def check(p,q,max_k,restrict=None):
    powv=cyclotomic_vectors(p,q)
    n=p*q;d=len(powv[0])
    # F(a,b) == sum zeta_(p*q)^(q*(a*x*x+b*x)+p*e).
    bank=[[[powv[(q*((a*x*x+b*x)%p)+p*e)%n] for a in range(p) for b in range(p)] for e in range(q)] for x in range(p)]
    cases=0; points=0; hist={}
    for k in range(1,max_k+1):
        for R in combinations(range(p),k):
            if restrict is not None and R not in restrict: continue
            totals={0:0,1:0,p:0}
            for phases in product(range(q),repeat=k):
                got=set()
                zrows=[bank[x][e] for x,e in zip(R,phases)]
                for a in range(p):
                    for b in range(p):
                        offset=a*p+b
                        sums=[0]*d
                        for row in zrows:
                            vec=row[offset]
                            for j in range(d):sums[j]+=vec[j]
                        if not any(sums):got.add((a,b))
                target=predicted(p,q,R,phases)
                assert got==target,(p,q,R,phases,got,target)
                totals[len(got)]+=1
                cases+=1;points+=p*p
            if k%2:
                want={0:q**k,1:0,p:0}
            else:
                r=k//2;A=arithmetic_A(q,r)
                symmetric=any(all((2*c-x)%p in R for x in R) for c in range(p))
                L=q**r if symmetric else 0
                want={0:q**k-A,1:A-L,p:L}
            assert totals==want,(p,q,R,totals,want)
            for n0,v in totals.items(): hist[n0]=hist.get(n0,0)+v
    return cases,points,hist

if __name__=='__main__':
    grand=0;freq=0
    for p,q,m,restriction in [(5,2,4,None),(5,4,4,None),(5,8,4,None),(7,2,4,None),(7,4,4,None),(7,8,4,{(0,1,3,5)})]:
        cases,points,hist=check(p,q,m,restriction)
        grand+=cases;freq+=points
        print('CASE p=%d q=%d arrays=%d frequencies=%d zero_counts=%s'%(p,q,cases,points,sorted(hist.items())))
    print('CHECK_OK arrays=%d Fourier_coefficients=%d'%(grand,freq))
