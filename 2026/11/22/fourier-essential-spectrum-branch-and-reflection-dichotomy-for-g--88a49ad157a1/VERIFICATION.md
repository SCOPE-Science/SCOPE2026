---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

# Verification notes

The theorem follows from an explicit unitary conjugacy, vector-valued dominated convergence for weakly null Fourier packets, the Fredholm left-parametrix obstruction, and Fourier-transform uniqueness for finite measures. No numerical cutoff is used as an infinite proof.

To replay supplementary checks, run `python check.py` with SymPy installed. The checks include the exact Cayley affine map, scalar amplitude after the logarithmic transformation, 192 rational matrix coefficient comparisons with a formal series recurrence, and three packet estimates.
