---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The source derivation is mathematically sound. Gaussian KL yields Q=M sum_i(1/x_i)-d-d log M+sum_i log x_i, invariant under scaling. At a hypothetical maximizing interior coordinate the stationary second derivative is positive by Cauchy-Schwarz, so all eigenvalues lie at endpoints 1,K. Evaluating j high eigenvalues gives dF_K(j/d)/2, and the derivative has a unique interior continuous maximum; finite mesh extrema and limiting coefficients follow. Independent differential-evolution tests for (d,K)=(2,1.5),(3,3),(4,10),(7,100) match endpoint formulas. These tests corroborate only; proof handles all d>=2 and K>1.

## originality

FAIL

Originality fails conclusively. A 2026-10-18 published sharp KL-envelope theorem proves identical finite-dimensional supremum and all endpoint equality spectra for precision B=C^{-1}, including a genuine coupled Lanczos realization. A Nov2 theorem explicitly treats condition number <=K with the same direction of KL. Converting precision eigenvalue fraction p to covariance high-eigenvalue fraction 1-p makes old Phi_K exactly new F_K. Thus every asserted inequality, equality case and asymptotic is already implied.

## value

FAIL

All apparent contributions—including sharp finite-dimensional constant, endpoint extremizers, asymptotics—are already derived in the stronger Oct18 and Nov2 papers; no separately motivated new invariant or result survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
