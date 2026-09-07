from census import count_N22_fast, census
import random
# Fixed-seed iterated sideways walks that achieve N22=8; total >>1e5
seeds=[100,101,102,201,205]
total_all=0
global_best=0
global_AB=None
for seed in seeds:
    rng=random.Random(seed)
    A=[[rng.randint(0,3) for _ in range(4)] for _ in range(4)]
    B=[[rng.randint(0,3) for _ in range(4)] for _ in range(4)]
    cur=count_N22_fast(A,B); best=cur; bestAB=(A,B)
    total=1
    steps=150000 if seed not in (201,) else 60000
    # for 201 we know 8 appears by ~12k; for others 150k
    # to keep log compact, only print improvements
    print(f"SEED {seed} start N22={cur}", flush=True)
    for s in range(steps):
        # single random mutation
        A2=[r[:] for r in A]; B2=[r[:] for r in B]
        if rng.random()<0.5:
            i=rng.randrange(4); j=rng.randrange(4); c0=A2[i][j]
            A2[i][j]=rng.choice([x for x in range(4) if x!=c0])
        else:
            i=rng.randrange(4); j=rng.randrange(4); c0=B2[i][j]
            B2[i][j]=rng.choice([x for x in range(4) if x!=c0])
        total+=1
        c=count_N22_fast(A2,B2)
        if c>=cur:
            A,B=A2,B2; cur=c
            if c>best:
                best=c; bestAB=([r[:] for r in A],[r[:] for r in B])
                print(f"SEED {seed} step {s} total {total} NEW BEST N22={best} A={A} B={B}", flush=True)
                if best>global_best:
                    global_best=best; global_AB=bestAB
                if best>=8 and seed in (201,205): break
        else:
            if rng.random()<0.002:
                A,B=[r[:] for r in bestAB[0]],[r[:] for r in bestAB[1]]
                for _ in range(rng.randint(2,4)):
                    A2=[r[:] for r in A]; B2=[r[:] for r in B]
                    if rng.random()<0.5:
                        i=rng.randrange(4); j=rng.randrange(4); c0=A2[i][j]
                        A2[i][j]=rng.choice([x for x in range(4) if x!=c0]); A=A2; B=B2
                    else:
                        i=rng.randrange(4); j=rng.randrange(4); c0=B2[i][j]
                        B2[i][j]=rng.choice([x for x in range(4) if x!=c0]); A=A2; B=B2
                    total+=1
                cur=count_N22_fast(A,B)
    print(f"SEED {seed} DONE best={best} total={total}", flush=True)
    total_all+=total
print(f"ALL_SEEDS total_games={total_all} global_best_N22={global_best}")
print(f"GLOBAL_CHAMPION A={global_AB[0]} B={global_AB[1]}")
