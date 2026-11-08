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

Run `python verify.py` using a standard Python interpreter. The program directly constructs the derivation action on the quotient polynomial basis; it does not reuse the valuation classification in the construction of the tested matrices. It checks all candidate maps for \(D^2=0\), performs full field-arithmetic row reduction, compares complete rank histograms with the theorem's coefficient formula, and checks the total counts. It exhausts all \(\mathbb F_2\)-linear derivations at truncation lengths \(2\) through \(9\), and the corresponding \(\mathbb F_4\)-linear derivations at lengths \(2\) through \(6\). Its terminal success marker is `VERIFY_OK`. These tests are finite and do not certify the general identity or weak convergence; those follow from the proof.

The \(\mathbb F_4\) arithmetic uses the binary polynomial basis modulo \(u^2+u+1\). Any unsupported field size is rejected explicitly. No external packages are required.
