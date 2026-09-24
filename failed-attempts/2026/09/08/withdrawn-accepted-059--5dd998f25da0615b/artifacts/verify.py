"""Independent verifier for rainbow-Schur maxima R(n), n<=12.
Independent code path from enumerate.py: full 3^n labeled product (no c1
fixing), set-based rainbow test, S3-orbit checks, and c0-template recount.
Usage: python3 verify.py  (run inside output/artifacts/)
"""
import json
import itertools

PERMS = list(itertools.permutations((0, 1, 2)))

def triples(n):
    return [(x, z - x, z) for z in range(1, n + 1) for x in range(1, z)]

def is_rainbow(col, t):
    a, b, c = (col[v - 1] for v in t)
    return len({a, b, c}) == 3

def count_rainbow(col, trips):
    return sum(1 for t in trips if is_rainbow(col, t))

def s3_orbit(col):
    return {tuple(p[v] for v in col) for p in PERMS}

def template_c0(n):
    # Parczyk-Spiegel c0 with labels 1,2,3 -> 0,1,2 ; 2n/5 threshold real-valued
    out = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            out.append(2)
        elif i <= 2 * n / 5:
            out.append(0)
        else:
            out.append(1)
    return tuple(out)

def main():
    res = json.load(open("results.json"))
    ok = True
    print("n  T(check)  R  R(recomputed)  witness_ok  classes_ok  c0_count")
    for n in range(1, 13):
        r = res[str(n)]
        trips = triples(n)
        assert len(trips) == n * (n - 1) // 2 == r["T"], f"T mismatch at {n}"
        # independent full labeled brute force
        best = -1
        opt_orbits = []
        for col in itertools.product((0, 1, 2), repeat=n):
            c = count_rainbow(col, trips)
            if c > best:
                best = c
                opt_orbits = [col]
            elif c == best:
                opt_orbits.append(col)
        R = r["R"]
        stat = "OK" if best == R else "MISMATCH"
        if best != R:
            ok = False
        # witness attains R
        w = tuple(r["witness_c1fix"])
        w_ok = (len(w) == n and w[0] == 0 and count_rainbow(w, trips) == R)
        if not w_ok:
            ok = False
        # labeled-optimum count cross-check
        if len(opt_orbits) != r["n_opt_labeled"]:
            ok = False
            lab = f"MISMATCH({len(opt_orbits)} vs {r['n_opt_labeled']})"
        else:
            lab = "OK"
        # S3 class reps: pairwise inequivalent, and cover all optima
        reps = [tuple(x) for x in r["class_reps"]]
        seen = set()
        cover_ok = True
        for q in reps:
            key = min(s3_orbit(q))
            if key in seen:
                cover_ok = False
            seen.add(key)
        if len(seen) != r["n_classes_S3"]:
            cover_ok = False
        for col in opt_orbits:
            if min(s3_orbit(col)) not in seen:
                cover_ok = False
                break
        if not cover_ok:
            ok = False
        c0 = template_c0(n)
        c0c = count_rainbow(c0, trips)
        print(f"{n:2d}  T={r['T']:3d}  R={R:3d}  recomputed={best:3d} {stat}  "
              f"wit={'OK' if w_ok else 'FAIL'} labcnt={lab} "
              f"classes={'OK' if cover_ok else 'FAIL'}({len(seen)})  c0={c0c}")
    print("VERIFY_" + ("OK" if ok else "FAIL"))
    assert ok, "verification failed"

if __name__ == "__main__":
    main()
