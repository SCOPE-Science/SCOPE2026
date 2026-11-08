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

# Reproducible verification

Run `python3 checker_matrix.py` and `python3 checker_states.py` using Python 3.8 or later. Both use only the standard library. Captured outputs appear as `checker_matrix.out` and `checker_states.out`.

The first checker builds each graph from its direct neighbor list, multiplies binary matrices exactly, computes ranks by independent row elimination and compares each nullity of a matrix power to the stated formula. It tested 1,250 exact power-kernel comparisons for \(3\le n\le72\) and five additional larger circumferences.

The second checker implements the graph update separately on every labelled binary state for \(3\le n\le8\), constructs the entire functional digraph, removes transient states by indegree elimination, and computes each state's distance to the recurrent set. It checked 174,720 configurations and 33 cumulative entrance counts.

These are finite tests. The infinite-family proof is algebraic, and extension from the binary field to all finite characteristic-two fields follows from exact kernel dimensions over field extensions. No primitive-period census of the invertible component is asserted.
