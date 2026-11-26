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

In edge coordinates g_i=u_i-u_0, put b_i=c_i sign(g_i)|g_i|^(p-1). Then g'=Ab with A=-diag(1/m_i)-(1/m_0)11^T. The right derivative of the weighted absolute-value norm is a sum of signed velocities on nonzero edges and absolute velocities on zero edges. Expanding by columns of A gives the upper bound sum_i |b_i|B_i for B_i=(W-2w_i)/m_0-w_i/m_i; the off-diagonal contributions can be no larger than sum_(j!=i) w_j/m_0. A one-edge signal achieves B_i in the normalized derivative, hence the supremum is the maximum of the B_i, not every B_i (the wording at line 62 is imprecise; the Finding and displayed proof are clear). The vector field stays inside the initial value bounds, and monotonicity in the mass inner product gives uniqueness without requiring local Lipschitzness for 1<p<2. The right derivative criterion therefore applies at every time; a strictly positive B_i gives immediate increase, while all B_i<=0 force monotonicity by absolute continuity in time. Normalized weights satisfy w_i/W>0 and w_i/W>=(2+m_0/m_i)^(-1), proving feasibility and uniqueness at equality. The frozen checker was inspected but not executed.

## originality

FAIL

The preceding weighted-tree linear heat record 9fedb9294a7c already evaluates the same signed columns and exact contraction criterion. The entire claimed nonlinear extension is a pointwise sign-preserving substitution into those derivative data: g and b=(c_i sign(g_i)|g_i|^(p-1)) have the same signs and zero set, so their weighted-norm directional derivatives in the common direction Ab coincide exactly. Every b is attainable, since the coordinate power maps are bijective and every star edge vector is realizable. Therefore the normalized supremum and its witnesses reduce to the previously covered unit-conductance linear star case. The mass feasibility criterion and equality are immediate normalization of those known column inequalities. The distinct same-day nonlinear graph record corroborates overlap, but is not needed to infer earlier coverage.

## value

FAIL

The underlying question of when graph heat diminishes edge variation is natural. But this record's claimed contribution is a pointwise substitution into known column data followed by normalization; the stability boundary and its equal-mass example add no substantive independent result. No valuable non-covered remainder of the frozen claim was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
