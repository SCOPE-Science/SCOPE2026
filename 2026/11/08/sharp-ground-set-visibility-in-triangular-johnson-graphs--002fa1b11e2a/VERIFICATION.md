---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Two standalone standard-library Python 3 programs are included. Execute `python3 verify_orbit_game.py` and `python3 verify_witness.py`. The captured expected outputs are `verify_orbit_game.out` and `verify_witness.out`.

The first checker enumerates all endpoint-permutation orbits of ordered graph-vertex tuples in sampled triangular graphs. Its direct successor computation replaces one coordinate by every feasible two-subset, and iterative, counting-free successor-color refinement computes the unlimited-round finite pebble-game partition. It compares all pairs of sampled ground orders at widths \(k=2,3,4\), with \(45\) pairwise comparisons and no discrepancy. The refinement has respectively \(17,80,715\) orbit positions and stabilizes in \(2,3,4\) iterations.

The second checker enumerates graph-vertex selections and evaluates the existential matching and one-adjacent-pair patterns directly. For each threshold \(4\le t\le9\), it observes absence on \(t-1\) hidden points and existence on \(t\), all \(12\) binary checks passing.

These bounded computations do not prove the theorem for arbitrary \(k,n,m\). The infinite-dimensional parameter range and arbitrarily long quantifier play are addressed by the self-contained support-bijection argument in `RESULT.md`. No independent mathematical audit has been performed.
