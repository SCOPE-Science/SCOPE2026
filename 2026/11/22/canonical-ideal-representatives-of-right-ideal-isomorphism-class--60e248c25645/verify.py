"""Finite checks for projective flags and canonical ideals in rooted-forest incidence algebras.

Run: python forest_iso_verify.py
Uses only the Python standard library. The proof, not the finite checks,
justifies the statements over arbitrary fields and all finite rooted forests.
"""
from itertools import combinations, product
from math import comb


def ancestors(par,v):
    result=[]
    while v!=-1:
        result.append(v);v=par[v]
    return tuple(reversed(result))


def matrix_positions(par):
    return tuple((u,v) for v in range(len(par)) for u in ancestors(par,v))


def profiles(par):
    def go(v,r):
        if v==len(par):
            yield tuple(r);return
        lower=r[par[v]] if par[v]!=-1 else 0
        for t in range(lower,len(ancestors(par,v))+1):
            yield from go(v+1,r+[t])
    yield from go(0,[])


def basis_for_profile(par,r):
    pos=matrix_positions(par)
    return [tuple(int((u,v)==entry) for entry in pos)
            for v in range(len(par)) for u in ancestors(par,v)[:r[v]]]


def rank(rows,p):
    if not rows:return 0
    a=[list(map(lambda z:z%p,v)) for v in rows]
    h=0
    for j in range(len(a[0])):
        piv=next((i for i in range(h,len(a)) if a[i][j]),None)
        if piv is None:continue
        a[piv],a[h]=a[h],a[piv]
        z=pow(a[h][j],-1,p)
        a[h]=[(z*b)%p for b in a[h]]
        for i in range(len(a)):
            if i!=h and a[i][j]:
                z=a[i][j];a[i]=[(b-z*c)%p for b,c in zip(a[i],a[h])]
        h+=1
        if h==len(a):break
    return h


def rref_subspaces(n,p):
    for d in range(n+1):
        for piv in combinations(range(n),d):
            slots=[(i,j) for i,x in enumerate(piv) for j in range(x+1,n) if j not in piv]
            for dig in product(range(p),repeat=len(slots)):
                B=[[int(j==piv[i]) for j in range(n)] for i in range(d)]
                for (i,j),x in zip(slots,dig):B[i][j]=x
                yield B


def product_unit(v,par,a,b,side):
    pos=matrix_positions(par);lookup=dict(zip(pos,v))
    if side=='right':
        return tuple(lookup.get((i,a),0) if j==b else 0 for i,j in pos)
    return tuple(lookup.get((b,j),0) if i==a else 0 for i,j in pos)


def profile_of(B,par,p):
    pos=matrix_positions(par)
    return tuple(rank([[x if j==v else 0 for x,(_,j) in zip(row,pos)] for row in B],p)
                 for v in range(len(par)))


def gaussian(n,k,q):
    if not 0<=k<=n:return 0
    num=den=1
    for i in range(1,k+1):
        num*=q**(n-i+1)-1;den*=q**i-1
    return num//den


def fiber_size(par,r,q):
    ans=1
    for v in range(len(par)):
        prev=r[par[v]] if par[v]!=-1 else 0
        ans*=gaussian(len(ancestors(par,v))-prev,r[v]-prev,q)
    return ans


def hom_dim(B,C,par,p):
    # Equivariant linear maps between the two canonical right-module bases.
    pos=matrix_positions(par);d=len(B);e=len(C)
    if d==0 or e==0:return 0
    bi=[next(k for k,z in enumerate(row) if z) for row in B]
    ci=[next(k for k,z in enumerate(row) if z) for row in C]
    eqs=[]
    for a,b in pos:
        RB=[[product_unit(v,par,a,b,'right')[k] for k in bi] for v in B]
        RC=[[product_unit(v,par,a,b,'right')[k] for k in ci] for v in C]
        for src in range(d):
            for dest in range(e):
                row=[0]*(d*e)
                for x in range(d):row[dest*d+x]=(row[dest*d+x]+RB[src][x])%p
                for y in range(e):row[y*d+src]=(row[y*d+src]-RC[y][dest])%p
                if any(row):eqs.append(row)
    return d*e-rank(eqs,p)


def test():
    families={
        'chain_3':(-1,0,1),
        'fork_3':(-1,0,0),
        'star_4':(-1,0,0,0),
        'two_chains':(-1,0,-1,2),
        'chain_4':(-1,0,1,2)
    }
    for name,par in families.items():
        pos=matrix_positions(par);R=list(profiles(par));seen=set()
        for r in R:
            B=basis_for_profile(par,r)
            assert profile_of(B,par,2)==r
            assert len(B)==sum(r)
            assert r not in seen;seen.add(r)
            # Each canonical normal form is a two-sided ideal.
            Bcoords={next(i for i,z in enumerate(row) if z) for row in B}
            for v in B:
                for a,b in pos:
                    for side in ('right','left'):
                        z=product_unit(v,par,a,b,side)
                        assert all(t==0 or i in Bcoords for i,t in enumerate(z))
        print(name,'isomorphism types',len(R),'right ideals over F2',sum(fiber_size(par,r,2) for r in R))
        if name=='chain_3':assert len(R)==14
        if name=='fork_3':assert len(R)==13
        if name=='star_4':assert len(R)==35
        if name=='two_chains':assert len(R)==25
        if name in ('chain_3','fork_3'):
            for r in R:
                for s in R:
                    actual=hom_dim(basis_for_profile(par,r),basis_for_profile(par,s),par,2)
                    expected=sum((r[v]-(r[par[v]] if par[v]!=-1 else 0))*s[v] for v in range(len(par)))
                    assert actual==expected,(name,r,s,actual,expected)
    for name,par,p in [('chain_3',(-1,0,1),2),('fork_3',(-1,0,0),2),('fork_3',(-1,0,0),3)]:
        pos=matrix_positions(par)
        obs={r:0 for r in profiles(par)}
        for B in rref_subspaces(len(pos),p):
            if all(rank(B+[product_unit(v,par,a,b,'right')],p)==len(B)
                   for v in B for a,b in pos):
                r=profile_of(B,par,p)
                assert r in obs
                obs[r]+=1
        assert all(obs[r]==fiber_size(par,r,p) for r in obs)
        print('exhaustive:',name,'F',p,'right ideals',sum(obs.values()))
    print('ROOTED_FOREST_ISO_MULTIPLICATION_CHECKS_OK')

if __name__=='__main__':test()
