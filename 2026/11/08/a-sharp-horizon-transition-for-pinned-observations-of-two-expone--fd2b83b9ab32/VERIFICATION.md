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

# Reproducible checks

Run `python verify.py` with Python 3.9 or later; no third-party packages are required. The program prints `VERIFICATION_OK 56063 exact-rational and sampled-grid assertions` if successful. It checks the closed Cauchy–Binet formula against an independently constructed Gram determinant for integer decay-rate ratios with exact rational arithmetic. It also checks exact first derivatives, global-design inequalities on dense deterministic grids for nonintegral ratios on both sides of the transition, and leading small-excess-horizon and large-horizon formulas.

The proof in `RESULT.md` is the mathematical evidence for the continuum claim. Rational examples and sampled real-parameter grids alone cannot certify all real parameters, all times, or the asymptotic limit. The records describe calculations performed from the contained script, not an independent mathematical audit. No external validation has yet been performed.
