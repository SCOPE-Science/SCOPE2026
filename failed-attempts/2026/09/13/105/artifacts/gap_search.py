"""Heuristic + exact discrepancy search for hereditary gap.
For |J|<=22 exact via bit-parallel enumeration; compare full set vs structured J.
"""
import itertools, random

def ap_sets(N):
    S=set()
    for a in range(N):
        for d in range(1,N):
            k=1
            while a+(k-1)*d < N:
                S.add(tuple(a+i*d for i in range(k)))
                k+=1
    for a in range(N):
        S.add((a,))
    return list(S)

def disc_exact(sets,N,J):
    idx={v:i for i,v in enumerate(J)}
    m=len(J)
    R=[]
    seen=set()
    for s in sets:
        t=tuple(v for v in s if v in idx)
        if t and t not in seen:
            seen.add(t); R.append([idx[v] for v in t])
    # bit-parallel: precompute masks
    masks=[]
    for r in R:
        mask=0
        for i in r: mask|=1<<i
        masks.append(mask)
    best=10**9
    # enumerate colorings as bitmask: bit=1 -> +1, 0 -> -1; sum = 2*popcount(mask&cm)-len
    for cm in range(1<<m):
        mx=0
        for mask,r in zip(masks,R):
            pc=bin(mask & cm).count("1")
            s=2*pc-len(r)
            a=abs(s)
            if a>mx:
                mx=a
                if mx>=best: break
        if mx<best:
            best=mx
            if best<=1:  # can't beat much; early exit only if 0/1 minimal possible
                pass
    return best

def disc_sa(sets,N,J,trials=4000):
    # simulated annealing / random search -> UPPER bound on disc
    idx={v:i for i,v in enumerate(J)}
    R=[]
    seen=set()
    for s in sets:
        t=tuple(v for v in s if v in idx)
        if t and t not in seen:
            seen.add(t); R.append([idx[v] for v in t])
    m=len(J)
    best=10**9
    random.seed(0)
    for _ in range(trials):
        bits=[random.choice((-1,1)) for _ in range(m)]
        # local improve: flip bits greedily few sweeps
        for _sw in range(3):
            for i in range(m):
                cur=max(abs(sum(bits[j] for j in r)) for r in R)
                bits[i]*=-1
                new=max(abs(sum(bits[j] for j in r)) for r in R)
                if new>=cur: bits[i]*=-1
        v=max(abs(sum(bits[j] for j in r)) for r in R)
        if v<best: best=v
    return best

for N in [12,15,18]:
    sets=ap_sets(N)
    full=list(range(N))
    if N<=16:
        d_full=disc_exact(sets,N,full)
    else:
        d_full=disc_sa(sets,N,full,trials=2000)
    print(f"N={N} disc(full)~{d_full}")
    cands={
        "odds":[i for i in range(N) if i%2==0],
        "init_half":list(range(N//2+1)),
        "mod3": [i for i in range(N) if i%3==0],
        "squares": sorted(set((i*i)%N for i in range(N))),
    }
    # random subsets size ~2N/3
    random.seed(1)
    for _ in range(3):
        cands[f"rand{_}"]=sorted(random.sample(range(N),2*N//3))
    for name,J in cands.items():
        if len(J)<=20 and N<=16:
            d=disc_exact(sets,N,J)
        else:
            d=disc_sa(sets,N,J,trials=2000)
        print(f"   J={name} |J|={len(J)} disc~{d}")
print("done")
