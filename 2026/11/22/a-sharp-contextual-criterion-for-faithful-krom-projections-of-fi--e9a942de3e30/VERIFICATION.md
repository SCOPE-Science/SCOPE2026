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

# Reproducible verification

Run `python verify.py` with Python 3.9 or later; no third-party packages or datasets are required. Successful execution prints `VERIFY_OK 84168 program/context-family comparisons; sharp examples t=2..6`.

The program independently enumerates every possible one-atom choice for each positive-body source clause and compares simultaneous least-model preservation against the per-rule false-witness condition. It checks all programs and all families of contexts over one and two atoms, all three-atom programs with at most two rules and every possible context family, plus 3,000 reproducible four-atom samples. It also checks the full fact-context criterion, constructs all compatible Krom factors, verifies body-union inclusion and intersection equality, and constructs width-sharp witnesses for widths two through six.

The mathematical theorem is proved in `RESULT.md` for *all* finite atom alphabets and arbitrary families of fact contexts. The finite checks cannot certify infinity or historical novelty. The package does not claim independent external validation.
