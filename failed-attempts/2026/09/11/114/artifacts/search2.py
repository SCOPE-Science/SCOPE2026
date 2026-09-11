"""Focused local search from the best config: hill-climb to minimize strict-uniform count."""
import itertools, random, time
import search as S
verts=list(range(10))
rng=random.Random(5)
best_cfg=[(0,5,3),(0,6,6),(3,6,0),(6,3,4),(0,4,5),(3,3,4),(0,4,0),(0,0,5),(0,2,3),(5,2,3)]
bs=S.score(best_cfg); print("start:",bs,flush=True)
t0=time.time(); it=0
while time.time()-t0<48:
    it+=1
    i=rng.randrange(10); j=rng.randrange(3)
    d=rng.choice([-1,1])
    cfg=list(best_cfg); c=list(cfg[i]); c[j]+=d
    if not (0<=c[j]<=6): continue
    cfg[i]=tuple(c)
    if len(set(cfg))<10: continue
    s=S.score(cfg)
    if s<bs:
        bs=s; best_cfg=cfg
        print(f"iter {it}: improved to {bs} cfg={best_cfg} t={round(time.time()-t0,1)}",flush=True)
        if bs==0: break
print("FINAL:",bs,best_cfg)
