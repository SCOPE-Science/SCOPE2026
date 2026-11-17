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

Execute `python scripts/check.py` with NumPy and SymPy installed (versions are not pinned). The checker constructs the exact first-derivative matrix of the three facet heights and two opposite-edge-pair coordinates; its determinant is \(64\sqrt2/19683\). It verifies symbolically the local density \(729/(128\pi^2)\) per orientation, the quadratic-form determinant \(3\), the five-dimensional volume integral \(16\pi\delta^4/(3\sqrt3)\), and both forms of the leading coefficient. It separately samples actual independent spherical points and determines facet orientation and distances geometrically. Monte Carlo results at finite threshold gaps are approximate and need not agree exactly with an asymptotic coefficient. No simulation is presented as an infinite proof.

The mathematical verification is the explicit local-coordinate proof in `RESULT.md`: coverage/support-function equivalence; the regular-tetrahedron extremal inequality; nonsingular shape chart; stationarity and negative-definite second variation; the uniform small-deficit localization estimate; and dominated convergence for both probability and conditional laws. Numerical tests do not independently establish historical novelty. No independent audit has been performed.
