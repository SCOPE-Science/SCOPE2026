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

Run `python3 check_hypergraph_xor.py` from this directory. The script requires Python 3.10 or newer and uses the standard library only. It constructs each graph from all three-element subsets, applies the open-neighbor XOR rule by integer bitset parity, and independently computes ranks and iterate matrices. The captured output is `check_output.txt` and ends in `ALL_CHECKS_PASS`.

The matrix checks cover the full orders from 4 through 16, including all four residues and checks of the polynomial update identities and Jordan rank predictions. Exhaustive trajectory enumeration covers 256 states at order 4 and 32,768 states at order 5, checking first entry times and primitive periods. Additional direct trajectory tests use 256 deterministic random states for each order 6 through 12, including all four residue classes.

Finite checks cannot prove an all-order or all-field result. The proof of the full-rank incidence property, the point Gram identity, idempotence, iterate ranks, Fitting decomposition and orbit/basin formulas is written in RESULT.md and is uniform over all finite fields of characteristic two. No independent external audit or certification was conducted.
