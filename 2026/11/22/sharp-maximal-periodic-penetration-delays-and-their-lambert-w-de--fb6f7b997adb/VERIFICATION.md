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

## Reproducibility

Run `python3 checks/verify.py` with Python 3 and no external modules. The program independently tests all admissible words through moduli and maximum lengths (2,15), (3,14), (4,13), (5,12), (6,11). It exhaustively searches their least valid cyclic completion period, compares the precise maximum-delay characterization, verifies 301 coefficient identities for each of five moduli and checks two high-precision expressions for the long-word proportion.

The observed finite cases cover 10,260 words; the all-length generating recurrence and the growing-modulus limit are proved analytically in RESULT.md. Finite checks alone would not certify either statement. The analytic comparison with other literature is subject to priority uncertainty, including unindexed specialized studies. No independent mathematical audit has been performed.
