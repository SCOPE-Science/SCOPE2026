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

Run `python verify.py` in this directory with Python 3 and SymPy installed. The code checks the exact formula for the modulus polynomial evaluated at the geometric cutoff, the symbolic Floquet multiplier factorization after eliminating the angular parameter, the rational boundary instance \(\alpha=4/5\), and the central half-turn multipliers. It additionally constructs and replays 12 pairs of noncentral primitive two-cycles for three choices of \(\alpha\), testing unit norms, return equations and sink/source multiplier ordering.

The mathematical proof in `RESULT.md` establishes the continuum of parameter values: the finite diagnostics test implementation and normalization only, and are neither an exhaustive search nor an infinite-parameter certificate. The source-publication comparisons concern the cited propositions and remarks. The complete wording of an earlier published erratum was unavailable; no conclusion about its content is made.
