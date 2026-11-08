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
# Reproducibility and verification

Execute `python3 verify_phase_transition.py` with standard-library Python 3.8 or later. The program requires no downloaded data or third-party packages. The run on the submitted script completed successfully with `ALL CHECKS PASSED`.

The checker evaluates all ordered nonnegative four-part compositions of each required integer, computes each fiber product exactly, independently compares the three low-dilation values with their closed expressions, and forms numerator coefficients by the finite binomial transform. For every integer \(1\le m\le11\) it checks the complete set of distinct adjacent log-concavity minors, including the central minor under Gorenstein reflection. The numerical table in the proof lists the exact minimum of these checks for each parameter.

For each integer \(12\le m\le20\), the checker tests the strict index-two failure and checks the printed exact value at parameter twelve. For larger parameters, the written analytic proof reduces failure to inequalities that are checked at integer 21 and propagated indefinitely by induction. The finite computation itself does not certify any untested parameter.

The source's Gorenstein symmetry and degree assertions are mathematical inputs from the cited primary theorem. No independent outside audit was performed. The claim is restricted to the explicitly defined one-parameter family.
