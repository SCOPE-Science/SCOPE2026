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

# Mathematical reproducibility

Execute `python3 verification/check_facet_stability.py` with a stock Python 3 installation. It checks all facet-active simplex volume identities by independently solved Gram linear systems and determinants over exact rational arithmetic, and cross-checks the projected-face membership inequalities. It tests dimensions 2 through 6, integral one-shears and heights, the symmetric sharp dihedral examples, and a published four-vertex benchmark. The replayed output is:

`PASS exact rational regression tests, dimensions 2..6`

The finite test set is neither a universal proof nor an exhaustive search over shape space. All-dimensional completeness and equality classification are established by the algebraic proof in RESULT.md. Scientific novelty is supported by the listed source comparisons and is subject to previously unknown equivalences. No independent validation has been performed.
