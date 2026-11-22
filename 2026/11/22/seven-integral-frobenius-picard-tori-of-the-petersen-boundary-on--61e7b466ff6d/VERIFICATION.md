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

# Mathematical verification

The proof reduces the nonstandard integral representation calculation to exact finite matrices in `verification/verify.py` and `verification/certificates.json`. The checker reconstructs all graph vertices and edges, a nine-edge spanning tree, and the six integral fundamental cycles. For each of seven representative conjugacy classes it checks an explicit 6-by-6 integral matrix has determinant ±1 and satisfies the exact intertwining equation. It checks graph actions for all 120 permutations of five labels, the complete seven-class count, and selected determinant/point-order identities. The actual executed output is embedded in `verification/verification_output.txt`, ending `PETERSEN_SEVEN_INTEGRAL_TORUS_TYPES_OK`. The script uses only Python's standard library.

These checks certify the finite integer algebra; the infinite-field family is established by the classical geometric graph identification, normalization-gluing exact sequence, finite-field descent classification, and explicit identification of the signed cyclic blocks with norm-one tori. The checker does not prove those cited general theorems and finite point samples are not used as proofs of the all-field statements. Literature priority is provisional; independent mathematical audit has not been performed.
