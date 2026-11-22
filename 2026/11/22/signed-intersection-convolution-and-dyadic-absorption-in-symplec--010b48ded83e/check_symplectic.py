"""Standalone exhaustive composition check for rank-n symplectic rook factors.
Only uses tuples encoding partial injections and explicit composition.
"""
from itertools import permutations, product, combinations
from collections import Counter
from math import comb, factorial

def transversals(n,r):
    for coords in combinations(range(n),r):
        for signs in product((0,1),repeat=r):
            yield tuple(2*i+s for i,s in zip(coords,signs))

def rank_r_maps(n,r):
    for domain in transversals(n,r):
        for im in transversals(n,r):
            for perm in permutations(im):
                arr=[-1]*(2*n)
                for x,y in zip(domain,perm): arr[x]=y
                yield tuple(arr)

def compose(g,f):
    return tuple(-1 if y==-1 else g[y] for y in f)

def rank(f):
    return sum(x!=-1 for x in f)

def verify(n,kmax):
    elems=list(rank_r_maps(n,n))
    assert len(elems)==4**n*factorial(n)
    freq=Counter(elems)
    for k in range(1,kmax+1):
        total=len(elems)**k
        pnum=1
        den=2**(k-1)
        rank_cnt=Counter()
        perrank={}
        for f,v in freq.items():
            r=rank(f)
            rank_cnt[r]+=v
            if r not in perrank: perrank[r]=v
            assert v==perrank[r],(n,k,r,v,perrank[r])
        for r in range(n+1):
            num=total*comb(n,r)*(den-1)**(n-r)
            denom=den**n
            assert num%denom==0
            predicted=num//denom
            assert rank_cnt[r]==predicted,(n,k,r,rank_cnt[r],predicted)
            number=4**r*comb(n,r)**2*factorial(r)
            assert perrank.get(r,0)*number==predicted,(n,k,r,perrank.get(r,0),predicted,number)
        print('PASS', 'n',n,'k',k,'factors',len(elems),'attained_targets',len(freq), 'rank_counts',sorted(rank_cnt.items()))
        if k<kmax:
            nxt=Counter()
            for f,c in freq.items():
                for g in elems:
                    nxt[compose(g,f)]+=c
            freq=nxt



def check_full_convolution(n):
    from fractions import Fraction
    levels={r:list(rank_r_maps(n,r)) for r in range(n+1)}
    for r in range(n+1):
        for s in range(n+1):
            out=Counter()
            for f in levels[r]:
                for g in levels[s]:
                    out[compose(g,f)]+=1
            rank_counts=Counter()
            values={}
            for f,c in out.items():
                t=rank(f)
                rank_counts[t]+=c
                if t not in values: values[t]=c
                assert values[t]==c,(n,r,s,t,'nonuniform',f)
            for t in range(min(r,s)+1):
                numerator=comb(r,t)*sum(comb(r-t,j)*comb(n-r,s-t-j)*2**(s-t-j)
                    for j in range(min(r-t,s-t)+1) if 0<=s-t-j<=n-r)
                probability=Fraction(numerator,2**s*comb(n,s))
                predicted=probability*len(levels[r])*len(levels[s])
                assert predicted.denominator==1
                assert rank_counts[t]==predicted.numerator,(n,r,s,t,rank_counts[t],predicted)
                nt=4**t*comb(n,t)**2*factorial(t)
                assert values.get(t,0)*nt==predicted.numerator,(n,r,s,t,'target',values.get(t,0),predicted)
            assert sum(rank_counts.values())==len(levels[r])*len(levels[s])
    print('PASS full rank-class convolution n',n,'levels',[len(levels[r]) for r in levels])

if __name__=='__main__':
    for n,kmax in [(1,6),(2,5),(3,4)]:
        verify(n,kmax)
    for n in (1,2,3): check_full_convolution(n)
    print('ALL EXHAUSTIVE CHECKS PASSED')

# Mixed-length independent validation of the signed-intersection formula.
# This is executed as a separate entrypoint call, not during the standard run.
def check_mixed(n,profiles):
    from fractions import Fraction
    classes={r:list(rank_r_maps(n,r)) for r in range(n+1)}
    for rs in profiles:
        freq=Counter({x:1 for x in classes[rs[0]]})
        for r in rs[1:]:
            nxt=Counter()
            for f,c in freq.items():
                for g in classes[r]:
                    nxt[compose(g,f)]+=c
            freq=nxt
        k=len(rs)
        tot=1
        for r in rs:tot*=len(classes[r])
        rank_count=Counter()
        seen={}
        for f,c in freq.items():
            j=rank(f)
            rank_count[j]+=c
            assert seen.setdefault(j,c)==c,(n,rs,j,'unequal fibers')
        for s in range(min(rs)+1):
            pm=Fraction(0)
            for j in range(s,min(rs)+1):
                v=Fraction(comb(n,j),2**((k-1)*j))
                for r in rs:
                    v*=Fraction(comb(r,j),comb(n,j))
                pm+=(-1)**(j-s)*comb(j,s)*v
            exp=tot*pm
            assert exp.denominator==1
            assert rank_count[s]==exp.numerator,(n,rs,s,rank_count[s],exp)
            Ns=4**s*comb(n,s)**2*factorial(s)
            assert seen.get(s,0)*Ns==exp.numerator
        print('PASS mixed all-arity',n,rs,sorted(rank_count.items()))

if __name__=='__main__':
    check_mixed(2,[(a,b,c) for a in range(3) for b in range(3) for c in range(3)])
    check_mixed(3,[(3,1,3),(2,2,1),(3,3,2)])
