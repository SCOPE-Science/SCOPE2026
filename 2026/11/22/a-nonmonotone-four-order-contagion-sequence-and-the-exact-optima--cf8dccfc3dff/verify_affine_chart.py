"""Exact census for 2-neighbour bootstrap on affine-plane incidence graphs.
Run: python3 verify_affine_chart.py . Uses only the Python standard library.
Every k-set, not merely a random sample, is evaluated in the stated ranges.
"""
from itertools import combinations
from collections import Counter

def graph(q, poly=None):
    def sub(a,b): return a^b if poly else (a-b)%q
    def mul(a,b):
        if not poly: return (a*b)%q
        z=0
        for i in range(2):
            if b>>i&1:z^=a<<i
        for i in (3,2):
            if z>>i&1:z^=poly<<(i-2)
        return z
    P=[(x,y) for x in range(q) for y in range(q)]
    L=[('s',a,b) for a in range(q) for b in range(q)]+[('v',a) for a in range(q)]
    n=len(P);nb=[0]*(n+len(L))
    for i,(x,y) in enumerate(P):
        for j,l in enumerate(L):
            is_incident = (x==l[1]) if l[0]=='v' else (sub(y,mul(l[1],x))==l[2])
            if is_incident:
                nb[i]|=1<<(n+j)
                nb[n+j]|=1<<i
    assert all(m.bit_count()==q+1 for m in nb[:n])
    assert all(m.bit_count()==q for m in nb[n:])
    return nb,n

def close(seed,nb):
    a=sum(1<<v for v in seed);t=0
    while True:
        new=0
        for i,m in enumerate(nb):
            if not (a>>i&1) and (a&m).bit_count()>=2:new|=1<<i
        if new==0:return a.bit_count(),t
        a|=new;t+=1

def check(q,poly,k,expected_by_shore,expected_times=None):
    nb,n=graph(q,poly);N=len(nb);cnt=Counter();times=Counter()
    for C in combinations(range(N),k):
        size,t=close(C,nb)
        if size==N:
            j=sum(x<n for x in C)
            cnt[j]+=1;times[t]+=1
    got=tuple(cnt[j] for j in range(k+1))
    assert got==expected_by_shore,(q,k,got,expected_by_shore)
    if expected_times is not None:assert dict(times)==expected_times,(q,times)
    print('q=%d, k=%d, contagious=%d, point-shore counts=%s, time counts=%s'%(q,k,sum(got),got,dict(sorted(times.items()))),flush=True)

if __name__=='__main__':
    # Check every smaller seed size too, using monotonicity: if no (k-1)-set works,
    # none of its subsets can work.
    check(2,None,3,(0,0,0,0))
    check(2,None,4,(3,4,0,0,1),{1:1,2:7})
    check(3,None,4,(0,0,0,0,0))
    check(3,None,5,(396,1224,1404,1080,396,72),{4:1332,5:2268,6:756,7:216})
    check(4,0b111,4,(0,0,0,0,0))
    check(4,0b111,5,(8448,32640,46080,36480,15840,2688),{3:48,4:5568,5:29040,6:86400,7:18240,8:2880})
    check(5,None,3,(0,0,0,0))
    check(5,None,4,(9000,32000,0,24000,5000),{7:5000,8:23000,9:18000,10:12000,11:12000})
    print('AFFINE-CHART EXHAUSTIVE VERIFICATION PASSED')
