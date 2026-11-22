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

# Exact finite verification

Run `python3 verify_mobius_two_matching.py` from the same directory and compare standard output with `expected_verification.txt` using a byte-for-byte comparison. The program uses only the Python standard library and deterministic ordering.

It enumerates all masks of the 9, 12, 15 and 18 edge graphs, checks the maximum selected incidence degree at each vertex, and constructs both forward- and reverse-order complete Morse matchings. Each is certified acyclic by a full directed incidence topological sort, not by a sample. The integer Morse incidence matrices are calculated from recursive unit-pivot cancellations with the signed simplicial boundary. Independently, mod-two simplicial boundary elimination checks reduced Betti numbers on the original full complexes. The script asserts exact face totals, cover totals, critical counts, and signed matrix entries.

The audit of mathematical novelty compares different simplicial complexes and graph families; database searches and abstract access cannot exclude an unpublished or unindexed theorem. No computation for larger graphs, equivariant action or infinite parameter range is claimed. Independent mathematical audit has not been performed.
