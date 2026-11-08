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

The accompanying `verify_collision.py` is a standalone Python 3 script with no third-party modules and no source-document dependencies. It checks the same quadratic collision statistic from all \(\binom dr\) subsets against the exact rational variance formula for 1,548 distinct matrix cases (all binary circulants on orders \(4\) through \(9\) in the stated degree range and generated degree-preserving random exchanges). It also evaluates both seven-vertex examples explicitly.

Execute `python3 verify_collision.py`. Expected output reports 1,548 exact comparisons, mean \(3\) and variance \(0\) for the difference-set graph, and mean \(3\) and variance \(6/5\) for the interval graph. All comparisons use `fractions.Fraction` rather than floating-point approximations. This finite enumeration is an implementation check, not an exhaustive verification of every regular graph or the infinite families. The proof in `RESULT.md` establishes the general finite identity and the stated equality classification.

Independent audit: not performed.
