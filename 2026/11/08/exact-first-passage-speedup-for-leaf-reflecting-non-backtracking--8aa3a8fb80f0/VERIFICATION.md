---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For target-rooted finite tree, a non-backtracking oriented arrival p(v)→v has expected first parent-return time F_v=2b_v−1 by induction: child excursions cost 2b_w and the linear child-arrival equations give U_w=1+2(k S_v−b_w)/(k+1), S_v=b_v−1, k=d_v−1. Fresh-start parent passage B_v=1+2kS_v/(k+1) handles the first step. Strong Markov decomposition along source-target path and SRW parent passage A_v=2b_v−1 give the exact difference 2[(b_s−1)/d_s+Σ_{i=1}^{ℓ−1}(b_{v_i}−1+b_{v_{i−1}})/d_{v_i}]. Every summand nonnegative and each intermediate strictly positive, so equality iff s leaf directly adjacent target. Independently rebuilt lifted directed-edge linear systems on 96 ordered-pair checks of finite trees, agreeing with formula. Uniform first neighbor, deterministic leaf reflection, and no-cycle hypotheses are essential.

## originality

PASS

The known graph-wide improvement direction for FIFO1 tabu walks is expressly credited; the submitted all-tree target-rooted exact positive difference and equality classification are not contained in the inspected general inequality or no-dangling-edge second-order formulas. Best-of-knowledge PASS, allowing possible unindexed elementary tree identity.

## value

PASS

The exact amount of first-passage improvement at any prescribed tree vertices is a natural quantitative invariant beyond the known sign. The closed branch-size expression and sharp equality boundary permit computation without solving the lifted walk, and expose structural dependence on side branches across every finite tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
