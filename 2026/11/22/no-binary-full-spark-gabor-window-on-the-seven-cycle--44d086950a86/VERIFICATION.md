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

# Verification of the binary seven-cycle Gabor obstruction

The attached theorem is established by exact determinant expansion, not by floating-point experiments. Run `python proof/check_exact.py` to generate the 64 normalized sign windows, verify the nine orbit representatives under shift/reflection/global sign, and evaluate every coefficient of each displayed determinant as an integer sum of 5,040 signed terms. The recorded run reports zero for all seven coefficients in all nine cases.

Run `python proof/check_modular.py` for a second finite-field method that constructs the matrix columns directly and performs Gaussian elimination. The nine rank profiles are recorded in `proof/check_modular_output.txt`. Such modular singularity is supportive only; by itself it cannot establish characteristic-zero singularity.

The theorem does not assert that every seven-column selection is singular, does not compute the minimum spark of every window, and does not address phase alphabets other than signs. Independent mathematical audit has not been performed.
