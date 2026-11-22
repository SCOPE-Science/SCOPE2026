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

Run `python3 verify.py` using Python 3 standard library only. Successful execution prints exactly `MATCHED_VERTEX_K3N_EXACT_PASS 54381`.

The checker independently recursively generates all matchings, sums direct Walsh characters across all frequencies through seven right-shore vertices, and compares both the Krawtchouk and cubic formulas. It checks every frequency-weight class through 160 right vertices; the exact Parseval identity at 11 sizes; the integer-divisor enumeration leading to the 43-column exception; and exact nullity, rank, parity and spectral extrema at that size.

The independently implemented matching recursion and class polynomial computations are finite computations. They do not certify the infinite theorem, whose proof instead rests on the combinatorial transform identity, the global sign symmetry, and the complete integer divisibility case analysis in RESULT.md. A separate independent audit has not been performed.
