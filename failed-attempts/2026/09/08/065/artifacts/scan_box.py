"""Guy-Smith non-closure scan for octal 0.007 through N=200.

For each candidate (preperiod q, period p) in 0<=q<=QMAX, 1<=p<=PMAX, find the
least failing index n with q <= n <= N-p and G[n] != G[n+p]. If none exists the
pair survives (would be consistent with eventual (q,p)-periodicity on [0,N]);
otherwise the witness (n, G[n], G[n+p]) refutes (q,p)-periodicity on this range.

Writes witnesses_Q100_P100.csv with columns: q,p,n,g_n,g_np.
"""
import csv
import os

N = 200
QMAX = 100
PMAX = 100
BASE = os.path.dirname(os.path.abspath(__file__))
IN_CSV = os.path.join(BASE, "grundy_007_N200.csv")
OUT_CSV = os.path.join(BASE, "witnesses_Q100_P100.csv")

def load():
    G = {}
    with open(IN_CSV) as f:
        r = csv.DictReader(f)
        for row in r:
            G[int(row["n"])] = int(row["g"])
    return [G[n] for n in range(N + 1)]

def main():
    G = load()
    assert len(G) == N + 1
    rows = []
    survivors = []
    for q in range(0, QMAX + 1):
        for p in range(1, PMAX + 1):
            found = None
            # need q <= n <= N-p; if q > N-p the pair is vacuous (not the case here
            # since q+p <= 200 always: max 100+100=200 gives single index n=100)
            for n in range(q, N - p + 1):
                if G[n] != G[n + p]:
                    found = (n, G[n], G[n + p])
                    break
            if found is None:
                survivors.append((q, p))
            else:
                n, a, b = found
                rows.append((q, p, n, a, b))
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["q", "p", "n", "g_n", "g_np"])
        w.writerows(rows)
    print(f"pairs: {(QMAX+1)*PMAX}, excluded: {len(rows)}, survivors: {len(survivors)}")
    if survivors:
        print("SURVIVORS:", survivors[:20])
    else:
        print("all pairs excluded: proved q>100 or p>100 (within N=200 window)")
    print(f"wrote {OUT_CSV}")

if __name__ == "__main__":
    main()
