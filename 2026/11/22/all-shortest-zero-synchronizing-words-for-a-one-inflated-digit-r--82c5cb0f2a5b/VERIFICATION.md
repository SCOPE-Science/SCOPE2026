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

Run `python3 verify.py` with Python 3. The standard-library checker constructs complete low-length representable sets and directly checks every legal zero-reset interval against the formula for 16 parameter pairs. Independently it performs a breadth-first search through subsets of the carry-state set for 16 selected pairs and confirms the shortest lengths. Both methods pass; sample output is included in `verification_output.txt`.

The mathematical proof in `RESULT.md` establishes the claimed generality; finite tests alone cannot do so. No external or independent audit has been performed.
