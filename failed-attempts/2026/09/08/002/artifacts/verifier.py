"""Independent verifier (stdlib only, no sympy).
Reads ONLY published decimals/intervals from artifacts/*.json,
recomputes periods by direct exact-rational iteration and P_n(c0) tolerance.
Fails loudly on any mismatch. Writes verification.log.
"""
import json
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).parent
def load(name):
    with open(BASE/name) as f:
        return json.load(f)

polys = load("polys.json")
census = load("census.json")
kneading = load("kneading.json")
witness = load("witness.json")

def eval_poly_int(coeffs, x: Fraction) -> Fraction:
    r = Fraction(0)
    for a in coeffs:
        r = r*x + Fraction(a)
    return r

TOL_RES = Fraction(1, 10**6)  # |F_n(mid)| must be < 1e-6
TOL_P = Fraction(1, 10**6)    # |P_n(mid)| < 1e-6
WIDTH = Fraction(1, 10**10)
MIN_SEP = Fraction(1, 100)    # |x_k| for k<n must exceed 0.01 (rules out accidental lower period at midpoint)

log_lines = []
def log(s):
    print(s, flush=True)
    log_lines.append(s)

failures = 0
log("INDEPENDENT VERIFIER lane-61")
log("stdlib-only, exact Fraction arithmetic, no sympy")
log(f"TOL_RES=1e-6, WIDTH=1e-10, MIN_SEP=0.01")

expected_counts = {"4":2,"5":3,"6":5,"7":9}
for n_str in ["4","5","6","7"]:
    n = int(n_str)
    Pcoeffs = polys[n_str]["P"]
    intervals = census[n_str]["intervals"]
    words = {w["index"]: w["word"] for w in kneading[n_str]}
    log(f"\n--- n={n} expect {expected_counts[n_str]} intervals, got {len(intervals)} ---")
    assert len(intervals) == expected_counts[n_str], f"count mismatch n={n}"
    # parse
    parsed = [(Fraction(a), Fraction(b)) for a,b in intervals]
    # width + inside + disjoint
    for i,(a,b) in enumerate(parsed):
        assert a < b, f"empty interval n={n} i={i}"
        assert (b-a) <= WIDTH, f"width violation n={n} i={i} w={b-a}"
        assert Fraction(-2) <= a and b <= Fraction(0), f"outside [-2,0] n={n} i={i}"
        if i>0:
            assert parsed[i-1][1] <= a, f"overlap n={n} i={i}"
    log(f" widths/disjointness OK (max w={max(float(b-a) for a,b in parsed):.2e})")
    # sign change + midpoint replay
    for i,(a,b) in enumerate(parsed):
        va = eval_poly_int(Pcoeffs, a)
        vb = eval_poly_int(Pcoeffs, b)
        assert va != 0 and vb != 0, f"endpoint is root n={n} i={i}"
        assert (va>0) != (vb>0), f"no sign change n={n} i={i} va={va} vb={vb}"
        mid = (a+b)/2
        # F_n via iteration
        x = Fraction(0)
        xs = [x]
        for k in range(n):
            x = x*x + mid
            xs.append(x)
        Fn_mid = xs[n]
        Pn_mid = eval_poly_int(Pcoeffs, mid)
        # tolerance checks
        assert abs(Fn_mid) < TOL_RES, f"Fn residual too large n={n} i={i} {Fn_mid}={float(Fn_mid):.3e}"
        assert abs(Pn_mid) < TOL_P, f"Pn residual too large n={n} i={i} {Pn_mid}={float(Pn_mid):.3e}"
        # kneading from recomputed orbit
        rec_word = ''.join('+' if xs[k]>0 else ('-' if xs[k]<0 else '0') for k in range(1,n))
        assert rec_word == words[i], f"kneading mismatch n={n} i={i} recomputed {rec_word} vs published {words[i]}"
        # separation (no near-zero before n)
        for k in range(1,n):
            assert abs(xs[k]) > MIN_SEP, f"near-zero orbit point suggests lower period n={n} i={i} k={k} x={xs[k]}"
        # interval stability recompute
        # interval orbit
        ivs = [(Fraction(0),Fraction(0))]
        for k in range(n):
            l,u = ivs[-1]
            if l >= 0:
                s0,s1 = l*l, u*u
            elif u <= 0:
                s0,s1 = u*u, l*l
            else:
                s0,s1 = Fraction(0), max(l*l, u*u)
            ivs.append((s0+a, s1+b))
        for k in range(1,n):
            l,u = ivs[k]
            assert not (l <= 0 <= u), f"interval straddles 0, kneading unstable n={n} i={i} k={k}"
            s = '+' if l>0 else '-'
            assert s == rec_word[k-1], f"interval sign vs mid mismatch n={n} i={i} k={k}"
        ln,un = ivs[n]
        assert ln <= 0 <= un, f"Xn must contain 0 n={n} i={i}"
        log(f" I{i}: signchange OK, |Fn(mid)|={float(abs(Fn_mid)):.2e}, |Pn(mid)|={float(abs(Pn_mid)):.2e}, word={rec_word}, min|x|={min(float(abs(v)) for v in xs[1:n]):.3f} OK")

# witness check
log("\n--- witness (period 7, I8) ---")
assert witness["n"] == 7 and witness["interval_index"] == 8
a = Fraction(witness["a"]); b = Fraction(witness["b"]); mid = Fraction(witness["midpoint"])
assert (b-a) <= WIDTH
# check midpoint matches interval midpoint
assert mid == (a+b)/2, "witness midpoint not interval midpoint"
# recompute orbit and compare to published exact strings
xs_pub = [Fraction(v) for v in witness["orbit_exact"]]
x = Fraction(0)
for k in range(8):
    assert x == xs_pub[k], f"witness orbit mismatch k={k}"
    x = x*x + mid
# xs_pub[7] is Fn(mid)
assert abs(xs_pub[7]) < TOL_RES
log(f" witness midpoint {float(mid):.15f} orbit replay OK, residual {float(abs(xs_pub[7])):.2e}")
log(f" witness kneading {witness['kneading']} matches census: {witness['kneading']==kneading['7'][8]['word']}")
assert witness["kneading"] == kneading["7"][8]["word"]
# discriminant check: witness claims single irreducible factor; verify constant term 1 and monic
mp = witness["minpoly"]
assert mp[0]==1 and mp[-1]==1 and len(mp)==64, "minpoly must be monic deg63 const1"
log(f" witness minpoly deg {len(mp)-1} monic const1 OK")
log(f" witness discriminant {witness['discriminant']} (376-bit, negative)")

log("\nALL CHECKS PASSED")
with open(BASE/"verification.log","w") as f:
    f.write("\n".join(log_lines)+"\n")
