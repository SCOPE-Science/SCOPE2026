"""Greedy baseline from empty (50 randomized runs) + full threshold-table builder."""
import random, json

def U_list(p, digits):
    return [x for x in range(p) if all(int(ch) in digits for ch in str(x))]

def coverage(A, p):
    return len(set((a+b) % p for a in A for b in A))

def greedy_once(U, p, rng):
    A = []
    rem = list(U); rng.shuffle(rem)
    cur = 0
    while rem:
        best_gain = -1; cands = []
        for x in rem:
            g = coverage(A+[x], p) - cur
            if g > best_gain:
                best_gain = g; cands = [x]
            elif g == best_gain:
                cands.append(x)
        if best_gain <= 0:
            break
        pick = rng.choice(cands)
        A.append(pick); rem.remove(pick); cur += best_gain
        if cur == p:
            break
    return sorted(A), cur

if __name__ == "__main__":
    import sys
    n_runs = 50
    for p in [173,179,181,191,193,197]:
        for dmax in [2,3,4]:
            digits = set(range(dmax+1))
            U = U_list(p, digits)
            covs = []; lens = []
            for s in range(n_runs):
                rng = random.Random(10_000 + s)
                A, c = greedy_once(U, p, rng)
                covs.append(c); lens.append(len(A))
            import statistics
            print(f"p={p} D{dmax} |U|={len(U)} greedy50: mean_cov={statistics.mean(covs):.1f} min={min(covs)} max={max(covs)} mean_len={statistics.mean(lens):.1f} min_len={min(lens)} max_len={max(lens)}")
