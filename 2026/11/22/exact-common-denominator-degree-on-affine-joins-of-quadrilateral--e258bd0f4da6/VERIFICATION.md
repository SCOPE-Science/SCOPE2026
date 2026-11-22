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

# Verification of the geometric claim

The universal argument uses a published common-denominator vanishing-order theorem and an elementary translation-invariance lemma. Its crucial quantities are \(\dim J=3k-1\), facets \(4k\), facets per vertex \(4k-2\), and excess \(k-1\) for every vertex. These are established directly by the face-lattice description of an affine join.

For sharpness, the homogeneous quadrilateral coordinate identities are \(\sum_a P_{i,a}=t_iH_i\) and \(\sum_a v_{i,a}P_{i,a}=z_iH_i\). Multiply by \(\prod_{j\ne i}H_j\) and sum across factors. This verifies normalization and linear precision of the common-denominator formula, with positivity inherited from each quadrilateral.

The standalone `VERIFY_JOIN_QUADRILATERALS.py` checks 336 cases using exact fractions for squares, trapezoids and mixed factors in dimensions five through twenty-three. Run `python VERIFY_JOIN_QUADRILATERALS.py` in an environment with Python 3 standard library. It verifies only selected explicit factor-coordinate models; the analytic proof covers all quadrilaterals and all integers \(k\ge2\). The external vanishing-order theorem is cited as a source-supported lemma, not independently re-proved here.

No independent audit was performed, and historical priority remains provisional.
