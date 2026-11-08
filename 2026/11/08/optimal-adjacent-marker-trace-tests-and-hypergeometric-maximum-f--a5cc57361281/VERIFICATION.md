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

Run `python3 check_trace.py` in the directory containing this file. The script uses only Python's standard library and checks exact rational trace probabilities by exhaustive deletion-mask enumeration at all lengths \(2\le n\le9\), every adjacent marker location, and retention probabilities \(1/4,1/2,2/3\). It checks (a) probability normalization, (b) optimal likelihood-sign ordering, (c) the arbitrary-position binomial expectation and weighted hypergeometric maximum identities, (d) central binomial-difference formulas, and (e) half-retention central Vandermonde closed forms. It also compares central Hellinger affinity with independent trace enumeration and prints non-certifying numerical convergence checks for the sharp asymptotic coefficients.

Expected first result: `EXACT_MASK_TESTS 108 PASS`. The mathematical justification of the infinite families uses elementary likelihood cancellation, a conditional hypergeometric shift lemma, the lattice local central limit theorem and a Taylor expansion with binomial concentration; finite tests alone do not prove these theorems. Confirm from `RESULT.md` that the source has exactly one marked symbol, and do not apply these formulas to arbitrary binary strings or nonhomogeneous channels. No independent mathematical audit has been performed.
