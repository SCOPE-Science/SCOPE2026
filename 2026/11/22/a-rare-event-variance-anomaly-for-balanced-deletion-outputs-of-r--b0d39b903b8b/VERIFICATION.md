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

# Reproduction

Use Python 3 with only the standard library. From the directory containing the files, run `python3 verify.py`. The checker generates all Dyck words of semilength one through ten and directly enumerates the **set** of distinct Dyck outputs from all one-open/one-close deletion-position choices; it independently applies the structural per-word formula and checks agreement. It also aggregates component-size interactions and checks the first two exact integer moment generating functions, including additional coefficients through semilength thirty-five. Successful execution prints `VERIFY_OK`.

The proof itself establishes the infinite asymptotics using exact generating-function identities, coefficient singularities, Narayana statistics and a giant-component limit; the finite program does not prove any limiting claim. No independent external audit or implementation certification has been performed.
