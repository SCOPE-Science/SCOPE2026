#!/usr/bin/env python3
"""Targeted adversarial search: tight instances where OPT forced above 8/5.
Ideas: (a) instances where every machine's configs are small (cap 1) but integral
packing collides; (b) structured families: k machines, jobs eligible on pairs;
(c) threshold sizes where beta in (0.5,0.8], alpha small; (d) jobs with |E|=2 mostly.
Also exhaustive-ish local neighborhood search starting from best random instances.
"""
import sys; sys.path.insert(0,'output/artifacts')
from search_gap import all_configs, config_lp_feasible, min_makespan
import random, time, itertools

def eval_inst(p):
    m=len(p); n=len(p[0])
    elig=[[ (j,p[i][j]) for j in range(n) if p[i][j] is not None] for i in range(m)]
    cfgs=[all_configs(es) for es in elig]
    feas,tv,_=config_lp_feasible(cfgs,n)
    if not feas: return (False,None,None)
    return (True,tv,min_makespan(p,None))

def search_pair_structured(seed=3,ntrials=30000):
    rng=random.Random(seed)
    best={'gap':0}
    t0=time.time(); checked=0; feasct=0
    for t in range(ntrials):
        # structured: m machines, jobs on random pairs/triples, sizes adversarial
        m=rng.choice([3,4,5,6,7,8]); n=rng.choice([6,7,8,9,10,11,12])
        a=rng.choice([0.2,0.25,0.3,0.33,0.4]); b=rng.choice([0.6,0.7,0.75,0.8,0.9])
        if a>=b: continue
        p=[[None]*n for _ in range(m)]
        for j in range(n):
            k=rng.choice([2,2,2,3,3])
            Ej=rng.sample(range(m),k=min(k,m))
            # adversarial: big on one, small on other(s) etc.
            style=rng.random()
            for idx,i in enumerate(Ej):
                if style<0.4:
                    p[i][j]=b if idx==0 else a
                elif style<0.7:
                    p[i][j]=a if rng.random()<0.6 else b
                else:
                    p[i][j]=b
        ok,tv,opt=eval_inst(p)
        checked+=1
        if not ok: continue
        feasct+=1
        if opt>best['gap']+1e-9:
            best={'gap':opt,'info':(a,b,m,n)}
            print(f"[{t}] BEST gap={opt:.4f} ({a},{b}) m={m} n={n} t={tv:.3f}",flush=True)
            print("elig=",[[i for i in range(m) if p[i][j] is not None] for j in range(n)],flush=True)
            print("p=",p,flush=True)
            if opt>1.6+1e-9: print("COUNTEREXAMPLE"); return best
    print(f"done checked={checked} feas={feasct} best={best} time={time.time()-t0:.1f}s",flush=True)
    return best

def local_search(seed_inst=None,seed=9,rounds=4000):
    rng=random.Random(seed)
    # start from random feasible tight instance
    a,b,m,n=0.33,0.8,6,7
    p=[[None, None, 0.33, None, None, 0.8, 0.33], [None, 0.33, None, None, 0.33, 0.8, None], [None, None, 0.8, None, None, None, 0.33], [0.33, None, None, 0.33, None, None, None], [None, 0.8, None, 0.8, 0.33, None, None], [0.33, None, None, None, None, None, None]]
    ok,tv,opt=eval_inst(p)
    print("start",ok,tv,opt,flush=True)
    best=(opt,p)
    for r in range(rounds):
        # mutate: flip one entry size or toggle eligibility
        import copy
        q=copy.deepcopy(best[1])
        mm=len(q); nn=len(q[0])
        i=rng.randrange(mm); j=rng.randrange(nn)
        act=rng.random()
        if act<0.5:
            q[i][j]=rng.choice([a,b,None])
        else:
            # swap sizes
            if q[i][j] is not None: q[i][j]=a if q[i][j]==b else b
        # keep every job eligible somewhere
        if all(q[ii][j] is None for ii in range(mm)): continue
        ok2,tv2,opt2=eval_inst(q)
        if not ok2: continue
        if opt2>best[0]+1e-9:
            best=(opt2,q)
            print(f"[{r}] LOCAL BEST gap={opt2:.4f} t={tv2:.3f}",flush=True)
            print("p=",q,flush=True)
            if opt2>1.6+1e-9: print("COUNTEREXAMPLE"); return best
    print("local done best=",best[0],flush=True)
    return best

if __name__=="__main__":
    mode=sys.argv[1] if len(sys.argv)>1 else "struct"
    if mode=="struct": search_pair_structured()
    else: local_search()
