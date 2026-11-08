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

The complete argument is the uniform geometric and integral relative-homology proof in `RESULT.md`. The standalone `verify.py` uses only the Python 3 standard library and checks the face enumeration, signed Lefschetz characters and Euler characteristics in all instances from 3 through 6 columns. Its actual console output is embedded as `verification_output.txt`; both are portable artifacts in this record.

The finite checks independently cover 12, 48, 240, and 1,440 elements of the respective full graph automorphism groups, for 1,740 checked group-element actions in total. They do not establish the general \(n\)-case or certify independent validation. The stated integral lattice depends on the explicit exact sequence with the common oriented boundary class, not on modular rank guesses or computer algebra.
