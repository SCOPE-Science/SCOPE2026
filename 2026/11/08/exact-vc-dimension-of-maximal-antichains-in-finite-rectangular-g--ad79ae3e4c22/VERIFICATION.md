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
# Reproducibility and verification

Run `python3 verify_maximal_antichain_grid.py` with Python 3 and no third-party dependencies. The script enumerates maximal antichains by their decreasing-coordinate placements and checks maximality by comparing every grid cell to at least one selected point; this does not use the VC formula to generate the hypotheses. It then checks every antichain support by direct pattern traces. Among the \(28\) rectangles with \(1\le m\le n\le7\), the program examines \(8750\) antichain supports, checks the four \(2\times3\) local patterns and two \(1\times2\) patterns, and confirms the previously known \(7\times7\) maximal-antichain count of \(817\). Its terminating line is `GRID_MAXIMAL_ANTICHAIN_VC_PASS: 28_rectangles; 8750_candidate_supports; local_gadgets_ok`.

The infinite-parameter theorem rests on a separate written argument. For the upper bound, each of the \(k\) shattered positions requires a slack coordinate level in an incident gap, and a single unused level can cover at most two positions. For the lower bound, independent four-trace gadgets occupy \(2\times3\) or \(3\times2\) blocks, with one-trace gadgets for odd \(k\); the union of local maximal antichains is extended globally without disturbing zero-labelled marked points. No numerical extrapolation, untested external package, or independent mathematical audit is claimed.
