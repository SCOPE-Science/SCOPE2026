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

# Verification of the analytic broadband-transmission formula

The theorem is reconstructed in RESULT.md from the published finite-array transfer formula and an explicit torus-average/Chebyshev-band argument. A standalone standard-library diagnostic CHECK.py numerically quadratures its normalized two-phase formula for four couplings \(b=1/4,1/2,1,2\); exact \(N=1,2\) results and the \(N=30\) approach to the derived infinite-array limit are compared with stated numerical tolerances. The asymptotic weak- and strong-coupling expansions receive separate finite checks. The executable printed `PASS: 17 deterministic quadrature and asymptotic checks` when run on this package.

The diagnostic is finite numerical evidence, not proof of equidistribution, the infinite-array limit, or the asymptotic error bounds. Those statements rely on the explicit proof. The original scattering formula and its normalization were separately checked against Theorem 1(i), equations (4.4) and (5.2) of arXiv:2606.14931. The paper's early public release date is June 12, 2026. The source complete text was inspected; an older transmission-coefficient phase-method work remained abstract-level accessible, as disclosed in REVIEW.md. No claim of independent review is made.
