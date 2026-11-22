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

# Verification and its limits

Run `python3 verify_bks_contacts.py` using a Python 3 standard-library installation. It constructs both finite fields as polynomial quotients, computes addition/multiplication/inversion exactly, tests all finite line coordinates, and compares every computed bitangent to its normalized binary-quadratic square. The test covers the six selected parameters over \(\mathbb F_9\) and \(\mathbb F_{81}\), verifying the complete 28-line geometric total in the latter field. Success prints `BKS_CONTACT_FROBENIUS_CLASSIFICATION_PASS`.

For each \(\mathbb F_9\) parameter, the geometric smoothness of the quartic is already proved in the primary cited source for \(\lambda\ne\pm1\). The universal count of 28 geometric bitangents is the classical odd-theta count in characteristic different from 2. The exact finite computations classify all 52 contact supports only after these mathematical premises are established. The verifier makes no claim about unexamined finite fields, infinite parameter families, independent validation, or historical uniqueness.
