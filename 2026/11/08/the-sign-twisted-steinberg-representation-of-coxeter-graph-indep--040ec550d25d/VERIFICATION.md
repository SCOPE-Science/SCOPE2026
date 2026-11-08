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

# Verification

The two Python programs use only the standard library. `python3 verify_coxeter_st.py --write-classes` checks all 196,008 nonempty independent simplices, the full 1,319,724-incidence acyclic Morse DAG, all 336 automorphisms and nine exact conjugacy classes. It creates `character_classes.json`. `python3 check_coxeter_signed.py` independently computes the reduced Lefschetz number from the orientation signs of all fixed simplices for each of the nine class representatives. Both recorded outputs are included and were reproduced before packaging.

The Morse certificate establishes the seven-sphere homotopy type for the explicitly constructed graph. The quotient-cycle signed trace is an exact alternating-chain identity. The Sylow-seven construction and equality of all 336 traces identify the rational module, without requiring a numerical irreducible-character table. No other graph or parameter family is certified. This is reproducibility evidence and not independent mathematical review.
