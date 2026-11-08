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

# Verification and scope

To reproduce the supplementary computational checks in this package, install the dependencies in `requirements.txt` and execute `python verify.py` from the directory containing the files. The expected output is reproduced in `verify_output.txt`. The packaged execution completed with 606 passing assertions.

The verifier checks exact SymPy factorization of the sign-versus-Gaussian difference, the derivative with respect to squared orientation, both boundary laws, the exact crossover, the unpowered harmonic–geometric–arithmetic identity, and the off-diagonal high-power limit. It then uses finite exact-rational enumeration over five curvature ratios, five power counts and five rational alignment values, independent numerical angular integration for small/moderate power ratios, and direct Frobenius projection of tall matrices for chosen angles and gaps.

The symbolic identities and proof are valid for the continuous parameter domains stated in RESULT.md. Finite rational grids and floating-point integration do not establish those universal statements by themselves. Quadrature tests deliberately avoid very ill-conditioned exponential concentration; direct matrix tests use stable two-branch formulas to avoid subtractive cancellation. No tests certify floating-point implementations or larger sketch widths. The dated prior literature and the algebraic statement comparison appear in REVIEW.md and AUDIT.json.

No independent scientific audit or external validation has been performed.
