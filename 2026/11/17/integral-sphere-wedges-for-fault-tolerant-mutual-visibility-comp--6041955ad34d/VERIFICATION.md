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

Fix q≥2, m,n≥q+2, a=m−q,b=n−q≥2. For a chosen vertex set with i on shore A and j on B, a pair on A has n−j internally disjoint unblocked length-two paths and a pair on B has m−i, giving the exact face criterion (i≤1 or j≤b) AND (j≤1 or i≤a). The simplicial complex decomposes as P_A*P_B ∪ Δ_A*D_B ∪ D_A*Δ_B; the latter two joins are cones. Attaching subcomplexes L_A=P_A*D_B and L_B=D_A*P_B map nullhomotopically to the core because a,b≥2 make the simplex skeletons path connected, so each discrete shore inclusion is null. The two cofiber attachments split as K≈P_A*P_B∨ΣL_A∨ΣL_B. The uniform-matroid skeletons are binomial wedge sums, giving sphere families of degrees a+b−1,a+1,b+1 with multiplicities c_Ac_B,(n−1)c_A,(m−1)c_B. The disjoint face regions give the exact polynomial. This proves integral and infinite-parameter assertions; does not extrapolate from finite mod2 tests.

## originality

PASS

Targeted Resultary search and accessible primary treatments distinguish ordinary q=1 mutual visibility (known) and general fault-tolerant definitions/maximum sizes on Cartesian or categorical products of complete graphs from the complete bipartite q≥2 face complex. None of the actually inspected primary claims computes a three-family integral homotopy wedge or its functorial core inclusion. The structural null-attachment calculation yields additional topology not implied by maximum visibility cardinality. Best-of-knowledge originality PASS with risk of an unindexed theorem applying to these same truncated-skeleton joins.

## value

PASS

Complete integral homotopy classification of a natural family of fault-tolerant visibility complexes for all shores and redundancy thresholds; explicit face counts and core-homology split explain how pairwise fault robustness changes topology, including three possible degrees. These are motivated graph-visibility invariants a future researcher can use, not a one-off small table or routine independent-set substitution. The boundary a,b≥2 is essential to connectivity and null attachments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
