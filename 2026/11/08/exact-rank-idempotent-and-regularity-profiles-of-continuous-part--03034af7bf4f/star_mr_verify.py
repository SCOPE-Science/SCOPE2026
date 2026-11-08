#!/usr/bin/env python3
"""Direct simplex-preimage census of continuous partial maps of star graphs."""
from collections import Counter
from itertools import product
from math import comb, perm


def observed(n):
    V=range(n+1)
    faces=[frozenset((i,)) for i in V]+[frozenset((0,i)) for i in range(1,n+1)]
    allowed=set(faces)|{frozenset()}
    def continuous(f):
        return all(frozenset(i for i,a in enumerate(f) if a in s) in allowed for s in faces)
    ranks=Counter(); idem=Counter(); nonregular=Counter()
    count=0
    for f in product(range(-1,n+1), repeat=n+1):
        if not continuous(f): continue
        count+=1
        im=set(f);im.discard(-1)
        k=len(im); ranks[k]+=1
        if all(f[i]==-1 or f[f[i]]==f[i] for i in V):idem[k]+=1
        # Search every section of f onto its image, not a structural classification.
        image=sorted(im)
        fib=[[i for i in V if f[i]==y] for y in image]
        regular=False
        for choices in product(*fib):
            g=[-1]*(n+1)
            for y,x in zip(image,choices):g[y]=x
            if not continuous(g):continue
            assert all(g[f[x]]!=-1 and f[g[f[x]]]==f[x] for x in V if f[x]!=-1)
            regular=True;break
        if not regular:nonregular[k]+=1
    return ranks,idem,nonregular,count

def prediction(n,k):
    B=lambda x,y: comb(x,y) if 0<=y<=x else 0
    F=lambda x,y: perm(x,y) if 0<=y<=x else 0
    ranks=B(n,k)*F(n+1,k) + n*n*B(n-1,k-1)*F(n-1,k-1) + B(n,k-1)*F(n,k-1) + (2*n if k==1 else 0) + (n*n if k==2 else 0)
    # The second term in the formula requires k>=1; the convention above fixes this.
    idems=(k+1)*B(n,k)+B(n,k-1)+(n if k==1 else 0)
    nonreg=B(n,k-1)*F(n,k) if k>=2 else 0
    return ranks,idems,nonreg


def main():
    configs=0; examined=0
    for n in range(1,6):
        ranks,idem,nonregular,total=observed(n)
        for k in range(n+2):
            expected=prediction(n,k)
            actual=(ranks[k],idem[k],nonregular[k])
            assert actual==expected,(n,k,actual,expected)
            configs+=1
        assert sum(idem.values())==2**(n+1)+n*2**(n-1)+n
        assert sum(ranks.values())==total
        examined+=total
        print(f'n={n} total={total} ranks={[ranks[k] for k in range(n+2)]} idempotents={[idem[k] for k in range(n+2)]} nonregular={[nonregular[k] for k in range(n+2)]}')
    print(f'VERIFY_OK stars=5 rank_strata={configs} maps={examined} complete_simplex_census=true')
if __name__=='__main__':main()
