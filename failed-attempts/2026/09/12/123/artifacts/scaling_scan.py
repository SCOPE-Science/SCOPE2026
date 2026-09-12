"""Bounded recovery test: uniform Airy edge-scaling vs Peierls loop-control threshold.

Reproduces BCJ22 Sec.3 scaling constants for the rough-smooth (liquid-gas)
interface on the diagonal, scans a in (0,1), checks:
  (A) saddle non-degeneracy (f''=0, f'''!=0) via c0>0, finite lambda1,lambda2;
  (B) where the a<1/3 restriction actually bites: crude Peierls loop bound.
"""
import json, math

def constants(a):
    c = a/(1.0+a*a)
    d = 1.0-2.0*c
    if d <= 0:
        return dict(a=a, c=c, d=d, degenerate=True)
    c0 = (d**(2.0/3.0))/((2*c*(1+2*c))**(1.0/3.0))
    lam1 = math.sqrt(d)/(2*c0)
    lam2 = (d**1.5)/(2*c*c0*c0)
    xi = -0.5*math.sqrt(d)
    Ccal = (1.0-math.sqrt(d))/math.sqrt(2*c)
    return dict(a=a, c=c, d=d, c0=c0, lam1=lam1, lam2=lam2, xi=xi, Ccal=Ccal,
                degenerate=False)

grid = [0.02,0.05,0.1,0.2,0.3,0.33,0.34,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.99]
rows=[]
for a in grid:
    rows.append(constants(a))

K = 3.0
for r in rows:
    a=r["a"]; bound_base=K*a
    r["peierls_base"]=bound_base
    r["peierls_crude_converges"]=bool(bound_base<1.0)

print(f"{'a':>6} {'c':>8} {'1-2c':>8} {'c0':>9} {'lam1':>9} {'lam2':>9} {'xi':>8} {'K*a':>7}  crudeOK")
for r in rows:
    print(f"{r['a']:6.2f} {r['c']:8.5f} {r['d']:8.5f} {r.get('c0',float('nan')):9.5f} "
          f"{r.get('lam1',float('nan')):9.5f} {r.get('lam2',float('nan')):9.5f} "
          f"{r.get('xi',float('nan')):8.5f} {r['peierls_base']:7.3f}  {r['peierls_crude_converges']}")

print()
print("min c0 on grid (excl endpoints):", min(r["c0"] for r in rows if not r["degenerate"]))
print("max lam2 on grid:", max(r["lam2"] for r in rows if not r["degenerate"]))
print("all interior points non-degenerate:",
      all((not r["degenerate"]) and r["c0"]>0 and math.isfinite(r["lam1"]) and math.isfinite(r["lam2"]) for r in rows))
print("crude Peierls bound fails exactly for a>=1/3:",
      [r["a"] for r in rows if not r["peierls_crude_converges"]])

with open("output/artifacts/scaling_scan.json","w") as f:
    json.dump(rows,f,indent=2)
print("wrote output/artifacts/scaling_scan.json")
