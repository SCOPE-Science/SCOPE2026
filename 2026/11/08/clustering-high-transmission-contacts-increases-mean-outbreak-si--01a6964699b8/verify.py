"""Independent finite bond-percolation enumerator and symbolic C4 checker.

Run: python verify.py
All assertions are finite exact checks; the proof for arbitrary cycle length
and real probabilities is supplied in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations


def components(n, mask):
    parent=list(range(n))
    def root(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    for i in range(n):
        if mask>>i&1:
            a,b=root(i),root((i+1)%n)
            parent[a]=b
    sizes=defaultdict(int)
    for i in range(n):
        sizes[root(i)]+=1
    return list(sizes.values())


def moments(n, rates):
    """Direct sum over all 2**n bond masks, no connectivity formula used."""
    ans=[F(0),F(0)]
    for mask in range(1<<n):
        prob=F(1)
        for i,r in enumerate(rates):
            prob*=r if mask>>i&1 else (1-r)
        sizes=components(n,mask)
        ans[0]+=prob*sum(s*s for s in sizes)/n
        ans[1]+=prob*sum(s*s*s for s in sizes)/n
    return ans


def rates(n,d,p,q):
    v=[q]*n
    v[0]=v[d]=p
    return v


def symbolic_c4(rate_labels):
    """Expand exact probabilities as bivariate polynomials in p,q."""
    ans=[defaultdict(F),defaultdict(F)]
    for mask in range(16):
        poly={(0,0):F(1)}
        for i,lab in enumerate(rate_labels):
            next_poly=defaultdict(F)
            for (ip,iq),a in poly.items():
                if mask>>i&1:
                    key=(ip+1,iq) if lab=='p' else (ip,iq+1)
                    next_poly[key]+=a
                else:
                    next_poly[(ip,iq)]+=a
                    key=(ip+1,iq) if lab=='p' else (ip,iq+1)
                    next_poly[key]-=a
            poly=next_poly
        sizes=components(4,mask)
        k1=F(sum(s*s for s in sizes),4)
        k2=F(sum(s*s*s for s in sizes),4)
        for key,a in poly.items():
            ans[0][key]+=k1*a
            ans[1][key]+=k2*a
    return [{k:v for k,v in z.items() if v} for z in ans]


def subtract(a,b):
    r=defaultdict(F,a)
    for k,v in b.items(): r[k]-=v
    return {k:v for k,v in r.items() if v}


def polyscale(p,a): return {k:v*a for k,v in p.items() if v*a}


def variance(m): return m[1]-m[0]**2


def main():
    checks=0
    a=symbolic_c4('ppqq')
    b=symbolic_c4('pqpq')
    delta_sq={(2,0):F(1),(1,1):F(-2),(0,2):F(1)}
    assert subtract(a[0],b[0])==polyscale(delta_sq,F(1,2));checks+=1
    assert subtract(a[1],b[1])==polyscale(delta_sq,F(3));checks+=1
    b_mean={(0,0):F(1),(1,0):F(1),(0,1):F(1),(1,1):F(2),
            (2,1):F(1),(1,2):F(1),(2,2):F(-3)}
    assert b[0]==b_mean;checks+=1
    for n in range(4,11):
        for p,q in [(F(3,4),F(1,4)),(F(5,6),F(1,3)),(F(2,3),F(1,5))]:
            vals={d:moments(n,rates(n,d,p,q)) for d in range(1,n//2+1)}
            for d in range(1,n//2):
                diff=vals[d][0]-vals[d+1][0]
                target=F(2,n)*(p-q)**2*sum(q**(k-2) for k in range(d+1,n-d))
                assert diff==target and diff>0,(n,p,q,d,diff,target)
                checks+=1
    for p,q in [(F(3,4),F(1,4)),(F(9,10),F(3,4)),(F(3,5),F(2,5)),(F(7,8),F(1,3))]:
        aa=moments(4,[p,p,q,q]);bb=moments(4,[p,q,p,q]);
        assert aa[0]-bb[0]==(p-q)**2/F(2);checks+=1
        assert aa[1]-bb[1]==3*(p-q)**2;checks+=1
        assert variance(aa)-variance(bb)==(p-q)**2*(3-(aa[0]+bb[0])/2);checks+=1
        if (p,q)==(F(3,4),F(1,4)):
            assert aa[0]==F(661,256) and bb[0]==F(629,256)
            assert variance(aa)-variance(bb)==F(123,1024)
            checks+=2
        if (p,q)==(F(9,10),F(3,4)):
            assert aa[0]==F(6013,1600) and bb[0]==F(1199,320)
            assert variance(aa)-variance(bb)==F(-2709,160000)
            checks+=2
    print('PASS',checks,'exact checks; symbolic C4 polynomials and independent finite-state enumeration.')

if __name__=='__main__':main()
