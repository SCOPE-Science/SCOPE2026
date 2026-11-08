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

# Reproducibility

Run `python3 verify.py` in this directory. No dependencies beyond the Python standard library are required. The program enumerates every independent face and every face-poset covering, verifies a deterministic acyclic discrete-Morse matching, reconstructs the integer attaching matrix via gradient paths, checks a unit maximal-rank minor, independently computes original mod-two boundary ranks, and checks all 84 natural graph automorphisms and their signed fixed-face Lefschetz traces.

The complete expected output is stored as `verification_output.txt`. The proof of torsion-freeness and the integral homotopy equivalence depends on the exact integer Morse differential and unit minor, not on the mod-two ranks. The finite computation does not imply any claim for other cycle lengths or color numbers. The character computation uses ordinary rational representation theory and does not claim an integral equivariant splitting.
