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

The fixed-point residual is 4V_k. Independence gives U_{k+1}=(1+cβ_k²)U_k and V_{k+1}=(1−2β_k)²V_k+cβ_k²U_k. With y_k=V_k/(U_kβ_k) the coefficient of y_k is 1−4β_k+o(β_k) and the forcing is cβ_k+o(β_k), since β_k/β_{k+1}=1+o(β_k). The tail recursion is a weighted average with weights asymptotic to 4β_k and targets tending to c/4; the weights sum to infinity, proving convergence. The exact gamma product for U_k at b=1/2 then gives the critical p=1/2, including the positive constant there. Below b=1/2, summing log(1+cβ_k²) gives the stated leading logarithmic constant. For the path law put a_j=σβ_j/sqrt(2) and S_k=Σ_{j<k}a_j². Nonresonant u_k is a nonzero product whose tail log increments have mean −a_j²/2+O(a_j⁴) and variance O(a_j²). The series of centered increments divided by S_{j+1} converges almost surely by squared summability (compare Σ a_j²/S_{j+1}² with the integral of 1/s² away from zero); Kronecker's lemma yields log|u_k|/S_k→−1/2. Since a_k²=o(β_k), an envelope C exp[−(1/2−2δ)S_k] for |v_k| is eventually a supersolution: forcing from u_k is O(β_k exp[−δ S_k]) relative to this envelope and the homogeneous contraction is 1−2β_k. Letting δ decrease to zero and bounding the norm below by |u_k| gives the rate. A resonance is unique under strict step decrease; on survival the tail argument works, and on killing u stays zero and v contracts since Σβ_k diverges. This covers the stated boundary and resonance cases without relying on finite trajectory evidence.

## originality

PASS

The original published reflection example and both second-moment recursions are prior, and so is qualitative residual divergence for b<1/2. The primary proof drops all but the most recent transverse forcing, giving sufficient divergence at b=1/2 only when p>1; its discussion says that the iterates may still converge almost surely. The distinct credit is the full variance-transfer equivalent, exact phase boundary and constant, precise subcritical-schedule log-growth constant, and a proven pathwise collapse with its norm rate. Neither the inspected generic convergence hypotheses nor the distinct indexed related phenomenon implies those exact results.

## value

PASS

Resolving the exact boundary in a published counterexample identifies the regime 1/2<p≤1 in which the prior sufficient test did not show divergence. It also explains how accumulated transverse noise changes the threshold and demonstrates almost-sure collapse at a quantitative rate despite a diverging expected squared residual. This is a meaningful sharp counterexample, not an arbitrary special schedule with a numerical constant alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
