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

# Reproducibility and scope

Both independent scripts run with the Python 3 standard library (no additional dependencies). Run `python check_dynamics.py` and `python check_formula.py` in the directory containing the embedded scripts and compare their per-graph distributions to `dynamics_output.txt` and `formula_output.txt`.

`check_dynamics.py` builds each labelled complete multipartite adjacency list directly, exhaustively generates all nonnegative chip allocations totaling the graph's number of edges, applies the original synchronous toppling update, and counts an initial state only if it returns to itself with each vertex firing exactly once. It checks nine part-size tuples and 20,814 total initial allocations. `check_formula.py` independently enumerates proper cyclic part words and assigns ordered nonempty blocks by Stirling counts. The resulting counts agree for every period in every checked case. For \(K_{2,2,1}\), both methods give periods \(3,4,5\) with respective configuration counts \(6,16,40\).

The correctness of the full infinite-family theorem rests on the proof's general phase correspondence and circular-word support lemma, **not** on these finite checks. The programs do not verify historical novelty or the absence of more general covering statements. The inaccessible full source-reversal paper remains an explicit source-inspection limitation.
