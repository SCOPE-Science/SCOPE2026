"""Computational cross-check for the repunit semigroup gap-spectrum theorem.

Uses direct forward semigroup membership and independent shortest residue paths. No
analytic claim is inferred from finite checks; see accompanying proof.
"""
from collections import Counter
import heapq


def R(b,j):
    return (b**j-1)//(b-1)


def predicted_hist(b,n):
    a=R(b,n)
    E={u for u in range(1,b+1)}
    for m in range(3,n+1):
        E={t*R(b,m-1)+u for t in range(b) for u in E}
    assert len(E)==b**(n-1)
    return Counter({a-r:b for r in E})


def direct_hist(b,n):
    a=R(b,n)
    gens=[R(b,n+j) for j in range(n)]
    member=[True];x=0;consecutive=0;out=Counter();start=None
    while consecutive<a:
        x+=1
        is_member=any(x>=g and member[x-g] for g in gens)
        member.append(is_member)
        consecutive=consecutive+1 if is_member else 0
        if not is_member and start is None:start=x
        if is_member and start is not None:
            out[x-start]+=1;start=None
        assert x < 1500000
    assert start is None
    return out


def predicted_apery_height(b,n):
    q=[b*u for u in range(b+1)]
    for m in range(3,n+1):
        q=[t*b**(m-1)+v for t in range(b) for v in q]+[b**m]
    return q


def dijkstra_heights(b,n):
    a=R(b,n)
    gens=[R(b,n+j) for j in range(1,n)]
    dist=[10**80]*a;dist[0]=0;heap=[(0,0)]
    while heap:
        d,r=heapq.heappop(heap)
        if d!=dist[r]:continue
        for g in gens:
            rr=(r+g)%a
            if d+g<dist[rr]:
                dist[rr]=d+g;heapq.heappush(heap,(d+g,rr))
    return [(dist[r]-r)//a for r in range(a)]


def main():
    cases=[(b,n) for b in range(2,8) for n in range(2,7) if R(b,n)<=700]
    cases += [(2,n) for n in range(7,10)]
    total=0;max_a=0
    for b,n in cases:
        h=direct_hist(b,n)
        pred=predicted_hist(b,n)
        assert h==pred,(b,n,h,pred)
        assert predicted_apery_height(b,n)==dijkstra_heights(b,n),(b,n,'Apéry')
        a=R(b,n)
        assert sum(h.values())==b**n
        assert min(h)==n-1 and max(h)==a-1
        assert set(h.values())=={b}
        assert sum(k*v for k,v in h.items())==((b**n-b)*b**n//(b-1) + b**n*(n-1))//2
        total+=sum(h.values());max_a=max(max_a,a)
    print('PASS: ',len(cases),'independent parameter cases, max multiplicity',max_a,
          'total maximal missing blocks',total)
    for b,n in ((2,4),(3,3),(3,4)):
        print('example',b,n,sorted(predicted_hist(b,n).items()))

if __name__=='__main__': main()
