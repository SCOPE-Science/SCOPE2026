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
# Finite and symbolic verification

The complete mathematical argument is given in `RESULT.md`. In the standalone script `verify.py`, `make_instance` generates the exact graph edges and its forbidden triangles without using the proposed simplicial cover. `brute_faces` independently enumerates all triangle-free vertex subsets; `faces_by_size` enumerates all subsets of the decomposition's simplices. Equality is tested for every face in nine examples.

Augmented mod-two simplicial chain boundaries are reduced by exact bitset elimination in each dimension, so the output computes reduced Betti numbers, including degree zero. For each example the only permitted nonzero reduced Betti number is \(\beta_3=(p-1)(q-1)\). `primitive_incidence_test` separately constructs a spanning-tree submatrix of the integer attaching map with columns \(e_i-f_j\) and checks a unit determinant by integer Bareiss elimination. The tested cases include \((p,q)=(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3)\), with both minimal and unmatched shore sizes.

To reproduce, run `python3 verify.py` from the extracted file directory, using Python 3 and no third-party packages. The recorded exact output appears in `verification_output.txt` and ends with `TWO_MATCHING_TRIANGLE_AVOIDANCE_PASS 9 cases 3853 faces`. These are finite independent corroborations and do not constitute exhaustive computation over unbounded parameters. The universal integral homotopy assertion is proven by the symbolic simplicial decomposition, exact relative homology, unimodular spanning-tree minor, and Hurewicz/Whitehead arguments.
