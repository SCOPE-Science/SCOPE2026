---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The standalone checker `verify_minimal_morphisms.py` was executed successfully for \(r=1,2,3,4,5\). For each parameter it verifies the full normalized chain complex of the explicit category, checks that the two boundary maps compose to zero, verifies the combinatorial sink-graph structure, and computes the full exact integral Smith normal form of the two-dimensional boundary matrix.

| \(r\) | \((a,b,c)\) | Nonidentity morphisms | Nonunit Smith factors | Rank of \(H_2\) |
|---:|---|---:|---|---:|
|1|(2,2,2)|6|2|0|
|2|(3,3,5)|11|2, 2|0|
|3|(4,4,10)|18|2, 2, 2|0|
|4|(5,5,17)|27|2, 2, 2, 2|0|
|5|(6,6,26)|38|2, 2, 2, 2, 2|0|

Reproduce: `python verify_minimal_morphisms.py` (Python 3, SymPy). The finite checks are not an exhaustive test of larger ranks; the general theorem is established in the written combinatorial and homotopy proof. No independent mathematical audit has been performed.
