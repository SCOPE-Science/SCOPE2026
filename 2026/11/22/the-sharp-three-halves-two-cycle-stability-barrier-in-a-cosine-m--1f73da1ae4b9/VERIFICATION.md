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

# Reproduction and verification

The self-contained `verify_cycle.py` file is executable with Python 3, SymPy and mpmath. Run `python verify_cycle.py` from the extracted directory; successful execution prints `SYMBOLIC_IDENTITIES_OK` and `VERIFY_OK`. Its exact symbolic assertions reconstruct both Floquet identities, the reduced determinant identity and the key factorization of the lower bound for the trace. Its 70-digit numerical diagnostics check that both map iterates return to the correct phases and inspect the two-step multipliers at six parameter points, with stable and unstable cases on opposite sides of the critical gain.

The infinite-parameter proof is in `RESULT.md`. Its two decisive inequalities concern separately \(0<p\le1\) and \(1<p<2\sqrt{1-1/\beta}\), and are valid for every \(\alpha>0\) in the excluded gain range. The sharpness argument constructs actual orbits for all sufficiently small positive forcing below the gain boundary. Neither the finite computations nor these reviews constitute independent mathematical validation. The gain interval above \(\beta=2\), global attraction and longer-period dynamics are not assessed.
