"""ECH-capacity census for E(1,a) -> P(1,beta), Frenkel-Mueller window.
Stdlib only, exact Fraction arithmetic. Replays Hutchings' lattice formulas:
  c_k(E(1,a)) = (k+1)-st smallest value of m + a*n over (m,n) in N^2 (Prop 1.2).
  c_k(P(1,b)) = min{ m + b*n : (m+1)(n+1) >= k+1 } (Thm 1.4).
  c_k(B(a))   = d*a with (d^2+d)/2 <= k <= (d^2+3d)/2 (Cor 1.3).
Cross-checks ellipsoid capacities against the McDuff weight-ball packing
union formula (Prop 1.5). All comparisons volume-vs-ECH done on squares,
exactly, in Q.
"""
import json
from fractions import Fraction as F

def weight_seq(p, q):
    """McDuff weight expansion of p/q >= 1 (greedy Euclidean), list of F."""
    w = []
    x0, x1 = p, q
    while x1 > 0:
        m = x0 // x1
        for _ in range(m):
            w.append(F(x1, q))
        x0, x1 = x1, x0 - m * x1
    return w

def ellipsoid_caps(an, ad, K):
    N = K + 2
    v = []
    for m in range(N + 1):
        for n in range(N + 1):
            v.append(F(m, 1) + F(an * n, ad))
    v.sort()
    return v[:K + 1]

def ellipsoid_witness(an, ad, k, cap):
    N = k + 2
    cands = []
    for m in range(N + 1):
        for n in range(N + 1):
            if F(m, 1) + F(an * n, ad) == cap:
                cands.append((m, n))
    return sorted(cands)[0]

def polydisk_caps(bn, bd, K):
    caps, wits = [], []
    for k in range(K + 1):
        best, bw = None, None
        for m in range(k + 2):
            for n in range(k + 2):
                if (m + 1) * (n + 1) >= k + 1:
                    val = F(m, 1) + F(bn * n, bd)
                    if best is None or val < best:
                        best, bw = val, (m, n)
        caps.append(best)
        wits.append(bw)
    return caps, wits

def ball_cap(a, k):
    d = 0
    while not (F(d * d + d, 2) <= k <= F(d * d + 3 * d, 2)):
        d += 1
    return a * d, d

def packing_crosscheck(weights, k):
    """max over k_1+...+k_n=k of sum c_{k_i}(B(w_i)); returns (val, dist)."""
    n = len(weights)
    singles = [[ball_cap(w, t)[0] for t in range(k + 1)] for w in weights]
    # DP over balls
    dp = {0: (F(0), [])}
    for i in range(n):
        ndp = {}
        for s, (val, dist) in dp.items():
            for t in range(k - s + 1):
                ns = s + t
                nv = val + singles[i][t]
                if ns not in ndp or nv > ndp[ns][0]:
                    ndp[ns] = (nv, dist + [t])
        dp = ndp
    return dp[k]

def convergents_cf():
    # 3+2*sqrt(2): CF [5;1,4,1,4,...]; generate convergents p_j/q_j
    import math
    x = 3 + 2 * math.sqrt(2)
    terms = []
    for _ in range(12):
        a = math.floor(x + 1e-12)
        terms.append(a)
        f = x - a
        if f < 1e-12:
            break
        x = 1 / f
    convs = []
    pm2, pm1, qm2, qm1 = 0, 1, 1, 0
    for a in terms:
        p, q = a * pm1 + pm2, a * qm1 + qm2
        convs.append((p, q))
        pm2, pm1, qm2, qm1 = pm1, p, qm1, q
    return terms, convs

def main():
    K = 80
    terms, convs = convergents_cf()
    # survey: convergents with small denominators + near neighbours + integers 5..8
    aset = {(5, 1), (6, 1), (7, 1), (8, 1), (11, 2), (19, 3), (45, 8),
            (17, 3), (29, 5), (41, 7), (99, 17), (169, 29)}
    for p, q in convs:
        if q <= 30:
            aset.add((p, q))
    alist = sorted(aset, key=lambda t: t[0] / t[1])
    betas = [(1, 1), (6, 5), (5, 4)]
    table = []
    for an, ad in alist:
        a = F(an, ad)
        E = ellipsoid_caps(an, ad, K)
        w = weight_seq(an, ad)
        assert sum(x * x for x in w) == a, (an, ad)
        for bn, bd in betas:
            b = F(bn, bd)
            P, PW = polydisk_caps(bn, bd, K)
            vol2 = a / (2 * b)  # lambda_vol^2
            best, bk = F(0), None
            beyond = []
            for k in range(1, K + 1):
                r = E[k] / P[k]
                if r > best:
                    best, bk = r, k
                if r * r > vol2:
                    beyond.append(k)
            ew = ellipsoid_witness(an, ad, bk, E[bk])
            row = {
                "a": [an, ad], "beta": [bn, bd],
                "Kmax": K,
                "weight_seq": [str(x) for x in w],
                "vol_sq": str(vol2),
                "inclusion_threshold": str(max(F(1), a / b)),
                "best_k": bk, "best_ratio": str(best),
                "best_E": str(E[bk]), "best_E_wit": list(ew),
                "best_P": str(P[bk]), "best_P_wit": list(PW[bk]),
                "beyond_vol_ks": beyond,
                "decided": "ECH-decided" if beyond else "volume-only",
            }
            table.append(row)
    # focused witness certificates with packing cross-check
    certs = []
    for (an, ad), (bn, bd), k in [((5, 1), (1, 1), 5), ((6, 1), (1, 1), 8),
                                 ((5, 1), (6, 5), 5), ((11, 2), (1, 1), 5)]:
        E = ellipsoid_caps(an, ad, k)
        P, PW = polydisk_caps(bn, bd, k)
        w = weight_seq(an, ad)
        pk, dist = packing_crosscheck(w, k)
        certs.append({
            "a": [an, ad], "beta": [bn, bd], "k": k,
            "E_k": str(E[k]), "E_wit": list(ellipsoid_witness(an, ad, k, E[k])),
            "P_k": str(P[k]), "P_wit": list(PW[k]),
            "ratio": str(E[k] / P[k]),
            "vol_sq": str(F(an * bd, ad * 2 * bn)),
            "ratio_sq_gt_vol_sq": bool((E[k] / P[k]) ** 2 > F(an * bd, ad * 2 * bn)),
            "packing_check": str(pk), "packing_dist": dist,
            "packing_agrees": bool(pk == E[k]),
        })
    out = {"CF_terms": terms, "CF_convergents": convs,
           "census": table, "certificates": certs}
    with open("census.json", "w") as f:
        json.dump(out, f, indent=1)
    for c in certs:
        print(c)
    print("rows:", len(table))

if __name__ == "__main__":
    main()
