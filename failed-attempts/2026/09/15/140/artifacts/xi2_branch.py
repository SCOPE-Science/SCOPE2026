"""xi2-branch check for the two BCH localizations.
ABL Cor.2: xi_ABL = min{xi1, xi2}, xi2 = root (in w* in [d'/2,1/2]) of
  R = (1-d')H((w*-d'/2)/(1-d')) + 1 + d' - H(w*); 'if the root is negative, put xi2 = 0'.
We tabulate gap(w) = RHS(w) - R over the full admissible interval."""
import math, csv
def H2(x):
    if x <= 0 or x >= 1: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)
def xi1(dp): return 0.5*(1-math.sqrt(dp*(2-dp)))
rows = []
for (n,k,dpn) in [(15,7,4),(31,15,7)]:
    R = k/n; dp = dpn/n
    lo = dp/2; N = 200
    gaps = []
    for i in range(N+1):
        w = lo + (0.5-lo)*i/N
        u = (w-dp/2)/(1-dp)
        rhs = (1-dp)*H2(u)+1+dp-H2(w)
        g = rhs - R
        gaps.append(g)
        rows.append([n,k,dpn,f"{R:.6f}",f"{dp:.6f}",f"{w:.6f}",f"{rhs:.6f}",f"{g:.6f}"])
    print(f"n={n} k={k} d'={dpn}: R={R:.6f} dp={dp:.6f} xi1={xi1(dp):.6f} "
          f"min_gap={min(gaps):.6f} max_gap={max(gaps):.6f} -> "
          f"{'ROOT EXISTS' if min(gaps)<=0<=max(gaps) else 'NO ROOT => xi2=0 by ABL convention'}")
with open("output/artifacts/xi2_scan.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["n","k","dpn","R","dp","wstar","RHS","gap_RHS_minus_R"])
    w.writerows(rows)
print("WROTE xi2_scan.csv")
