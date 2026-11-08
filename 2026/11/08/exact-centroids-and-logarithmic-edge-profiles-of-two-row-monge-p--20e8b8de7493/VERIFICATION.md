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

# Verification and reproducibility

Run `python3 verify_centroid.py` alongside `RESULT.md` using Python 3.9 or later; no nonstandard packages are required. Execution of the embedded script returned `PASS: 4036 exact rational assertions; q=1..36`.

The script evaluates the exact beta-polynomial integrals by rational binomial expansion, recomputes all moments by an adjacent-spacing recurrence, and checks extreme-column harmonic identities, symmetry, exact row normalization, strict row monotonicity, and strict discrete convexity. At \(q=2\) it uses an independent Beta-distribution centroid calculation: the sum of the two constrained coordinates is \(\operatorname{Beta}(2,2)\), truncated to \([0,1/2]\), yielding \(5/32\) and \(11/32\) entries. The \(q=3\) centroid is checked exactly as well.

Finite calculations cannot establish the theorem for unbounded \(q\); the analytic proof in `RESULT.md` supplies the universal quantifiers, the measure normalization and the asymptotic arguments. Historical originality is assessed separately from numerical verification. No independent audit has been conducted.
