---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

FAIL

For every NONTRIVIAL nilpotent finite group, the Sylow-Frattini spanning rank test gives the stated piecewise partner count; for d>=2 a pair extends to d generators iff rank{g_p,h_p}>=d_p−d+2, and |Φ| lifts count neighbors. For d=1 nontrivial G is cyclic and Γ_1 is edgeless; formula indeed gives 0. HOWEVER THE ACTUAL UNRESTRICTED CLAIM IS FALSE AT THE TRIVIAL GROUP G={1}: d(G)=0, π(G)=∅, |Φ(G)|=1, empty product ∏ A_p=1, so displayed degree formula yields 1 although Γ_0 has one vertex and degree 0 (or Γ_0 is undefined in versions restricting u>=1). This explicit omitted quantifier boundary prevents correctness PASS for the original all-finite-nilpotent formulation. No repair files supplying the nontrivial restriction were prepared; do not certify the original.

## originality

PASS

The nontrivial mixed-Sylow rank-dependent formula is not supplied by Lucchini’s all-minimal-set graph degree formula; Γ_{d(G)} can be a strict subgraph when Sylow ranks differ. The p-group specialization is already implicit, so priority assessment attaches only to the mixed-prime formula and its divisibility consequence on nontrivial nilpotent groups. This originality does not rescue the false trivial-group statement.

## value

PASS

Exact minimum-generator independence degrees and a divisibility theorem for a natural nontrivial class address an explicit Lucchini question and reveal distinct Sylow-rank regimes. The corrected nontrivial variant would be valuable; current claim is rejected on correctness, not lack of motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
