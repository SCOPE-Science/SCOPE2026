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

# Verification procedure and limits

The certificate `verify_sphere_census.py` was executed with Python 3 in the same directory as the completed research materials. The recorded terminal output is in `verification_output.txt`. Its only dependencies are Python standard-library modules (`collections`, `functools`, `hashlib`). For each \(1\le n\le6\), it carries out two full enumerations of the monoid, comparing exact sets; it then checks two independent implementations of the ultrametric level on every canonical element. The loop implements the published unique-canonical-word theorem and exhausts all \(85823\) words across the six cases. It prints exact sphere counts and reproducibility SHA-256 digests of sorted canonical words. The largest single case has \(83973\) elements. All checks passed and the complete printed output was compared with the table in `RESULT.md`.

The canonical uniqueness theorem itself is cited from the mathematical literature and is **not** re-established by the code. Agreement with known total monoid orders is a consistency check, not the reason enumeration is exhaustive. The computation does **not** prove an all-size symmetry or supply any result for seven or more generators. Independent external audit has not been performed.
