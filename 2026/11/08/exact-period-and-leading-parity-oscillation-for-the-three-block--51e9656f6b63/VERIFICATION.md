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

The proof is self-contained in `RESULT.md`, equations (1)–(3), apart from classical rational Ehrhart polynomiality and full-dimensional leading volume. The standalone checker `verify.py` (Python 3 and SymPy) was executed and printed `PASS: 110 exact assertions`. It compares 65 direct enumerations with a different minimum-layer enumeration for five block sizes and thirteen dilations, and separately checks 39 exact rational-series coefficients and three exact principal Laurent coefficients, with three additional pole nonvanishing checks.

Exact symbolic rational examples are printed for \(a=2\) and \(a=3\). No finite range is used to justify the all-parameter conclusion; the proof identifies the pole analytically by isolating the highest-degree height moment. All statements concern the ordinary integer lattice and the rational polytope explicitly defined in `RESULT.md`. Historical-priority assessment is provisional, and independent audit has not been performed.
