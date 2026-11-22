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

# Computational verification

Run `python3 verify.py` with Python 3. The program independently implements the simultaneous rule and prints `VERIFY_OK 67728` if all tests succeed. It checks all 66,066 binary relations on 1–4 vertices, 62 directed-path examples through 64 vertices, and 1,600 reproducible pseudorandom examples on 5–12 vertices. It also checks the initial-target invariant, the two-round undirected graph characterization, and predicted fixed-point stages. Finite verification does not establish an all-size theorem; the proof is in RESULT.md.

No independently performed mathematical or historical-priority audit is claimed.
