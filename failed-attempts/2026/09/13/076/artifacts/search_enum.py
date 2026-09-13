#!/usr/bin/env python3
"""Proof-route check: can the Shmoys-Tardos / GAP rounding be pushed for two sizes?
Key lemma to verify computationally: given assignment-LP solution y at T=1 with
two sizes {a,b}, does there exist rounding to makespan <= 8/5?
Check the 'fractional big-job' structure: prove that any fractional extreme point
has a machine with <=1 fractional big job etc. Instead: brute-force check on small
instances whether the natural LP-guided rounding (match bigs then flow smalls)
succeeds, to find where it breaks. For now: exhaustive enumeration of tiny
instances (m=2,3; n<=6; sizes from small grid) computing exact gap — full coverage
of small cases to either find counterexample or confirm gap<=1.6 there."""
import sys; sys.path.insert(0,'output/artifacts')
from search_gap import all_configs, config_lp_feasible, min_makespan
import itertools, time

def enum_two_machine():
    """m=2: full enumeration over eligibility patterns and size assignments.
    For m=2, each job: E in {{0},{1},{0,1}}, sizes on eligible machines in {a,b}.
    Fix (a,b) grid; enumerate all instances with n<=5 up to symmetry. Report max gap."""
    import itertools
    grid=[(0.2,0.6),(0.25,0.75),(1/3,2/3),(0.3,0.8),(0.4,0.7),(0.4,0.9),(0.5,0.8),(0.2,0.8),(0.1,0.9),(0.45,0.8),(0.6,1.0),(0.5,1.0)]
    worst=0; worstinfo=None
    for a,b in grid:
        # job types: (E, sizes...). E=0:{0},1:{1},2:{0,1} with (s0,s1) in {a,b}^2
        types=[(0,(a,)),(0,(b,)),(1,(a,)),(1,(b,)),(2,(a,a)),(2,(a,b)),(2,(b,a)),(2,(b,b))]
        for n in [3,4,5]:
            for inst in itertools.product(range(len(types)),repeat=n):
                # symmetry break: nondecreasing type sequence
                if list(inst)!=sorted(inst): continue
                p=[[None]*n for _ in range(2)]
                for j,t in enumerate(inst):
                    E,ss=types[t]
                    if E==0: p[0][j]=ss[0]
                    elif E==1: p[1][j]=ss[0]
                    else: p[0][j]=ss[0]; p[1][j]=ss[1]
                elig=[[ (j,p[i][j]) for j in range(n) if p[i][j] is not None] for i in range(2)]
                cfgs=[all_configs(es) for es in elig]
                feas,tv,_=config_lp_feasible(cfgs,n)
                if not feas: continue
                opt=min_makespan(p,None)
                if opt>worst+1e-9:
                    worst=opt; worstinfo=(a,b,n,inst)
                    print(f"m=2 NEW worst gap={opt:.4f} ({a:.3f},{b:.3f}) n={n} types={inst} t={tv:.3f}",flush=True)
                    if opt>1.6+1e-9: print("COUNTEREXAMPLE m=2!"); return
    print("m=2 exhaustive done worst=",worst,worstinfo,flush=True)

def enum_three_machine_sample():
    """m=3 random dense coverage with n<=7 already done; here: all-eligible small
    enumeration to test the all-eligible proof sketch."""
    import random
    rng=random.Random(5)
    worst=0
    for trial in range(20000):
        m=3; n=rng.choice([4,5,6,7])
        a=rng.choice([0.2,0.3,0.4]); b=rng.choice([0.6,0.7,0.8,0.9])
        p=[[rng.choice([a,b]) for _ in range(n)] for _ in range(m)]
        elig=[[ (j,p[i][j]) for j in range(n)] for i in range(m)]
        cfgs=[all_configs(es) for es in elig]
        feas,tv,_=config_lp_feasible(cfgs,n)
        if not feas: continue
        opt=min_makespan(p,None)
        if opt>worst+1e-9:
            worst=opt; print(f"allel BEST {opt:.4f} ({a},{b}) n={n} t={tv:.3f}",flush=True)
    print("all-eligible sample worst=",worst,flush=True)

if __name__=="__main__":
    enum_two_machine()
    enum_three_machine_sample()
