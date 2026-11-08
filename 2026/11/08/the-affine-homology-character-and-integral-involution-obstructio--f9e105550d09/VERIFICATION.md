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

Execute `python3 checks/check.py` from the extracted package root. It uses only Python 3 standard-library modules and reconstructs the clique complex without a downloaded graph table. Its output must match `checks/check-output.txt` byte-for-byte. The important exact certificates are the 52-by-52 minor of determinant +1 (with displayed tree rows and columns in RESULT.md), the backtracking count 136 for the full automorphism group, all 136 signed simplicial trace checks, and the rank-eight involution calculation over the field of two elements.

The determinant is computed with fraction-free Bareiss elimination; divisibility is asserted at each step. The group enumeration checks both adjacency and nonadjacency and does not assume the 136 affine maps are the entire group. The involution calculation uses mod-two inversion of the specified unimodular minor to construct the full top-homology cycle lattice basis modulo two; it is not a numerical guess or a rational approximation. This is an exact finite proof for the specified 17-vertex complex, not an assertion about all Paley graphs. No external audit or validation is claimed.
