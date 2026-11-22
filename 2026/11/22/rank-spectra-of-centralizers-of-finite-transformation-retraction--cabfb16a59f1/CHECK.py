"""Independent exhaustive finite checks of rank enumerators of idempotent transformation centralizers."""
from itertools import product
from math import comb
from collections import Counter

def model(blocks):
    n = sum(blocks); roots=[]; group=[]; ix=0
    for j,b in enumerate(blocks):
        roots.append(ix);group.extend([j]*b);ix+=b
    e=tuple(roots[group[i]] for i in range(n))
    return e,roots,group

def occupancy(b,m):
    return {h:comb(b-1,h)*sum((-1)**k*comb(h,k)*(1+h-k)**m for k in range(h+1)) for h in range(min(b-1,m)+1)}

def rank_poly(blocks,idempotent_only=False):
    r=len(blocks)
    out=Counter()
    for g in product(range(r),repeat=r):
        if idempotent_only and any(g[g[i]]!=g[i] for i in range(r)):
            continue
        poly=Counter({0:1})
        for j in set(g):
            m=sum(blocks[i]-1 for i in range(r) if g[i]==j)
            if not idempotent_only:
                terms={h+1:c for h,c in occupancy(blocks[j],m).items()}
            else:
                terms={h+1:comb(blocks[j]-1,h)*(h+1)**(m-h) for h in range(blocks[j])}
            new=Counter()
            for a,ca in poly.items():
                for b,cb in terms.items():new[a+b]+=ca*cb
            poly=new
        out.update(poly)
    return dict(sorted((k,v) for k,v in out.items() if v))

def brute(blocks):
    e,roots,group=model(blocks)
    n=sum(blocks)
    full=Counter(); idem=Counter()
    for f in product(range(n),repeat=n):
        if any(f[e[i]]!=e[f[i]] for i in range(n)):continue
        r=len(set(f));full[r]+=1
        if all(f[f[i]]==f[i] for i in range(n)):idem[r]+=1
    return dict(sorted(full.items())),dict(sorted(idem.items()))

def part(n,low=1):
    if n==0: yield ()
    else:
        for a in range(low,n+1):
            for tail in part(n-a,a):yield (a,)+tail

def run():
    total=0
    for n in range(1,6):
        for b in part(n):
            f,i=brute(b)
            F,I=rank_poly(b),rank_poly(b,True)
            assert f==F,(b,f,F)
            assert i==I,(b,i,I)
            total+=1
    for b in [(3,2,1),(2,2,2),(4,2),(5,1)]:
        f,i=brute(b)
        F,I=rank_poly(b),rank_poly(b,True)
        assert f==F,(b,f,F)
        assert i==I,(b,i,I)
        total+=1
    for n in range(1,9):
        for blocks in part(n):
            r=len(blocks)
            if r>5:continue
            N=n-r
            F,I=rank_poly(blocks),rank_poly(blocks,True)
            expected_f=comb(r,2)*(2**r-2)+(N*(2**N-1) if N else 0)
            expected_i=comb(r,2)*2**(r-2) if r>=2 else 0
            expected_i+=N*2**(N-1) if N else 0
            assert F.get(1,0)==I.get(1,0)==r
            assert F.get(2,0)==expected_f,(blocks,'full rank 2',F,expected_f)
            assert I.get(2,0)==expected_i,(blocks,'idem rank 2',I,expected_i)
        
    print('ALL PASS configurations',total)
    for b in [(3,2),(3,2,1),(2,2,2),(4,2)]:
        print('BLOCKS',b,'F',rank_poly(b),'I',rank_poly(b,True))
if __name__=='__main__':run()
