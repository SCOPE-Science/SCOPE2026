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

The theorem is proved in `RESULT.md`; finite tests check exact rational certificates and numerical implementations, but cannot establish infinite-dimensional coverage or historical novelty.

Run `python checks/check_ferrers.py` in an environment with Python 3, NumPy, SciPy and SymPy. The script constructs the surviving grid vertices directly and checks 441 parameter configurations with class sizes from two through seven. It verifies 3,136 missing-vertex rational projection certificates, 441 exact contact-face Gram determinants, and 441 hypergeometric identities against separate finite-shuffle enumerations. It additionally solves 100 constrained quadratic programs independently of the formulas. Its replay completed with:

`FERRERS_DELETION_PASS configurations=441 exact_missing_vertices=3136 independent_QP=100 max_gap=3.85e-14 exact_hypergeom_and_gram=441`

Separate numerical normal-limit diagnostics compared exact hypergeometric tails with standard-normal CDF values for symmetric configurations of size 100, 400 and 1600 and offsets near minus one, zero and one standard deviations. All comparisons were consistent; these diagnostics are not packaged as a standalone independent certificate. The proof, not finite enumeration, establishes the asymptotic statement.

No independent audit, expert review, or formal infinite verification has been performed. The first cited public source is dated 2021-03-28 in the original arXiv submission history; that date is a literature-anchor date, not a claim of priority for this theorem.
