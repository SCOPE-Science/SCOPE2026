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

The proof specifies two elementary invertible modular transitions, all reachable primitive pairs, complete suffix-row reachability, and both Myhill–Nerode equivalence classifications. The checker verifies direct counts for all binary words through length twelve; for moduli 2–31, it builds reachability and separately minimizes the complete DFAs for the two specified residues. The checker also checks the stated output-distinguishing suffixes. There is no dependence on external data or unbounded numerical enumeration. Finite checks cannot establish all-modulus correctness, which is addressed by the proof in RESULT.md.

Reproduce from the containing directory with `python3 check_distinct_subsequence_mod.py`.
