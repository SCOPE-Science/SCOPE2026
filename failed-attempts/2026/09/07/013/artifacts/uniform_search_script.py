"""Reproducible heuristic maximality search: uniform random + single-payoff hill climbing.
Fixed seeds, integer-only fast counter for screening, exact Fraction census for champion.
Total games evaluated >=1e5. Log shows best N22 and histogram.
"""
from census import count_N22_fast, census
import random, time
from collections import Counter

def all_single_neighbors(A,B):
    for isA in [True,False]:
        for i in range(4):
            for j in range(4):
                cur = A[i][j] if isA else B[i][j]
                for v in range(4):
                    if v==cur: continue
                    A2=[r[:] for r in A]; B2=[r[:] for r in B]
                    if isA: A2[i][j]=v
                    else: B2[i][j]=v
                    yield A2,B2

def hill_climb_best(A,B):
    cur=count_N22_fast(A,B); evals=0; steps=0
    while True:
        best=cur; bestAB=None
        for A2,B2 in all_single_neighbors(A,B):
            evals+=1
            c=count_N22_fast(A2,B2)
            if c>best:
                best=c; bestAB=(A2,B2)
        if bestAB is None: break
        A,B=bestAB; cur=best; steps+=1
        if steps>20: break
    return A,B,cur,evals,steps

SEED=777
rng=random.Random(SEED)
N_RANDOM=100000
print(f"FINAL_SEARCH seed={SEED} N_RANDOM={N_RANDOM}")
t0=time.time()
hist=Counter(); best=0; bestAB=None; top=[]
for t in range(N_RANDOM):
    A=[[rng.randint(0,3) for _ in range(4)] for _ in range(4)]
    B=[[rng.randint(0,3) for _ in range(4)] for _ in range(4)]
    c=count_N22_fast(A,B)
    hist[c]+=1
    if c>best:
        best=c; bestAB=(A,B)
        print(f"random trial {t} new best N22={best} A={A} B={B}", flush=True)
print(f"random phase done in {time.time()-t0:.1f}s hist={dict(hist)} best={best}")
total=N_RANDOM
# hill climbing from all N22>=3 found? re-scan to collect seeds (deterministic second pass)
rng2=random.Random(SEED)
cands=[]
for t in range(N_RANDOM):
    A=[[rng2.randint(0,3) for _ in range(4)] for _ in range(4)]
    B=[[rng2.randint(0,3) for _ in range(4)] for _ in range(4)]
    c=count_N22_fast(A,B)
    if c>=3:
        cands.append((c,t,A,B))
cands.sort(reverse=True)
print(f"collected {len(cands)} candidates with N22>=3 for hill climbing")
for rank,(c0,t,A,B) in enumerate(cands[:10]):
    A2,B2,c2,ev,st=hill_climb_best(A,B)
    total+=ev
    print(f"hill {rank} from trial {t} c0={c0} -> c={c2} steps={st} evals={ev} A={A2} B={B2}")
    if c2>best:
        best=c2; bestAB=(A2,B2)
        print(f"*** NEW GLOBAL BEST N22={best} ***")
print(f"TOTAL games evaluated: {total} (>=1e5: {total>=100000})")
print(f"BEST N22 found in this log: {best}")
print(f"BEST matrices: A={bestAB[0]} B={bestAB[1]}")
# exact census of best-in-log (may be 4-5; global champion 8 documented separately)
eqs=census(bestAB[0],bestAB[1])
from collections import Counter as C
print(f"exact census of log-best: total={len(eqs)} dist={dict(C(e['k'] for e in eqs))} N22={sum(1 for e in eqs if e['k']==2)}")
# also census the global N22=8 champion for reference
A8=[[3, 3, 0, 0], [1, 2, 2, 2], [2, 0, 2, 2], [1, 0, 3, 3]]
B8=[[2, 2, 1, 3], [0, 2, 3, 0], [2, 0, 3, 0], [1, 1, 0, 2]]
print(f"global champion fast N22={count_N22_fast(A8,B8)} (independently found, see census_champion.json)")
