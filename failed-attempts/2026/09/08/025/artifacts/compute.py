#!/usr/bin/env python3
"""Lane 62: certified regulator + class-number core for squarefree d<=200.
Stdlib only. Writes table.csv, table_full.json, ideals.json, principals.json,
Lbounds.json, extremal.json and prints a run log.

CONVENTIONS.
  O' = Z[sqrt(d)] (order), O = maximal order (O=O' unless d=1 mod 4, when
  O=Z[(1+sqrt(d))/2]).
  x0,y0,norm: minimal solution of x^2-d*y^2=+-1 (CF convergent, exact).
  eps = x0+y0*sqrt(d) (fundamental unit of O').
  R_conv = log(eps).
  regulator (CSV column, topic convention): log of minimal +1 unit of O',
      i.e. R_conv if norm=+1 else 2*R_conv (the square).
  EPS = fundamental unit of O; R_field = log(EPS) (standard regulator).
      [O:O']=1 or 2; unit index m=[O^x:O'^x] is 1 unless d=1 mod 4, and then
      m|3 (injection O^x/O'^x -> (O/2O)^x/(O'/2O)^x; split case trivial,
      inert case order 3). So EPS=eps or a cube root of eps (d=5 mod 8 only);
      cube-root candidacy from floats, decided by EXACT verification.
  The class-number formula h*R_field = sqrt(D)/2*L(1,chi) then pins h.

Theory (proofs sketched in DRAFT.md):
  P1 CF period via exact integer arithmetic; N(p_{l-1},q_{l-1})=(-1)^l.
  P2 norm -1 unit in O exists iff l odd (period parity + index argument).
  P3 rho-cycles of reduced forms of D count narrow classes h+ (exact ints;
      primitivity asserted per form).
  P4 class-number formula with rigorous tail |R_N|<=D/N+1/(M0+1)+1e-9 (float).
  P5 Minkowski M=sqrt(D)/2 (never an integer here) + prime witnesses => h=1.
"""
import math, json, csv
from decimal import Decimal, getcontext

getcontext().prec = 80

def is_squarefree(n):
    m = n
    p = 2
    while p * p <= m:
        if m % (p * p) == 0:
            return False
        while m % p == 0:
            m //= p
        p += 1 if p == 2 else 2
    return True

def primes_below(x):
    n = max(3, int(math.ceil(x)) + 1)
    sieve = bytearray(b"\x01") * n
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = b"\x00" * len(range(i*i, n, i))
    return [i for i in range(n) if sieve[i] and i < x]

def is_square(n):
    if n < 0:
        return None
    r = math.isqrt(n)
    return r if r * r == n else None

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def kronecker(a, n):
    if n == 0:
        return 1 if abs(a) == 1 else 0
    if n == 1:
        return 1
    if n == -1:
        return 1 if a >= 0 else -1
    if n < 0:
        return kronecker(a, -1) * kronecker(a, -n)
    if math.gcd(a, n) != 1:
        return 0
    res = 1
    m = n
    e = 0
    while m % 2 == 0:
        m //= 2
        e += 1
    if e:
        res *= (1 if (a % 8) in (1, 7) else -1) ** e
    p = 3
    while p * p <= m:
        if m % p == 0:
            cnt = 0
            while m % p == 0:
                m //= p
                cnt += 1
            if cnt % 2 == 1:
                res *= legendre(a, p)
        p += 2
    if m > 1:
        res *= legendre(a, m)
    return res

# ---------- CF period, two code paths ----------
def cf_period_A(d):
    """Stop when a == 2*a0 (standard theorem)."""
    a0 = math.isqrt(d)
    assert a0 * a0 != d
    m, den, a = 0, 1, a0
    part = [a0]
    while True:
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den
        part.append(a)
        if a == 2 * a0:
            break
    return len(part) - 1, part

def cf_period_B(d):
    """Independent stopping rule: first t>=1 with a_t = 2*a0 AND
    N(p_{t-1},q_{t-1}) = (-1)^t, convergents built incrementally."""
    a0 = math.isqrt(d)
    m, den, a = 0, 1, a0
    p_mm, p_m = 0, 1
    q_mm, q_m = 1, 0
    part = [a0]
    p_mm, p_m = p_m, a0 * p_m + p_mm
    q_mm, q_m = q_m, a0 * q_m + q_mm
    for t in range(1, 10000):
        m = den * a - m
        den = (d - m * m) // den
        a = (a0 + m) // den
        part.append(a)
        if a == 2 * a0 and p_m * p_m - d * q_m * q_m == (1 if t % 2 == 0 else -1):
            return t, part[:t + 1]
        p_mm, p_m = p_m, a * p_m + p_mm
        q_mm, q_m = q_m, a * q_m + q_mm
    raise AssertionError("period not found")

def check_minimal(ext, l):
    assert len(ext) >= 2 * l + 1
    for i in range(1, l + 1):
        assert ext[i] == ext[i + l], "period block must repeat"
    for k in range(1, l):
        if l % k == 0 and all(ext[1+i] == ext[1+i+k] for i in range(l - k)):
            raise AssertionError("non-minimal period")

def convergent(cyc, l):
    p_mm, p_m = 0, 1
    q_mm, q_m = 1, 0
    for i in range(l):
        a = cyc[i]
        p_mm, p_m = p_m, a * p_m + p_mm
        q_mm, q_m = q_m, a * q_m + q_mm
    return p_m, q_m

# ---------- maximal-order fundamental unit ----------
def cube_root_unit(d, x0, y0):
    """If eps=x0+y0*sqrt(d) is a cube in O, return (U,V) with
    ((U+V*sqrt(d))/2)^3 = eps, U=V mod 2. Else None. Decided exactly."""
    ef = float(x0) + float(y0) * math.sqrt(d)
    ec = float(x0) - float(y0) * math.sqrt(d)
    sp = ef ** (1.0 / 3.0)
    sm = -((-ec) ** (1.0 / 3.0)) if ec < 0 else ec ** (1.0 / 3.0)
    U0 = int(math.floor(sp + sm))  # 2u approx
    V0 = int(math.floor((sp - sm) / math.sqrt(d)))  # 2v approx
    for U in range(U0 - 1, U0 + 2):
        for V in range(V0 - 1, V0 + 2):
            if (U - V) % 2 != 0:
                continue
            # ((U+V√d)/2)^3 =?= x0+y0√d  <=>  (U+V√d)^3 =?= 8x0+8y0√d
            A = U*U*U + 3*U*V*V*d
            B = 3*U*U*V + V*V*V*d
            if A == 8*x0 and B == 8*y0:
                return (U, V)
    return None

# ---------- reduced indefinite forms -> narrow class number (exact) ----------
def reduced_forms(D):
    sq = math.sqrt(D)
    forms = []
    b = D & 1
    if b == 0:
        b = 2
    while b * b < D:
        Kmax = int((sq + b) / 2) + 2
        for k in range(1, Kmax + 1):
            if not (D < (2*k + b) * (2*k + b)):
                continue
            if not ((2*k - b < 0) or ((2*k - b) * (2*k - b) < D)):
                continue
            for a in (k, -k):
                num = b * b - D
                if num % (4 * a) == 0:
                    c = num // (4 * a)
                    assert b*b - 4*a*c == D and b >= 0 and b*b < D
                    u = 2*abs(a)
                    assert (u - b <= 0 or (u-b)*(u-b) < D) and D < (u+b)*(u+b)
                    assert math.gcd(math.gcd(abs(a), abs(b)), abs(c)) == 1, \
                        "imprimitive reduced form"
                    forms.append((a, b, c))
        b += 2
    return forms

def rho_step(D, a, b, c):
    """Exact rho: unique b1 with |sqrt(D)-2|c|| < b1 < sqrt(D), b1=-b+2ck."""
    assert c != 0
    mod = 2 * c
    K = (b + math.isqrt(D) + 3) // abs(mod) + 3
    cands = []
    for k in range(-K, K + 1):
        b1 = -b + mod * k
        if b1 <= 0 or b1 * b1 >= D:
            continue
        u = 2 * abs(c)
        if (u - b1 <= 0 or (u-b1)*(u-b1) < D) and D < (u+b1)*(u+b1):
            num = b1 * b1 - D
            if num % (4 * c) == 0:
                cands.append((c, b1, num // (4 * c)))
    assert len(cands) == 1, (D, (a, b, c), cands)
    return cands[0]

def narrow_class_number(D):
    forms = reduced_forms(D)
    assert forms, "no reduced forms"
    visited = {}
    ncyc = 0
    cyclens = []
    for f in forms:
        if f in visited:
            continue
        cur = f
        walk = []
        while cur not in visited:
            visited[cur] = ncyc
            walk.append(cur)
            cur = rho_step(D, *cur)
        assert visited[cur] == ncyc, "rho orbit merged into older cycle"
        assert walk.index(cur) == 0, "rho tail inside reduced set"
        cyclens.append(len(walk))
        ncyc += 1
    for f in forms:  # closure replay: every form lies on a closed cycle
        cur = f
        for _ in range(len(forms) + 1):
            cur = rho_step(D, *cur)
            if cur == f:
                break
        assert cur == f
    return ncyc, sorted(cyclens)

# ---------- analytic L(1,chi) with rigorous tail ----------
def L_interval(D, N):
    tbl = [kronecker(D, r) for r in range(D)]
    assert sum(tbl) == 0, "character mean must vanish"
    s = 0.0
    for n in range(1, N + 1):
        s += tbl[n % D] / n
    M0 = N // D
    E = D / N + 1.0 / (M0 + 1) + 1e-9  # block tail + float allowance
    return s - E, s + E, s, E

# ---------- generator search for norms +-p (in O) ----------
def find_witness(d, D, p, B):
    if D == 4 * d:
        for bb in range(B + 1):
            dd = d * bb * bb
            for sgn in (1, -1):
                r = is_square(dd + sgn * p)
                if r is not None:
                    for aa in ({r, -r} if r else {0}):
                        if aa * aa - d * bb * bb == sgn * p:
                            return {"a": aa, "b": bb, "den": 1, "norm": sgn * p}
        return None
    for vv in range(B + 1):
        dd = d * vv * vv
        for sgn in (1, -1):
            r = is_square(dd + sgn * 4 * p)
            if r is not None:
                for uu in ({r, -r} if r else {0}):
                    if (uu - vv) % 2 == 0 and (uu * uu - d * vv * vv) == sgn * 4 * p:
                        return {"a": uu, "b": vv, "den": 2, "norm": sgn * p}
    return None

def main():
    ds = [d for d in range(2, 201) if is_squarefree(d)]
    assert len(ds) == 121, len(ds)
    rows, ideals, princ, Lbounds = [], {}, {}, {}
    h1_no_wit = []
    for d in ds:
        lA, pA = cf_period_A(d)
        lB, pB = cf_period_B(d)
        assert (lA, pA) == (lB, pB)
        l = lA
        a0 = pA[0]
        m, den, a = 0, 1, a0
        ext = [a0]
        for _ in range(2 * l):
            m = den * a - m
            den = (d - m * m) // den
            a = (a0 + m) // den
            ext.append(a)
        check_minimal(ext, l)
        x0, y0 = convergent(pA, l)
        norm = x0 * x0 - d * y0 * y0
        assert norm == (1 if l % 2 == 0 else -1)
        assert x0 + y0 * math.sqrt(d) > 1
        sqd = Decimal(d).sqrt()
        R_conv = (Decimal(x0) + Decimal(y0) * sqd).ln()
        assert abs(float(R_conv) - math.log(x0 + y0 * math.sqrt(d))) < 1e-9
        R_topic = R_conv if norm == 1 else 2 * R_conv
        # maximal-order fundamental unit
        if d % 4 == 1:
            rt = cube_root_unit(d, x0, y0)
            if d % 8 == 1:
                assert rt is None, (d, "cube root exists but 2 splits: theory violated")
                m_idx, sig = 1, None
            else:
                m_idx, sig = (3, rt) if rt is not None else (1, None)
        else:
            m_idx, sig = 1, None
        if m_idx == 3:
            U, V = sig
            R_field = R_conv / 3
        else:
            R_field = R_conv
        D = d if d % 4 == 1 else 4 * d
        M = math.sqrt(D) / 2.0
        ps = primes_below(M)
        ps2 = [n for n in range(2, int(math.ceil(M))) if n < M and
               all(n % t for t in range(2, int(n ** 0.5) + 1))]
        assert ps == ps2, (d, "prime census incomplete")
        split = {}
        for pp in ps:
            k = kronecker(D, pp)
            assert k in (-1, 0, 1)
            if D % pp == 0:
                assert k == 0
                typ = "ramified"
            elif k == 1:
                typ = "split"
            else:
                typ = "inert"
            split[str(pp)] = {"kronecker": k, "type": typ}
        ideals[str(d)] = {"D": D, "M": M, "primes": split}
        hplus, clens = narrow_class_number(D)
        # exact h: parity rule + rigorous analytic pinning/cross-check
        N = 100000
        while True:
            lo, hi, mid, E = L_interval(D, N)
            assert lo > 0, (d, N)
            sqD = float(Decimal(D).sqrt())
            Rf = float(R_field)
            hlo = sqD * lo / (2 * Rf)
            hhi = sqD * hi / (2 * Rf)
            delta = (hhi - hlo) / 2
            if l % 2 == 1:
                h = hplus
                assert hlo <= h <= hhi, (d, hlo, hhi, N)
                method = "odd-period: h=h+; analytic cross-check N=%d" % N
                break
            else:
                assert hplus % 2 == 0, (d, hplus)
                h = hplus // 2
                if delta < 0.5 and hlo <= h <= hhi and not (
                        hplus != h and hlo <= hplus <= hhi):
                    method = "even-period: h=h+/2 pinned by analytic interval N=%d" % N
                    break
                N *= 4
                assert N <= 1600000, (d, hlo, hhi)
                continue
        Lbounds[str(d)] = {"N": N, "Lmid": mid, "E": E, "hlo": hlo, "hhi": hhi,
                           "hplus": hplus, "h": h, "m_index": m_idx}
        inv = ("C1" if h == 1 else "C%d" % h) if h <= 3 else "unresolved"
        if h == 1:
            wit = {}
            for pp in ps:
                if split[str(pp)]["type"] == "inert":
                    continue
                w = find_witness(d, D, pp, 2000)
                if w is None:
                    w = find_witness(d, D, pp, 200000)
                if w is None:
                    h1_no_wit.append((d, pp))
                else:
                    wit[str(pp)] = w
            princ[str(d)] = wit
        rows.append({"d": d, "D": D, "period": l, "R_conv": R_conv,
                     "R_topic": R_topic, "R_field": R_field, "m_idx": m_idx,
                     "sig": sig, "x0": x0, "y0": y0, "norm": norm,
                     "M": M, "h": h, "hplus": hplus, "inv": inv,
                     "method": method, "cycles": clens})
    assert not h1_no_wit, h1_no_wit
    with open("output/artifacts/table.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["d", "D", "period", "regulator", "x0", "y0",
                                          "norm", "M", "h", "invariants"])
        w.writeheader()
        for r in rows:
            w.writerow({"d": r["d"], "D": r["D"], "period": r["period"],
                        "regulator": "%.10f" % r["R_topic"], "x0": str(r["x0"]),
                        "y0": str(r["y0"]), "norm": r["norm"], "M": "%.10f" % r["M"],
                        "h": r["h"], "invariants": r["inv"]})
    full = {}
    for r in rows:
        e = {"D": r["D"], "period": r["period"],
             "R_conv": str(r["R_conv"]), "regulator": str(r["R_topic"]),
             "R_field": str(r["R_field"]), "m_index": r["m_idx"],
             "Rlo": str(r["R_topic"] - Decimal("1e-10")),
             "Rhi": str(r["R_topic"] + Decimal("1e-10")),
             "x0": str(r["x0"]), "y0": str(r["y0"]), "norm": r["norm"], "M": r["M"],
             "h": r["h"], "hplus": r["hplus"], "invariants": r["inv"],
             "method": r["method"], "cycle_lengths": r["cycles"]}
        if r["sig"] is not None:
            e["sigma"] = {"U": r["sig"][0], "V": r["sig"][1]}
        full[str(r["d"])] = e
    json.dump(full, open("output/artifacts/table_full.json", "w"), indent=1)
    json.dump(ideals, open("output/artifacts/ideals.json", "w"), indent=1)
    json.dump(princ, open("output/artifacts/principals.json", "w"), indent=1)
    json.dump(Lbounds, open("output/artifacts/Lbounds.json", "w"), indent=1)
    maxp = max(r["period"] for r in rows)
    maxRf = max(rows, key=lambda r: r["R_field"])
    sRf = sorted(rows, key=lambda r: r["R_field"])
    maxRt = max(rows, key=lambda r: r["R_topic"])
    maxh = max(r["h"] for r in rows)
    dist = {}
    for r in rows:
        dist[str(r["h"])] = dist.get(str(r["h"]), 0) + 1
    h1list = [r["d"] for r in rows if r["h"] == 1]
    m3 = sorted(r["d"] for r in rows if r["m_idx"] == 3)
    ext = {
        "n_fields": len(rows),
        "max_period": {"value": maxp,
                       "fields": sorted(r["d"] for r in rows if r["period"] == maxp)},
        "max_field_regulator": {"value": str(maxRf["R_field"]), "field": maxRf["d"],
                                "runner_up": {"field": sRf[-2]["d"],
                                              "value": str(sRf[-2]["R_field"])}},
        "max_topic_regulator": {"value": str(maxRt["R_topic"]), "field": maxRt["d"]},
        "index_3_fields": m3,
        "max_class_number": {"value": maxh,
                             "fields": sorted(r["d"] for r in rows if r["h"] == maxh),
                             "status": "orders certified by rho-cycle count + parity rule + "
                                       "rigorous analytic interval; full invariant-factor "
                                       "relation log QUARANTINED (ideal-multiplication Smith "
                                       "replay not completed in this pass)"},
        "h_distribution": dist,
        "h1_count": len(h1list),
        "h1_fields": h1list,
        "unresolved_invariants": sorted(r["d"] for r in rows if r["inv"] == "unresolved"),
    }
    json.dump(ext, open("output/artifacts/extremal.json", "w"), indent=1)
    print("fields:", len(rows))
    print("max period:", ext["max_period"])
    print("max R_field: d=%d R=%s" % (maxRf["d"], str(maxRf["R_field"])[:14]))
    print("max R_topic: d=%d R=%s" % (maxRt["d"], str(maxRt["R_topic"])[:14]))
    print("index-3 fields:", m3)
    print("max h:", maxh, sorted(r["d"] for r in rows if r["h"] == maxh))
    print("h dist:", dist)
    print("h=1 count:", len(h1list))
    print("unresolved invariants:", len(ext["unresolved_invariants"]))

if __name__ == "__main__":
    main()
