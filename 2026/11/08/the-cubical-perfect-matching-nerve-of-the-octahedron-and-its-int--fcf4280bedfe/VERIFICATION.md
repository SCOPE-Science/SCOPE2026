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

# Reproducibility and scope

Execute `python3 verify_octahedral_perfect.py` using Python 3 with no additional libraries. The artifact `verification_octahedral_perfect.txt` is the stdout recorded from a successful run of that exact code. All graph edges, perfect matchings, perfect-extendible faces, automorphisms and signed character values are derived from definitions rather than copied from a table.

The code verifies 12 graph edges, 8 perfect matchings by two methods, 12/24/8 nonempty perfect-complex simplices by dimension, 12/30/8 ordinary-complex simplices, the six unextendible 2-edge matchings, the 12 nerve edges and absence of triple intersections. It checks 48 distinct induced cube automorphisms, ten rational-character classes, central inversion traces and reversing stabilizers for all cube edges. The finite verification supports the combinatorial premises, while the mathematical proof of the equivariant nerve equivalence and relative exact sequence is in `RESULT.md`.

The integral short exact sequence is not asserted to split equivariantly; the Specht-module identification is rational. No independent audit has been performed.
