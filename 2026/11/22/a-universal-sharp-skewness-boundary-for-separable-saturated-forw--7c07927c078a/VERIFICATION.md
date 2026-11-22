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

# Reproducible checks

Run `python3 CHECK.py` in the directory containing the extracted files. The script is self-contained and requires Python 3 only. It returns `VERIFY_OK 18792 exact-rational assertions` in the tested environment.

Checks include the exact inverse of the skewed planar operator, the key Fejér inequality at 3,750 rational states per skew value, exact rational tests within the asserted stepsize region, local supercritical witnesses, negative-drift witnesses above the skew boundary, local derivative witnesses disproving pairwise nonexpansiveness, and a concrete \(s=2\) distance-increasing step. The tests use exact rational arithmetic throughout.

The analytic proof in RESULT.md covers arbitrary admissible scalar responses and uncountably many parameter and initial-state choices. The finite checks neither exhaust this domain nor certify the general theorem independently. The proof of convergence relies on an exact smooth-convex descent inequality rather than simulation. The endpoint \(\gamma=2/(1+s^2)\) is covered by the Fejér inequality, not by the summable-descent convergence argument.
