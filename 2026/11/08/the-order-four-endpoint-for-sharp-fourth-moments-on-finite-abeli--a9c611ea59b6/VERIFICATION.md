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

# Verification of coordinate-cross fourth-moment results

The main proof is analytic. In the critical order-four case, check the identities \(c_4=7/3\), \(m_4=2/\sqrt3\), and the bound in (5), followed by constrained minimization at \(v=2\sqrt3\,t\). When \(t\le1/(2\sqrt3)\), its minimum is at least \(1/2\); otherwise the factored expression (6) is nonnegative, with equality only for \(t=1/\sqrt3\) and \(v=1\). In larger orders use the factorization (4) and note \(c_q>3\).

The standalone check is `python artifacts/verify_cross_axes.py` using only the Python standard library. It evaluates raw character sums for cyclic orders four through seven and the Klein-four group on two- and three-axis sets. The observed log is `CROSS_AXES_CHECK_PASS randomized_and_axis=480 exact_witnesses=2`. Its final two assertions use exact integer convolution counts of \(21\) and \(77\). Finite tests do not establish the universally quantified result or independent certification.
