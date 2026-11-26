---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

RESULT.md, lines 62–116: the sine transform puts each e_m in the domain of L^{-alpha/2} when alpha<3/2. The weighted Gram factorization and dense range of L^{alpha/2} give the exact nonnegativity threshold; a strictly negative form value gives a negative eigenvalue by finite-rank perturbation. The cosine formula and integrability prove the short-range limit. At alpha=1/2 subtract theta^{-1}; the L^1 remainder contributes o(1) off diagonal, and the cosine-integral tail is O(1/|m_i-m_j|), leaving the log ratio. Above 1/2, the rescaled integrand is bounded by a constant times min(u^2,1)u^{-2alpha}; the cosine integral gives the displayed normalization (in particular K_1(x,y)=min(x,y)). Independence of distinct sine frequencies gives positive definiteness. The two-site criterion is the sign of det(I-M) under the two strict diagonal bounds, and the spectral gaps persist. CHECKER.py and VERIFICATION.md were inspected; the recorded numerical assertions were not used as independent evidence of the limits.

## originality

FAIL

The strongest earlier paper supplies the exact zero-energy Green entries for this same spectral half-line operator, not merely the sine integral and a single-site result. Its Proposition 2.1, Remark 2.3 and the Birman–Schwinger formula in §3 mechanically imply all three leading finite-site laws and their strict two-site consequence. The comparison does not assert that the earlier article literally states the remote-impurity theorem.

## value

FAIL

Cooperative binding is a natural question, and the presentation is useful as an exposition. Here the precise constants, the interaction at the logarithmic boundary, and the strict cooperation window are all direct consequences of the earlier closed form and elementary spectral tests. No independently useful unknown exact claim survives on this evidence; the limiting equality case or higher-order threshold information is not resolved in the Finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
