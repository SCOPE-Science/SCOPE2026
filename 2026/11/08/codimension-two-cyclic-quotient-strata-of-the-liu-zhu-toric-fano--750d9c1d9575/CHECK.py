"""Exact check of two-dimensional orbit-cone strata for a box-slice toric fan."""
from math import gcd, comb
from itertools import combinations

def vertex(n,p,q):
    assert n>=3 and p!=q
    r=2*n-1
    return tuple(-r if i==p else 1 if i==q else 2 for i in range(n+1))

def hj(num,den):
    seq=[]
    while den:
        a=(num+den-1)//den
        seq.append(a)
        num,den=den,a*den-num
    return seq

def check(n):
    names=[(p,q) for p in range(n+1) for q in range(n+1) if p!=q]
    rays={pq:vertex(n,*pq) for pq in names}
    acts={pq:frozenset([('lo',pq[0])]+[('hi',i) for i in range(n+1) if i not in pq]) for pq in names}
    short=long=0
    for a,b in combinations(names,2):
        common=len(acts[a] & acts[b])
        typ='short' if a[0]==b[0] else 'long' if a==(b[1],b[0]) else 'not'
        assert (common==n-1)==(typ!='not'),(n,a,b,common,typ)
        if typ=='not': continue
        v,w=rays[a][1:],rays[b][1:]
        determinants=[v[i]*w[j]-v[j]*w[i] for i,j in combinations(range(n),2)]
        index=0
        for z in determinants:index=gcd(index,abs(z))
        assert index == (1 if typ=='short' else 4*n),(n,a,b,index)
        if typ=='short':short+=1
        else:long+=1
    assert short==(n+1)*comb(n,2)
    assert long==comb(n+1,2)
    assert hj(4*n,2*n-1)==[3]+[2]*(n-2)+[3]
    # ages of all elements of the local cyclic group 1/(4n)(1,2n-1)
    ages=[(k+(k*(2*n-1))%(4*n))/(4*n) for k in range(1,4*n)]
    assert min(ages)==0.5 and all(a>=0.5 for a in ages)
    print(f'n={n}: short regular edges={short}, long quotient edges={long}, index={4*n}, HJ={hj(4*n,2*n-1)}, minage={min(ages)}')

if __name__=='__main__':
    for n in range(3,10):check(n)
    print('ALL_FAN_EDGE_AND_QUOTIENT_CHECKS_OK')
