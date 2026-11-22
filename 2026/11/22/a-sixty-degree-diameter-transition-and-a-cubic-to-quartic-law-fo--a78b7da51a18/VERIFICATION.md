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

The analytical verification is in `RESULT.md`: the exact polar-law sampling distribution, diameter maximizer classification, radial and angular localizations, evaluated weighted-simplex integrals, and the critical co-scaling argument. The fourth-power term uses the **linear zero** of the planar sector's angle-gap density at its maximal angular separation; the folded-cone angle law does not have that zero.

Execute `python sector_verifier.py` with Python 3.9 or newer. The last actual standalone replay printed `SECTOR_CHECKS_OK 88`. The checker uses only the Python standard library and independently integrates an exact angular-survival formula over two radial variables. Finite-deficit error tolerance is diagnostic only: the maximal allowed relative discrepancy is nine percent for selected wide-sector tests; this is not a rigorous global bound. The proof, not numerical convergence, supports the asymptotic claims.

No separate mathematical audit has been performed. Historical priority is not globally certified. The moving-angle crossover is pointwise in its fixed parameter, with no uniformity claimed at unbounded parameter values.
