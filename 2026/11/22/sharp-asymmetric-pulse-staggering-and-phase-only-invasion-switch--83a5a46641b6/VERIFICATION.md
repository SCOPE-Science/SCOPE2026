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

The self-contained `verify.py` uses only Python's standard library. Running `python3 verify.py` performs independent midpoint quadrature against the closed-form overlap, tests positivity and equal-phase boundaries for 350 deterministic pseudo-random parameter sets, checks finite-period and small-period limits, and produces a rational-interval certificate of strict invasion reversal. In its recorded execution, 3,166 assertions/check groups passed.

The rational certificate uses \(42\) Taylor terms for \(e^q\) with nonnegative rational \(q\le4\); the remainder is enclosed by the next term multiplied by \(1/(1-q/44)\). Reciprocals handle negative exponents. The certificate establishes \(I_T(1/2)<8/25<I_T(0)\) for the stated rates and doses. This exact inequality combined with continuity and strict convexity, not sampled phase values alone, proves an open interval of opposite stability signs and two exact neutral phases.

The universal assertions are proven analytically in `RESULT.md`; no finite loop is used to certify all parameter choices. This verification does not include a field experiment, ecological parameter estimation, external independent audit, or exhaustive historical priority review.
