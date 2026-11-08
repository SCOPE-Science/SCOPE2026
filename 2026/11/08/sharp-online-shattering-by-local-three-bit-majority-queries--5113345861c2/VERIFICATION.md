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

The independently executable `verify_majority.py` uses only the Python standard library. Run `python3 verify_majority.py` from the package root. It checks the complete recursive mistake-tree certificate, all terminal witness assignments, and the mixed-witness invariant for every order \(4\le n\le11\). A separate exact minimax search over distinct truth tables establishes the dimensions for \(1\le n\le8\); the script asserts that depths one greater cannot be shattered in each finite case. Its recorded output is `verification_output.txt`.

The theorem for all ambient orders relies on the full inductive proof in RESULT.md. Neither finite checking nor a successful runtime log is claimed to certify infinitely many cases. Independent audit has not been performed.
