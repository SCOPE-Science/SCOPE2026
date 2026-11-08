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
# Reproducibility and verification

The complete proof is in `RESULT.md`; the executable finite check is `verify.py` with recorded output `verify_output.txt`. Run `python3 verify.py` in a standard Python 3 environment (standard library only). This enumerates vertex subsets using the actual adjacency relation of complete split graphs and independently tests for forbidden cliques.

Across 30 parameter triples in the stated domain, the executable constructs modular boundary maps and checks all reduced homology ranks over 2 and 3 against the predicted integral free ranks. For 137 part-permutation choices it constructs the signed chain Lefschetz trace and checks the exterior-power character after the alternating-degree correction. The maximum number of nonempty faces encountered is 496. The expected final line is `ALL_VERIFY_OK`.

These computations establish all assertions only for the enumerated finite test cases; they cannot prove any statement for all parameters or exclude torsion outside those cases. The infinite-family proof depends instead on the fully explicit equivariant contractible subcomplex and its sphere-wedge quotient. Neither the code nor these computations constitute independent mathematical validation.
