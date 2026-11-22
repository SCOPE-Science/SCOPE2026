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

The theorem is proved analytically in RESULT.md. In particular, the exact one-sided quadratic-coboundary identity, the telescoping bound, the sigmoid Lipschitz bound, the integer block threshold, invariant-probability integration and zero-feedback escape are stated with their hypotheses and constants.

Run `python3 check.py` using Python 3 and its standard library. The checker independently evaluates 93 rational transition identities (including both signs and zero boundaries), a bounded illustrative trajectory with published parameter choices, and zero-feedback sign and amplitude checks over several gains. All these diagnostics passed when run from the package's own `check.py`. These finite checks do not certify all real parameters, all iterates, or publication priority; the infinite assertions rest on the proof in RESULT.md.

No independent mathematical audit or external certification has been performed. The bound on sign-return windows is sufficient, not optimal; the claims do not extend to noninteger fractional orders.
