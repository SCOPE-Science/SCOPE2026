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

# Reproducibility checks

The formulas are proved in `RESULT.md`; verification here records bounded exhaustive corroboration, not a proof for infinitely many parameters.

Run `python power_checker.py` with Python 3 standard library. It enumerates each input coefficient matrix, multiplies directly from the semigroup-basis law, and compares the observed multiplicity at every possible target matrix to the closed formula. Expected output is recorded verbatim in `power_checker_output.txt`.

Checked field orders: \(2,3,4,5,9\), with \(\mathbb F_4\) represented by \(t^2+t+1\) and \(\mathbb F_9\) by \(t^2+1\). Checked rectangular sizes: \((1,2),(2,2),(2,3),(3,3)\), for the indicated field orders; powers \(2,3,4,5\) where computationally feasible. All 29 specified configurations matched every target. The largest checked coefficient algebra contains \(9^4=6561\) elements.

An independent symbolic mass check proves that all prescribed fiber multiplicities sum to exactly \(q^{mn}\), in each exponent regime. This detects a missing or duplicated target stratum but is not by itself a substitute for the individual-fiber proof.

Unproved: any extension to rank-higher-than-one sandwich structures, or historical uniqueness among all prior publications. No independent audit has been performed.
