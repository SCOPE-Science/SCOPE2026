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
# Reproducible finite and symbolic verification

Run `python3 verify_full_aut.py` and `python3 verify_signed_trace.py` in the same directory as this document, using Python 3.9 or later. Both are standalone and depend only on the standard library. Output files `verify_full_aut_output.txt` and `verify_signed_trace_output.txt` contain the expected exact stdout of separate successful runs. A nonzero exit, failed assertion or an output discrepancy invalidates the reported finite certificate.

The first program constructs the canonical 18-vertex LCF graph; exhaustively enumerates 2,597 independent simplices; matches 1,293 pairs; checks all 11,430 nonempty face-poset covering relations for acyclicity; recursively enumerates every graph automorphism, finding 216 and checking full composition/inverses; determines 13 conjugacy classes; and computes the reduced Lefschetz trace of every element with the quotient-cycle independence-polynomial formula. The class trace table includes exact representative permutations. Its final marker is `PAPPUS_FULL_AUT_PASS`.

The second program independently enumerates independent simplices recursively; computes all mod-two simplicial boundary ranks and the reduced Betti vector; independently tests graph-automorphism validity for 13 fixed representatives; and computes signed simplicial chain traces by actual oriented-face permutations, not via the quotient formula. Its final marker is `DIRECT_SIGNED_LEFSCHETZ_CHECK_PASS`.

The proof of the finite group exhaustiveness depends on the backtracking considering every admissible candidate partial bijection, and the proof of the homotopy concentration depends on every face-poset covering relation being oriented and checked acyclic. The identification of the rational character additionally uses the mathematically proved Lefschetz fixed-chain identity, and the zero fixed-subspace/two-constituent conclusions use ordinary character orthogonality. Mod-two Betti numbers by themselves do **not** certify rational representation structure, and mere finite experiments would not prove an infinite-family result; none is claimed.

The nonequivariant Pappus sphere wedge and one order-three subgroup character were already published, and are used as background and consistency checks rather than claimed as original. The present verification does not identify integral representation lattices, irreducible constituent degrees or equivariant homotopy type. External independent audit and global publication-priority certification have not been performed.
