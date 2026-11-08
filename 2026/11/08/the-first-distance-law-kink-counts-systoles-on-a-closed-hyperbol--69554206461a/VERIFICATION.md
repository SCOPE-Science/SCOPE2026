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

The self-contained `verify_hyperbolic_systole.py` uses Python 3 standard-library quadrature and no external datasets. Execute `python3 verify_hyperbolic_systole.py` in the extracted package directory.

The program checks the same hyperbolic disk lens against two distinct exact representations, computes cyclic-cover orbital corrections at shortest-geodesic lengths 0.5, 2 and 4, checks that the coefficient tends to the universal value \(2\pi\ell\), and tests its second-derivative jump normalization. The expected final line is `HYPERBOLIC_SYSTOLE_CHECK_OK lenses=5 collar_lengths=3`.

Analytic scope: the main result is proved by a two-sheet covering identity, conjugacy-class unfolding, and controlled local lens-asymptotics. Floating-point quadrature supports but cannot establish the theorem for every closed hyperbolic surface. Tests do not generate a closed surface or identify a new metric. No independent external validation has taken place.
