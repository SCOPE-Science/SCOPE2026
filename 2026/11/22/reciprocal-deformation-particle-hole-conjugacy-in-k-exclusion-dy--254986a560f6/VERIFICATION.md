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

## Reproducible checks

Execute `python3 check_duality.py` in the same directory as this file. This script relies only on the standard library (`fractions`, `itertools`) and constructs the directed marked event list independently from the local rate definition. It verifies the complement–reflection involution and bijectively compares all event labels and exact rational rates against the reciprocal-parameter system, not merely row sums. The checked finite families have \((L,K)=(3,2),(4,2),(5,2),(3,3),(4,3),(3,4),(4,4)\), deformation \(t\in\{1/2,2/3,3/2,3\}\), and asymmetry \(q\in\{0,1/3,1,2\}\). The passing totals are 112 cases, 22,736 configurations and 90,832 marked transition comparisons.

## Mathematical limits

The all-parameter conclusion follows from the two geometric-sum identities and the generator argument in `RESULT.md`, not from a finite enumeration. The script does not independently check the finite-time semigroup, spectrum or equilibrium probabilities; these are exact corollaries of the established generator conjugacy. No independent scientific audit or publication-priority certification has been performed.
