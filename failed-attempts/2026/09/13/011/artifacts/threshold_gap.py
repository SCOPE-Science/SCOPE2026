"""Bounded recovery test: claimed threshold vs flat-length model threshold.

For smooth worm with total winding half-length beta and caps consuming
cap>0 on each side, flat half-width mu_flat = beta - cap. Standard
cap = pi/2 in DF construction. Dirichlet first-mode heuristic on model
strip of half-width mu gives critical Sobolev exponent pi/(2*mu).
Compares c_claim = pi/(2*beta) vs c_flat = pi/(2*mu_flat).
"""
import json, math

def c_claim(beta):
    return math.pi/(2*beta)

def c_flat(beta, cap=math.pi/2):
    mu = beta - cap
    if mu <= 0:
        return float('inf')
    return math.pi/(2*mu)

betas = [1.58, 1.7, 2.0, 3.0, 5.0, 10.0]
rows = []
for b in betas:
    cc = c_claim(b)
    cf = c_flat(b)
    rows.append({"beta": b, "c_claim_pi/2beta": cc, "c_flat_pi/(2beta-pi)": cf, "gap": cf-cc})

with open("threshold_gap_results.json","w") as f:
    json.dump({"cap_assumed": math.pi/2, "rows": rows}, f, indent=2)

for r in rows:
    print(r)
