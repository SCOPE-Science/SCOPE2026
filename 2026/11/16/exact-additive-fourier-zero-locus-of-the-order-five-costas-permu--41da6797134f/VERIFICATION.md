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

The complete claim is a finite cyclotomic-zero census for all 40 Costas permutations of order five in the 3125-element additive group. The necessary calculation is integer-only: count, for each character, the frequencies of its five possible exponents modulo five. The fifth cyclotomic polynomial proves that exact vanishing is equivalent to all five counts being equal.

`check_integer.py` was run and returned `COSTAS5_PROJECTIVE_CYCLOTOMIC_PASS 40 157 16 320 2805 2500 625`, together with the four exceptional representatives and the Hamming-weight distribution. It filters all 120 permutations and verifies the normalization and zero test for all 3125 characters.

`check_independent.cpp` was compiled as C++17 and executed, returning `COSTAS5_INDEPENDENT_PASS 40 16 125 12`. It generates Costas permutations by a different, incremental backtracking method, enumerates all full-group characters and recomputes the finite-orbit results.

`certificate.json` holds the complete 157-by-two residue profile table. Every class not marked zero has an explicitly unequal pair of integer counts in that table, making the finite nonvanishing check exhaustive and inspectable. The rank conclusion uses only Fourier diagonalization; no floating-point rank threshold is involved.

The computation does not address orders other than five or establish priority against unpublished and unindexed sources.
