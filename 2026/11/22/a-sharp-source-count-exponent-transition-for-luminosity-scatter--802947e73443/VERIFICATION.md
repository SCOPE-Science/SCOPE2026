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

# Verification instructions and boundaries

Execute `python3 verify.py` with the complete package extracted to a single directory. The script uses only Python's standard library and checks independently computed radial-quadrature values, derivative identities, sign regimes, nonzero optimum root equations, a three-dimensional numerical example, and a limiting approximation. Its printed assertion count is a finite diagnostic record, not a proof of infinite-parameter statements.

The mathematical proof is in `RESULT.md`. Reconstruct it by checking (i) conditional visibility as a capped radial count, (ii) the displayed lognormal Gaussian completion of squares, (iii) the ratio differential equation and its integrating-factor sign argument, and (iv) the bounded-offset expansion used for the faint-mean limit. The primary-source comparison and historical-priority limits are described in `REVIEW.md` and `AUDIT.json`.

No independent audit or external certificate has been performed.
