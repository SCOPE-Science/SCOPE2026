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

The proof in `RESULT.md` is analytical: exact distance decomposition, a quantitative uniform localization bound, convergence of moving minimum, planar indicator convergence, and an anisotropic change of variables. Finite quadrature only diagnoses the constants and the asymptotic regime and does not establish infinite quantifiers.

Run `python checker.py` with Python 3, NumPy and SciPy. It computes the crossover normalization two ways at the critical point and compares exact-cost cross-sectional areas at fixed \(\lambda\in\{-2,-0.75,0,0.75,2\}\) and \(t\in\{0.004,0.001\}\). The numerical test uses the exact Fermat minimum formula on the interior-minimizer side, independent of the local crossover expansion. The output terminates in `FERMAT_CRITICAL_CROSSOVER_DIAGNOSTIC_OK` on success.

The tested angles remain strictly between zero and \(\pi\). The exact-cost integration is deterministic numerical quadrature over a near-vertex portion, with its upper boundary checked to have zero active width for the tested cases; it does not claim an exhaustive finite parameter certification. Historical originality is not independently certified.
