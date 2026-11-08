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

# Verification of the exact capture-time theorem

**Statement checked.** For every negative real \(B\) and all \((X,Y)\in\mathbb R^2\), the map \(F_B(X,Y)=(Y+\max(0,2X),B-\max(0,2X))\) reaches \((B,B)\) by the sixth original iteration. The theorem also lists each first-hitting-time region, including zero, one and switching-boundary cases.

**Analytical check.** Under the conjugacy by the positive factor \(-B\), the map reduces to a single normalized affine/max-plus system. A complete four-branch sign exhaustion proves the fourth first coordinate is strictly negative, the fifth state has a nonpositive first coordinate and second coordinate \(-1\), and the sixth state is the sink. A complete separate case division, including equality, gives exact first-hit times; explicit witnesses attain all seven values. See `RESULT.md`, Proof Steps 1–4.

**Machine check actually run.** Execute `python3 verify_capture.py` from the package directory with standard Python 3; no external dependencies. The script performs exact Fraction arithmetic on 16,353 specified test cases: five distinct negative parameter scales, symmetric rational grids, exact knife-edge thresholds and outlier states. Each case compares the direct first-hit iterate against the independently coded partition and confirms the sixth iterate is the sink. All seven capture-time values occur. The observed final output is `CHECK_OK exact-rational cases= 16353` followed by first-hit counts.

**Limits.** Finite tests do not establish the theorem for all real initial states. The all-real result uses the explicit proof. No independent mathematical audit or external certification was conducted. Only deterministic finite-step capture in the unsmoothed specified system is asserted.
