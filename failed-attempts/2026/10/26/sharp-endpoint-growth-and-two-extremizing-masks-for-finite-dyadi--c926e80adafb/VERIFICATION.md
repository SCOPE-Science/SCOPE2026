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

The conditional-expectation differences are pairwise orthogonal projections. For a fixed row, first mismatch at level k gives kernel S_k−b_k2^k with probability 2^(−k−1), while the diagonal gives S_n with mass 2^(−n). Symmetry identifies endpoint norms, and the sign of any row achieves its row sum. With z_k=S_k/2^k the optimization is terminal z_n plus the sum of |z_k−b_k|/2. The one-step envelope is one and the one-step maximizing bit is one for every reachable state z<1. For longer horizons, evaluating the two branches of the tent envelope gives a crossing at 1/2 and slope magnitude a_{r+1}=(1−a_r)/2. The resulting closed sum is n/3+7/9+(-1)^n/(9·2^(n−1)). Starting at zero forces the first bit one and creates the only possible nonterminal tie at the next state 1/2. Thereafter both update maps send interior states strictly to one side or the other and the optimal middle bits alternate, until the mandatory terminal one. This gives the two masks and the separate n=1,2 cases. Independent integer checks through n=9 constructed an actual conditional-expectation row for every mask and checked its identity with the corresponding modulated Walsh kernel; exact maxima and maximizing lists agreed. Checks are finite corroboration, not proof of the induction.

## originality

FAIL

The prior Resultary q-ary analysis, record 1564c6e21e01, formally states its new theorem for q≥3, but the exact kernel formula and the proved Bellman action thresholds mechanically specialize to q=2. Its proof uses λ≤c, not λ<c, for the two affine branch recurrences, and explicitly allows the boundary equality there. At q=2 both thresholds coincide at 1/2, the slope gap remains strictly positive, and the one extra tie gives exactly the binary equality classification. Thus there is demonstrated prior mathematical coverage of the full substantive claim, not merely an uncited remark or a possible literature overlap. The exact Walsh equivalence points to an earlier literature but Fine's priority is not decided here; it is not the reason for failure.

## value

FAIL

An exact finite-depth norm and equality classification of a natural projection family has mathematical use in principle, but here both, and the row-norm identity and growth, are direct boundary consequences of the earlier available Bellman analysis. The original supplies no independently useful unknown invariant or structural lemma beyond that specialization. No scientifically distinct remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
