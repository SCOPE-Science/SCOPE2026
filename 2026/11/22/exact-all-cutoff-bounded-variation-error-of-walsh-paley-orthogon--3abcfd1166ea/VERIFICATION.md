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

The exact-rational script `checker.py` constructs the Walsh-Paley characters directly on sufficiently fine dyadic grids, integrates step functions coefficient by coefficient, computes the orthogonal projection residual by Parseval, and compares it with the proved closed formula. Tests cover integers from 1 to 40, selected dyadic cells and rational jump positions, predicted equality positions, and finite sums of signed jumps. The package was executed successfully with 1,658 rational assertions.

The proof of the universal assertion is analytical: dyadic subspace identity, next-Rademacher block identity, optimization of an explicit quadratic, finite-measure representation of bounded variation, and noncollinearity of distinct maximizing step residuals. The finite checker is not a universal proof and contains no assertion of external certification.

To reproduce: `python3 checker.py`. Requires only a standard Python 3 installation. Scientific boundaries are ordinary interval variation, the standard Paley Walsh order, unweighted \(L^2(0,1)\), and real input functions. No independent audit has been conducted.
