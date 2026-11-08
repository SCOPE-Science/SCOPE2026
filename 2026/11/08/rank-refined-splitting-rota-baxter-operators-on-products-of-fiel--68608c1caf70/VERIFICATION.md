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

The included `verify.py` uses only the Python standard library. It independently checks the operator identity at every basis pair, the splitting polynomial identity, and the resulting rank histogram of all admissible small matrices over \(\mathbb F_2\) and \(\mathbb F_3\) through dimension four. It also independently enumerates all rooted labeled trees using Prüfer codes through five non-root vertices and checks their valid two-color ranks.

Run: `python3 verify.py`. The saved-package replay completed with the terminal line `VERIFY_OK`. These are finite checks; the all-dimensional formula and Gaussian limit follow from the argument in `RESULT.md`. An independent mathematical audit has not been performed.
