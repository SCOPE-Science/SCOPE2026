---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the shared-versus-independent parent coupling, the paired same-label degree polynomial has exact drift with collision correction (1−alpha)(z−1)(w−1) Z_n/n². Its normalized coefficients converge by triangular stochastic approximation to Q_alpha=1/[3−alpha−(1−alpha)(z+w)−alpha zw]. Conditional innovation cross bracket = alpha(z−1)(w−1)(Z_n/n−F1_n F2_n/n²), giving S_alpha=alpha(1−z)(1−w)(Q_alpha−P(z)P(w)). The fixed-cutoff martingale array with bounded increments and stable drift B=−I+J yields a Gaussian limit, and integration over age t gives C_alpha=S_alpha/(3−z−w). Independently verified with exact symbolic algebra that C_alpha equals the four-denominator rational formula and extracted c00,c01,c11 plus derivative. The proof is finite-dimensional and the direct second-moment recursion supports covariance convergence, not merely weak convergence.

## originality

PASS

The central source Bäumler–Rácz–Ross–Sridhar (2026) analyzes the precise sprinkled-correlated uniform-attachment model, proves leaf Gaussian covariance, and explicitly says in Appendix A that the higher-degree covariance matrix is not then available in tractable form. The submitted result supplies that rational kernel for every fixed pair of degrees and a joint finite-dimensional Gaussian limit; the known leaf coefficient and Janson single-tree marginal at alpha=1 are subsumed special cases, not new. Initial-common-prefix correlation is a distinct coupling. Generic martingale CLTs do not supply the specific covariance closed form automatically.

## value

PASS

Solves a naturally identified gap in the same stochastic tree model: explicit all-degree profile cross-covariance for statistical comparison and dependence calculations, plus a strict first non-leaf monotonicity law; a substantive structural function not a tiny numerical enhancement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
