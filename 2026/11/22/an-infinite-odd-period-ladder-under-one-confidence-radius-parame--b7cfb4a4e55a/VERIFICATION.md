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

The supplied `check_hk.py` uses exact `fractions.Fraction` arithmetic, not floating-point approximations. Executing `python check_hk.py` tests the complete five-agent update rule for every integer \(1\le m\le30\) and three distinct interior-radius choices at one-quarter, one-half, and three-quarters of the stated window, yielding 90 complete trajectory tests. It checks that each frozen anchor trusts only itself, the fifth-agent's expected full or partial confidence neighborhoods at every phase, the exact primitive return, endpoint and width identities, disjoint consecutive windows, and the affine contraction multiplier. All tests passed.

The analytic proof in `RESULT.md` establishes the claims for every integer \(m\ge1\), irrespective of the finite test cutoff. No theorem about completeness of the periodic-orbit census, endpoint dynamics, or unrestricted-state-space asymptotic attraction is being asserted. Independent audit has not been performed.
