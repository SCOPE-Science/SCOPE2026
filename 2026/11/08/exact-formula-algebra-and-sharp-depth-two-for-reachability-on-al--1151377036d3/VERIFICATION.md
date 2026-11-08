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

# Reproduction and limits

Run `python checker.py` with Python 3 (standard library only). The successful run prints `ALEXANDROV_STAR_GAMMA_ALGEBRA_OK`, then `5456 PATH_PAIRS` and the profile-coordinate table. Independently programmed comparability-component and up-down reachability algorithms are compared against the explicit root/leaf identity for every pair of subsets on all rooted stars with one through five leaves. The checker also enumerates all pointed atomic-color profiles for the listed small variable and leaf counts, tests depth-two formula indicators, and checks the depth-one separating valuations through four leaves. The mathematical proof in `RESULT.md` handles unrestricted finite parameters; no finite experiment is claimed to verify an infinite family exhaustively.

Formal proof-assistant checking and independent mathematical auditing have not been performed. Historical originality is assessed only against the inspected primary literature and research records.
