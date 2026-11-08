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

# Verification record

From a directory containing `verify_star_gauss.py`, run `python verify_star_gauss.py` with Python 3 and SymPy. The program constructs weighted-star Laplacians, directly computes the exact-rational endpoint matrices and compares their off-diagonal entries against independently written rational formulas. The completed replay returned `VERIFY_OK 1537` with no assertion failures.

The checking examples include two through six leaves, equal and unequal conductances, both safe and unsafe regimes, small and large positive steps, and exact reductions of the general condition to the known one-exceptional-spoke boundaries for degrees two through thirty. The proof in `RESULT.md`, not the finite sample, supports the general theorem. Critical analytic checks are the resolvent Schur complement, complex partial-fraction identity, positivity of every denominator, and monotone scalar sign reduction. Independent mathematical audit is not yet performed.
