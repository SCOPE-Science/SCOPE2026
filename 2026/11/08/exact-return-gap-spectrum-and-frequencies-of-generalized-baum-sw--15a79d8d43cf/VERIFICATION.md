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

# Reproducibility and limits

Run `python3 verify.py` with no third-party dependencies. The verifier computes generalized Baum–Sweet acceptance independently from the binary representation, enumerates all accepted positions within a finite range, checks the predicted gap for every adjacent pair, and checks the exact shell multiplicities by separately enumerating accepted binary words and evaluating the tiling recurrence. Finite diagnostics do not prove results for all integers; the proof is in RESULT.md. No independent audit has been performed.
