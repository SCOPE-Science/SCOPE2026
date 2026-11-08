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

# Reproducibility and limits

Run `python3 verify.py` using Python 3's standard library. It checks the exact polynomial factorization and rank-one PSD curvature identities with rational arithmetic, the explicit stable counterexample, and a finite sample of additional parameter cases. Floating-point evaluation of a small collection of exponential quadrature defects is supplementary. The proof in `RESULT.md` proves the universal statements by a Peano-kernel argument and a cyclic-degree lemma; finite tests do not certify all dimensions, inputs, or step sizes. This package contains no independent external mathematical audit.
