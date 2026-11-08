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

# Reproducibility and limits

Run `python verify.py` using Python 3.10 or newer and its standard library. The script requires no external datasets, network access, or third-party packages. It reconstructs complete split graphs independently from their edge rule, enumerates all vertex subsets for moderate parameters, searches graph paths with depth-first recursion rather than assuming the theorem's longest-path formula, verifies the star-relative exceptional facets and their boundaries, and calculates mod-two homology by bitset Gaussian elimination.

A separate signed permutation test computes the alternating reduced chain trace directly from fixed oriented faces and compares it with the stated cycle-polynomial formula, including signed traces of critical relative facets for automorphisms fixing a chosen leaf. Finally, explicit full-group averages test the zero-invariant assertion on several cases.

The recorded output `verify_output.txt` was obtained by executing the embedded script directly. It reports 41 topology triples, 7,591 vertex-subset tests, 880 signed automorphism checks, 310 leaf-stabilizer checks, and five full-invariant checks, ending in `ALL_VERIFY_OK`.

**Limits.** Such finite computations do not prove the all-parameter homotopy equivalence, integral decomposition, or character formula. Those follow from the mathematical steps in `RESULT.md`. The script calculates reduced Betti numbers mod two and permutation traces over the integers; it does not compute all Smith normal forms. Integral torsion freeness is supplied by the explicit quotient and relative-chain proof, not by these mod-two tests. The motivating primary source's full manuscript was not accessible for comprehensive overlap inspection, so independent originality review remains necessary.
