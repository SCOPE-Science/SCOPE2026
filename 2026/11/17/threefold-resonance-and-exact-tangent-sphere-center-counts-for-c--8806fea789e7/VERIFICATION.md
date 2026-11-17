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

The analytic derivation in `RESULT.md` verifies all real parameters \(a>0\), \(k>0\), all integers \(n\ge3\), and all positive prescribed radii, including the exact equality thresholds. The proof uses a complete Fourier-mode separation and explicit branch parametrizations; no finite search is used to infer the universal statement.

The self-contained Python standard-library checker `check.py` was executed and printed `PASS: 2796 deterministic numerical consistency checks`. It tests independent point-to-line projection calculations against the exact branch formula, plus axis and higher-cyclic normalization. Its tests are finite numerical regression evidence and do not establish independent or formal verification.

No independent mathematical audit or human validation has been performed. Literature comparisons have access and priority limitations described in `REVIEW.md` and `AUDIT.json`.
