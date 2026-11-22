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

# Verification details

On the extracted package path, run `python3 checker.py` with Python 3. The source is standalone, uses only the Python standard library, and returns `VERIFICATION_OK 177256`. The checker explicitly evaluates exact rational beta moments for five parameters, compares two representations of compressed multiplication quadratic forms across positive and negative angular sectors and degrees, tests central rank-two determinant positivity, tail signs, and the exact telescoping identity. The illustrative unweighted two-degree radical calculation is also checked.

These are supporting finite identity checks only. The full-spectrum eigenvalue claim follows from the analytic angular decomposition, the uniform beta moment formulas, the gamma ratio asymptotics and summability, and not from a bounded enumeration. Historical priority is not mathematically certified; one 2021 source on the same ambient space remained inaccessible in full. No independent mathematical validation was performed.
