"""Exact finite-state proof checks for SIR peak-capacity monotonicity under edge addition.
Usage: python verify_peak.py --start 0 --stop 5  (repeat through 21)
       python verify_peak.py --witness
Dependencies: Python 3.10+, SymPy 1.12+ (small-graph symbolic check).
"""
import argparse
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations
import sympy as S

r = S.Symbol('r')


def connected(n, edges):
    seen={0}; changed=True
    while changed:
        changed=False
        for u,v in edges:
            if u in seen and v not in seen: seen.add(v);changed=True
            if v in seen and u not in seen: seen.add(u);changed=True
    return len(seen)==n


def unlabeled_connected(n):
    pairs=list(combinations(range(n),2)); idx={e:i for i,e in enumerate(pairs)}
    maps=[]
    for perm in permutations(range(n)):
        maps.append(tuple(idx[tuple(sorted((perm[u],perm[v])))] for u,v in pairs))
    reps=set()
    for bits in range(1<<len(pairs)):
        E=tuple(pairs[j] for j in range(len(pairs)) if bits>>j&1)
        if not connected(n,E):continue
        canonical=min(sum(1<<mapping[j] for j in range(len(pairs)) if bits>>j&1) for mapping in maps)
        reps.add(canonical)
    return [tuple(pairs[j] for j in range(len(pairs)) if bits>>j&1) for bits in sorted(reps)]


@lru_cache(None)
def all_seeds(n, edges, threshold):
    nei=[0]*n
    for a,b in edges:nei[a]|=1<<b;nei[b]|=1<<a
    @lru_cache(None)
    def hit(s,i):
        if i.bit_count()>=threshold:return S.S.One
        if i==0:return S.S.Zero
        total=S.Integer(i.bit_count()); terms=[]
        for v in range(n):
            if i>>v&1:terms.append(hit(s,i^(1<<v)))
            if s>>v&1:
                cnt=(nei[v]&i).bit_count()
                if cnt:
                    total+=r*cnt
                    terms.append(r*cnt*hit(s^(1<<v),i|(1<<v)))
        return S.cancel(S.Add(*terms)/total)
    return tuple(hit(((1<<n)-1)^(1<<v),1<<v) for v in range(n))


def check_graph(n,E):
    pairs=set(combinations(range(n),2)); checked=0;nonzero=0;maxdegree=0
    for extra in sorted(pairs-set(E)):
        H=tuple(sorted(E+(extra,)))
        for threshold in range(2,n+1):
            before=all_seeds(n,E,threshold); after=all_seeds(n,H,threshold)
            for seed in range(n):
                checked+=1
                num,den=S.fraction(S.cancel(after[seed]-before[seed]))
                if num==0:continue
                PN,PD=S.Poly(num,r),S.Poly(den,r)
                if not all(z>=0 for z in PN.all_coeffs()):
                    raise AssertionError(('numerator negative coefficient',n,E,extra,seed,threshold,str(PN)))
                if not all(z>=0 for z in PD.all_coeffs()):
                    raise AssertionError(('denominator negative coefficient',n,E,extra,seed,threshold,str(PD)))
                if not (PN.eval(1)>0 and PD.eval(1)>0):
                    raise AssertionError(('wrong sign at r=1',n,E,extra,seed,threshold))
                nonzero+=1;maxdegree=max(maxdegree,PN.degree(),PD.degree())
    return checked,nonzero,maxdegree


def exact_witness(edges,seed=1,k=6,beta=50):
    n=6;nei=[0]*n
    for a,b in edges:nei[a]|=1<<b;nei[b]|=1<<a
    @lru_cache(None)
    def hit(s,i):
        if i.bit_count()>=k:return Fraction(1)
        if i==0:return Fraction(0)
        total=Fraction(i.bit_count()); terms=[]
        for v in range(n):
            if i>>v&1: terms.append((Fraction(1),s,i^(1<<v)))
            if s>>v&1:
                cnt=(nei[v]&i).bit_count()
                if cnt:total+=beta*cnt;terms.append((Fraction(beta*cnt),s^(1<<v),i|(1<<v)))
        return sum((rate*hit(ss,ii) for rate,ss,ii in terms),Fraction(0))/total
    return hit(((1<<n)-1)^(1<<seed),1<<seed)


def witness():
    E=((0,4),(0,5),(1,3),(2,3),(3,4))
    old=exact_witness(E);new=exact_witness(E+((1,2),))
    assert old==Fraction(14289062500,18273931533)
    assert new==Fraction(1946796875000,2491078937193)
    assert old-new==Fraction(24352320312500,56704429847324259)>0
    print('WITNESS_PASS', 'tree',old,'with_extra',new,'difference',old-new)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--start',type=int,default=0);parser.add_argument('--stop',type=int,default=21);parser.add_argument('--witness',action='store_true');args=parser.parse_args()
    if args.witness:witness();return
    totals=[]
    classes={n:unlabeled_connected(n) for n in (2,3,4,5)}
    assert {n:len(g) for n,g in classes.items()}=={2:1,3:2,4:6,5:21}
    for n in (2,3,4):
        if args.start:continue
        for E in classes[n]:totals.append((n,*check_graph(n,E)))
    for idx in range(args.start,min(args.stop,len(classes[5]))):
        E=classes[5][idx]; results=check_graph(5,E);totals.append((5,*results))
        print('CLASS_PASS',idx,'edges',len(E),'tested',results[0],'strict',results[1],'max_degree',results[2],flush=True)
    print('BATCH_PASS',args.start,args.stop,'checks',sum(x[1] for x in totals),'strict',sum(x[2] for x in totals),'max_degree',max((x[3] for x in totals),default=0))

if __name__=='__main__':main()
