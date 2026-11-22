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

# Reproduction and verification

Run `python3 verify_pentagonal.py` from the package after extraction (standard-library Python 3). The measured result was `VERIFY_OK 10829 assertions`; it includes five candidate distributions, every triple support type, five strict four-coordinate exchange certificates, exact rational surrogate algebra, seeded simplex/face checks, and two simulated long finite iid index sequences. The proof of the almost-sure claim is the even/odd strong law applied to adjacent transition costs, not those simulations. The global maximum relies on the rigorous positive exchange coefficient, complete support enumeration, and a strictly concave scalar optimization, not on numerical search. The references and scope limitations are in `RESULT.md`.
