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

The theorem has an analytic generator-and-matrix proof in `RESULT.md`; `verify.py` independently implements each of three conditional moment systems using rational arithmetic and compares their output with the closed signed factorization. A successful execution reports 1,536 exact assertions and the counter-switching example \(-192/3625\). The checker is finite diagnostic evidence, not a substitute for proving the rational factorization for all positive parameters. All algebraic assumptions required by the proof are stated in `RESULT.md`. Independent audit has not been performed.
