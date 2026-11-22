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

# Reproducible finite verification

Execute `python3 hermitian_orbits.py` to construct the \(\mathbb F_4\)-linear normalized Hermitian solution space for each rational projective class, test all 1,023 nonzero vectors, divide by the three scalar representatives, and decompose Frobenius on exactly 165 isotropic classes. Its complete output contains the thirteen codes, their matrix-order bounds, each cycle multiset, and the irreducible field polynomial. These are exact enumerations, not probabilistic samples.

Compile and execute `cc -O3 -std=c11 verify_orbits.c -o verify_orbits && ./verify_orbits` to re-enumerate the thirteen disjoint congruence orbits, with their sizes adding to 9,999,360. Compile `cc -O3 -std=c11 verify_full.c -o verify_full && ./verify_full` for a second enumeration of the rational Eckardt-point spectrum across all 9,999,360 invertible binary matrices; it obtains the five ground-field counts \(0:4221952,1:4166400,3:1388800,7:208320,15:13888\).

Execute `python3 verify_small_fields.py` in the same directory to check each class directly against the tangent-quadratic cone condition over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), independently of the semilinear isotropic-point test. These three-field checks are supporting regression checks; the full kernel and all-cycle computation is the complete finite certificate.

The irreducibility of each used binary field polynomial is tested by the standard Frobenius/GCD criterion. The finite-field vector-space kernel is represented by bit matrices and its rank is checked exactly. No assertion of independent expert audit is made.
