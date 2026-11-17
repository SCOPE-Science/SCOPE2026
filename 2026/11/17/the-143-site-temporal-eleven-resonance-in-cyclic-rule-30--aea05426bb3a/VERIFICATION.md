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

# Computational verification

The standalone sources in this directory reconstruct the exact time-column recurrence for temporal period eleven of cyclic Rule 30. Both C++ programs traverse the entire set of \(2^{22}=4,194,304\) encoded ordered column pairs. `cycle_walk.cpp` follows functional components and records every recurrent directed cycle. `indegree_certificate.cpp` independently computes the indegree of every state, removes the nonrecurrent states by queue, and traverses the remaining cycles. Both give the complete recurrent length-multiplicity list \((1,1),(2,1),(143,1),(275,1)\), with \(421\) recurrent and \(4,193,883\) transient profile pairs. Neither program relies on a statistical sample.

`direct_witness.py` uses the original binary three-neighbor Rule 30 and the two complete bitstrings embedded in `cycle_walk_output.txt`. It verifies exact return at eleven updates, no return at any earlier positive time, and minimal spatial block lengths \(143\) and \(275\). The witness \(143\) contains \(73\) ones, and witness \(275\) contains \(137\).

For replay, use standard C++17 and Python 3 in the directory containing all files. The compilation and run commands appear in `RESULT.md`. Successful outputs were captured as `cycle_walk_output.txt`, `indegree_output.txt`, and `direct_witness_output.txt`. The finite certificate proves a claim for **all** spatial circumferences by a bijection with closed walks in a fixed finite graph, not by enumerating spatial rings only up to some length. No independent external audit has occurred.
