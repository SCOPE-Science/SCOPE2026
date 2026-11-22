"""Direct finite-field checks of brace left-action cycle laws (prime fields)."""
from itertools import product
from collections import Counter
from math import comb


def locations(n): return [(i,j) for i in range(n) for j in range(i+1,n)]

def mat(n,values):
    m=[[0]*n for _ in range(n)]
    for (i,j),v in zip(locations(n),values): m[i][j]=v
    return m

def flatten_upper(a):
    return tuple(a[i][j] for i in range(len(a)) for j in range(i+1,len(a)))

def mul(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def rank(m,p):
    if not m:return 0
    a=[row[:] for row in m]
    rows=len(a); cols=len(a[0]); t=0
    for j in range(cols):
        z=next((i for i in range(t,rows) if a[i][j]%p),None)
        if z is None: continue
        a[t],a[z]=a[z],a[t]
        inv=pow(a[t][j],-1,p)
        a[t]=[(u*inv)%p for u in a[t]]
        for i in range(t+1,rows):
            d=a[i][j]
            if d:a[i]=[(x-d*y)%p for x,y in zip(a[i],a[t])]
        t+=1
        if t==rows:break
    return t

def power(a,k,p):
    n=len(a); r=[[int(i==j) for j in range(n)] for i in range(n)]
    for _ in range(k):r=mul(r,a,p)
    return r

def predict(a,p):
    n=len(a); d=comb(n,2)
    vals=[]; u=1
    while True:
        fixed=q_pow = p**sum((r-rank([row[:r] for row in power(a,u,p)[:r]],p)) for r in range(1,n))
        vals.append(fixed)
        if fixed==p**d:break
        u*=p
    return dict([(1,vals[0])]+[(p**s,(vals[s]-vals[s-1])//(p**s)) for s in range(1,len(vals))])

def direct_cycles(a,p):
    n=len(a); d=comb(n,2)
    words=list(product(range(p),repeat=d)); idx={x:i for i,x in enumerate(words)}
    nxt=[]
    for w in words:
        b=mat(n,w);ab=mul(a,b,p)
        nxt.append(idx[tuple((b[i][j]+ab[i][j])%p for i,j in locations(n))])
    used=set(); cycles=Counter()
    for i in range(len(words)):
        if i in used:continue
        k=i;c=0
        while k not in used:
            used.add(k);c+=1;k=nxt[k]
        assert k==i,(n,p,i,k)
        cycles[c]+=1
    return dict(cycles)

def check_all(n,p):
    d=comb(n,2); reg=0; max_order=0; types=set()
    for a_tuple in product(range(p),repeat=d):
        a=mat(n,a_tuple)
        pred=predict(a,p)
        got=direct_cycles(a,p)
        if pred!=got:raise AssertionError((n,p,a_tuple,pred,got))
        types.add(tuple(sorted(got.items())))
        regular=all(a[i][i+1]!=0 for i in range(n-2))
        if regular:
            reg+=1
            for s in range(1,n):
                r=rank(power(a,s,p),p)
                expect=comb(max(n-s,0),2) if n-s>=2 else 0
                # rank of left multiplication (not of a itself) is the sum of prefix powers.
                Lrank=sum(rank([row[:j] for row in power(a,s,p)[:j]],p) for j in range(1,n))
                assert Lrank==expect,(n,p,s,Lrank,expect)
        if (n-2)&(n-3)==0 and n>=3: # n-2 is power of two; p-specific checked below
            pass
    expected=(p-1)**(n-2)*p**(d-(n-2))
    assert reg==expected,(n,p,reg,expected)
    return f'n={n} p={p}: all {p**d} left actions, {len(types)} cycle types, regular={reg}; PASS'

def check_jump(n,p,s,samples=500):
    assert n==p**s+2
    d=comb(n,2); observed=0
    if p**d <= 250:
        cases=list(product(range(p),repeat=d)); exhaustive=True
    else:
        from random import Random
        rng=Random(n*100+p)
        cases=[(0,)*d,(1,)*d]
        cases += [tuple(rng.randrange(p) for _ in range(d)) for _ in range(samples)]
        exhaustive=False
    for vals in cases:
        a=mat(n,vals)
        lead=[row[:n-1] for row in a[:n-1]]
        isnonzero=any(any(x for x in row) for row in power(lead,p**s,p))
        criterion=all(a[i][i+1] for i in range(n-2))
        assert isnonzero==criterion,(n,p,vals)
        observed+=isnonzero
    expected=(p-1)**(p**s)*p**(d-p**s)
    if exhaustive: assert observed==expected
    return f'n={n} p={p} p^s={p**s}: cases={len(cases)} (exhaustive={exhaustive}), top-order among cases={observed}, theorem population={expected}/{p**d}; PASS'

if __name__=='__main__':
    for n,p in [(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(4,3)]: print(check_all(n,p),flush=True)
    for n,p,s in [(3,2,0),(4,2,1),(6,2,2),(3,3,0),(5,3,1)]:print(check_jump(n,p,s),flush=True)
    print('ALL CHECKS PASSED',flush=True)
