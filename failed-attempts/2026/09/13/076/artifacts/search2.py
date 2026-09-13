#!/usr/bin/env python3
import sys; sys.path.insert(0,'output/artifacts')
from search_gap import all_configs, config_lp_feasible, min_makespan
import random, time, json
seed=int(sys.argv[1]) if len(sys.argv)>1 else 2
ntrials=int(sys.argv[2]) if len(sys.argv)>2 else 20000
rng=random.Random(seed)
best={'gap':1.0}
checked=0; feasct=0; t0=time.time()
pairs=[(0.2,0.8),(0.3,0.7),(0.25,0.75),(0.4,0.8),(0.15,0.65),(0.35,0.75),(0.3,0.6),(0.5,0.9),(0.1,0.6),(0.45,0.9),(0.2,0.7),(0.33,0.8),(0.4,1.0)]
for t in range(ntrials):
    a,b=rng.choice(pairs)
    m=rng.choice([3,4,5,6]); n=rng.choice([6,7,8,9,10])
    dens=rng.choice([0.35,0.45,0.55])
    p=[[None]*n for _ in range(m)]
    for j in range(n):
        Ej=rng.sample(range(m),k=max(1,int(round(dens*m))))
        for i in Ej:
            p[i][j]=a if rng.random()<0.5 else b
    elig=[[ (j,p[i][j]) for j in range(n) if p[i][j] is not None] for i in range(m)]
    cfgs=[all_configs(es) for es in elig]
    feas,tv,_=config_lp_feasible(cfgs,n)
    checked+=1
    if not feas: continue
    feasct+=1
    opt=min_makespan(p,None)
    if opt>best['gap']+1e-9:
        best={'gap':opt,'info':(a,b,m,n)}
        print(f"[{t}] NEW BEST gap={opt:.4f} ({a},{b}) m={m} n={n}",flush=True)
        print("elig=",[[i for i in range(m) if p[i][j] is not None] for j in range(n)],flush=True)
        print("p=",p,flush=True)
        if opt>1.6+1e-9:
            print("COUNTEREXAMPLE",flush=True); break
print(f"done checked={checked} feas={feasct} best={best} time={time.time()-t0:.1f}s",flush=True)
