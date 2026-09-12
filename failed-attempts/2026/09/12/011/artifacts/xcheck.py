"""Independent cross-check: plain recursive generation inserting max n,
checking pattern containment by brute force over all index quadruples.
Different code path from census.c (no incremental lemma)."""
import itertools, sys

def contains(pat, perm):
    k = len(pat)
    for idx in itertools.combinations(range(len(perm)), k):
        vals = [perm[i] for i in idx]
        # rank
        order = sorted(range(k), key=lambda t: vals[t])
        rank = [0]*k
        for r, t in enumerate(order):
            rank[t] = r+1
        if rank == list(pat):
            return True
    return False

def census(bases, nmax):
    counts = [0]*(nmax+1)
    counts[0] = 1
    live = [()]  # perms of current length avoiding all bases
    for n in range(1, nmax+1):
        new = []
        for q in live:
            for p in range(n):
                c = q[:p] + (n,) + q[p:]
                if any(contains(b, c) for b in bases):
                    continue
                new.append(c)
        counts[n] = len(new)
        live = new
        print(f"n={n} count={len(new)}", flush=True)
    return counts

N = int(sys.argv[1]) if len(sys.argv) > 1 else 9
print("A = Av(4231,3124):")
a = census([(4,2,3,1),(3,1,2,4)], N)
print("B = Av(4231,3214):")
b = census([(4,2,3,1),(3,2,1,4)], N)
print("A:", a)
print("B:", b)
