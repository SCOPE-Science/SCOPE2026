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

# Verification of the two-frequency exterior-energy theorem

The proof is analytic and complete under the hypotheses in `RESULT.md`. The two diagonal energy identities follow by integration of \(\cos^2(dt/2)\) and \(\sin^2(dt/2)\) over symmetric sets. Their cross terms vanish by parity. The generalized norm is the larger diagonal quotient because both input diagonal weights are positive. The exact gap minimum follows from opposing signed deviations from \(h\), and the infinitely many resonant gaps follow from strict opposite signs at successive \((n+1/2)\pi\).

The standard-library `CHECK.py` script is executable with `python3 CHECK.py`; it compares independent Simpson quadrature with both analytic generalized eigenvalues for several real gaps and exterior lengths, checks arbitrary complex mixtures, locates representative resonance roots by rigorous *bracketing logic implemented numerically*, and tests the displayed asymptotic coefficient. Numeric bisection and quadrature are illustrative, not interval-certified and not substitutes for the universal proof.

The input and exterior integrals are unnormalized; the result concerns the infimum over positive gap values of the worst-case **fixed-gap** transfer, not the global worst-gap extrapolation constant. The root equation may have more than one solution in a given bracket, and that multiplicity is not classified. No independent mathematical audit has been performed.
