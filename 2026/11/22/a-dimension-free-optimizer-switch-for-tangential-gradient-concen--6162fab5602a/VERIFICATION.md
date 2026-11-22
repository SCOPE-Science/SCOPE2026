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

# Verification and reproduction

The accompanying `verify.py` performs symbolic identity tests with formal dimension parameter, 125 numerical beta-integral evaluations in five dimensions and five squared apertures each, five independent coordinate-level S² gradient Gram computations, and four high-concentration condition-number asymptotic checks. The verified symbolic identities are the three normalized means and all three exact beta-density differentiation identities appearing in `RESULT.md`.

Execute `python verify.py` from this package with Python, NumPy, SciPy and SymPy installed. The run must print four `PASS` lines without assertion failure. This self-contained program uses no external input data. The all-dimensional proof is the exact invariant-subspace and beta-identity argument in `RESULT.md`; finite numerical quadrature is only supplementary checking. The web-literature comparison is confined to the sources and sections documented in `AUDIT.json`. No independent external audit has been performed.
