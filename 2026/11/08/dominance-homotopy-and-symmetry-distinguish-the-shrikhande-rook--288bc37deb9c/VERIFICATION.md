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

# Reproduction and limitations

Using Python 3 standard library, run `python3 verify.py` followed by `python3 verify_orbits.py` beside `certificate.json`. The first program exhaustively checks all sixteen-bit subsets of each graph against two equivalent dominance predicates; builds two distinct acyclic Morse matchings per graph; enumerates all cover relations and proves the directed Hasse graph acyclic by a full topological sort; and calculates the Shrikhande group and complete character. The second independently calculates all character values by a cycle-orbit inclusion sum and compares against the first method.

The recorded successful output is `verification_output.txt`. The output and code are computational witnesses; the homotopy equivalence uses Forman's theorem, and the character result uses the simplicial Lefschetz formula. The rook homotopy type beyond integral homology is not settled; no independent mathematical audit has been performed.
