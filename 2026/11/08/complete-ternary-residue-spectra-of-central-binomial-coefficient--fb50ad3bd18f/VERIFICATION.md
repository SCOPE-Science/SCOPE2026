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
# Reproducibility and limits
Run `python3 artifacts/verify.py` using Python 3 with no third-party dependencies. It checks the digit witnesses for all coprime-to-three moduli from one to forty and offsets from the negative modulus to the positive modulus, and validates small central binomial residues against exact arithmetic. Observed output: `VERIFY_OK witness_classes=2761 moduli=1..40_coprime_to_3 offsets=-b..b direct_central=0..99`.

Finite checks do not certify unbounded index or modulus claims. Those claims follow from Lucas' theorem, Kummer's carry characterization, and the constructive multiplicative-order proof in `RESULT.md`. Independent audit remains unperformed.
