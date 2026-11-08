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

The proof derives the degree distribution directly from the ring multiplication and then uses exact finite-field isotropic-vector formulas and known classifications of nonsingular symmetric bilinear forms. The field-size and dimension reconstruction uses the unique maximum-degree stratum and graph order. The precise hypotheses include finite fields, equicharacteristic, Gorenstein socle dimension one, and nonzero radical square with radical cube zero.

Run `python3 verify.py` using Python 3 with no third-party packages. The program constructs all nonzero nonunit vertices of independently defined multiplication tables and their pairwise zero products. It verifies direct degrees against the theorem in 109 finite cases, and independently counts quadratic isotropic vectors against characteristic-dependent formulas. Observed final line: `VERIFY_OK 109`.

Finite enumeration proves nothing for untested sizes or fields; the universal result rests on the algebraic proof. The program does not establish publication priority or independently certify the stated bilinear-form classification. There has been no independent mathematical audit.
