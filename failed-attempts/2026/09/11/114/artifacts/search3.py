"""Continue hill-climb; also restart from multiple seeds. Import trick: load search without rerun."""
import itertools, random, time, importlib, sys
sys.path.insert(0,'output/artifacts')
import search as S
rng=random.Random(9)
start_cfg=[(0,5,4),(0,6,5),(3,6,1),(6,3,3),(0,4,5),(3,3,4),(0,3,0),(0,0,5),(0,2,3),(6,2,3)]
bs=S.score(start_cfg); print("start:",bs,flush=True)
best_cfg=start_cfg; t0=time.time(); it=0
while time.time()-t0<50:
    it+=1
    i=rng.randrange(10); j=rng.randrange(3)
    d=rng.choice([-1,1])
    cfg=list(best_cfg); c=list(cfg[i]); c[j]+=d
    if not (-1<=c[j]<=7): continue
    cfg[i]=tuple(c)
    if len(set(cfg))<10: continue
    s=S.score(cfg)
    if s<bs:
        bs=s; best_cfg=cfg
        print(f"iter {it}: improved to {bs} cfg={best_cfg} t={round(time.time()-t0,1)}",flush=True)
        if bs==0: break
print("FINAL:",bs,best_cfg)
