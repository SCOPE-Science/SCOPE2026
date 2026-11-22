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

# Reproduction and scope
The direct verification command is `python3 verify_chord.py` in the directory containing the embedded files. The script requires only the Python standard library. It tests the eleven exact trigonometric reductions against direct evaluation, the analytic frequency-tail inequalities against explicit finite checks through mode 4000, and numerical finite differences of the **arclength-defined endpoint** for the two sharp directions. Full infinite coverage and the \(C^2\)-relative remainder follow from the arguments in `RESULT.md`, not from finite tests. The linearized Fourier constants are sharp; no independence of this review or external audit is asserted.
