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

# Reproducible mathematical checks

Run `python3 CHECKER.py` with a standard Python 3 interpreter from the directory containing these files. The script requires no external modules and constructs every labeled tree of order two through seven from its Prüfer sequence. For each tree, it computes every vertex directly from all independent incidence-edge signings and independently forms the degree-factorized squared-radius polynomial. Exact integer counters and rational arithmetic verify equality of the complete spectra and all claimed finite extremal counts and first two moments.

The script additionally computes the full joint distribution of all eight absolute-coordinate squares for a specified eight-vertex branched tree, checking exact product probabilities for every possible joint state, and compares the complete spectra of two nonisomorphic degree-equivalent six-vertex spiders.

Successful observed output:

`TREE_RADIAL_PASS labelled_trees=18248 orientations=1119262 joint_states=16 six_vertex_shells={4: 6, 8: 12, 12: 8, 16: 4, 20: 2}`

The checks exhaust those finite domains only. The arbitrary-tree factorization and the limits require the induction and probability arguments in `RESULT.md`. Historical priority has not been independently established, and no external audit has occurred.
