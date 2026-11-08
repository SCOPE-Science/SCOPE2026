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

The characteristic-uniform theorem is proved algebraically in `RESULT.md` using the factorization of \(s^qt-st^q\), the rational-point ideal in \(\mathbb P^3\), and the rank-four alternating-form argument. No finite experiment substitutes for that proof.

Run `python3 verify_binary_example.py` and `python3 verify_ternary_example.py` with Python 3. These scripts use only the standard library. They verify the rational-point and quadratic-extension counts and line incidences for the published examples over \(\mathbb F_2\) and \(\mathbb F_3\), respectively. They do not test geometric smoothness or prove the theorem for all prime powers.

The proofs of the initial source examples' smoothness and existence are external to these scripts. No independent mathematical audit has been performed.
