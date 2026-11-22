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

# Verification and reproducibility

The accompanying `CHECK_EXACT.py` is an independent finite enumeration of all quaternary six-tap windows using Gaussian integer operations, with no floating point. Execute `python3 CHECK_EXACT.py` to reproduce `CHECK_EXACT_OUT.txt`. It reports \(128\) antipodal solutions, zero order-ten cases for the full four-lag cancellation requirement, and zero binary antipodal solutions.

The accompanying `CHECK.py` separately enumerates normalized alphabets of orders \(2,4,6,8\), tests every nonzero modulation gap on cyclic orders \(12\) and \(20\), checks agreement with the analytic parametrization, and constructs the entire frame operator explicitly for sample tight windows. Run `python3 CHECK.py` to reproduce `CHECK_OUT.txt`. The phase enumeration and matrix calculations use floating-point tolerance and are **supplementary**; they do not establish universal existence or nonexistence. The full mathematical proof in `RESULT.md` supplies the exact all-order statements, including continuous phases and all integer alphabets.

The proof depends on Fourier orthogonality of the complete translation orbit, injectivity of the frequency labels \(0,\pm1,\ldots,\pm5\) for \(N\ge12\), geometry of three unit complex numbers summing to zero, and elementary unit-circle algebra. These steps are restated and proved in `RESULT.md` rather than delegated to numerical logs. The prior quaternary Golay-pair count is credited, and independent scientific audit has not been conducted.
