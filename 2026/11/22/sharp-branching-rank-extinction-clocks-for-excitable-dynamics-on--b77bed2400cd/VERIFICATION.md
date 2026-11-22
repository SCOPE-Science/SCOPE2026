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

# Verification of the sharp forest extinction clock

The theorem concerns all finite forests with contact threshold \(\theta\ge2\) and color count \(\kappa\ge3\), not merely the tested instances. Its critical step is that a time-\(t\) excited vertex forces \(\theta\) distinct time-\(t-1\) active neighbors, and the predecessor event path cannot backtrack in a forest because a vertex cannot be excited two steps apart. An embedded complete \(\theta\)-ary witness follows by induction. Starting with precisely its deepest leaves excited generates the reverse branch-by-branch advancing wave and attains the bound.

## Executed checks

`python3 verify_exhaustive.py` was executed successfully from the packaged source. It enumerates all states of every nonisomorphic tree to the listed vertex limits for five `(threshold,colors)` cases; 241 tree/parameter comparisons and 1,882,829 initial-state trajectories were checked against the structural formula. It rejects unexpected nonzero cycles. The exact output is stored in `verification_output.txt`.

`python3 verify_witness.py` was executed successfully from the packaged source. This second independent program checks 8,896 deterministic complete-branching and seeded pseudorandom tree constructions for thresholds 2–5 and colors 3–6; in each case it asserts a late excitation at the chosen root and exactly the expected first all-rest time. The source uses only the standard library; the exhaustive program requires NetworkX.

## Unproved by computation and limitations

Enumeration through finite orders cannot prove the all-size theorem, exclude historical equivalents, or establish results for cyclic graphs. The proof is included in `RESULT.md` and is independent of test coverage. The review is not an independent mathematical audit.
