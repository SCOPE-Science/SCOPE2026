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

# Reproduction
Run `python3 verify.py` with Python 3 and no third-party dependencies. The script independently enumerates projected interval starts and compares their integer overlap-count histograms against the cyclic-gap-composition distribution. It checks the complete integer count spectrum, exact first and second moments, and direct generalized CRT enumerations for three genuinely different moduli.

Expected terminal prefix: `VERIFY_OK spectra_parameter_cases=4274 interval_start_configs=301736 CRT_direct_cases=92176`.

# Scope of verification
The checks are finite: cyclic moduli \(2\) through \(8\) for three intervals, cyclic moduli \(2\) through \(5\) for four intervals, and direct CRT across 92176 start/length choices. Arbitrary-parameter correctness is furnished by the mathematical proof, not extrapolated from this test.
