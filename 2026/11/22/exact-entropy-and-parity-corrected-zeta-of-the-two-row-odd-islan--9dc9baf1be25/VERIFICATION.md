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

# Reproduction

Run `python3 check.py` in the directory containing the six research files and the checker. The checker uses only the Python standard library and derives the two characteristic polynomials from exact integer matrix products and Newton trace identities; it also uses independent connected-component searches on every two-row column word through length eight.

The printed finite closed-island counts for lengths one through eight are 3, 11, 37, 127, 445, 1559, 5451, 19061. The independently enumerated horizontal-periodic point counts are 4, 14, 40, 158, 514, 1844, 6374, 22446. The run performed 174,760 distinct finite component admissibility decisions, with eight exact transfer-comparison checks, eight exact periodic-count comparisons, and two polynomial identities; all passed.

The finite checks test the state transitions and signed periodic correction only at finite lengths. The full equivalence of the odd-island language with the parity-frontier graph, the Perron asymptotic and the all-period trace difference depend on the proofs in `RESULT.md`. Independent scientific validation has not been performed.
