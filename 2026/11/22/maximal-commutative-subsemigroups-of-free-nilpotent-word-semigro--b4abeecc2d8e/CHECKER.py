"""Direct finite checks for word-length Rees quotient commuting classification."""
from itertools import product
from collections import Counter
from math import gcd


def words(a, n):
    return [tuple(z) for k in range(1, n + 1) for z in product(range(a), repeat=k)]


def mul(u, v, n):
    if u is None or v is None or len(u)+len(v)>n:
        return None
    return u+v


def primitive_period(w):
    return next(d for d in range(1, len(w)+1) if len(w)%d==0 and w[:d]*(len(w)//d)==w)


def expected_maximal(a,n):
    m=n//2
    W=words(a,n)
    tail=frozenset([None]+[w for w in W if len(w)>m])
    ans=[]
    if n%2: ans.append(tail)
    for k in range(1,m+1):
        for w in product(range(a),repeat=k):
            d=primitive_period(w);p=w[:d]
            ans.append(frozenset([None]+[v for v in W if len(v)>n-k or (len(v)>=k and len(v)%d==0 and v==p*(len(v)//d))]))
    return set(ans)


def brute_maximal(a,n):
    W=words(a,n)
    nbr={w:{v for v in W if v!=w and mul(w,v,n)==mul(v,w,n)} for w in W}
    maximal=[]
    def bk(R,P,X):
        if not P and not X:
            maximal.append(frozenset(R|{None}));return
        pivot=max(P|X,key=lambda u:len(P&nbr[u])) if P or X else None
        for v in list(P-(nbr[pivot] if P or X else set())):
            bk(R|{v},P&nbr[v],X&nbr[v]);P.remove(v);X.add(v)
    bk(set(),set(W),set())
    return set(maximal)


def run():
    configurations=0
    for a,n in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3)]:
        W=[None]+words(a,n)
        counts={w:sum(mul(w,v,n)==mul(v,w,n) for v in W) for w in W}
        assert counts[None]==len(W)
        for w in W[1:]:
            d=primitive_period(w);k=len(w)
            expected=1+sum(a**j for j in range(n-k+1,n+1))+(n-k)//d
            assert counts[w]==expected,(a,n,w,counts[w],expected)
        brute=sum(v==w or mul(w,v,n)==mul(v,w,n) for w in W for v in W)
        arithmetic=len(W)**2-sum(a**(i+j)-a**gcd(i,j) for i in range(1,n+1) for j in range(1,n+1) if i+j<=n)
        assert brute==arithmetic,(a,n,brute,arithmetic)
        maxs=brute_maximal(a,n)
        predicted=expected_maximal(a,n)
        assert maxs==predicted,(a,n,len(maxs),len(predicted),maxs^predicted)
        m=n//2
        largest=1+sum(a**j for j in range(m+1,n+1))+(n%2==0)
        multiplicity=a**m if n%2==0 else 1
        observed_sizes=[len(c) for c in maxs]
        assert max(observed_sizes)==largest,(a,n,'maximum size',largest)
        assert observed_sizes.count(largest)==multiplicity,(a,n,'maximizers',multiplicity)
        configurations+=1
        print('PASS a=%d N=%d |S|=%d maximal=%d commuting_pairs=%d' %(a,n,len(W),len(maxs),brute))
    print('PASS all %d configurations'%configurations)

if __name__=='__main__':run()
