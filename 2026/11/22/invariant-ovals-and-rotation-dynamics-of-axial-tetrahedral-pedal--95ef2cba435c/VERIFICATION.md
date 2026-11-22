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

The included `check.py` uses Python's standard-library `fractions.Fraction` for exact rational cross-checks, with fixed reproducible random seed. It reported `PASS: 3712 exact Fraction identities/cross-checks` when executed directly. Checks include the two-parameter pedal recurrence, its birational conjugacy, rational invariant, sum-of-squares maximum, Jacobian density, and direct facet-plane projections from 128 exact rational symmetry-axis tetrahedra. 

The infinite level-oval and dynamical conclusions follow from the independently displayed algebra, discriminant, invariant positive area form and standard coarea/circle-rotation arguments, not from finite sampling. No formal proof assistant or independent audit has been used.
