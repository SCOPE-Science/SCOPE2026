---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Positive-good EFX reduces exactly to L_i≥S_ij−s_ij for a nonempty parallel-edge subbundle owned by j, because deletion of its lightest edge leaves its highest remaining value to i. At a violation, L_j−L_i>s_ij>0. The two loads after moving that edge are a doubly stochastic mixing of the old pair, with parameter s_ij/(L_j−L_i) strictly between 0 and 1. This proves the Lorenz comparison for the entire vector even if the loads cross. The square cost drops by 2s_ij(L_j−L_i−s_ij)>0; finite orientations ensure termination for arbitrary real weights. Fixed total, exact endpoint assignment and majorization give the Schur-objective consequences. In the nonexistence example, vertex 2 has possible load 0,4,8; load 4 forces max at least 7 and min at most 4, and load 8 forces min at most 5 and max at least 8, proving the two cited optima are incomparable and undominated. In the asymmetric example, every split has peak R and the unconstrained minimum is 2. The frozen checker was inspected, not run; its bounded integer checks are not the real-weight proof.

## originality

PASS

The supported distinct assertion is Lorenz cofinality of positive-good EFX orientations at heterogeneous symmetric weights, or equivalently a balancing repair of every complete orientation. Prior existence in richer classes and Lorenz dominance in dichotomous classes do not give that assertion. No independent covered statement or local transfer theorem establishing the weighted property was identified in the compared sources.

## value

PASS

The repair preserves every Lorenz lower-tail bound simultaneously from a prescribed allocation without discarding value. This materially strengthens mere existence and transfers to all Schur objectives in a weighted class where a single globally Lorenz-best orientation need not exist. It is not claimed as a polynomial-time optimization algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
