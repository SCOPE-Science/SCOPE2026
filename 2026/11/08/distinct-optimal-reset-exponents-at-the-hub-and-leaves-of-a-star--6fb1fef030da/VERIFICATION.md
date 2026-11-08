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

Run `python3 verify.py` in the directory containing `RESULT.md` and `verify.py`. The reference execution printed `CHECKS_OK` and reported 185 checks, including direct full-state matrix stationary solutions for stars with \(2\le m\le40\), both root choices and six probabilities per size; exact center-root optimal identities; analytic peripheral derivatives against central finite differences; and the asymptotic scaling table up to \(m=10^8\). The numerical matrix tests are supplementary. Uniformly quantified assertions are proved in `RESULT.md`, especially the comparison inequality, large-degree localization and derivative expansion. No floating-point sampling is presented as a proof of uniqueness, global optimality or an infinite limit. Independent audit: not performed.
