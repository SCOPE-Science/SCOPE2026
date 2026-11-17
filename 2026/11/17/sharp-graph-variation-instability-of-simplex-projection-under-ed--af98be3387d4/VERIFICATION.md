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

The proof uses the exact simplex KKT threshold, full-dimensional active-support cells, coarea for graph total variation, a universal active/cut edge count, a parity-sensitive integer optimization, and explicit connected matching-joined clique witnesses.

The standalone `checker.py` was executed using Python 3 and the standard library. It enumerated every connected labelled graph for vertex orders 2, 3, 4, and 5, with respectively 1, 4, 38, and 728 graphs, and compared every nonempty active set and proper cut. Its exact rational comparisons numbered 6, 168, 7,980, and 677,040. Additional checks included 45,000 rational active/cut inequalities in connected graphs of orders 6 through 11, 45 exact stratified witness pairs, and the actual projected-input equality witnesses for every order from 2 through 60. The script confirms the proposed finite results but is not a proof over all orders or all edge connectivity parameters.

Reproduce by running `python3 checker.py` alongside this file. No third-party packages, network calls, or external certificates are required. All analytic quantifiers and infinite families are justified by the proof in `RESULT.md`; finite enumerations alone cannot establish them.
