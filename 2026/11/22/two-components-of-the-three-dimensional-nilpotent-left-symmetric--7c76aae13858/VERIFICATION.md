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

# Reproduction of mathematical checks

Run `python3 checks/verify.py` using Python 3. No third-party packages, external data, or network access are needed. The program forms both multiplication tensors and checks the four LSDA axioms on all 27 basis triples. It exhausts every eight-parameter candidate for the intrinsic fixed-flag non-two-step stratum over the fields of orders 2 and 3 (with field arithmetic valid for these primes); predicted and computed admissibility agree in every case, with 28 and 468 admissible tables respectively. It also checks the explicit degeneration and evaluates the closed-form stratified labelled census for field orders 2, 3, 4 and 5. Values at 4 and 5 are formula evaluations, not an exhaustive enumeration of all tables.

Expected terminal output: `LSDA_TWO_COMPONENT_GEOMETRY_CHECKS_OK`. Exact full-field geometry is established by the normal-form and proper-incidence proof in `RESULT.md`; exhaustive small-prime experiments cannot certify all field sizes, irreducibility, or arbitrary characteristic.

No independent mathematical audit has been conducted.
