"""Standalone exhaustive checks of the 2-extension witness minimum in Grassmann graphs.
Only prime-field instances are constructed; the theorem for arbitrary prime powers uses its symbolic proof.
"""
import itertools, math

def rref(rows, p):
    a = [list(r) for r in rows]
    n = len(a[0]); pivot = 0
    for c in range(n):
        z = next((i for i in range(pivot, len(a)) if a[i][c] % p), None)
        if z is None: continue
        a[pivot], a[z] = a[z], a[pivot]
        inv = pow(a[pivot][c], -1, p)
        a[pivot] = [(x*inv)%p for x in a[pivot]]
        for i in range(len(a)):
            if i == pivot: continue
            t = a[i][c]
            a[i] = [(x-t*y)%p for x,y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a): break
    return tuple(tuple(row) for row in a if any(row))

def graph(n,p):
    vecs = [z for z in itertools.product(range(p), repeat=n) if any(z)]
    spaces = sorted({rref([u,v],p) for u in vecs for v in vecs if u!=v and len(rref([u,v],p))==2})
    v=len(spaces); nb=[0]*v
    for i in range(v):
        for j in range(i+1,v):
            if len(rref(spaces[i]+spaces[j],p))==3:
                nb[i]|=1<<j
                nb[j]|=1<<i
    return nb

def gauss2(n,q):
    return (q**n-1)*(q**(n-1)-1)//((q*q-1)*(q-1))

def calc(n,q):
    nb=graph(n,q);v=len(nb);d=q*(q+1)*((q**(n-2)-1)//(q-1))
    mu=(q+1)**2
    lam=(q**(n-1)-1)//(q-1)-2+q*q
    counts={('edge', '11'):set(),('edge','10'):set(),('edge','00'):set(),('nonedge','11'):set(),('nonedge','10'):set(),('nonedge','00'):set()}
    full=(1<<v)-1; least=v
    for i in range(v):
        assert nb[i].bit_count()==d
        for j in range(i+1,v):
            e='edge' if nb[i] & (1<<j) else 'nonedge'
            both=(nb[i]&nb[j]).bit_count()
            only=(nb[i] & ~nb[j] & ~(1<<j)).bit_count()
            neither=(full & ~(nb[i]|nb[j]) & ~(1<<i) & ~(1<<j)).bit_count()
            counts[(e,'11')].add(both); counts[(e,'10')].add(only); counts[(e,'00')].add(neither)
            least=min(least,both,only,neither)
    assert v==gauss2(n,q)
    assert counts[('edge','11')]=={lam}
    assert counts[('nonedge','11')]=={mu}
    assert counts[('edge','10')]=={d-1-lam}
    assert counts[('nonedge','10')]=={d-mu}
    assert counts[('edge','00')]=={v-2*d+lam}
    assert counts[('nonedge','00')]=={v-2-2*d+mu}
    result=min(mu,q**3*((q**(n-3)-1)//(q-1)),v-2-2*d+mu)
    assert least==result
    expected=6 if (n,q)==(4,2) else (q+1)**2
    assert least==expected
    return f'n={n} q={q} vertices={v} degree={d} lambda={lam} mu={mu} min_witnesses={least} formula={result} PASS'

if __name__=='__main__':
    for n,q in [(4,2),(5,2),(4,3)]: print(calc(n,q))
    for n in range(4,9):
      for q in [2,3,4,5,7,8,9,11]:
        v=gauss2(n,q)
        d=q*(q+1)*((q**(n-2)-1)//(q-1))
        lam=(q**(n-1)-1)//(q-1)-2+q*q
        mu=(q+1)**2
        profile=[lam,mu,d-1-lam,d-mu,v-2*d+lam,v-2-2*d+mu]
        expected=6 if (n,q)==(4,2) else mu
        assert min(profile)==expected, (n,q,profile)
    print('symbolic-profile integer checks: 40 parameter pairs PASS')
