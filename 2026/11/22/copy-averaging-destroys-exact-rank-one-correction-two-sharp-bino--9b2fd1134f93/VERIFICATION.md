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

# Verification

Run `python3 check.py` from the extracted package directory. The checker uses Python 3 standard-library rational arithmetic to evaluate independent exact multinomial and sequence enumerations, verifies both centered/one-sided closed binomial formulas and the rank-one projection minimum, and performs numerical checks of the asymptotic constants. The executed package passed 2,557 deterministic assertions.

The proof in `RESULT.md` (in particular the independent-rotated-walk argument and the exact binomial first absolute moment) establishes all-copy formulas without relying on finite enumeration. The large-copy limits follow analytically from the central-binomial asymptotic. Numeric tests do not certify an infinite limit or literature novelty. The risk is for an oracle optimal single-column correction and cannot be identified with full iterative-solver convergence.
