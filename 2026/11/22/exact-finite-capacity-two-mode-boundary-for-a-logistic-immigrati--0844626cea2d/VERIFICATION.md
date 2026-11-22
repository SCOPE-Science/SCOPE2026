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

# Verification scope

Reconstruct the adjacent stationary mass ratios directly from the stated birth and death rates, then confirm the exact difference identity, the strict threshold equivalence, and the quadratic double-contact factorization in `RESULT.md`. These algebraic identities prove the theorem for every integer capacity.

The included `verify.py` uses Python 3 standard-library rational arithmetic (`fractions.Fraction`) to check 1,939 exact finite diagnostics, including all sizes 2 through 100 with sampled positive immigration rates and threshold-crossing growth parameters. It also performs 56 floating-point diagnostics of the continuous envelope and the stated asymptotic scale. On extraction, run `python3 verify.py` in the same directory. Expected output is two named counts and a successful completion message. Finite tests and floating-point checks are supplementary; they do not independently establish the infinite-size asymptotic or all-capacity claim.

No independent scientific audit or expert validation has been performed. Historical-priority risk from older, incompletely accessible logistic immigration literature remains; see `REVIEW.md`.
