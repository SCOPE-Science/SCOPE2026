---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Checked the exact first integral f(u)+f(v)=L and compact regular levels, the original-time generator identities <u>=<v>=<uv>=1, and positivity/normalization dnu=uv dmu. Reconstructed inverse branches a(q)<1<b(q) of f(z)=z-1-log(z), their square-root turning-point and large-q bounds; the positive-time branch integrals give T_L=L+O(log L), a dominant logarithmic slow leg of physical-time mass 1-O(log L/L), and an upper-concentration flux leg of mass 1-O(log L/L). Coupling along the energy relation yields both stated l1-W1 bounds and the fixed-integer beta mixed-moment constants. The O(log L/L) rates are upper bounds, not sharp assertions. Verified independently C exact generator identities and the beta transform; inspected check_dual_occupation.py for assumptions; its finite-energy quadratures do not establish the limit.

## originality

PASS

Best-of-knowledge original paired quantitative high-energy ordinary-time/flux-time distribution laws. Earlier analytic quadratures and periods, and stronger exact conditional mean-independence, cover basic normalization and first moments but not the joint W1 laws or all higher mixed moments. The 2026 unequal-rate singular crossover addresses a different asymptotic regime and does not substitute for flux weighting. Residual risks: an unindexed prior high-energy stationary occupation analysis or a derivative of existing quadratures.

## value

PASS

The actual gap is the paired asymptotic law of two naturally different invariantly sampled views of the SAME classical oscillator: uniformly distributed log extinction shares under physical-time sampling versus linear abundance shares under a canonically normalized reaction-flux bias, with every fixed positive mixed moment evaluated by Beta(r,s). This explains a significant scale separation obscured by exact first-moment and period formulas; these distributions and all higher mixed moments do not follow mechanically from the previously known covariance identity. Natural physical and flux measures, quantitative W1 rate, and exact universal coefficients make the result useful despite the classical model and modest proof length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
