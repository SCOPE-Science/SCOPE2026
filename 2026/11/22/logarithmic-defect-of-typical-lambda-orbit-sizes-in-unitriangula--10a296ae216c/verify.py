"""Independent finite λ-orbit enumeration and the exact deficiency transfer. Standard library only."""
from collections import defaultdict,Counter
from itertools import product

def dp(n,q):
    N=n-2
    state={(0,0):1}
    for m in range(N):
        out=defaultdict(int)
        for (d,s),v in state.items():
            old=q**(m-d)
            out[(d,s+d)] += v*(q**(m+1)-old)
            out[(d+1,s+d+1)] += v*old
        state=out
    M=N*(N+1)//2
    el=Counter(); orbit=Counter()
    for (d,s),v in state.items():
        L=M-s
        el[L] += q**(n-1)*v
    for L,num in el.items():
        assert num % q**L == 0
        orbit[L]=num//q**L
    return el,orbit

def direct(n,q):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    pos={p:k for k,p in enumerate(pairs)}
    vec=list(product(range(q),repeat=len(pairs)))
    unseen=set(vec)
    hist_orbit=Counter()
    hist_elements=Counter()
    while unseen:
        b=next(iter(unseen))
        visited=set()
        for a in vec:
            result=list(b)
            for i,j in pairs:
                result[pos[(i,j)]] = (result[pos[(i,j)]] + sum(a[pos[(i,k)]]*b[pos[(k,j)]] for k in range(i+1,j)))%q
            visited.add(tuple(result))
        if not visited<=unseen:
            raise AssertionError('Bad lambda orbit partition')
        unseen-=visited
        sz=len(visited)
        L=0; value=1
        while value<sz:
            value*=q; L+=1
        assert value==sz
        hist_orbit[L]+=1
        hist_elements[L]+=sz
    return hist_elements,hist_orbit

if __name__=='__main__':
    for q, ns in [(2,range(2,6)),(3,range(2,5))]:
        for n in ns:
            E,O=dp(n,q)
            E2,O2=direct(n,q)
            assert E==E2, (q,n,E,E2)
            assert O==O2, (q,n,O,O2)
            assert sum(E.values()) == q**(n*(n-1)//2)
            print('q=',q,'n=',n,'element sizes',dict(sorted(E.items())),'orbit sizes',dict(sorted(O.items())))
    for q in [2,3,4,5,7]:
        for n in range(2,22):
            E,O=dp(n,q)
            assert sum(E.values())==q**(n*(n-1)//2)
            assert sum(O[k]*q**k for k in O)==sum(E.values())
    print('UNITRIANGULAR_BRACE_ORBIT_SPECTRUM_VERIFIED')
