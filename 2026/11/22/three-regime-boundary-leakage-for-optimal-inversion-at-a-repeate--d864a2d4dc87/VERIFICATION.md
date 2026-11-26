---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the replacement, the minimum-norm residual is characterized by its Euler jets at 1 (equivalent to the ordinary jets by a triangular change of basis). Gram positivity and the fixed-dimensional Riemann-sum limit give L^(beta+j) A_(j,L) -> a_j. The interpolating rational function with poles -beta-j and zeros 1 through m-1 gives P(1)=C and P(0)=D from its leading term at infinity and its residue at -beta. On interior compacts the remaining powers k^j are summably dominated after geometric decay. For 0<alpha<1, Dirichlet convergence is uniform since every geometric partial sum is bounded by 2/|1-z|. The frozen proof incorrectly multiplied O(L^(j-alpha)) by O(L^-j) to obtain O(L^-1); the corrected bound O(L^-alpha)=o(1) suffices for every fixed alpha>0. For alpha<=0, multiply by z-1 to isolate the endpoint terms; Abel summation bounds the remaining first-difference series by endpoint first differences and total second variation. Each monomial contributes O(L^(-beta-j) sum_(k=1)^L (k+1)^(beta+j-3)), plus endpoint bounds O(L^(-beta-j)+L^-2). All are o(1/L) for beta+j>1; the beta=1,j=0 term has exactly zero differences. At |z|=1, z!=1 the negative-weight oscillation has nonzero constant modulus after scaling; at -1 the positive-weight coefficient has positive alternating sum, and at alpha=0 the reverse triangle inequality gives m^2-m>0. No numerical certificate is needed; the supplied finite diagnostic was inspected, not run. The corrected proof is replayable in repairs/4/RESULT.md. The limits require fixed m, alpha, and positive separation from z=1 for closed-disk estimates.

## originality

PASS

Best-of-knowledge pass for the three-regime off-root asymptotics, not the finite moment formula, the initial coefficient constant, or Legendre endpoint identities in the Hardy setting. The precise uniform non-Hardy limits require oscillatory-sum estimates not supplied by known norm or moment asymptotics.

## value

PASS

This resolves a stated off-root boundary-uniformity gap for a canonical repeated-root factor, quantifying the dominant endpoint and sharp decay order. Comparing boundary leakage with faster interior decay at negative weights and isolating the Hardy transition provide information missing from norm convergence. No general multiple-root-location or moving-parameter conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
