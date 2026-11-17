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

The exact formula, bound, multiplicity, and asymptotic are proved symbolically in `RESULT.md`. The packaged standalone `verify.py` independently constructs the full deterministic rotor state map and detects the first repeated state for all initial assignments of each tested graph; it also checks the primitive orbit length and maximum multiplicity. The embedded `verification_output.txt` records the successful exhaustive tests of 24,344 states. To replay: `python3 verify.py` from the extracted directory. This finite test does not prove the theorem for untested sizes and is not an independent mathematical audit.
