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

The proof establishes the infinite identities using known binomial-parity run-length representations, an elementary finite-word recurrence, and exact characteristic polynomials. The standalone verifier `checks/check.py` enumerates 1200 independent binomial-parity pairs, compares five moment identities over all 15 dyadic blocks through length 14, and uses rational arithmetic to isolate all nine roots and verify the strict inequality between spectral radii.

The script can be run using `python3 checks/check.py`; it has no third-party dependencies. The root-asymptotic argument is analytic and algebraic, not certified by the finite enumerations. The previously recorded single-sequence squared moment is credited to OEIS A030186. No separate external validation has been conducted.
