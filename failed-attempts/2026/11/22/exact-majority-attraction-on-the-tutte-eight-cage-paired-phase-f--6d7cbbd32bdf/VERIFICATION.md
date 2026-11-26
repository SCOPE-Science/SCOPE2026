---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

I independently built synthemes by testing triples of disjoint duads and computed each local majority bit by marking all supersets of a winning neighbor pair. Reverse traversal on the alternating single-shore state space (65536 states total) visits every state from the exact two-cycles. A full configuration first becomes recurrent when both independent coordinate histories have reached these cycles, so the entrance time is the maximum of the two coordinate entrance times. A recurrent full state has two phase labels and the update swaps them. For phase labels U,W, the ordered basin has product a_U b_W, and a two-cycle with unequal labels adds its two disjoint ordered basins. The independent replay matches all nine paired types, both complete histograms, both orbit counts, total mass 2^30 and the whole entry census. The mask trajectory (106,0) → (0,1544) → (72,0) → (0,1024) → (0,0) → (0,0) verifies sharpness. In particular 240 fixed basins have size 836 and exactly one two-cycle basin has size 38579328. The scope is labelled synchronous strict majority on this single graph.

## originality

FAIL

The distinct earlier record 937ad301f17d already gives the same graph, update, sharp identity, phase swap, orbit counts and the stronger period-resolved entrance census. It also explicitly defines and its published code computes the same paired terminal fiber counts per phase label. The later nine-type histogram and full basin spectrum are mechanical summaries of those counters, not a new graph-specific calculation beyond the prior exact data and phase rule. This failure is based on demonstrated coverage and implication, not absence of literature or similarity of titles.

## value

FAIL

The cage and its synchronous majority basin invariant are naturally motivated. Nevertheless, once the previous exact phase counts and alignment are used, the incremental claim here is a routine regrouping of already computed numbers. The mismatches (22,38) and (38,22), and the largest basin, are obtained by inspecting and sorting those same counters. They are useful summaries, but no independently valuable unknown mathematical remainder is established under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
