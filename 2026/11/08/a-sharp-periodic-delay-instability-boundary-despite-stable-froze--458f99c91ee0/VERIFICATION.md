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

# Mathematical verification

Reproduction: run `python verify.py` using Python 3.9+ and SymPy 1.10+. It verifies the stage-dependent three-matrix product and the exact cubic characteristic polynomial, the closed Schur conditions, the rational critical factorization, a negative-feedback witness, and the frozen constant-delay characteristic equations for three sample delay lengths. It ran successfully on the packaged source before delivery and reported `CHECKS_OK`.

The self-contained proof in `RESULT.md` supplies the all-parameter inequalities, real unstable-root argument, fixed-delay Rouché stability and continuous-time Halanay comparison; the checker is supplementary. It does not prove stronger arbitrary-switching behavior or validate results in independent software or by a separate mathematical auditor.
