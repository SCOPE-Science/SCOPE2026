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

# Verification of the annular extreme-stretch theorem

The analytic proof is in `RESULT.md`. The following finite checks are reproducible from the included `verify_annulus_stretch.py` using Python 3 with NumPy and SciPy:

`python verify_annulus_stretch.py`

Expected final line: `ANNULUS_STRETCH_TAIL_CHECKS_OK 20017`.

The checker integrates the exact angular threshold of the event by two-dimensional Gaussian quadrature in the radial defects, using the shortest-path formula and a root-finder. Nine tail-integral tests span three aspect ratios and three deficit sizes; 20,000 generated pairs test the deterministic upper bound, and additional checks cover the local expansion and shape inversion. Two finer deficit integrations are printed separately in the research result but are not counted in the checker marker. The finite sample and quadrature do not prove uniformity, optimality or the asymptotic limit. The proof's global geometric comparison, tangent-angle identity, Taylor remainder and simplex volume supply those statements.

Independent audit has not been performed.
