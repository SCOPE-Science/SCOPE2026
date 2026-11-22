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

The analytic proof establishes exact source normalization, the two strict concavity regions, the necessary and sufficient boundary inequalities, the nonempty interval, unique upper-bound switch, and both limit expansions.

Reproduction: save `check.py` beside `RESULT.md`, run `python3 check.py` with Python 3.10 or newer. A replay from the package reported `PASS 894 assertions`. The code uses standard-library math and bisection. It does not attempt exhaustive verification over continuous parameters; analytic arguments in the proof are decisive.

Numerical example: for \(a=2\log 2\), \(d=1/2\), \(w=1/3\), the nontrivial roots are approximately \(0.3125783675\) and \(0.6383174433\), and the exact surplus at activation is \(-1/18\).

Scientific limits: no weather, rainfall routing calibration, or empirical field-validation experiment has been performed. Historical priority remains provisional.
