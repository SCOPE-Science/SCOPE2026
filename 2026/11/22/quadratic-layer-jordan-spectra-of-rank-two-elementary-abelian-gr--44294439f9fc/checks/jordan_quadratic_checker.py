"""Independent finite-field checks for quadratic-leading Jordan partitions.

Run: python jordan_quadratic_checker.py
Uses only the Python standard library. All arithmetic below is exact in F_p.
"""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def add(a, b, p):
    z = dict(a)
    for e, c in b.items():
        t = (z.get(e, 0) + c) % p
        if t: z[e] = t
        elif e in z: del z[e]
    return z


def mul(a, b, p):
    z = {}
    for (i, j), c in a.items():
        for (k, l), d in b.items():
            if i+k < p and j+l < p:
                key = (i+k, j+l)
                z[key] = (z.get(key, 0)+c*d) % p
    return {e:c for e,c in z.items() if c}


def power(a, k, p):
    z = {(0,0):1}
    for _ in range(k): z = mul(z,a,p)
    return z


def linear_rank(columns, p):
    n = len(columns)
    a = [[columns[j][i] % p for j in range(n)] for i in range(n)]
    r = 0
    for j in range(n):
        h = next((i for i in range(r,n) if a[i][j]),None)
        if h is None: continue
        a[r],a[h] = a[h],a[r]
        inv = pow(a[r][j],-1,p)
        a[r][j:] = [(v*inv)%p for v in a[r][j:]]
        for i in range(r+1,n):
            if a[i][j]:
                c = a[i][j]
                a[i][j:] = [(x-c*y)%p for x,y in zip(a[i][j:],a[r][j:])]
        r += 1
    return r


def rank_of_multiplication(f, p):
    basis = [(i,j) for i in range(p) for j in range(p)]
    idx = {a:i for i,a in enumerate(basis)}
    cols=[]
    for (i,j) in basis:
        c=[0]*len(basis)
        for (a,b),v in f.items():
            if i+a<p and j+b<p: c[idx[i+a,j+b]]=v
        cols.append(c)
    return linear_rank(cols,p)


def jordan_partition(f,p):
    ranks=[p*p]
    g={(0,0):1}
    for _ in range(p):
        g=mul(g,f,p)
        ranks.append(rank_of_multiplication(g,p))
    assert ranks[p]==0, (p,f,ranks)
    ranks.append(0)
    ans=Counter()
    for i in range(1,p+1):
        z=ranks[i-1]-2*ranks[i]+ranks[i+1]
        assert z>=0
        if z: ans[i]=z
    assert sum(k*v for k,v in ans.items())==p*p
    return tuple(sorted(ans.items()))


def predicted(p,s):
    assert s>=3 and s<=p
    a=[(p+1)//2,(p-1)//2]
    b=[(p-1-j)//s+1 for j in range(s)]
    c=Counter()
    for i in a:
        for j in b:
            for k in range(1,min(i,j)+1):
                c[i+j-2*k+1] +=1
    return tuple(sorted(c.items()))


def predicted_nondegenerate(p):
    c=Counter({p:1})
    c.update({j:2 for j in range(1,p)})
    return tuple(sorted(c.items()))


def evaluate_x_shift(f,u,p):
    x={(1,0):1}
    y={(0,1):1}
    xnew=add(x,u,p)
    xp=[{(0,0):1}]
    for _ in range(p-1):xp.append(mul(xp[-1],xnew,p))
    z={}
    for (i,j),c in f.items():
        t={(a,b+j):c*v%p for (a,b),v in xp[i].items() if b+j<p}
        z=add(z,t,p)
    return z


def residual_order(f,p):
    # f has exact quadratic symbol x^2 and no other degree-two terms.
    g=dict(f)
    for d in range(3,2*p-1):
        u={}
        for (i,j),c in g.items():
            if i>0 and i+j==d:
                u[i-1,j]=(-c*pow(2,-1,p))%p
        if u: g=evaluate_x_shift(g,u,p)
    assert all(i==0 or (i,j)==(2,0) for i,j in g)
    return next((s for s in range(3,p) if g.get((0,s),0)),p)


def test():
    # Exhaust all quadratic-leading and higher elements in the p=3 example.
    p=3
    monoms=[(i,j) for i in range(p) for j in range(p) if i+j>=2]
    tally=Counter()
    for coeff in product(range(p),repeat=len(monoms)):
        f={m:v for m,v in zip(monoms,coeff) if v}
        a=f.get((2,0),0);b=f.get((1,1),0);c=f.get((0,2),0)
        if not (a or b or c):continue
        disc=(b*b-4*a*c)%p
        got=jordan_partition(f,p)
        exp=predicted_nondegenerate(p) if disc else predicted(p,p)
        assert got==exp,(p,f,got,exp)
        tally['nondegenerate' if disc else 'rank_one']+=1
    assert tally==Counter(nondegenerate=486,rank_one=216),tally
    print('p=3 complete quadratic-leading enumeration:',dict(tally))

    rng=Random(18513)
    for p in [5,7]:
        h=[(i,j) for i in range(p) for j in range(p) if i+j>=3]
        for kind in ['nondegenerate','rank_one']:
            for it in range(20 if p==5 else 8):
                f={(i,j):rng.randrange(p) for i,j in h}
                f={key:c for key,c in f.items() if c}
                if kind=='nondegenerate':
                    f[(1,1)]=1
                    exp=predicted_nondegenerate(p)
                else:
                    f[(2,0)]=1
                    s=residual_order(f,p)
                    exp=predicted(p,s)
                got=jordan_partition(f,p)
                assert got==exp,(p,kind,it,f,got,exp)
            print('p=%d %s: all 20/8 randomized lifted elements verified'%(p,kind))
        for s in range(3,p+1):
            f={(2,0):1}
            if s<p: f[(0,s)]=1
            assert jordan_partition(f,p)==predicted(p,s)
        assert jordan_partition({(1,1):1},p)==predicted_nondegenerate(p)
        print('p=%d: all residual monomial normal forms verified'%(p,))
    print('ALL EXACT CHECKS PASS')

if __name__=='__main__':test()
