"""Exact finite checks for edge-agreement covariance under fixed-composition coloring.
No external packages. Run: python3 verify.py
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from math import comb


def parts(n, least=1):
    if not n:
        yield ()
    else:
        for r in range(least, n+1):
            for rest in parts(n-r, r):
                yield (r,) + rest


def eigs(comp):
    n=sum(comp)
    m=comb(n,2)
    p=Q(sum(r*(r-1) for r in comp),n*(n-1))
    mu=Q(sum(r*(r-1) for r in comp),n)
    s2=Q(sum(r*(r-1)**2 for r in comp),n)-mu*mu
    star=Q(n,(n-1)*(n-2))*s2
    cycle=Q((n-1),n-3)*p*(1-p)-Q(2,(n-2)*(n-3))*s2
    assert star>=0 and cycle>=0
    return star,cycle,p


def variance_formula(comp, weights, edges):
    n=sum(comp)
    star,cycle,p=eigs(comp)
    total=sum(weights)
    ds=[0]*n
    for (i,j),w in zip(edges,weights):
        ds[i]+=w;ds[j]+=w
    ss=sum((Q(d)-Q(2*total,n))**2 for d in ds)
    vstar=Q(ss,n-2)
    vcycle=sum(w*w for w in weights)-Q(total*total,comb(n,2))-vstar
    assert vstar>=0 and vcycle>=0
    return star*vstar+cycle*vcycle


def assignments(comp):
    n=sum(comp)
    # Generate each labeled coloring of the prescribed histogram once.
    seq=tuple(i for i,r in enumerate(comp) for _ in range(r))
    # Recursive multinomial iterator without materializing duplicate permutations.
    counts=list(comp)
    prefix=[0]*n
    def rec(k):
        if k==n:
            yield tuple(prefix)
            return
        for i,c in enumerate(counts):
            if c:
                counts[i]-=1;prefix[k]=i
                yield from rec(k+1)
                counts[i]+=1
    yield from rec(0)


def truth_zero(comp,w,edges):
    vals=set()
    for a in assignments(comp):
        vals.add(sum(w[e] for e,(i,j) in enumerate(edges) if a[i]==a[j]))
        if len(vals)>1:
            return False
    return True


def direct_variance(comp,w,edges):
    number=0; a=0;b=0
    for coloring in assignments(comp):
        x=sum(w[e] for e,(i,j) in enumerate(edges) if coloring[i]==coloring[j])
        a+=x;b+=x*x;number+=1
    return Q(b,number)-Q(a,number)**2, number


def oracle_class(comp,w,edges):
    n=sum(comp)
    m=sum(w)
    ds=[0]*n
    for (i,j),v in zip(edges,w):
        ds[i]+=v;ds[j]+=v
    if len(comp)==1 or len(comp)==n:
        return True
    if comp[-1]==n-1 and comp[0]==1:
        return len(set(ds))==1
    if len(set(comp))==1:
        return m in (0,len(edges)) or (m in (n-1,comb(n-1,2)) and
                (sorted(ds)==([1]*(n-1)+[n-1]) or sorted(ds)==([0]+[n-2]*(n-1))))
    return m in (0,len(edges))


checks=0; histogram_count=0; coloring_count=0; graph_count=0
for n in range(4,9):
    edges=list(combinations(range(n),2))
    m=len(edges)
    patterns=[tuple(0 for _ in edges),tuple(1 for _ in edges),
              tuple(int(i==0 or j==0) for i,j in edges),
              tuple(int(i!=0 and j!=0) for i,j in edges),
              tuple(int(j==i+1) for i,j in edges),
              tuple(int(i+j<n) for i,j in edges),
              tuple(((-1)**(i+j))*(i+2*j+1) for i,j in edges)]
    for comp in parts(n):
        histogram_count+=1
        star,cycle,p=eigs(comp)
        assert (star==0)==(len(set(comp))==1)
        assert (cycle==0)==(len(comp)==1 or len(comp)==n or
                                  comp==(1,n-1))
        checks+=2
        # Direct summation over every distinct coloring (no moment identity reused).
        colorings=list(assignments(comp))
        coloring_count+=len(colorings)
        ps=sum(a[0]==a[1] for a in colorings)
        qi=sum(a[0]==a[1]==a[2] for a in colorings)
        qd=sum((a[0]==a[1]) and (a[2]==a[3]) for a in colorings)
        directp=Q(ps,len(colorings));directqi=Q(qi,len(colorings));directqd=Q(qd,len(colorings))
        assert directp==p
        # Direct covariance eigenvalues from disjoint / incident pair events.
        v=p*(1-p); c1=directqi-p*p;c2=directqd-p*p
        assert star==v+(n-4)*c1-(n-3)*c2
        assert cycle==v-2*c1+c2
        assert v+2*(n-2)*c1+comb(n-2,2)*c2==0
        checks+=4
        for w in patterns:
            vals=[sum(w[e] for e,(i,j) in enumerate(edges) if a[i]==a[j]) for a in colorings]
            vv=Q(sum(x*x for x in vals),len(vals))-Q(sum(vals),len(vals))**2
            assert vv==variance_formula(comp,w,edges),(comp,n,w,vv,variance_formula(comp,w,edges))
            checks+=1
        if n<=5:
            for mask in range(1<<m):
                w=tuple((mask>>e)&1 for e in range(m))
                predicted=oracle_class(comp,w,edges)
                actual=variance_formula(comp,w,edges)==0
                assert predicted==actual,(n,comp,mask)
                if (mask in (0,1,3,(1<<m)-1)) or actual:
                    assert truth_zero(comp,w,edges)==actual
                graph_count+=1;checks+=1
print(f'VERIFY_OK {histogram_count} class-size compositions; {coloring_count} exhaustive assignments; {graph_count} graph classifications; {checks} exact assertions')
