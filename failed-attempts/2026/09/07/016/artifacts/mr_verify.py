#!/usr/bin/env python3
"""Deterministic Miller-Rabin (7-base, <2^64) + sympy cross-check for all survivors."""
import json, time, sys

MR_BASES = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

def is_prime_mr(n):
    if n < 2: return False
    small = [2,3,5,7,11,13,17,19,23,29,31,37]
    for p in small:
        if n % p == 0:
            return n == p
    d = n-1; s = 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in MR_BASES:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = (x*x) % n
            if x == n-1:
                break
        else:
            return False
    return True

def mr_transcript(n):
    """Return per-base transcript: list of {base, x0, pass}."""
    if n < 2:
        return {"n": n, "prime": False, "reason": "n<2"}
    small = [2,3,5,7,11,13,17,19,23,29,31,37]
    for p in small:
        if n % p == 0:
            return {"n": n, "prime": (n==p), "reason": f"trial p={p}"}
    d = n-1; s = 0
    while d % 2 == 0:
        d //= 2; s += 1
    recs = []
    prime = True
    for a in MR_BASES:
        if a % n == 0:
            recs.append({"base": a, "result": "base_multiple_of_n_skip"})
            continue
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            recs.append({"base": a, "x0": x, "result": "pass_first"})
            continue
        y = x
        passed = False
        seq = [x]
        for _ in range(s-1):
            y = (y*y) % n
            seq.append(y)
            if y == n-1:
                passed = True
                break
        if passed:
            recs.append({"base": a, "seq": seq, "result": "pass_later"})
        else:
            recs.append({"base": a, "seq": seq, "result": "FAIL_composite"})
            prime = False
    return {"n": n, "d": d, "s": s, "prime": prime, "bases": recs}

def main():
    cin = sys.argv[1] if len(sys.argv)>1 else "output/artifacts/census.json"
    cout = sys.argv[2] if len(sys.argv)>2 else "output/artifacts/mr_transcripts.json"
    with open(cin) as f:
        data = json.load(f)
    offs = [0,4,6,10,12,16]
    t0 = time.time()
    out = {"bases": MR_BASES, "results": []}
    ncheck = 0
    try:
        import sympy
        has_sympy = True
        symver = sympy.__version__
    except Exception as e:
        has_sympy = False
        symver = f"unavailable: {e}"
    out["sympy_version"] = symver
    allpass = True
    for p in data["list"]:
        for o in offs:
            q = p+o
            tr = mr_transcript(q)
            try:
                import sympy
                sp = bool(sympy.isprime(q))
            except Exception:
                sp = None
            if not tr["prime"]:
                allpass = False
            if sp is not None and sp != tr["prime"]:
                allpass = False
                print(f"MISMATCH q={q} mr={tr['prime']} sympy={sp}")
            out["results"].append({"q": q, "p_base": p, "offset": o,
                                   "mr_prime": tr["prime"], "sympy_prime": sp,
                                   "transcript": tr})
            ncheck += 1
    dt = time.time()-t0
    out["n_checked"] = ncheck
    out["all_prime"] = allpass
    out["elapsed_s"] = dt
    with open(cout, "w") as f:
        json.dump(out, f)
    print(f"checked {ncheck} numbers, all_prime={allpass}, sympy={symver}, time={dt:.2f}s")

if __name__ == "__main__":
    main()
