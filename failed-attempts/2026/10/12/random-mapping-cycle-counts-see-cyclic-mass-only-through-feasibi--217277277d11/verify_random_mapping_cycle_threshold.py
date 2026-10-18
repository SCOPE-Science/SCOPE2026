#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, Counter
from fractions import Fraction
from math import prod

def falling(x,r):
    z=1
    for j in range(r): z*=x-j
    return z

def cycle_data(f):
    n=len(f)
    seen_global=[False]*n
    cycles=[]
    for start in range(n):
        if seen_global[start]:
            continue
        path=[]; pos={}; x=start
        while not seen_global[x] and x not in pos:
            pos[x]=len(path); path.append(x); x=f[x]
        if x in pos:
            cyc=path[pos[x]:]
            cycles.append(tuple(cyc))
        for y in path: seen_global[y]=True
    L=sum(len(c) for c in cycles)
    counts=Counter(len(c) for c in cycles)
    return L,counts

def q(n,s):
    return Fraction(falling(n,s),n**s)

def run():
    mappings=0; dist_checks=0; conditional_checks=0; covariance_checks=0
    indicator_independence_checks=0; fixed_mean_checks=0; second_moment_checks=0
    for n in range(2,7):
        rows=[]
        byL=defaultdict(list)
        for f in product(range(n), repeat=n):
            L,c=cycle_data(f)
            F=c.get(1,0)
            I0=int(f[0]==0)
            rows.append((L,c,F,I0))
            byL[L].append((c,F,I0))
            mappings+=1
        N=n**n
        # exact law and tails
        countsL=Counter(L for L,c,F,I0 in rows)
        for m in range(1,n+1):
            target=Fraction(m*falling(n,m),n**(m+1))
            assert Fraction(countsL[m],N)==target
            dist_checks+=1
        for s in range(1,n+1):
            assert Fraction(sum(v for m,v in countsL.items() if m>=s),N)==q(n,s)
            dist_checks+=1

        # all conditional factorial moments
        for ell in range(1,n+1):
            for r in range(1,n//ell+1):
                for m in range(1,n+1):
                    vals=byL[m]
                    if not vals: continue
                    got=Fraction(sum(falling(c.get(ell,0),r) for c,F,I0 in vals),len(vals))
                    target=Fraction(1,ell**r) if m>=r*ell else Fraction(0)
                    assert got==target
                    conditional_checks+=1

                # covariance master for h=L, L^2, and threshold indicators
                X=[falling(c.get(ell,0),r) for L,c,F,I0 in rows]
                for hfun in [lambda L:L, lambda L:L*L, lambda L:int(L>=2)]:
                    H=[hfun(L) for L,c,F,I0 in rows]
                    B=[Fraction(int(L>=r*ell),ell**r) for L,c,F,I0 in rows]
                    EX=Fraction(sum(X),N); EH=Fraction(sum(H),N)
                    covX=Fraction(sum(x*h for x,h in zip(X,H)),N)-EX*EH
                    EB=sum(B,Fraction(0))/N
                    covB=sum((b*h for b,h in zip(B,H)),Fraction(0))/N-EB*EH
                    assert covX==covB
                    covariance_checks+=1

        # fixed point indicator I_0 independent of L
        pI=Fraction(sum(I0 for L,c,F,I0 in rows),N)
        assert pI==Fraction(1,n)
        for m in range(1,n+1):
            joint=Fraction(sum(1 for L,c,F,I0 in rows if L==m and I0),N)
            assert joint==pI*Fraction(countsL[m],N)
            indicator_independence_checks+=1

        # E[F|L=m]=1 and Cov(F,h(L))=0
        for m,vals in byL.items():
            assert Fraction(sum(F for c,F,I0 in vals),len(vals))==1
            fixed_mean_checks+=1
        EL=Fraction(sum(L for L,c,F,I0 in rows),N)
        EF=Fraction(sum(F for L,c,F,I0 in rows),N)
        EFL=Fraction(sum(F*L for L,c,F,I0 in rows),N)
        assert EF==1 and EFL==EL
        fixed_mean_checks+=1

        EF2L=Fraction(sum(F*F*L for L,c,F,I0 in rows),N)
        EF2=Fraction(sum(F*F for L,c,F,I0 in rows),N)
        cov=EF2L-EF2*EL
        assert cov==Fraction(EL-1,n)
        second_moment_checks+=1

    print('VERIFY_OK '
          f'mappings={mappings} dist_checks={dist_checks} '
          f'conditional_checks={conditional_checks} covariance_checks={covariance_checks} '
          f'indicator_independence_checks={indicator_independence_checks} '
          f'fixed_mean_checks={fixed_mean_checks} second_moment_checks={second_moment_checks}')

if __name__=='__main__': run()
