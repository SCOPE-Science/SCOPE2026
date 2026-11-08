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

# Computational verification

Run `python3 verify.py` using the Python standard library. This reproduces 60 exact rational generator/renewal comparisons, finite polynomial identity and coefficient-sign tests for every path length 2 through 150, finite-volume monotonicity probes, and the stated large-volume optimum constants. The unlimited-length assertions are established by the algebraic proof in RESULT.md; finite testing cannot establish them by itself. All tests reported here passed.
