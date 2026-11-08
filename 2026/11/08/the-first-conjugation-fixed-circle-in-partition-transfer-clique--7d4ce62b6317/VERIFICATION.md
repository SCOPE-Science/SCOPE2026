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

# Computational verification

Run `python3 verify.py` from a directory containing only the included standalone program and its output. The program uses only Python's standard library. It regenerates all partitions of every integer from 1 through 18, all distinct unit-transfer edges, and transposed partitions. It checks transposition preserves every edge and directly enumerates all invariant original cliques. It separately builds eligible orbit barycenters and orbit-compatibility cliques, asserting exact equality of the two finite face sets.

At every elementary collapse, the removed face is checked to lie in exactly one strict coface in the current simplicial complex; hence each deletion is a genuine homotopy-preserving elementary collapse. No faces of dimension at least two remain. Graph component and cycle-rank checks are then exact. The full verified range has no residual cycle for parameters 1–17, and at 18 has 15 orbit vertices, 18 edges, four triangles, four legal collapse pairs, two components, and a unique graph cycle. The original graph complex has Euler characteristic 311 at 18, consistent with the earlier published value.

The actual execution record is `verification_output.txt`; its concluding line is `PARTITION_CONJUGATION_FIRST_CIRCLE_EXACT_CHECKS_OK`. This is a finite exhaustive verification for the precise claimed cutoff, not a sample-based infinite theorem, and it does not supply an independent scientific review.
