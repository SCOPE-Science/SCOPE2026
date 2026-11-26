---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For H=d(zI−P), the endpoints are exact because the regular bipartite graph has P-eigenvalues ±1. The optimal interval residual gives C_m=D_m(z,P)/(d T_m(z)), with D_m the Chebyshev divided difference. The first four expansions have nonnegative coefficients for z>1. At m=5 only the P and P² coefficients can become negative, and both are nonnegative exactly when z≥√5/2, equivalent to κ≤9+4√5, including equality. For Q_d the adjacent entry of D_5 sees only P and P³: the three-step count is 3d−2 versus one direct edge. Consequently after removing a positive prefactor its sign is that of z²−5/4+(3d−2)/d². This is negative for every fixed forbidden z as soon as d is sufficiently large. The positive constant row sum allows a strictly positive perturbation of a basis vector. Exact evaluation at Q32, z=21/20 gives T_5=503601/200000, the entry −17825/49113088 and the stated positive perturbation leaves output −17825/98226176. The Neumann series shows the exact inverse is strictly positive.

## originality

PASS

The sharp degree-five graph-uniform bound, and unconditional positivity of the first four final iterates in this class, are distinct from the strongest retrieved positivity bounds. The Chebyshev residual construction and coefficientwise sufficient test themselves are not credited as new.

## value

PASS

For graph diffusion and inverse problems the exact inverse preserves positivity, but minimax acceleration need not. This identifies a precise regime where a common accelerated polynomial is safe across a natural class, shows an unconditional guarantee for four final steps, and proves when that guarantee fails even for strictly positive data. The high-degree hypercube witnesses make the boundary necessary at every supercritical condition number, not merely a coefficient-bound estimate or a single failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
