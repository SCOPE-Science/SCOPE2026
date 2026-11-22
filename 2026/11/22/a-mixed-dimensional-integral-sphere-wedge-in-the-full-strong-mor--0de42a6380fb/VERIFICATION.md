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

# Verification instructions and scope
Run `python3 verify_strong_c10.py` from this directory with Python 3 and its standard library. Successful stdout must match `VERIFY_EXPECTED.txt` exactly. The executable builds all 6,480 nonempty simplices from 1,022 nonconstant orientations of ten cyclic edges and, independently, from all ternary words satisfying the face criterion. It checks their equality, constructs 3,238 specified face–coface matches, checks all 31,840 covers and full directed acyclicity, records four critical masks and computes both signed integer coefficients in the Morse boundary from critical dimension five to four.

The checker also computes the unreduced simplicial boundary ranks over \(\mathbb F_2\) in every positive degree and derives reduced Betti ranks. It also reconstructs the pure subcomplex from maximum-cardinality generators, verifies its 6,280 faces and 200 omitted faces, and computes its separate mod-two Betti ranks. These finite calculations cover **all** faces of the specified finite simplicial complex and thus are complete for this object; they do not imply an infinite-family theorem. The homotopy upgrade additionally uses Forman's finite discrete-Morse theorem and the fact that maps \(S^4\to S^4\) are classified by integer degree. An independent mathematical audit has not yet been performed.
