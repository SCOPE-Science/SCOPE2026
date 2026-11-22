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

# Reproduction and scope

Execute `python3 verify_determinant.py` and compare its two deterministic output lines to `determinant_output.txt`. Its 833 exact integer determinants (all grid points \(t=0,\ldots,16\), \(u=0,\ldots,48\)) prove the polynomial identity by the stated bidegree bounds; this is not a floating-point experiment.

Execute `python3 verify_recurrence.py`, save stdout, and compare it to `recurrence_output.txt`. The full rational-function coefficient recurrence is checked for \(5\le n\le80\), including all five maximum-set multiplicities.

Compile `verify_direct.cpp` with `g++ -std=c++17 -O3 verify_direct.cpp -o direct_check`; run `./direct_check` and compare stdout to `direct_output.txt`. Its brute-force enumeration of all \(2^n\) labelled subsets for \(5\le n\le18\) independently checks the local packing definition and every cardinality coefficient. The fourteen direct-census lines must also match the recurrence file's corresponding fourteen lines after its initial PASS line.

The proofs of the infinite-family claims depend on the finite exact determinant identity together with symbolic formal-series extraction, not on extrapolating the finite experiments. Historical-literature novelty and independent audit remain unperformed externally.
