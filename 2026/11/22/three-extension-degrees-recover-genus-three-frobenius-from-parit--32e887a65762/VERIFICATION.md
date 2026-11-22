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

# Verification record

The exact standalone source `verify_sp6_theta.cpp` generates all 1,451,520 six-dimensional symplectic matrices over the binary field using eight explicit transvections. A matrix is represented by six six-bit columns; uniqueness is enforced by an exact integer hash set. The transformation of quadratic refinements is derived from the symplectic bilinear form and checked to preserve parity for every group element and every one of the 64 refinement labels.

The script `verify_theta_certificate.py` recompiles the C++ source, checks that exactly 30 joint odd/even cycle types occur, checks each 30-row CSV record against the freshly computed output, verifies that the element multiplicities sum to 1,451,520, and checks prefix signatures: 18 for extension one, 24 through extension two, 30 through extension three. The separate source `verify_hyperelliptic_theta.py` builds unordered branch pairs and unordered 4+4 partitions for all 22 cycle types of the eight branch points, and verifies the (7,1)/(5,3) collision and its resolution in degree three. To replay: `python3 verify_theta_certificate.py`, requiring Python 3 and a C++17 compiler.

The external cross-check for the number of group conjugacy classes and their sizes is the ATLAS online \(\operatorname{Sp}_6(2)\) table, not an assertion inferred from the local program. The existence argument for both sharpness families uses standard irreducible-polynomial existence over finite fields, not limited testing. These checks do not prove that every abstract class is realized by a genus-three curve over a fixed base field. Independent audit remains unperformed.
