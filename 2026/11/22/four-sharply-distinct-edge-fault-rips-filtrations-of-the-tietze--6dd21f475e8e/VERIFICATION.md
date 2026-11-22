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

# Replaying the complete finite proof

Run `python3 FAULT_VERIFY.py` in the directory containing `FAULT_CERTIFICATE.json`. The verifier uses only Python 3 standard-library modules; `FAULT_CHECKS.txt` contains the successful replay output.

The certificate contains the full edge list, twelve exact graph automorphisms, all four edge orbits, all four sets of radius-two elementary free-face pairs, reduced two-dimensional face sets, spanning trees, and ordered triangular relator eliminations. The same file contains higher-radius collapses for all stages not already full simplices. The verifier reconstructs every graph after recomputing shortest paths, checks the orbit invariants, verifies all collapse pairs on the current face sets, checks spanning-tree connectivity and every nonabelian one-generator triangle cancellation, and corroborates the resulting homology by independent binary boundary ranks.

The integral conclusion follows because these triangle relations provide an ordered integral unimodular boundary minor of maximal rank and kill all non-tree generators of the fundamental group. A simply connected two-complex with free second homology is a wedge of two-spheres. These logical steps are stated in RESULT.md; characteristic-two ranks alone would not justify the claim. No theorem for infinitely many graphs, non-isomorphic edge faults outside these four orbits, or continuous metric graphs is inferred.
