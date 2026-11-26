---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In tangent coordinates at v1 the sphere gradient has differential lambda1 I-A on the tangent space, and normalization differentiates to projection onto that space. The state map is smooth near (v1,v1); the unnormalized vector there is v1. Each independent transverse eigengap Delta gives z^2-[1-(1-p)x]z+px, x=eta Delta. The strict disk test is px<1, x>0, and 2-(1-2p)x>0. Replay by evaluating the polynomial at +/-1 and its root product: for real roots the endpoint inequalities and product bound force both roots inside, and for conjugate roots the product is their squared modulus. The maximal gap L is attained and controls all upper bounds; the flip and product bounds meet at p=1/4. Above the ceiling either the product exceeds one or the value at -1 is negative, which in the latter case forces a real root below -1. At equality the largest-gap block has roots -1 and -2p/(1-2p) if p<1/4, a repeated root -1 with a nonzero rank-one nilpotent part if p=1/4, and a nonreal unit pair if p>1/4. For strict Schur stability use an adapted contracting norm in local coordinates. Conversely a uniform exponential inequality for independent nearby pairs differentiates to ||D(F^t)||<=C r^t at the fixed point, which is impossible for a unit or larger multiplier. For the critical companion matrix N=M+I satisfies N^2=0 and M^k=(-1)^k(I-kN); determinant one and Frobenius norm squared 2+4k^2 give the larger singular value k+sqrt(k^2+1) including k=0. This measures the linearized response, not nonlinear instability at the boundary. The supplied script was inspected but not executed; its sampled root and finite-difference tests do not determine the all-parameter result.

## originality

FAIL

Repnikov–Faleichik–Moysa explicitly give the same 3/4 fresh, 1/4 previous two-step rule and real stability length 4 as the k=2 case of their earlier stabilized Adams-type construction. Substitution gives the identical critical polynomial and companion matrix. The specific application to the normalized sphere map is not shown to have been stated earlier, and the prior theorem is not claimed to print the entire p-frontier or the Euclidean norm. However, the headline stability gain is covered, and the application obtains it by the tangent linearization of an existing cached polar update; the rest is the routine quadratic disk test and powers of its very same critical matrix. The record does not establish a distinct substantive theorem beyond that transfer and calculation.

## value

FAIL

Fixed-delay polar dynamics are a motivated model and the transfer is pedagogically useful. But the central gain is the previously computed two-step Adams rule acting on transverse spectral modes. The gap reduction uses only the standard tangent Hessian and normalization derivative; the remaining frontier and exact Euclidean norm are mechanical consequences of quadratic root testing and the power of its fixed two-by-two companion matrix. No distinct boundary dynamics, robustness analysis, changed optimization quantity or other independently needed nonroutine invariant is established. Narrowing to the remaining calculation alone would not meet the value threshold, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
