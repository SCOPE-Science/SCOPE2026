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

# Verification notes

The mathematical proof is in `RESULT.md`. The standalone Python 3 checker `incidence_noncounital_checker.py` builds the bimodule centralizer equations in the incidence tensor basis, performs modular Gaussian elimination, and checks the structural formula over \(\mathbb F_2\) and \(\mathbb F_3\) for each topologically labeled transitive finite poset of sizes 1 through 5. This comprises 814 field-poset cases. The computed dimensions are, in every case, the counts of bounded undirected comparability components. It also checks substitution of all explicit component basis vectors and injectivity of their tensor images.

Reproduction: run `python3 incidence_noncounital_checker.py` from the same directory. Expected output starts `INCIDENCE_COPRODUCT_CLASSIFICATION_OK` and records 814 checks.

Finite checks do not verify the theorem for all finite posets or arbitrary fields; the symbolic coefficient argument proves that claim. No independent mathematical audit or historical-priority certification has been carried out. The literal-scope comparison with an older quiver theorem is a scientific literature comparison rather than an external validation.
