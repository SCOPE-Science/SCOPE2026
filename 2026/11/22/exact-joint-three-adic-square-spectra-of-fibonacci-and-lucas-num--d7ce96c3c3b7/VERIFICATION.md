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

The proof uses the exact matrix \(M^8=I+3A\), the valuation-sensitive expansion of \((I+3A)^d\), four normalized isometries, and a disjoint cylinder count for three-adic squares. The finite square-residue formula is derived by splitting according to even valuation. Infinite statements are proved mathematically in `RESULT.md`; numerical tests cannot certify all precisions.

Run `python3 verify.py`. The checker independently enumerates all full periods modulo \(3^k\) for \(1\le k\le9\); it compares each four-cell histogram to the closed formulas, verifies the exact period return, checks the square-residue cardinality formula for \(0\le m\le8\), and checks 4,644 normalized-branch isometry differences. The observed simultaneous-square counts are \(3,5,13,35,103,305,913,2735,8203\). These finite checks passed.

Unproved by the executable alone: the assertions for all \(k\), the limiting measure \(5/32\), and the logarithmic discrepancy. Those follow from the explicit arguments in `RESULT.md`. No independent mathematical audit or external certification has been performed.
