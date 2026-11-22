---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The specific matrix and polynomial weights are reconstructed from RESULT.md, not from an old verdict. Sympy exact-polynomial expansion independently gave det(F)-2rho*x(1-x)*(x-eps^2)*(x-1/2)=0 identically. The original primary theorem supplies positive semidefiniteness on K_epsilon and existence of finite-degree certificates. On a fixed I strictly inside [1/2,1], every generator weight has uniform positive lower bound, so each SOS matrix coefficient is bounded by the bounded target. Bernstein–Walsh/Cauchy from I to a disk about 0 gives uniform C_R R^d control on first and second jets with any R>3+2sqrt2. At x=0 positivity of all unweighted blocks forces first column zero and S11 prime=0; the global PSD determinant inequality bounds S12 prime by sqrt(S11 second derivative * S22(0)/2). Differentiate off-diagonal identity: unit-size rho derivative must be at most const*(sqrt(eps*R^d)+eps^2*R^d), a contradiction below degree coefficient 1/log R. Sending R down proves liminf, not degree equality, and finite rational tests do not prove it.

## originality

PASS

Primary Jindal–Zalar Sections 6.2–6.3 already contain the exact parameterized matrix and unbounded-degree fact, but the quantitative logarithmic coefficient is absent from the inspected proof; the new claim has strictly stronger rate information, not a new example. Resultary search found the identical present finding plus unrelated matrix spectral and positivity work, no earlier dominating rate. Best-of-knowledge PASS only.

## value

PASS

An explicit quantitative logarithmic lower rate for matrix-SOS certificates under degeneration of an interval is a motivated degree-complexity obstruction; original literature establishes only divergence with no rate, and the gap between scalar and matrix preorderings is mathematically substantive. This result is not just a normal-form rewrite and may guide sharpness and complexity lower bounds; neither an optimal constant nor a universal family is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
