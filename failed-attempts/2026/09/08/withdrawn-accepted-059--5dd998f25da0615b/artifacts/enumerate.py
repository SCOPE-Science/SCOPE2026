"""Exhaustive enumeration of max rainbow-Schur counts R(n), n<=12.
Convention: ordered triples (x,y,z) in [1,n]^3 with x+y=z.
WLOG fix c(1)=0 by global S3 color permutation (valid for maximum value).
Enumerates 3^(n-1) colorings per n; tracks max, labeled-optimum count,
and S3-inequivalent class representatives (canonical min over 6 perms).
Stdlib only.
"""
import json, time, itertools

def schur_triples(n):
    t = []
    for z in range(2, n + 1):
        for x in range(1, z):
            y = z - x
            t.append((x, y, z))
    return t

def rcount(col, trips):
    # col 1-indexed list
    c = 0
    for x, y, z in trips:
        a, b, d = col[x], col[y], col[z]
        if a != b and b != d and a != d:
            c += 1
    return c

PERMS = list(itertools.permutations((0, 1, 2)))

def canonical(col_tuple):
    return min(tuple(p[v] for v in col_tuple) for p in PERMS)

def main():
    t0 = time.time()
    out = {}
    for n in range(1, 13):
        trips = schur_triples(n)
        T = len(trips)
        best = -1
        nfix_opt = 0      # # optima with c1=0
        classes = {}      # canonical -> example
        wit = None
        # enumerate positions 2..n base-3
        m = 3 ** (n - 1) if n >= 1 else 1
        for idx in range(m):
            col = [0] * (n + 1)
            v = idx
            for i in range(2, n + 1):
                col[i] = v % 3
                v //= 3
            c = rcount(col, trips)
            if c > best:
                best = c
                wit = tuple(col[1:])
                nfix_opt = 1
                classes = {canonical(wit): wit}
            elif c == best:
                nfix_opt += 1
                key = canonical(tuple(col[1:]))
                if key not in classes:
                    classes[key] = tuple(col[1:])
        labeled_opt = nfix_opt * 3  # lift c1=0 slice -> all 3 choices of c1
        out[str(n)] = {
            "T": T,
            "R": best,
            "witness_c1fix": list(wit),
            "n_opt_c1fix": nfix_opt,
            "n_opt_labeled": labeled_opt,
            "n_classes_S3": len(classes),
            "class_reps": [list(r) for r in sorted(classes.values())],
        }
        print(f"n={n} T={T} R={best} frac={best/T if T else 0:.4f} "
              f"opt_c1fix={nfix_opt} labeled={labeled_opt} classes={len(classes)}", flush=True)
    out["_meta"] = {"convention": "ordered triples x+y=z", "symmetry": "c1 fixed to 0, lifted by 3",
                    "seconds": round(time.time() - t0, 2)}
    with open("results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote results.json in %.1fs" % (time.time() - t0))

if __name__ == "__main__":
    main()
