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

## Reproducibility

From the directory containing the two standalone check files, run:

```sh
python check_rectangular_logic.py
```

The complete recorded output appears in `check_output.txt`. It reports 392 matching-coordinate extension comparisons across widths \(3\) through \(6\), and 90 finite-graph colour/diameter checks. The checker uses Python's standard library only. Both checked properties are proved in the main result for all permitted parameters; these runs test examples rather than certify the infinite claims.

## Direct mathematical checks

For an edge in a Cartesian product of cliques, all common neighbours lie in its varying coordinate fibre, so the maximum clique containing it has size equal to that factor order. This justifies the intrinsic edge-colour formula. For each colour, a pure-colour path changes only coordinates from that factor-size class; within a component, the maximum distance equals the number of such coordinates. A new vertex in the \(k\)-pebble strategy can repeat an already present symbol or use a fresh symbol; with at most \(k-1\) stationary pebbles, this set of options depends exactly on the alphabet size truncated at \(k\). These are the core proof obligations, independently described in `RESULT.md`.

## Limits

The test programs do not execute infinitely many pebble rounds or exhaust all factor lengths. They provide finite examples; the unrestricted first-order conclusion rests on the explicit permanent strategy. The reviewed result has not received independent mathematical audit.
