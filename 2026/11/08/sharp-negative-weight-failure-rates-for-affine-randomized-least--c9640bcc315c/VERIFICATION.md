---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The accompanying `verify.py` uses standard-library Python 3. Its exact-rational test checks the affine weights and sign-event equivalence. Its numerical rate test compares the uniform error-function formula against composite Simpson integration and locates the stationary point by bisection. The script also includes a check of the previously known three-node probability; that check is not evidence of a new three-node result and is not needed for the rate theorem.

For a direct numerical replay of the uniform example, apply the composite Simpson rule with 16,384 equal subintervals of \([-1,1]\) to each of \(e^{-t(x^2-x)}/2\) and \(-(x^2-x)e^{-t(x^2-x)}/2\). Bisect the zero of the latter integral for 50 iterations starting from \([0,2]\), and take the negative logarithm of the former integral at that point. This gives approximately \(t_*=1.263164403304\) and \(I_\nu=0.172761450635\). This floating-point replay is not a rigorous interval enclosure.

The proof of the general asymptotic law uses the independent designated-node event and a Cramér lower bound at strictly negative means approaching zero, followed by the compactness argument for the scalar tilts. No finite check or simulation certifies that law.
