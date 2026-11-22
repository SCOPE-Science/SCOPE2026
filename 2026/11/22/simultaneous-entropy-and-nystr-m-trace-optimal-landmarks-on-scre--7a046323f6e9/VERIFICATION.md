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

# Verification

The file `check.py` uses Python 3's standard library (`fractions`, `itertools`, `math`) and was executed against the complete present source. It reported:

`PASS 8695 exact rational checks including all subsets at n<=10; independent n<=7 direct covariance comparisons`

The checker exhaustively enumerates nonempty landmark subsets on cycles of sizes three through ten at three exact rational screening shifts; separately checks complementary minors and the explicit Nyström Schur complement at all subsets on cycles through seven vertices at two rational shifts; verifies the strict discrete Wronskian and convexity test at those shifts; compares optimizer sets, values, cardinalities and second-best deficits; and checks failure of nested optima between two and three landmarks on the six-cycle.

The general result for every \(n\ge3\), positive real \(\mu\), and budget is established by the analytic proof in `RESULT.md`, not by the finite checker. The calculation assumes exact arithmetic, exact observations, a unit-edge cycle, and uniform screening. The mathematical result has not undergone an independent audit.
