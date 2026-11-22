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
# Verification record

The complete general proof is in RESULT.md. Run `python CHECKER.py` with Python 3. The source is self-contained and checks every possible input and output in thirty configurations: orders \(3,5,7,9,11\), dimensions \(2,3,4\), and two nondegenerate diagonal determinant classes each. The quadratic field of nine elements is explicitly constructed as \(\mathbb F_3[\theta]/(\theta^2+1)\). The provided CHECK_OUTPUT.json is the captured result from executing that exact checker source. Each case verifies every exact target-fiber cardinality, the norm counts and the two-/four-root target multiplicities as well as the total image count.

Finite exhaustive computations cannot establish the theorem for unbounded field sizes and dimensions; the proof uses polynomial elimination, involution-orbit counting and the finite-field Gauss-sum evaluation. No independent audit or certification is claimed.
