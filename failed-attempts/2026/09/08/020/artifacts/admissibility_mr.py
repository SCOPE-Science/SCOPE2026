"""Admissibility proof data, deterministic MR certs, neighborhood map."""
import json
from sympy import isprime

H = [0, 2, 6, 8, 30, 32, 36, 38, 42]
N0 = 685124351

# 1. Admissibility: occupied residues for p <= 9, plus nu table to 43
adm = {p: sorted({h % p for h in H}) for p in [2, 3, 5, 7]}
adm_ok = all(len(v) < p for p, v in adm.items())
nu_table = {p: len({h % p for h in H}) for p in
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]}
# competing bottom-cap extension B is inadmissible mod 7
B = [0, 2, 6, 8, 12, 30, 32, 36, 38]
b_mod7 = sorted({b % 7 for b in B})

# 2. Deterministic Miller-Rabin, bases 2,7,61 (valid for n < 2^32)
def mr_trace(n):
    assert 2 <= n < 2**32
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    per = []
    for a in (2, 7, 61):
        if a % n == 0:
            per.append({"base": a, "result": "pass-trivially (base multiple of n)"})
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            per.append({"base": a, "result": "pass"})
            continue
        r = 0
        while r < s - 1:
            x = (x * x) % n
            r += 1
            if x == n - 1:
                break
        per.append({"base": a, "result": "pass" if x == n - 1 else "COMPOSITE"})
    return {"n": n, "odd_part_d": d, "power_s": s, "bases": per,
            "pass": all(b["result"] != "COMPOSITE" for b in per)}

vals = [N0 + h for h in H]
mr_logs = [mr_trace(v) for v in vals]
sympy_check = [bool(isprime(v)) for v in vals]

# 3. Neighborhood consecutiveness map on [N0-50, N0+82]
lo, hi = N0 - 50, N0 + 82
primes_in = [t for t in range(lo, hi + 1) if isprime(t)]
i = primes_in.index(N0)
lower_run = primes_in[i:i+4]
upper_run = primes_in[i+4:i+9]
prev_prime = primes_in[i-1] if i > 0 else None
next_prime = primes_in[i+9] if i+9 < len(primes_in) else None

out = {
    "H": H, "N0": N0,
    "admissibility_residues": {str(p): v for p, v in adm.items()},
    "admissible": bool(adm_ok),
    "nu_table_to_43": {str(p): v for p, v in nu_table.items()},
    "bottom_cap_B_mod7": b_mod7,
    "bottom_cap_inadmissible_mod7": len(b_mod7) == 7,
    "upper_cluster_minus_30": [h - 30 for h in H[4:]],
    "mr_logs": mr_logs,
    "all_mr_pass": all(l["pass"] for l in mr_logs),
    "sympy_crosscheck": sympy_check,
    "all_sympy_prime": all(sympy_check),
    "neighborhood": {"lo": lo, "hi": hi, "primes": primes_in,
                     "prev_prime": prev_prime, "lower_run": lower_run,
                     "upper_run": upper_run, "next_prime": next_prime},
    "lower_run_is_consecutive_quadruplet": lower_run == vals[:4] and primes_in[i+4] == vals[4],
    "upper_run_is_consecutive_quintuplet": upper_run == vals[4:] and (next_prime is None or next_prime > vals[-1]),
}
with open("output/artifacts/admissibility_mr.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "mr_logs"}, indent=1))
print("MR pass:", out["all_mr_pass"], "| sympy:", out["all_sympy_prime"])
print("lower consecutive:", out["lower_run_is_consecutive_quadruplet"],
      "| upper consecutive:", out["upper_run_is_consecutive_quintuplet"])
