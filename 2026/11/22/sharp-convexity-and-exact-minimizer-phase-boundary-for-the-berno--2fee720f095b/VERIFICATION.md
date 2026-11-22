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

The proof uses analytic identities with all quantifiers stated in \(\texttt{RESULT.md}\). The accompanying \(\texttt{verify.py}\) was executed using Python 3 with SymPy installed. Its exact polynomial checks confirm \(Q_q(p)\), the maximizing probability, the curvature factorization, and the exact roots of the curvature-sign interval. Rational-label tests cover the phase boundary, both nonconvex endpoints, and the strict-minimizer derivative factor for admissible stepsizes. Floating-point tests exercise additional labels and stepsizes.

Command: `python verify.py`

Observed result: `PASS: exact curvature identity, exact sharp threshold, roots, unique minimizer, 10 numerical labels`

The verifier does not prove novelty or independently certify the universal theorem; those rest on the displayed proof and literature comparison. Independent audit has not been performed. The full primary paper was not available for complete comparison, so priority remains provisional.
