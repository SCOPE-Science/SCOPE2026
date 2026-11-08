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

# Verification procedure
Run `python3 verify.py` in a clean directory containing the supplied file. The script checks 2730 parameter pairs and exact orbit partitions, followed by a separately implemented rooted nonbacktracking unfolding comparison across all refinement rounds for 160 parameter pairs. It ends with `VERIFY_OK`. The packaged `verification_output.txt` records the actual execution. The symbolic proof in RESULT.md establishes the unrestricted mathematical statement; the script checks only the explicitly stated finite ranges. No independent audit has been carried out.
