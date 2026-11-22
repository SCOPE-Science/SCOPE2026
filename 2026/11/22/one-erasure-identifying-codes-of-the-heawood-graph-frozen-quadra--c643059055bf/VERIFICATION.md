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

# Verification

- The Python program performs a complete enumeration of all \(2^{14}=16384\) subsets of the fourteen labelled graph vertices and tests all fourteen neighborhood conditions and ninety-one pairwise symmetric-difference conditions for each.
- The C++ program independently constructs the fourteen-cycle-plus-chords presentation and tests resilience by removing every selected detector in turn, recomputing all fourteen ordinary identifying signatures.
- Both programs establish the full code polynomial \(98z^{10}+224z^{11}+91z^{12}+14z^{13}+z^{14}\), verify the two geometric optimum types, construct all optimal exchange adjacencies and reproduce component and distance results.
- The Python program additionally scans all \(2002\) five-vertex omissions to certify the sharp bound, and checks equality of every optimum mask against the two complete geometric catalogues.
- The exact BFS calculation covers all 98 starting code configurations and all 98 possible target configurations, not a sample of representatives.
- Code paths are `code/check_fano.py` and `code/check_hamiltonian.cpp`; corresponding reference outputs are in `certificates/`.
- These are finite computational certificates for one labelled graph. A formal proof assistant and independent scholarly audit were not used; no conclusion about other graph orders is asserted.
