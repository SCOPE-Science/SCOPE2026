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

Run `python cycle_cutoff3_verify.py` using Python ≥3.10 and SymPy ≥1.10; `cycle_cutoff3_output.txt` records a successful exact run. For each of the four graphs the program enumerates **every** normalized ordered tuple through dimension three, constructs every signed boundary entry and asserts that consecutive boundaries compose to zero. It computes integer Smith normal forms, verifies every nonzero invariant factor equals 1, and independently calculates exact rational ranks. It reconstructs the cutoff-two complex and calculates the rank of its induced second-homology map into cutoff three by augmenting the entire third boundary image with every cutoff-two rational two-cycle. The four computed transition ranks are exactly zero.

The finite arithmetic does not by itself prove any homotopy equivalence. The accompanying mathematical proof separately establishes simple connectivity using explicit two-cell relations and invokes the three-dimensional Hurewicz/Whitehead argument. No fourth or higher nondegenerate cells exist at cutoff three.

Independent external validation has not been performed. The proofs do not apply to general graphs or later cutoffs, and exhaustive external publication-priority verification is not asserted.
