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

Run `python3 artifacts/verify_reaching.py` from the containing directory. It uses only the Python standard library. The accompanying `artifacts/verification_output.txt` records the actual result of this command on the embedded code and reads `VERIFY_OK`.

The script independently performs exact breadth-first search of every reachable image with at most three missing states for \(4\le n\le18\). For each omitted triple, it compares the distance formula, constructs a minimal three-merge witness and replays its transformations. It tests every predicted histogram. Separately, for \(4\le n\le95\), it checks every transition on missing sets of size at most three that stays within that domain, verifying the claimed local potential inequality.

These computations are finite tests; the mathematical proof in `RESULT.md`, especially the universal one-step potential inequality and constructive witnesses, supplies the all-parameter claim. No external verification, independent mathematical audit or novelty certification is claimed.
