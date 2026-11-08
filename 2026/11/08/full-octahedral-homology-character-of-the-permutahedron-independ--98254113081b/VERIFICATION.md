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

Execute `python3 verification/verify_character.py` (Python 3, standard library only). It exhaustively reconstructs graph edges by squared distance, independent faces, 18,536 disjoint augmented matching pairs, all 219,240 Hasse edges, and a complete directed acyclicity check. It separately enumerates all graph automorphisms by backtracking and confirms they equal the 48 signed coordinate permutations. The program then computes the full rational character twice, by signed fixed simplex traces and by a quotient orbit-conflict graph independence polynomial, and checks the compact closed formula on all 48 symmetries. The exact recorded output is `verification/verify_character.out`.

Acyclic matching proves the claimed nonequivariant homology concentration integrally. Rational character is deduced using signed reduced Lefschetz; the program's finite checks are exhaustive for the stated fixed 24-vertex graph, not extrapolations. An integral equivariant lattice identification and equivariant homotopy equivalence have not been checked or claimed.
