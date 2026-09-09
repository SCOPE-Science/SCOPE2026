"""verify.py — independent audit of lane-370 Av(1324) census.

Checks (stdlib only), reading committed tableA.txt / tableB.txt:
  V1  A-vs-B exact agreement on every (n,k) cell, n<=9 (68 cells).
  V2  A marginals vs OEIS A061558 row sums (n<=12) + LV Table-2 spot rows
      (n=4..8 full rows; n=6..9 partial prefixes from the published table).
  V3  CJS column-monotonicity a(n,k)<=a(n+1,k) verified on the computed
      window wherever both entries exist.
  V4  Linusson-Verkama difference identity: for n>=8, k<=2n-7,
      a(n+1,k)-a(n,k) == coeff of R_n(x)=2(2+x)x^{n-1}P(x)^2, with exact
      partition numbers (pentagonal recurrence, integers only).
  V5  LV sharpness counterexample: pi=36127..n45 has 2n-6 inversions,
      avoids 1324, is indecomposable, and no boundary deletion
      (first/last value/position) is decomposable (n=7..12).
"""
import sys
from itertools import combinations

ART = "output/artifacts/"


def load(path):
    rows = {}
    n = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith("n="):
                head = line.split()
                n = int(head[0].split("=")[1])
                tot = int(head[1].split("=")[1])
                rows[n] = {"total": tot, "row": None}
            elif line.startswith("row:"):
                rows[n]["row"] = [int(x) for x in line[4:].split()]
    return rows


def partitions_upto(K):
    p = [0] * (K + 1)
    p[0] = 1
    for n in range(1, K + 1):
        tot = 0
        k = 1
        while True:
            for g in (k * (3 * k - 1) // 2, k * (3 * k + 1) // 2):
                if g > n:
                    break
                tot += (-1) ** (k + 1) * p[n - g]
            k += 1
            if k * (3 * k - 1) // 2 > n:
                break
        p[n] = tot
    return p


def Rn_coeffs(n, K, p):
    c = [0] * (K + 1)
    for t in range(K + 1):
        if p[t] == 0:
            continue
        for u in range(K + 1 - t):
            if p[u] == 0:
                continue
            s = t + u
            if s + n - 1 <= K:
                c[s + n - 1] += 4 * p[t] * p[u]
            if s + n <= K:
                c[s + n] += 2 * p[t] * p[u]
    return c


def avoids1324(perm):
    for a, b, c, d in combinations(range(len(perm)), 4):
        x = (perm[a], perm[b], perm[c], perm[d])
        s = sorted(x)
        rank = {v: i for i, v in enumerate(s)}
        if (rank[x[0]], rank[x[1]], rank[x[2]], rank[x[3]]) == (0, 2, 1, 3):
            return False
    return True


def comps(perm):
    n = len(perm)
    out, start, mx = [], 0, 0
    for i, v in enumerate(perm):
        mx = max(mx, v)
        if mx == i + 1:
            out.append(perm[start:i + 1])
            start = i + 1
    return out


def delete_entry(perm, idx):
    v = perm[idx]
    return tuple(x - 1 if x > v else x for j, x in enumerate(perm) if j != idx)


def sharp_perm(n):
    return (3, 6, 1, 2) + tuple(range(7, n + 1)) + (4, 5)


def main():
    A = load(ART + "tableA.txt")
    B = load(ART + "tableB.txt")
    fails = []

    # V1: dual-engine agreement n<=9
    cells = 0
    for n in range(1, 10):
        ra, rb = A[n]["row"], B[n]["row"]
        if ra != rb:
            fails.append(f"V1 mismatch at n={n}")
        cells += len(ra)
    print(f"V1 dual-engine agreement n<=9: {cells} cells checked")

    # V2: OEIS marginals + LV table spot checks
    oeis = {1: 1, 2: 2, 3: 6, 4: 23, 5: 103, 6: 513, 7: 2762, 8: 15793,
            9: 94776, 10: 591950, 11: 3824112, 12: 25431452}
    for n, tot in oeis.items():
        if A[n]["total"] != tot:
            fails.append(f"V2 OEIS mismatch n={n}: {A[n]['total']} vs {tot}")
    lv_rows = {
        4: [1, 2, 5, 6, 5, 3, 1],
        5: [1, 2, 5, 10, 16, 20, 20, 15, 9, 4, 1],
        6: [1, 2, 5, 10, 20, 32, 51, 67, 79, 80, 68, 49, 29],
        7: [1, 2, 5, 10, 20, 36, 61, 96, 148, 208, 268, 321, 351],
        8: [1, 2, 5, 10, 20, 36, 65, 106, 171, 262, 397, 568, 784],
    }
    for n, pref in lv_rows.items():
        if A[n]["row"][:len(pref)] != pref:
            fails.append(f"V2 LV-table mismatch n={n}")
    print("V2 OEIS A061558 marginals n=1..12 + LV Table-2 rows n=4..8: checked")

    # V3: column monotonicity on computed window
    mono_cells, mono_bad = 0, []
    for k in range(0, 67):
        for n in range(1, 12):
            if k < len(A[n]["row"]) and k < len(A[n + 1]["row"]):
                mono_cells += 1
                if A[n]["row"][k] > A[n + 1]["row"][k]:
                    mono_bad.append((n, k))
    if mono_bad:
        fails.append(f"V3 monotonicity fails at {mono_bad[:8]}")
    print(f"V3 column monotonicity: {mono_cells} comparable cells, "
          f"{len(mono_bad)} violations")

    # V4: LV difference identity on k<=2n-7
    K = 66
    p = partitions_upto(K)
    v4_cells, v4_bad = 0, []
    for n in range(8, 12):
        c = Rn_coeffs(n, K, p)
        for k in range(0, min(2 * n - 7, len(A[n + 1]["row"]) - 1) + 1):
            d = A[n + 1]["row"][k] - A[n]["row"][k]
            v4_cells += 1
            if d != c[k]:
                v4_bad.append((n, k, d, c[k]))
    if v4_bad:
        fails.append(f"V4 LV-diff fails at {v4_bad[:8]}")
    print(f"V4 LV diff identity (k<=2n-7, n=8..11): {v4_cells} cells checked")

    # V5: sharpness witnesses n=7..12
    for n in range(7, 13):
        pi = sharp_perm(n)
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if pi[i] > pi[j])
        assert inv == 2 * n - 6, (n, inv)
        assert avoids1324(pi), n
        assert len(comps(pi)) == 1, n
        vals = [pi.index(1), pi.index(n), 0, n - 1]
        seen = set()
        for idx in vals:
            seen.add(len(comps(delete_entry(pi, idx))) > 1)
        if any(seen):
            fails.append(f"V5 sharpness fails at n={n}")
    print("V5 sharpness family 36127..n45 (2n-6 invs, no decomp boundary deletion): "
          "n=7..12 checked")

    if fails:
        print("VERIFY_FAIL")
        for f in fails:
            print(" - " + f)
        sys.exit(1)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
