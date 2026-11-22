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

The supplied `check.py` uses Python standard-library exact fractions and seeded floating-point inversion. Run `python check.py` beside the accompanying result. It verifies exact count-polynomial moment identities for three and four occasions on a rational grid, one exact pair of distinct three-occasion parameters with equal count laws, a mismatch of their four-occasion laws, the rational Jacobian determinant identity, and randomized reconstruction of four physical parameters.

The checked run reported 4,768 supplementary assertions. Finite numerical checks do not establish global identifiability: the analytic monotonicity and connected-level-set argument in the proof does. Near the excluded persistence boundaries, numerical inversion may be ill-conditioned. Independent external audit has not been performed.
