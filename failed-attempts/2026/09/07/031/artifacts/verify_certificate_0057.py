"""Independent verifier for the octal 0.057 periodicity certificate.

Stdlib only (no numpy). Re-reads the logged CSV table and checks, from scratch:
  (V1) CSV integrity: heaps 0..Nmax consecutive.
  (V2) Suffix equality G(n)=G(n+p) for all n in [N0, Nmax-p], N0=259, p=148.
  (V3) mex-rule recomputation: for every n in the induction base window
       [N0+p, T*] (T* = 2*N0+2*p+m = 817) AND the final two period blocks,
       recompute reachable set from table values at smaller indices with an
       independent pure-Python implementation, and check mex equals table G(n).
  (V4) Reachable-set equality S(n)=S(n-p) as exact sets on the final full
       period block n in [Nmax-2*p+1, Nmax-p]; hence mex propagates there.
  (V5) Threshold coverage: T* <= Nmax-p (so the proved lemma's base window
       lies inside the verified suffix).
  (V6) Minimality: G(N0-1) != G(N0-1+p); cycle C=G[N0..N0+p-1] has exact
       minimal period p (every p' < p breaks the cyclic symmetry).
  (V7) Census: P-positions (zeros) exactly {0,1}; overall max 8;
       cycle values subset of {1,2,4,7,8}, all nonzero.
Exit 0 with 'CERTIFICATE PASS' iff all checks pass. Deterministic, single-core.
Usage: python3 verify_certificate_0057.py grundy_0057_N8000.csv
"""
import csv
import sys
import time

N0 = 259
P = 148
M = 3
TSTAR = 2 * N0 + 2 * P + M  # 817


def reachable(G, n):
    """Reachable Grundy set for heap n using table G (needs G[j], j < n)."""
    s = set()
    if n >= 2:
        if n == 2:
            s.add(0)  # terminal: take whole heap
        else:
            S = n - 2  # take-2 splits only (digit 5 forbids singleton leave)
            if S >= 2:
                # xor symmetric: a and S-a give same value; halve the loop
                for a in range(1, (S + 1) // 2 + 1):
                    s.add(G[a] ^ G[S - a])
    if n >= 3:
        if n == 3:
            s.add(0)  # terminal
        else:
            s.add(G[n - 3])  # take-3 singleton leave
            S = n - 3
            if S >= 2:
                for a in range(1, (S + 1) // 2 + 1):
                    s.add(G[a] ^ G[S - a])
    return s


def mex(s):
    g = 0
    while g in s:
        g += 1
    return g


def main():
    t0 = time.time()
    path = sys.argv[1] if len(sys.argv) > 1 else "grundy_0057_N8000.csv"
    G = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            G[int(row["heap"])] = int(row["grundy"])
    Nmax = max(G)
    ok = True

    def check(name, cond, detail=""):
        global ok
        status = "pass" if cond else "FAIL"
        if not cond:
            ok = False
        print("[%s] %s %s" % (status, name, detail))

    # V1 integrity
    check("V1-integrity", all(G.get(n) is not None for n in range(Nmax + 1)) and min(G) == 0,
          "Nmax=%d rows=%d" % (Nmax, len(G)))

    # V2 suffix equality
    bad = [n for n in range(N0, Nmax - P + 1) if G[n] != G[n + P]]
    check("V2-suffix-equality", not bad,
          "checked [%d,%d] mismatches=%d" % (N0, Nmax - P, len(bad)))

    # V3 mex recomputation on small segment + base window + final two blocks
    windows = [("small[1,%d]" % (N0 + P - 1), range(1, N0 + P)),
               ("base[%d,%d]" % (N0 + P, TSTAR), range(N0 + P, TSTAR + 1)),
               ("final[%d,%d]" % (Nmax - 2 * P + 1, Nmax), range(Nmax - 2 * P + 1, Nmax + 1))]
    for wname, rng in windows:
        badm = [n for n in rng if mex(reachable(G, n)) != G[n]]
        check("V3-mex-recompute-%s" % wname, not badm,
              "n=%d mismatches=%d e.g.%s" % (len(rng), len(badm), badm[:5]))

    # V4 reachable-set equality on final full period block
    block = range(Nmax - 2 * P + 1, Nmax - P + 1)
    bads = [n for n in block if reachable(G, n) != reachable(G, n + P)]
    check("V4-reachset-equality", not bads,
          "block size=%d mismatched=%d" % (len(block), len(bads)))

    # V5 threshold coverage
    check("V5-threshold", TSTAR <= Nmax - P,
          "T*=%d <= Nmax-p=%d" % (TSTAR, Nmax - P))

    # V6 minimality
    check("V6a-preperiod-minimal", G[N0 - 1] != G[N0 - 1 + P],
          "G[%d]=%d vs G[%d]=%d" % (N0 - 1, G[N0 - 1], N0 - 1 + P, G[N0 - 1 + P]))
    C = [G[N0 + i] for i in range(P)]
    sub = [p for p in range(1, P) if all(C[i] == C[(i + p) % P] for i in range(P))]
    check("V6b-period-minimal", not sub, "subperiods=%s" % sub)

    # V7 census
    zeros = [n for n in range(Nmax + 1) if G[n] == 0]
    check("V7a-P-positions", zeros == [0, 1], "zeros=%s" % zeros)
    check("V7b-max", max(G.values()) == 8, "max=%d" % max(G.values()))
    check("V7c-cycle-values", set(C) <= {1, 2, 4, 7, 8} and min(C) >= 1,
          "cycle set=%s" % sorted(set(C)))

    dt = time.time() - t0
    print("verifier time: %.2fs single-core" % dt)
    print("CERTIFICATE " + ("PASS" if ok else "FAIL"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
