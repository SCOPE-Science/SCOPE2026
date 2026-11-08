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

# Reproducibility

Execute `python3 verify.py` with Python 3.8+ and the standard library. The checker first constructs the actual periodic factors up to one symbol longer than the displayed period; every longer factor has a fully determined continuation from its cyclic state. It obtains minimal forbidden factors independently by extending all observed prefixes and checking the observed suffix, and obtains bispecial factors independently from all cyclic predecessor/successor pairs. It compares the observed sets to the claimed explicit list, and compares the number and greatest length of minimal forbidden factors to the formulas.

The packaged script passed 1,296 profiles with each of the four run lengths in \(\{1,2,3,4,5,6\}\), including the 36 cases representing a doubled two-run primitive period. It also passed 200 deterministically selected profiles with each length in the range 1 through 40. These checks exercise edge cases and are reproducible, but finite experiments do not prove the result for all positive integers; the unbounded argument is given in RESULT.md.

No independent scientific audit or external formal certification has been performed.
