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

# Verification and reproducibility

This package contains two independent executable tests (Python 3, standard library only). Run `python3 verify_direct.py` and `python3 verify_motzkin.py`. The exact standard output of each successful run is stored in `direct_output.txt` and `motzkin_output.txt` respectively. Their version-independent assert statements are the checks.

The direct program enumerates all \(3^n\) labelled vertex states for each \(2\le n\le10\), computes the actual forward cycles rather than inferring periodicity from repeated transient states, and checks the all-state entry-time bound, last-entry count and eventual basin labels. The independent particle program evaluates the exact binary collision equations, exhausts all admissible modular edge words for \(2\le n\le11\), compares all late-entry edge words with \(n\) cyclic placements of the Motzkin excursions, and checks the predicted scaling at \(n=50,100,200,400\). Outputs include per-size totals and PASS statements.

These tests are finite evidence. The bound for arbitrary \(n\), unique-last-collision/Motzkin bijection, winding basin formulas and asymptotic constant are established in the proof rather than inferred from the enumerations. No numerical result is used to infer an unproved universal condition. Mathematical novelty remains qualified by incomplete access to the full 1995 ballistic-annihilation article. No independent scientific audit has been performed.
