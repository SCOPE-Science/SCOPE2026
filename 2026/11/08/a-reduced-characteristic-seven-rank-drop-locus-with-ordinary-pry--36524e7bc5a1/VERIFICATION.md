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

# Reproducible verification

Install Python 3 and SymPy, then in this package run `python3 verify_cartier.py` and `python3 verify_quotient.py`. Both scripts were executed successfully from the archived source contents. The expected messages are `TRIGONAL_GENUS4_CARTIER_PASS`, `GENUS2_QUOTIENT_HASSE_PASS`, and `GF49_QUOTIENT_POINTCHECK_PASS`.

`verify_cartier.py` exactly reconstructs the \(4\times4\) Cartier coefficient blocks over \(\mathbb F_7\), their constant eigenbasis, the polynomial discriminant, the determinant and radical-root criteria. `verify_quotient.py` independently extracts the \(2\times2\) genus-two Hasse--Witt matrix from the sextic quotient and performs a finite point-count check over \(\mathbb F_{49}\). The output point counts are \(22\) for \(t=3i\) (\(i^2=-1\)) and \(37\) for \(t=1\); these counts support the formal calculation but are not a proof over every algebraic parameter. The proof of semilinear stable ranks, the quotient and Prym geometry, and the moduli-point identification is in `RESULT.md`.

No independent external mathematical audit has been performed. Potential older normal-form literature could cover a statement equivalent to the claim, notwithstanding the documented comparisons.
