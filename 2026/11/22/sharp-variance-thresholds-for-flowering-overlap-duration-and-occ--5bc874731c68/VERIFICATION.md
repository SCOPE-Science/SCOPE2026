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

# Verification notes

The primary scientific verification is the derivation of \(F'(s)\) by the heat-kernel identity and distributional triangular second derivative; the normal CDF derivative for \(P'(s)\); strict convexity of the log-cosh scalar equation; and the layer-cake comparison of distinct variance optima. These cover all stated ranges and boundary cases. The independent Gaussian-moment formula and Simpson integration in the accompanying `verify_overlap.py` provide a second computational representation to cross-check formulas. The checker uses deterministic randomized samples and finite differences, and is not an exhaustive proof or an external certification.

To replay, from the directory containing the embedded files execute `python3 verify_overlap.py`. It requires only the Python standard library. No data files, unpublished manuscripts, external services or numerical libraries are necessary. The program's output reports sample checks and the two worked parameter cases. No independent audit was performed, and the historical-priority comparison does not establish absolute uniqueness among all literature.
