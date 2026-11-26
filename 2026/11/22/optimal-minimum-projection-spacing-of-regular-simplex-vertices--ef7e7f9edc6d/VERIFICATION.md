---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the centered coordinate model the projected vector is uniform on the radius-1/sqrt(2) sphere in the zero-sum hyperplane. In any label chamber the inverse difference map has Gram matrix M equal to the inverse path Cartan matrix, with determinant 1/(d+1), positive entries, and row sums a_j. Thus g^T M g >= A_d(min g_j)^2, with equality only at the positive equal-gap point of each chamber. This gives the stated maximum and (d+1)! oriented maximizers. Coarea with the gap Jacobian (d+1)^(-1/2) and the slack change of variables h_j=s q_j/a_j gives the displayed integral: the positive root solves 2ts+s^2H=B_t and its radial derivative is 2(t+sH). Summing chambers and dividing by sphere area gives exactly the stated prefactor. At t=0 the chambers exhaust the sphere up to ties, and at t>=g_d the strict event is empty. Uniformly on the compact q-simplex as t=g_d-epsilon increases, s=A_d epsilon+O_d(epsilon^2) and the inverse denominator is g_d^(-1)+O_d(epsilon). Integrating over simplex coordinate volume 1/(d-1)! gives C_d and the stated error; normalizing the same uniformly expanded density gives total variation convergence. Coordinate permutation leaves that density invariant, giving exact independent uniform label order. An independent 80-by-80 Gauss–Legendre quadrature on the tetrahedral simplex at t=0 gave 1.000000000000; substitution into C_d gives 2*5^(5/2)/(3*pi). These spot checks do not prove the general formula; the supplied verifier was inspected, not executed.

## originality

PASS

Best of the inspected evidence: the complete statement for minimum adjacent projected spacing, including its finite-threshold and conditional endpoint laws, is distinguishable from both projection-width results and affine-section results. The exact catalogue hit is the assigned item itself, not a separate claim.

## value

PASS

A support-width statistic cannot tell whether every projected vertex is resolvable. The exact survival integral quantifies whole-configuration resolvability at a prescribed tolerance, while the sharp tail and conditional weighted gap law explain how the near-optimal directions share that tolerance. The combined findings go materially beyond the elementary equal-gap optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
