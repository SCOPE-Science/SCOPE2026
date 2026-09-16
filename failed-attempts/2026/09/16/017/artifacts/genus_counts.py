"""Reproducible arithmetic checks for the genus-bound rigidity claim (lane-20451).
Verifies only the numerical/genus-counting skeleton:
 -chi(H_std) = 4g for genus 2g+1; threshold d_AC > 4g forces minimal genus 2g+1;
 any closed genus-h surface with 2h-2 < d is incompatible with strong irreducibility.
"""
import json, pathlib

def chi_closed(h): return 2 - 2*h
def neg_chi_closed(h): return 2*h - 2

rows = []
for g in [2, 3, 4, 5, 10]:
    std = 2*g + 1
    assert neg_chi_closed(std) == 4*g, (g, std)
    # threshold d > 4g: every h <= 2g has 2h-2 <= 4g-2 < d -> ruled out as strongly irreducible/minimal
    d = 4*g + 1
    ruled_out = [h for h in range(2, std) if neg_chi_closed(h) < d]
    assert ruled_out == list(range(2, std)), (g, ruled_out)
    rows.append({"g": g, "std_genus": std, "neg_chi_std": neg_chi_closed(std), "threshold_4g": 4*g,
                 "sample_d": d, "ruled_out_h": ruled_out})

# pants count: pants in a pants decomposition of closed genus-h surface = 2h-2
for h in [2, 3, 5, 7]:
    assert 2*h - 2 == -chi_closed(h)

out = {"checks": rows, "pants_identity_ok": True,
       "g1_note": "g=1 excluded: 2g+1=3 but figure-8 exterior has Heegaard genus 2, so formula not sharp; consistent with g>=2 hypothesis."}
p = pathlib.Path(__file__).with_name("genus_counts.json")
p.write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
