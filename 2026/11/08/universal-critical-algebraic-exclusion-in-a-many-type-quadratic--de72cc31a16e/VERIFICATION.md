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

# Reproducibility and verification

The exact projective update is \(F_i(p)=\vartheta_i p_i(2-p_i)/\sum_k\vartheta_kp_k(2-p_k)\). The proof derives the scalar identity \(u-u'=(1-u)(2u^2+B)/E\) and a decreasing ratio of the largest and smallest subordinate coordinates. These are the critical analytic steps; their formulas and quantifiers are written in RESULT.md.

Run `python3 CHECK.py` using the standard Python library. The script verifies agreement with the original homogeneous map using rational arithmetic, exact critical drift and fixed-composition identities, finite illustrations of the universal critical decay in dimensions two through seven, and the supercritical geometric upper bound. A printed PASS line indicates all script assertions completed successfully.

Computational checks cover finitely many initial states, parameter values and time horizons. They cannot certify the limiting claims, originality, or the absence of literature equivalents. Only the self-contained mathematical proof establishes the asserted all-dimensional infinite-time statements. Independent audit has not been performed.
