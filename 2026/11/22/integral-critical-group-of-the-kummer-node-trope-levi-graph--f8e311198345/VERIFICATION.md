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

Execute `python3 verify_kummer.py` in the directory containing the file. Its only requirement is Python 3's standard library. The expected completion marker is `KUMMER_BIPLANE_CRITICAL_GROUP_VERIFIED_OK`.

The exact verifier (a) rebuilds the sixteen-by-sixteen grid-incidence matrix without stored data, (b) proves the biplane identity through all entries, (c) constructs the reduced integral graph Laplacian and its exact determinant by Bareiss elimination, and (d) diagonalizes over modular local rings using invertible operations. It checks two precisions at primes two and three and repeats the calculation with sinks at four distinct vertices; a check at prime five provides an additional control.

The symbolic spectrum follows from the biplane identity in the proof. The modular procedures certify finite matrices, not an unbounded family of graphs. Their correctness rests on the explicitly described matrix and invertible row and column operations over each indicated ring. Independent mathematical or external review is not claimed.
