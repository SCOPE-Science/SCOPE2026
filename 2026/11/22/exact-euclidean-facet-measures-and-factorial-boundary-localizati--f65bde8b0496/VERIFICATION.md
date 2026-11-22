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

## Reproducible geometry diagnostics
Run `python check.py` using Python 3 with NumPy and SciPy installed. The script constructs the actual two-layer \(0/1\) vertex configurations and invokes independent convex-hull geometry for each \(1\le n\le6\). It verifies unique supporting-hyperplane identification for **every** convex-hull facet, the total predicted facet count, the Euclidean \((n+1)\)-volume, the Euclidean \(n\)-boundary measure, and the normalized-volume arithmetic identity.

Observed output terminates with `CAYLEY_CUBE_SIMPLEX_HULL_FACET_AREA_PASS`; the checks succeeded on all six parameters. They are floating-point checks of finite-dimensional cases, with  tolerance in `check.py`, not exact arbitrary-dimensional verification.

The general result is established in `RESULT.md` by (i) an exact halfspace description and proof of all listed facet dimensions, (ii) a combinatorial section-volume identity, (iii) a beta integral, and (iv) the tangential-gradient coarea formula for arbitrary subset size. The factorial asymptotic is an infinite-series argument independent of the numerical checker.

No independent external audit has been performed. Historical priority is subject to search coverage limits, especially possible earlier computations under different Cayley-prismatoid terminology.
