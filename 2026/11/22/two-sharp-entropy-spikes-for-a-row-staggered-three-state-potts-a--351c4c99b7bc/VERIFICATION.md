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

# Mathematical verification

Run `python3 verify_staggered_potts.py` with Python 3 using its standard library only. This reconstructs the three endpoint dual-potential certificates, checks all \(243\) exact rational inequalities, verifies the period-three and period-one witness energies, derives each zero-slack transfer polynomial by integer Newton identities, and independently enumerates all \(531441\) six-column spin assignments at five representative field values. The observed counts are \(6,21,3,98,1\), agreeing with the general formulas for six columns.

The code and proof involve no stochastic approximations. The finite enumeration does not by itself establish the all-size result: the telescoping dual inequality and exact transfer-matrix trace give the infinite family theorem. An earlier equivalent theorem could exist outside the materials compared, and no independent mathematical assessment has been performed.
