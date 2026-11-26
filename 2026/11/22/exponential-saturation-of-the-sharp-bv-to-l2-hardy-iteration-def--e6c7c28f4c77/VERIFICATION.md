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

With real BV and open-interval variation, represent f modulo constants by integrating upper step functions against Df. The probability kernel for H^m gives bounded integrands against the finite variation measure, justifying interchange; Minkowski then gives the optimal norm as the supremum of single-jump norms. Products of m independent uniforms give a Gamma(m,1) logarithmic delay and the stated Q_m residual. Its squared norm R_m satisfies R_m'=Q_m²-R_m and integration by parts gives the displayed root equation; the bracket is strictly decreasing and its limit is at most -1. The unique maximizer forces variation supported at a single jump, including both jump signs. The m=1 squared norm is t(1-t), and Q_{m+1}>Q_m for positive arguments proves strict growth. The root lies between b_m and (1+epsilon)b_m by a Gamma lower-tail bound, which then gives 0<=m log(L_m/b_m)<=-log Q_m(L_m)=O(exp(-cm)). In the Poisson tail expansion at L_m, L_m^m/m! tends to 1/2, and successive terms after factoring the lead are uniformly geometrically dominated and tend to (1/e)^j. This yields the exact squared-deficit prefactor after Stirling. No weighted or general Lp claim is inferred.

## originality

PASS

The closest known formula uses the same averaging/variation model but integrates the step residual to power one rather than two. The L2 norm, strictly monotone root equation, rigidity and precise squared-deficit coefficient are a distinct conclusion; neither the L1 formula nor standard Hardy operator norms supply that root or coefficient.

## value

PASS

The variation-ball identity defect is an interpretable exact error benchmark for repeated prefix averaging, rather than the usual Hardy operator norm. It determines all worst inputs and their boundary migration and distinguishes the norm-dependent saturation coefficients from the analogous L1 result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
